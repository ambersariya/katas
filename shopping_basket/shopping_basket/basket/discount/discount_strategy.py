from typing import List, Protocol

from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.basket.discount.discount import Discount
from shopping_basket.product.product_category import ProductCategory


class DiscountStrategy(Protocol):
    def apply(self, basket: ShoppingBasket) -> Discount:
        pass


class ThreeBooksDiscountStrategy(DiscountStrategy):
    MIN_BOOKS = 3
    PERCENTAGE = 10.00

    def apply(self, basket: ShoppingBasket) -> Discount:
        if self._number_of_books(basket) >= self.MIN_BOOKS:
            return Discount(percentage=self.PERCENTAGE, amount=self._calculate(basket))

    @staticmethod
    def _number_of_books(basket) -> int:
        books = 0
        for item in basket.items.items():
            if item.category == ProductCategory.BOOK:
                books += item.quantity
        return books

    def _calculate(self, basket: ShoppingBasket) -> float:
        return basket.total_amount() * (self.PERCENTAGE / 100)


class MultiCategoryDiscountStrategy(DiscountStrategy):
    PERCENTAGE = 20.00

    def __init__(self, categories: List[ProductCategory]):
        self._categories = categories

    def apply(self, basket: ShoppingBasket) -> Discount:
        category_list = self._categories.copy()
        for item in basket.items.items():
            if item.category in category_list:
                category_list.remove(item.category)
        if len(category_list) == 0:
            return Discount(percentage=self.PERCENTAGE, amount=self._calculate(basket))

    def _calculate(self, basket: ShoppingBasket) -> float:
        return basket.total_amount() * (self.PERCENTAGE / 100)
