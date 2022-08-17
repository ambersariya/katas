from typing import Final
from unittest import TestCase
from unittest.mock import MagicMock

from shopping_basket.basket.shopping_basket_error import ShoppingBasketNotFoundError
from shopping_basket.discount.discount import Discount, ThreeBooksDiscount
from shopping_basket.discount.discount_calculator import DiscountCalculator
from shopping_basket.discount.discounted_shopping_basket import DiscountedShoppingBasket
from shopping_basket.product.product import Product
from shopping_basket.product.product_id import ProductId
from shopping_basket.product.product_category import ProductCategory
from shopping_basket.product.product_service import ProductService
from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.basket.shopping_basket_items import ShoppingBasketItems
from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem
from shopping_basket.basket.shopping_basket_repository import ShoppingBasketRepository
from shopping_basket.basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.basket.user import UserId
from shopping_basket.core.utilities import ItemLogger

USER_ID: Final[UserId] = UserId('some-id')
PRODUCT: Final[Product] = Product(ProductId('product-1'), name='the hobbit dvd', price=5,
                                  category=ProductCategory.VIDEO)
QUANTITY_FIVE = 5
QUANTITY_TWO = 2
BASKET_ITEM_QUANTITY_FIVE: Final[ShoppingBasketItem] = ShoppingBasketItem.for_product(product=PRODUCT,
                                                                                      quantity=QUANTITY_FIVE)
BASKET_ITEM_QUANTITY_TWO: Final[ShoppingBasketItem] = ShoppingBasketItem.for_product(product=PRODUCT,
                                                                                     quantity=QUANTITY_TWO)
BASKET_CREATION_DATE = '15/06/2022'
SHOPPING_BASKET = ShoppingBasket(user_id=USER_ID, created_at=BASKET_CREATION_DATE,
                                 items=ShoppingBasketItems(items=[BASKET_ITEM_QUANTITY_TWO]))
DISCOUNTABLE_SHOPPING_BASKET = ShoppingBasket(user_id=USER_ID, created_at=BASKET_CREATION_DATE,
                                              items=ShoppingBasketItems(items=[BASKET_ITEM_QUANTITY_FIVE])
                                              )

DISCOUNTED_SHOPPING_BASKET = DiscountedShoppingBasket.from_basket(basket=DISCOUNTABLE_SHOPPING_BASKET,
                                                                  discount=ThreeBooksDiscount())


class ShoppingBasketServiceShould(TestCase):
    def setUp(self):
        self.shopping_basket_repository = MagicMock(ShoppingBasketRepository)
        self.product_service = MagicMock(ProductService)
        self.item_logger = MagicMock(ItemLogger)
        self.discount_service = MagicMock(DiscountCalculator)
        self.basket_service = ShoppingBasketService(self.shopping_basket_repository, self.product_service,
                                                    item_logger=self.item_logger,
                                                    discount_service=self.discount_service)

    def test_raise_error_when_user_doesnt_have_a_basket(self):
        self.shopping_basket_repository.basket_for.return_value = None

        with self.assertRaises(ShoppingBasketNotFoundError):
            self.basket_service.basket_for(USER_ID)

    def test_return_basket_with_no_discount_for_given_user(self):
        self.shopping_basket_repository.basket_for.return_value = SHOPPING_BASKET

        basket = self.basket_service.basket_for(user_id=USER_ID)

        self.assertIsInstance(basket, ShoppingBasket)
        self.assertEqual(USER_ID, basket.user_id)

    def test_create_shopping_basket_when_item_is_added_and_basket_doesnt_exist(self):
        self.product_service.reserve.return_value = PRODUCT

        self.basket_service.add_item(user_id=USER_ID, product_id=PRODUCT.id, quantity=QUANTITY_TWO)
        self.item_logger.log.assert_called_once()
        self.shopping_basket_repository.add_item.assert_called_once_with(item=BASKET_ITEM_QUANTITY_TWO, user_id=USER_ID)

    def test_return_basket_with_discount_for_given_user(self):
        self.shopping_basket_repository.basket_for.return_value = SHOPPING_BASKET
        self.discount_service.apply_discount.return_value = DISCOUNTED_SHOPPING_BASKET

        basket = self.basket_service.basket_for(user_id=USER_ID)

        self.assertIsInstance(basket, ShoppingBasket)
        self.assertEqual(USER_ID, basket.user_id)
