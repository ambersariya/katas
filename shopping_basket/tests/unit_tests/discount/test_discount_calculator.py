from typing import Final
from unittest import TestCase

from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem
from shopping_basket.basket.shopping_basket_items import ShoppingBasketItems
from shopping_basket.basket.user import UserId
from shopping_basket.discount.discount import ThreeBooksDiscount, Discount
from shopping_basket.discount.discount_calculator import DiscountCalculator
from shopping_basket.discount.discounted_shopping_basket import DiscountedShoppingBasket
from shopping_basket.product.product import Product
from shopping_basket.product.product_category import ProductCategory
from shopping_basket.product.product_id import ProductId

USER_ID: Final[UserId] = UserId('some-id')
PRODUCT: Final[Product] = Product(ProductId('product-1'), name='architectural design patterns in python', price=31,
                                  category=ProductCategory.BOOK)
QUANTITY_FIVE = 5
QUANTITY_TWO = 2
BASKET_ITEM_QUANTITY_FIVE: Final[ShoppingBasketItem] = ShoppingBasketItem.for_product(product=PRODUCT,
                                                                                      quantity=QUANTITY_FIVE)
BASKET_ITEM_QUANTITY_TWO: Final[ShoppingBasketItem] = ShoppingBasketItem.for_product(product=PRODUCT,
                                                                                     quantity=QUANTITY_TWO)
BASKET_CREATION_DATE = '15/06/2022'
DISCOUNT = ThreeBooksDiscount()
SHOPPING_BASKET = ShoppingBasket(user_id=USER_ID, created_at=BASKET_CREATION_DATE,
                                 items=ShoppingBasketItems(items=[BASKET_ITEM_QUANTITY_TWO]))
DISCOUNTABLE_SHOPPING_BASKET = ShoppingBasket(user_id=USER_ID, created_at=BASKET_CREATION_DATE,
                                              items=ShoppingBasketItems(items=[BASKET_ITEM_QUANTITY_FIVE])
                                              )

DISCOUNTED_SHOPPING_BASKET = DiscountedShoppingBasket.from_basket(basket=DISCOUNTABLE_SHOPPING_BASKET,
                                                                  discount=ThreeBooksDiscount())


class DiscountCalculatorShould(TestCase):

    def setUp(self):
        self.discount_calculator = DiscountCalculator()

    def test_return_shopping_basket_when_no_discount_is_applicable(self):
        discounted_basket = self.discount_calculator.apply_discount(SHOPPING_BASKET)
        self.assertEqual(SHOPPING_BASKET, discounted_basket)

    def test_return_discounted_shopping_basket_with_ten_percent_discount_when_it_contains_at_least_three_books(self):
        discounted_basket = self.discount_calculator.apply_discount(DISCOUNTABLE_SHOPPING_BASKET)

        self.assertEqual(DISCOUNTED_SHOPPING_BASKET, discounted_basket)
