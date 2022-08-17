from typing import Protocol, List

from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.discount.discount import ThreeBooksDiscount, MultiCategoryDiscount, Discount
from shopping_basket.product.product_category import ProductCategory


class DiscountStrategy(Protocol):

    def apply(self, basket: ShoppingBasket) -> Discount:
        pass


class ThreeBooksDiscountStrategy(DiscountStrategy):
    MIN_BOOKS = 3

    def apply(self, basket: ShoppingBasket) -> Discount:
        if self._number_of_books(basket) >= self.MIN_BOOKS:
            return ThreeBooksDiscount()

    @staticmethod
    def _number_of_books(basket) -> int:
        books = 0
        for item in basket.items:
            if item.category == ProductCategory.BOOK:
                books += item.quantity
        return books


class MultiCategoryDiscountStrategy(DiscountStrategy):
    MIN_QUANTITY = 1

    def __init__(self, categories: List[ProductCategory]):
        self._categories = categories

    def apply(self, basket: ShoppingBasket) -> Discount:
        category_list = self._categories
        for item in basket.items:
            if item.category in category_list:
                category_list.remove(item.category)
        if len(category_list) is 0:
            return MultiCategoryDiscount()
