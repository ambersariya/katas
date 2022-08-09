from unittest import TestCase
from unittest.mock import MagicMock

from shopping_basket.product import Product, ProductId
from shopping_basket.product_repository import ProductRepository
from shopping_basket.shopping_basket import ShoppingBasket, ShoppingBasketItems, ShoppingBasketItem
from shopping_basket.shopping_basket_repository import ShoppingBasketRepository
from shopping_basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.user import UserId


class ShoppingBasketServiceShould(TestCase):
    def test_raise_error_when_user_doesnt_have_a_basket(self):
        user_id = UserId('abc-123')
        shopping_basket_repository = MagicMock(ShoppingBasketRepository)
        product_repository = MagicMock(ProductRepository)

        basket_service = ShoppingBasketService(shopping_basket_repository, product_repository)
        shopping_basket_repository.basket_for.return_value = None

        with self.assertRaises(basket_service.ShoppingBasketNotFoundError):
            basket_service.basket_for(user_id)

        shopping_basket_repository.basket_for.assert_called_once()

    def test_return_basket_for_given_user(self):
        user_id = UserId('abc-123')
        basket_created_at = '15/06/2022'

        shopping_basket_repository = MagicMock(ShoppingBasketRepository)
        product_repository = MagicMock(ProductRepository)

        basket_service = ShoppingBasketService(shopping_basket_repository, product_repository)
        shopping_basket = ShoppingBasket(user_id=user_id, created_at=basket_created_at, items=[])

        shopping_basket_repository.basket_for.return_value = shopping_basket

        basket = basket_service.basket_for(user_id=user_id)

        self.assertIsInstance(basket, ShoppingBasket)
        self.assertEqual(user_id, basket.user_id)

    def test_create_shopping_basket_when_item_is_added_and_basket_shouldnt_exist(self):
        # given
        basket_created_at = '15/06/2022'
        user_id = UserId('abc-123')
        quantity = 2
        product = Product(ProductId('product-1'), name='the hobbit dvd', price=5)
        shopping_basket_item = ShoppingBasketItem.for_product(product=product, quantity=quantity)

        product_repository = MagicMock(ProductRepository)
        product_repository.find_product_by_id.return_value = product
        shopping_basket_repository = MagicMock(ShoppingBasketRepository)

        # when
        basket_service = ShoppingBasketService(shopping_basket_repository, product_repository)
        basket_service.add_item(user_id=user_id, product_id=product.id, quantity=quantity)

        # then
        shopping_basket_repository.add_item.assert_called_once_with(shopping_basket_item)
