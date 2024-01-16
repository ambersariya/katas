import pytest

from shopping_cart_kata.shopping_cart import ShoppingCart, CartItems

PRODUCT_ICEBERG = "iceberg"
PRODUCT_TOMATO = "tomato"
PRODUCT_CHICKEN = "chicken"
PRODUCT_BREAD = "bread"
PRODUCT_CORN = "corn"
PROMO_5 = 5.0
PROMO_10 = 10.0

PRINTED_CART = """-
| Product name | Price with VAT | Quantity |
| - | - | - |
| Iceberg | 2.17 | 3 |
| Tomato | 0.73 | 1 |
| Chicken | 1.83 | 1 |
| Bread | 0.88 | 2|
| Corn | 1.50 | 1 |
| - |
| Promotion: 5% off with code PROMO_5 |
-
| Total products: 8 |
| Total price: 11.71 |
-"""

CART_ITEMS = CartItems()


@pytest.fixture
def shopping_cart():
    return ShoppingCart()


def test_print_shopping_cart_contents(shopping_cart):
    shopping_cart.add_item(PRODUCT_ICEBERG)
    shopping_cart.add_item(PRODUCT_ICEBERG)
    shopping_cart.add_item(PRODUCT_ICEBERG)
    shopping_cart.add_item(PRODUCT_TOMATO)
    shopping_cart.add_item(PRODUCT_CHICKEN)
    shopping_cart.add_item(PRODUCT_BREAD)
    shopping_cart.add_item(PRODUCT_BREAD)
    shopping_cart.add_item(PRODUCT_CORN)
    shopping_cart.apply_discount(PROMO_5)
    shopping_cart_items = shopping_cart.print_shopping_cart()

    assert CART_ITEMS == shopping_cart_items
