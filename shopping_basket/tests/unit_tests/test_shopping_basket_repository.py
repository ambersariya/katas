from typing import Final
from unittest import TestCase
from unittest.mock import MagicMock

from shopping_basket.date_provider import DateProvider
from shopping_basket.product import Product, ProductId
from shopping_basket.shopping_basket import ShoppingBasket, ShoppingBasketItem
from shopping_basket.shopping_basket_repository import InMemoryShoppingBasketRepository
from shopping_basket.user import UserId

USER_ID: Final[UserId] = UserId('some-id')
PRODUCT: Final[Product] = Product(ProductId('product-1'), name='the hobbit dvd', price=5)
BASKET_ITEM: Final[ShoppingBasketItem] = ShoppingBasketItem.for_product(product=PRODUCT, quantity=5)


class InMemoryShoppingBasketRepositoryShould(TestCase):
    def setUp(self) -> None:
        self.date_provider = MagicMock(DateProvider)
        self.repository = InMemoryShoppingBasketRepository(date_provider=self.date_provider)

    def test_return_no_shopping_basket_for_user(self):
        result = self.repository.basket_for(user_id=USER_ID)
        self.assertIsNone(result)

    def test_create_shopping_basket_only_when_we_add_an_item(self):
        self.date_provider.current_date.return_value = '15/06/2022'
        self.repository.add_item(item=BASKET_ITEM, user_id=USER_ID)

        result = self.repository.basket_for(user_id=USER_ID)

        self.assertIsInstance(result, ShoppingBasket)
        self.assertEqual(1, len(result.items))
