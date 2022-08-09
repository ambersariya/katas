from unittest import TestCase
from unittest.mock import MagicMock

from shopping_basket.shopping_basket import ShoppingBasket
from shopping_basket.shopping_basket_repository import ShoppingBasketRepository
from shopping_basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.user import UserId


class ShoppingBasketServiceShould(TestCase):
    def test_throw_error_when_user_doesnt_have_a_basket(self):
        user_id = UserId('abc-123')
        shopping_basket_repository = MagicMock(ShoppingBasketRepository)
        basket_service = ShoppingBasketService(shopping_basket_repository)
        shopping_basket_repository.basket_for.return_value = None

        with self.assertRaises(basket_service.ShoppingBasketNotFoundError):
            basket_service.basket_for(user_id)

        shopping_basket_repository.basket_for.assert_called_once()

    def test_return_basket_for_given_user(self):
        user_id = UserId('abc-123')
        shopping_basket_repository = MagicMock(ShoppingBasketRepository)
        basket_service = ShoppingBasketService(shopping_basket_repository)
        shopping_basket_repository.basket_for.return_value = ShoppingBasket(user_id=UserId('abc-123'))

        basket = basket_service.basket_for(user_id=user_id)

        self.assertIsInstance(basket, ShoppingBasket)
        self.assertEquals(user_id, basket.user_id)
