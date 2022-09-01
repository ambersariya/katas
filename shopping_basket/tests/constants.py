from copy import copy
from typing import Final
from unittest.mock import MagicMock

from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem
from shopping_basket.basket.shopping_basket_items import ShoppingBasketItems
from shopping_basket.basket.user import UserId
from shopping_basket.core.event import EventHandler
from shopping_basket.discount.discount import Discount
from shopping_basket.discount.discount_strategy import (
    MultiCategoryDiscountStrategy,
    ThreeBooksDiscountStrategy,
)
from shopping_basket.discount.discounted_shopping_basket import DiscountedShoppingBasket
from shopping_basket.order.order import PaidOrder, UnpaidOrder
from shopping_basket.order.order_id import OrderId
from shopping_basket.payment.payment_details import PaymentDetails
from shopping_basket.payment.payment_reference import PaymentReference
from shopping_basket.product.product import Product
from shopping_basket.product.product_category import ProductCategory
from shopping_basket.product.product_id import ProductId
from shopping_basket.stock.stock import Stock

USER_ID: Final[UserId] = UserId("some-id")

PRODUCT_ID_LORD_OF_THE_RINGS: Final[ProductId] = ProductId("10001")
PRODUCT_ID_BREAKING_BAD: Final[ProductId] = ProductId("20110")
PRODUCT_ID_HOBBIT: Final[ProductId] = ProductId("10002")
PRODUCT_ID_GAME_OF_THRONES: Final[ProductId] = ProductId("20001")


PRODUCT_BOOK_LORD_OF_THE_RINGS: Final[Product] = Product(
    id=PRODUCT_ID_LORD_OF_THE_RINGS,
    name="architectural design patterns in python",
    price=31,
    category=ProductCategory.BOOK,
)
PRODUCT_VIDEO_BREAKING_BAD: Final[Product] = Product(
    id=PRODUCT_ID_BREAKING_BAD, name="Breaking Bad", price=5, category=ProductCategory.VIDEO
)

UPDATED_PRODUCT_WITH_OLD_ID: Final[Product] = Product(
    id=PRODUCT_ID_BREAKING_BAD,
    name="breaking bad 4k remastered",
    price=5,
    category=ProductCategory.VIDEO,
)

STOCK_BOOK_LORD_OF_THE_RINGS: Final[Stock] = Stock(
    available=5, reserved=0, product_id=PRODUCT_ID_LORD_OF_THE_RINGS, min_available=5
)
STOCK_VIDEO_BREAKING_BAD: Final[Stock] = Stock(
    available=5, reserved=0, product_id=PRODUCT_ID_BREAKING_BAD, min_available=5
)
RESERVED_STOCK_VIDEO_BREAKING_BAD: Final[Stock] = Stock(
    available=0, reserved=5, product_id=PRODUCT_ID_BREAKING_BAD, min_available=5
)
SOLD_STOCK_VIDEO_BREAKING_BAD: Final[Stock] = Stock(
    available=0, reserved=0, product_id=PRODUCT_ID_BREAKING_BAD, min_available=5
)
PURCHASED_STOCK_VIDEO_BREAKING_BAD = copy(STOCK_VIDEO_BREAKING_BAD)
QUANTITY_FIVE: Final[int] = 5
QUANTITY_TWO: Final[int] = 2

BASKET_ITEM_LORD_OF_THE_RINGS_QUANTITY_FIVE: Final[
    ShoppingBasketItem
] = ShoppingBasketItem.for_product(product=PRODUCT_BOOK_LORD_OF_THE_RINGS, quantity=QUANTITY_FIVE)
BASKET_ITEM_BREAKING_BAD_QUANTITY_TWO: Final[ShoppingBasketItem] = ShoppingBasketItem.for_product(
    product=PRODUCT_VIDEO_BREAKING_BAD, quantity=QUANTITY_TWO
)
BASKET_CREATION_DATE: Final[str] = "15/06/2022"
SHOPPING_BASKET_WITH_ONE_ITEM: Final[ShoppingBasket] = ShoppingBasket(
    user_id=USER_ID,
    created_at=BASKET_CREATION_DATE,
    items=ShoppingBasketItems(items=[BASKET_ITEM_BREAKING_BAD_QUANTITY_TWO]),
)
DISCOUNTABLE_SHOPPING_BASKET_WITH_ONE_ITEM: Final[ShoppingBasket] = ShoppingBasket(
    user_id=USER_ID,
    created_at=BASKET_CREATION_DATE,
    items=ShoppingBasketItems(items=[BASKET_ITEM_LORD_OF_THE_RINGS_QUANTITY_FIVE]),
)

DISCOUNT: Final[Discount] = Discount(percentage=10, amount=15.5)
DISCOUNTED_SHOPPING_BASKET: Final[ShoppingBasket] = DiscountedShoppingBasket.from_basket(
    basket=DISCOUNTABLE_SHOPPING_BASKET_WITH_ONE_ITEM, discount=DISCOUNT
)
PRODUCT_CATEGORIES = [ProductCategory.BOOK, ProductCategory.VIDEO]
DISCOUNT_STRATEGIES = [
    ThreeBooksDiscountStrategy(),
    MultiCategoryDiscountStrategy(PRODUCT_CATEGORIES),
]

ORDER_ID = OrderId("order-01")
UNPAID_ORDER = UnpaidOrder(user_id=USER_ID, shopping_basket=SHOPPING_BASKET_WITH_ONE_ITEM)
PAID_ORDER = PaidOrder.from_unpaid_order(order_id=ORDER_ID, order=UNPAID_ORDER)
PAYMENT_DETAILS = PaymentDetails()
PAYMENT_REFERENCE = PaymentReference("payment-reference-01")
