from typing import Final
from unittest import TestCase
from unittest.mock import MagicMock

from shopping_basket.basket.shopping_basket_error import ShoppingBasketNotFoundError
from shopping_basket.product.product import Product, ProductId
from shopping_basket.product.product_category import ProductCategory
from shopping_basket.product.product_service import ProductService
from shopping_basket.basket.shopping_basket import ShoppingBasket, ShoppingBasketItem, ShoppingBasketItems
from shopping_basket.basket.shopping_basket_repository import ShoppingBasketRepository
from shopping_basket.basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.basket.user import UserId
from shopping_basket.core.utilities import ItemLogger

USER_ID: Final[UserId] = UserId('some-id')
PRODUCT: Final[Product] = Product(ProductId('product-1'), name='the hobbit dvd', price=5, category=ProductCategory.VIDEO)
BASKET_ITEM_QUANTITY = 5
BASKET_ITEM: Final[ShoppingBasketItem] = ShoppingBasketItem.for_product(product=PRODUCT, quantity=BASKET_ITEM_QUANTITY)
BASKET_CREATION_DATE = '15/06/2022'
SHOPPING_BASKET = ShoppingBasket(user_id=USER_ID, created_at=BASKET_CREATION_DATE, items=ShoppingBasketItems(items=[]))


class ShoppingBasketServiceShould(TestCase):
    def setUp(self):
        self.shopping_basket_repository = MagicMock(ShoppingBasketRepository)
        self.product_service = MagicMock(ProductService)
        self.item_logger = MagicMock(ItemLogger)
        self.basket_service = ShoppingBasketService(self.shopping_basket_repository, self.product_service,
                                                    item_logger=self.item_logger)

    def test_raise_error_when_user_doesnt_have_a_basket(self):
        self.shopping_basket_repository.basket_for.return_value = None

        with self.assertRaises(ShoppingBasketNotFoundError):
            self.basket_service.basket_for(USER_ID)

    def test_return_basket_for_given_user(self):
        self.shopping_basket_repository.basket_for.return_value = SHOPPING_BASKET

        basket = self.basket_service.basket_for(user_id=USER_ID)

        self.assertIsInstance(basket, ShoppingBasket)
        self.assertEqual(USER_ID, basket.user_id)

    def test_create_shopping_basket_when_item_is_added_and_basket_doesnt_exist(self):
        self.product_service.find_and_reserve.return_value = PRODUCT

        self.basket_service.add_item(user_id=USER_ID, product_id=PRODUCT.id, quantity=BASKET_ITEM_QUANTITY)
        self.item_logger.log.assert_called_once()
        self.shopping_basket_repository.add_item.assert_called_once_with(item=BASKET_ITEM, user_id=USER_ID)
