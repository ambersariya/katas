from unittest import TestCase
from unittest.mock import MagicMock

from constants import BASKET_ITEM_QUANTITY_FIVE, BASKET_ITEM_QUANTITY_TWO, USER_ID

from shopping_basket.basket.infrastructure.in_memory_shopping_basket_repository import (
    InMemoryShoppingBasketRepository,
)
from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem
from shopping_basket.core.date_provider import DateProvider


class InMemoryShoppingBasketRepositoryShould(TestCase):
    def setUp(self) -> None:
        self.date_provider = MagicMock(DateProvider)
        self.repository = InMemoryShoppingBasketRepository(
            date_provider=self.date_provider
        )

    def test_return_no_shopping_basket_for_user(self):
        result = self.repository.basket_for(user_id=USER_ID)
        self.assertIsNone(result)

    def test_create_shopping_basket_only_when_we_add_an_item(self):
        self.date_provider.current_date.return_value = "15/06/2022"
        self.repository.add_item(item=BASKET_ITEM_QUANTITY_FIVE, user_id=USER_ID)

        result = self.repository.basket_for(user_id=USER_ID)

        self.assertIsInstance(result, ShoppingBasket)
        self.assertEqual(1, len(result.items))

    def test_save_more_than_one_kind_of_item_with_different_id(self):
        self.date_provider.current_date.return_value = "15/06/2022"
        self.repository.add_item(item=BASKET_ITEM_QUANTITY_FIVE, user_id=USER_ID)
        self.repository.add_item(item=BASKET_ITEM_QUANTITY_TWO, user_id=USER_ID)

        result = self.repository.basket_for(user_id=USER_ID)

        self.assertIsInstance(result, ShoppingBasket)
        self.assertEqual(2, len(result.items))
        self.assertEqual(BASKET_ITEM_QUANTITY_FIVE, result.items[0])
        self.assertEqual(BASKET_ITEM_QUANTITY_TWO, result.items[1])

    def test_update_quantity_and_total_of_item_that_is_added_twice(self):
        self.date_provider.current_date.return_value = "15/06/2022"
        self.repository.add_item(item=BASKET_ITEM_QUANTITY_TWO, user_id=USER_ID)
        self.repository.add_item(item=BASKET_ITEM_QUANTITY_TWO, user_id=USER_ID)

        result = self.repository.basket_for(user_id=USER_ID)

        self.assertIsInstance(result, ShoppingBasket)
        self.assertEqual(1, len(result.items))
        item = result.items[0]
        self.assertIsInstance(item, ShoppingBasketItem)
        self.assertEqual(4, item.quantity)
        self.assertEqual(20, item.total())
