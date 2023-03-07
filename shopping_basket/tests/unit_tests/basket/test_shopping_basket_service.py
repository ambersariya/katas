import pytest

from tests.constants import (
    BASKET_ITEM_BREAKING_BAD_QUANTITY_TWO,
    DISCOUNTED_SHOPPING_BASKET,
    PRODUCT_ID_BREAKING_BAD,
    PRODUCT_VIDEO_BREAKING_BAD,
    QUANTITY_TWO,
    SHOPPING_BASKET_WITH_ONE_ITEM,
    USER_ID,
)
from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.basket.shopping_basket_error import ShoppingBasketNotFoundError


class TestShoppingBasketServiceShould:
    def test_raise_error_when_user_doesnt_have_a_basket(
        self, mocked_shopping_basket_repository, shopping_basket_service
    ) -> None:
        mocked_shopping_basket_repository.basket_for.return_value = None

        with pytest.raises(ShoppingBasketNotFoundError):
            shopping_basket_service.basket_for(USER_ID)

    def test_return_basket_with_no_discount_for_given_user(
        self, mocked_shopping_basket_repository, mocked_discount_calculator, shopping_basket_service
    ) -> None:
        mocked_shopping_basket_repository.basket_for.return_value = SHOPPING_BASKET_WITH_ONE_ITEM
        mocked_discount_calculator.apply_discount.return_value = SHOPPING_BASKET_WITH_ONE_ITEM

        basket = shopping_basket_service.basket_for(user_id=USER_ID)

        assert isinstance(basket, ShoppingBasket)
        assert USER_ID == basket.user_id

    def test_create_shopping_basket_when_item_is_added_and_basket_doesnt_exist(
        self,
        mocked_shopping_basket_repository,
        mocked_product_service,
        shopping_basket_service,
        mocked_item_logger,
    ) -> None:
        mocked_product_service.reserve.return_value = PRODUCT_VIDEO_BREAKING_BAD

        shopping_basket_service.add_item(
            user_id=USER_ID, product_id=PRODUCT_ID_BREAKING_BAD, quantity=QUANTITY_TWO
        )
        mocked_item_logger.log.assert_called_once()
        mocked_shopping_basket_repository.add_item.assert_called_once_with(
            item=BASKET_ITEM_BREAKING_BAD_QUANTITY_TWO, user_id=USER_ID
        )

    def test_return_basket_with_discount_for_given_user(
        self, mocked_shopping_basket_repository, mocked_discount_calculator, shopping_basket_service
    ) -> None:
        mocked_shopping_basket_repository.basket_for.return_value = SHOPPING_BASKET_WITH_ONE_ITEM
        mocked_discount_calculator.apply_discount.return_value = DISCOUNTED_SHOPPING_BASKET

        basket = shopping_basket_service.basket_for(user_id=USER_ID)

        assert isinstance(basket, ShoppingBasket)
        assert USER_ID == basket.user_id
