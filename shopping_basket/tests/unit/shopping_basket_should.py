import unittest
from unittest.mock import MagicMock

from shopping_basket.src.shopping_basket.basketitem import BasketItem
from shopping_basket.src.shopping_basket.shopping_basket_repository import ShoppingBasketRepository
from shopping_basket.src.shopping_basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.src.shopping_basket.product import ProductID
from shopping_basket.src.shopping_basket.user import UserID


class ShoppingBasketServiceShould(unittest.TestCase):
    USER_ID = UserID("user-1")
    PRODUCT_ID = ProductID("product-1")
    PRODUCT_QUANTITY = 5

    def setUp(self) -> None:
        self.shopping_basket_repository = MagicMock(ShoppingBasketRepository, autospec=True)
        self.shopping_basket_service = ShoppingBasketService(self.shopping_basket_repository)

    def test_add_product_for_a_user(self):
        item = BasketItem(user_id=self.USER_ID, product_id=self.PRODUCT_ID, quantity=self.PRODUCT_QUANTITY)
        self.shopping_basket_service.add_item(
            user_id=self.USER_ID,
            product_id=self.PRODUCT_ID,
            quantity=self.PRODUCT_QUANTITY
        )

        self.shopping_basket_repository.add_item.assert_called_with(item)
