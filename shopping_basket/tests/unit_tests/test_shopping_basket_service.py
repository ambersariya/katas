from typing import Final
from unittest import TestCase
from unittest.mock import MagicMock

from shopping_basket.product import Product, ProductId
from shopping_basket.product_repository import ProductRepository
from shopping_basket.shopping_basket import ShoppingBasket, ShoppingBasketItem
from shopping_basket.shopping_basket_repository import ShoppingBasketRepository
from shopping_basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.user import UserId

USER_ID: Final[UserId] = UserId('some-id')
PRODUCT: Final[Product] = Product(ProductId('product-1'), name='the hobbit dvd', price=5)
BASKET_ITEM_QUANTITY = 5
BASKET_ITEM: Final[ShoppingBasketItem] = ShoppingBasketItem.for_product(product=PRODUCT, quantity=BASKET_ITEM_QUANTITY)
BASKET_CREATION_DATE = '15/06/2022'
SHOPPING_BASKET = ShoppingBasket(user_id=USER_ID, created_at=BASKET_CREATION_DATE, items=[])


class ShoppingBasketServiceShould(TestCase):
    def setUp(self):
        self.shopping_basket_repository = MagicMock(ShoppingBasketRepository)
        self.product_repository = MagicMock(ProductRepository)

    def test_raise_error_when_user_doesnt_have_a_basket(self):
        basket_service = ShoppingBasketService(self.shopping_basket_repository, self.product_repository)
        self.shopping_basket_repository.basket_for.return_value = None

        with self.assertRaises(basket_service.ShoppingBasketNotFoundError):
            basket_service.basket_for(USER_ID)

    def test_return_basket_for_given_user(self):
        basket_service = ShoppingBasketService(self.shopping_basket_repository, self.product_repository)
        self.shopping_basket_repository.basket_for.return_value = SHOPPING_BASKET

        basket = basket_service.basket_for(user_id=USER_ID)

        self.assertIsInstance(basket, ShoppingBasket)
        self.assertEqual(USER_ID, basket.user_id)

    def test_create_shopping_basket_when_item_is_added_and_basket_shouldnt_exist(self):
        self.product_repository.find_product_by_id.return_value = PRODUCT

        basket_service = ShoppingBasketService(self.shopping_basket_repository, self.product_repository)
        basket_service.add_item(user_id=USER_ID, product_id=PRODUCT.id, quantity=BASKET_ITEM_QUANTITY)

        self.shopping_basket_repository.add_item.assert_called_once_with(BASKET_ITEM)
