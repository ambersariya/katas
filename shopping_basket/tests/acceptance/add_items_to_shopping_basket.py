import unittest

from shopping_basket.src.shopping_basket.basketitem import BasketItem
from shopping_basket.src.shopping_basket.in_memory_shopping_basket_repository import InMemoryShoppingBasketRepository
from shopping_basket.src.shopping_basket.shopping_basket import ShoppingBasket
from shopping_basket.src.shopping_basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.src.shopping_basket.product import ProductID
from shopping_basket.src.shopping_basket.user import UserID
from shopping_basket.tests.builders.shopping_basket_builder import build_shopping_basket


class AddItemsToShoppingBasket(unittest.TestCase):
    _PRODUCT_ID_THE_HOBBIT = ProductID("product-1")
    _QUANTITY_THE_HOBBIT = 2
    _PRODUCT_ID_THE_BREAKING_BAD = ProductID("product-2")
    _QUANTITY_BREAKING_BAD = 5
    _USER_ID_DANISH = UserID("user-1")
    _USER_ID_NOAH = UserID("user-2")

    def setUp(self) -> None:
        self.shopping_basket_repository = InMemoryShoppingBasketRepository()
        self.shopping_basket_service = ShoppingBasketService(self.shopping_basket_repository)

    def test_shows_shopping_basket_details_after_adding_items_to_it(self):
        self.shopping_basket_service.add_item(
            user_id=self._USER_ID_DANISH,
            product_id=self._PRODUCT_ID_THE_HOBBIT,
            quantity=self._QUANTITY_THE_HOBBIT
        )
        self.shopping_basket_service.add_item(
            user_id=self._USER_ID_DANISH,
            product_id=self._PRODUCT_ID_THE_BREAKING_BAD,
            quantity=self._QUANTITY_BREAKING_BAD
        )

        shopping_basket: ShoppingBasket = self.shopping_basket_service.basket_for(self._USER_ID_DANISH)
        sample_basket = build_shopping_basket() \
            .created_at('2022-06-01 00:00:00') \
            .with_item(BasketItem(user_id=self._USER_ID_DANISH, quantity=self._QUANTITY_THE_HOBBIT,
                                  product_id=self._PRODUCT_ID_THE_HOBBIT)) \
            .with_item(BasketItem(user_id=self._USER_ID_NOAH, quantity=self._QUANTITY_BREAKING_BAD,
                                  product_id=self._PRODUCT_ID_THE_BREAKING_BAD)) \
            .build()

        assert shopping_basket == sample_basket
        assert shopping_basket.has_total() == 45.00
