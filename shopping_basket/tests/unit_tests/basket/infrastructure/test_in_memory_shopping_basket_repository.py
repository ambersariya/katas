from unittest import TestCase
from unittest.mock import MagicMock

from constants import (
    BASKET_ITEM_LORD_OF_THE_RINGS_QUANTITY_FIVE,
    BASKET_ITEM_BREAKING_BAD_QUANTITY_TWO,
    USER_ID,
)
from shopping_basket.basket.infrastructure.in_memory_shopping_basket_repository import (
    InMemoryShoppingBasketRepository,
)
from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem
from shopping_basket.core.date_provider import DateProvider


class TestInMemoryShoppingBasketRepositoryShould:
    def test_return_no_shopping_basket_for_user(self, in_memory_shopping_basket_repo) -> None:
        result = in_memory_shopping_basket_repo.basket_for(user_id=USER_ID)
        assert result is None

    def test_create_shopping_basket_only_when_we_add_an_item(
        self, date_provider, in_memory_shopping_basket_repo
    ) -> None:
        date_provider.current_date.return_value = "15/06/2022"
        in_memory_shopping_basket_repo.add_item(
            item=BASKET_ITEM_LORD_OF_THE_RINGS_QUANTITY_FIVE, user_id=USER_ID
        )

        result = in_memory_shopping_basket_repo.basket_for(user_id=USER_ID)

        assert isinstance(result, ShoppingBasket)
        assert len(result.items) == 1

    def test_save_more_than_one_kind_of_item_with_different_id(
        self, in_memory_shopping_basket_repo, date_provider
    ) -> None:
        date_provider.current_date.return_value = "15/06/2022"
        in_memory_shopping_basket_repo.add_item(
            item=BASKET_ITEM_LORD_OF_THE_RINGS_QUANTITY_FIVE, user_id=USER_ID
        )
        in_memory_shopping_basket_repo.add_item(
            item=BASKET_ITEM_BREAKING_BAD_QUANTITY_TWO, user_id=USER_ID
        )

        result = in_memory_shopping_basket_repo.basket_for(user_id=USER_ID)

        assert isinstance(result, ShoppingBasket)
        assert len(result.items) == 2
        assert BASKET_ITEM_LORD_OF_THE_RINGS_QUANTITY_FIVE == result.items[0]
        assert BASKET_ITEM_BREAKING_BAD_QUANTITY_TWO == result.items[1]

    def test_update_quantity_and_total_of_item_that_is_added_twice(
        self, in_memory_shopping_basket_repo, date_provider
    ):
        date_provider.current_date.return_value = "15/06/2022"
        in_memory_shopping_basket_repo.add_item(
            item=BASKET_ITEM_BREAKING_BAD_QUANTITY_TWO, user_id=USER_ID
        )
        in_memory_shopping_basket_repo.add_item(
            item=BASKET_ITEM_BREAKING_BAD_QUANTITY_TWO, user_id=USER_ID
        )

        result = in_memory_shopping_basket_repo.basket_for(user_id=USER_ID)

        assert isinstance(result, ShoppingBasket)
        assert len(result.items) == 1

        item = result.items[0]
        assert isinstance(item, ShoppingBasketItem)
        assert item.quantity == 4
        assert item.total() == 20
