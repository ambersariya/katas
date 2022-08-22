from unittest import TestCase
from unittest.mock import MagicMock

from constants import (
    USER_ID,
    SHOPPING_BASKET,
    PRODUCT_VIDEO,
    QUANTITY_TWO,
    PRODUCT_ID_VIDEO,
    BASKET_ITEM_QUANTITY_TWO,
    DISCOUNTED_SHOPPING_BASKET,
)
from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.basket.shopping_basket_error import ShoppingBasketNotFoundError
from shopping_basket.basket.shopping_basket_repository import ShoppingBasketRepository
from shopping_basket.basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.core.utilities import ItemLogger
from shopping_basket.discount.discount_calculator import DiscountCalculator
from shopping_basket.product.product_service import ProductService


class ShoppingBasketServiceShould(TestCase):
    def setUp(self):
        self.shopping_basket_repository = MagicMock(ShoppingBasketRepository)
        self.product_service = MagicMock(ProductService)
        self.item_logger = MagicMock(ItemLogger)
        self.discount_calculator = MagicMock(DiscountCalculator)
        self.basket_service = ShoppingBasketService(
            shopping_basket_repository=self.shopping_basket_repository,
            product_service=self.product_service,
            item_logger=self.item_logger,
            discount_calculator=self.discount_calculator,
        )

    def test_raise_error_when_user_doesnt_have_a_basket(self):
        self.shopping_basket_repository.basket_for.return_value = None

        with self.assertRaises(ShoppingBasketNotFoundError):
            self.basket_service.basket_for(USER_ID)

    def test_return_basket_with_no_discount_for_given_user(self):
        self.shopping_basket_repository.basket_for.return_value = SHOPPING_BASKET
        self.discount_calculator.apply_discount.return_value = SHOPPING_BASKET

        basket = self.basket_service.basket_for(user_id=USER_ID)

        self.assertIsInstance(basket, ShoppingBasket)
        self.assertEqual(USER_ID, basket.user_id)

    def test_create_shopping_basket_when_item_is_added_and_basket_doesnt_exist(self):
        self.product_service.reserve.return_value = PRODUCT_VIDEO

        self.basket_service.add_item(
            user_id=USER_ID, product_id=PRODUCT_ID_VIDEO, quantity=QUANTITY_TWO
        )
        self.item_logger.log.assert_called_once()
        self.shopping_basket_repository.add_item.assert_called_once_with(
            item=BASKET_ITEM_QUANTITY_TWO, user_id=USER_ID
        )

    def test_return_basket_with_discount_for_given_user(self):
        self.shopping_basket_repository.basket_for.return_value = SHOPPING_BASKET
        self.discount_calculator.apply_discount.return_value = (
            DISCOUNTED_SHOPPING_BASKET
        )

        basket = self.basket_service.basket_for(user_id=USER_ID)

        self.assertIsInstance(basket, ShoppingBasket)
        self.assertEqual(USER_ID, basket.user_id)
