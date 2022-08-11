from typing import Final
from unittest import TestCase
from unittest.mock import MagicMock, patch

from shopping_basket.console_logging_decorator import ConsoleLoggingDecorator
from shopping_basket.product import ProductId
from shopping_basket.product_service import ProductService
from shopping_basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.user import User, UserId

USER_ID: Final[UserId] = UserId('some-id')
PRODUCT_ID: Final[ProductId] = ProductId('product-1')
QUANTITY = 5


class ConsoleLoggingDecoratorShould(TestCase):
    def setUp(self) -> None:
        self.basket_service = MagicMock(ShoppingBasketService)
        self.decorator = ConsoleLoggingDecorator(self.basket_service)

    @patch('builtins.print')
    def test_log_nothing_when_we_add_non_existent_product_to_basket(self, mock_print):
        self.basket_service.add_item.side_effect = ProductService.ProductNotFoundError()

        self.decorator.add_item(user_id=USER_ID, product_id=PRODUCT_ID, quantity=QUANTITY)
        self.basket_service.add_item.assert_called_once_with(
            user_id=USER_ID, product_id=PRODUCT_ID, quantity=QUANTITY)
        mock_print.assert_not_called()

    @patch('builtins.print')
    def test_log_message_when_we_add_a_product_to_basket(self, mock_print):
        expected_log_message = f'[ITEM ADDED TO SHOPPING CART]: User[{USER_ID}], ' \
                               f'Product[{PRODUCT_ID}], Quantity[{QUANTITY}]'
        self.decorator.add_item(user_id=USER_ID, product_id=PRODUCT_ID, quantity=QUANTITY)

        self.basket_service.add_item.assert_called_once_with(
            user_id=USER_ID, product_id=PRODUCT_ID, quantity=QUANTITY)
        mock_print.assert_called_with(expected_log_message)
