from unittest import TestCase
from unittest.mock import MagicMock

from shopping_basket.date_provider import DateProvider
from shopping_basket.product import Product, ProductId
from shopping_basket.shopping_basket import ShoppingBasket, ShoppingBasketItem
from shopping_basket.shopping_basket_repository import InMemoryShoppingBasketRepository
from shopping_basket.user import UserId


class InMemoryShoppingBasketRepositoryShould(TestCase):
    def test_return_no_shopping_basket_for_user(self):
        user_id = UserId('some-id')
        date_provider = MagicMock(DateProvider)
        repository = InMemoryShoppingBasketRepository(date_provider=date_provider)
        result = repository.basket_for(user_id=user_id)
        self.assertIsNone(result)

    def test_create_shopping_basket_only_when_we_add_an_item(self):
        user_id = UserId('some-id')
        basket_created_at = '15/06/2022'
        quantity = 5
        product = Product(ProductId('product-1'), name='the hobbit dvd', price=5)
        shopping_basket_item = ShoppingBasketItem.for_product(product=product, quantity=quantity)
        date_provider = MagicMock(DateProvider)
        date_provider.current_date.return_value = basket_created_at

        repository = InMemoryShoppingBasketRepository(date_provider=date_provider)
        repository.add_item(item=shopping_basket_item, user_id=user_id)
        result = repository.basket_for(user_id=user_id)

        self.assertIsInstance(result, ShoppingBasket)
        self.assertEqual(1, len(result.items))
