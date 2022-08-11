from typing import Final
from unittest import TestCase
from unittest.mock import MagicMock

from shopping_basket.date_provider import DateProvider
from shopping_basket.product import Product, ProductId
from shopping_basket.shopping_basket import ShoppingBasket, ShoppingBasketItem
from shopping_basket.shopping_basket_repository import InMemoryShoppingBasketRepository
from shopping_basket.user import UserId

USER_ID: Final[UserId] = UserId('some-id')
PRODUCT_1: Final[Product] = Product(ProductId('product-1'), name='the hobbit dvd', price=5)
PRODUCT_2: Final[Product] = Product(ProductId('product-2'), name='Topgun DVD', price=5)
BASKET_ITEM_1: Final[ShoppingBasketItem] = ShoppingBasketItem.for_product(product=PRODUCT_1, quantity=5)
BASKET_ITEM_2: Final[ShoppingBasketItem] = ShoppingBasketItem.for_product(product=PRODUCT_2, quantity=5)


class InMemoryShoppingBasketRepositoryShould(TestCase):
    def setUp(self) -> None:
        self.date_provider = MagicMock(DateProvider)
        self.repository = InMemoryShoppingBasketRepository(date_provider=self.date_provider)

    def test_return_no_shopping_basket_for_user(self):
        result = self.repository.basket_for(user_id=USER_ID)
        self.assertIsNone(result)

    def test_create_shopping_basket_only_when_we_add_an_item(self):
        self.date_provider.current_date.return_value = '15/06/2022'
        self.repository.add_item(item=BASKET_ITEM_1, user_id=USER_ID)

        result = self.repository.basket_for(user_id=USER_ID)

        self.assertIsInstance(result, ShoppingBasket)
        self.assertEqual(1, len(result.items))

    def test_save_more_than_one_kind_of_item_with_different_id(self):
        self.date_provider.current_date.return_value = '15/06/2022'
        self.repository.add_item(item=BASKET_ITEM_1, user_id=USER_ID)
        self.repository.add_item(item=BASKET_ITEM_2, user_id=USER_ID)

        result = self.repository.basket_for(user_id=USER_ID)

        self.assertIsInstance(result, ShoppingBasket)
        self.assertEqual(2, len(result.items))
        self.assertEqual(BASKET_ITEM_1, result.items[0])
        self.assertEqual(BASKET_ITEM_2, result.items[1])

    def test_update_quantity_and_total_of_item_that_is_added_twice(self):
        self.date_provider.current_date.return_value = '15/06/2022'
        self.repository.add_item(item=BASKET_ITEM_1, user_id=USER_ID)
        self.repository.add_item(item=BASKET_ITEM_1, user_id=USER_ID)

        result = self.repository.basket_for(user_id=USER_ID)

        self.assertIsInstance(result, ShoppingBasket)
        self.assertEqual(1, len(result.items))
        item = result.items[0]
        self.assertIsInstance(item, ShoppingBasketItem)
        self.assertEqual(10, item.quantity)
        self.assertEqual(50, item.total())
