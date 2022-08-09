from unittest import TestCase

from shopping_basket.shopping_basket import ShoppingBasket
from shopping_basket.shopping_basket_repository import InMemoryShoppingBasketRepository
from shopping_basket.user import UserId


class InMemoryShoppingBasketRepositoryShould(TestCase):
    def test_return_no_shopping_basket_for_user(self):
        user_id = UserId('some-id')
        repository = InMemoryShoppingBasketRepository()
        result = repository.basket_for(user_id=user_id)
        self.assertIsNone(result)

    def test_return_shopping_basket_for_user(self):
        user_id = UserId('some-id')
        basket_created_at = '15/06/2022'

        repository = InMemoryShoppingBasketRepository()
        repository.add(basket=ShoppingBasket(user_id=user_id, created_at=basket_created_at, items=None))
        result = repository.basket_for(user_id=user_id)

        self.assertIsInstance(result, ShoppingBasket)
