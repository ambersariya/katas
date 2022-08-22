from typing import Final

from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem
from shopping_basket.basket.shopping_basket_items import ShoppingBasketItems
from shopping_basket.basket.user import UserId
from shopping_basket.discount.discount import Discount
from shopping_basket.discount.discount_strategy import (
    ThreeBooksDiscountStrategy,
    MultiCategoryDiscountStrategy,
)
from shopping_basket.discount.discounted_shopping_basket import DiscountedShoppingBasket
from shopping_basket.order.order import UnpaidOrder, PaidOrder
from shopping_basket.order.order_id import OrderId
from shopping_basket.payment.payment_details import PaymentDetails
from shopping_basket.payment.payment_reference import PaymentReference
from shopping_basket.product.product import Product
from shopping_basket.product.product_category import ProductCategory
from shopping_basket.product.product_id import ProductId
from shopping_basket.stock.stock import Stock

USER_ID: Final[UserId] = UserId("some-id")

PRODUCT_ID_BOOK: Final[ProductId] = ProductId("product-1")
PRODUCT_ID_VIDEO: Final[ProductId] = ProductId("product-2")

PRODUCT_BOOK: Final[Product] = Product(
    id=PRODUCT_ID_BOOK,
    name="architectural design patterns in python",
    price=31,
    category=ProductCategory.BOOK,
)
PRODUCT_VIDEO: Final[Product] = Product(
    id=PRODUCT_ID_VIDEO, name="the hobbit dvd", price=5, category=ProductCategory.VIDEO
)

NEW_VIDEO_PRODUCT: Final[Product] = Product(
    id=PRODUCT_ID_VIDEO,
    name="the hobbit 4k remastered 15hrs directors uncut",
    price=5,
    category=ProductCategory.VIDEO,
)

STOCK_BOOK: Final[Stock] = Stock(available=5, reserved=0, product_id=PRODUCT_ID_BOOK)
STOCK_VIDEO: Final[Stock] = Stock(available=5, reserved=0, product_id=PRODUCT_ID_VIDEO)
UPDATED_STOCK_VIDEO: Final[Stock] = Stock(
    available=0, reserved=5, product_id=PRODUCT_ID_VIDEO
)

QUANTITY_FIVE: Final[int] = 5
QUANTITY_TWO: Final[int] = 2

BASKET_ITEM_QUANTITY_FIVE: Final[ShoppingBasketItem] = ShoppingBasketItem.for_product(
    product=PRODUCT_BOOK, quantity=QUANTITY_FIVE
)
BASKET_ITEM_QUANTITY_TWO: Final[ShoppingBasketItem] = ShoppingBasketItem.for_product(
    product=PRODUCT_VIDEO, quantity=QUANTITY_TWO
)
BASKET_CREATION_DATE: Final[str] = "15/06/2022"
SHOPPING_BASKET: Final[ShoppingBasket] = ShoppingBasket(
    user_id=USER_ID,
    created_at=BASKET_CREATION_DATE,
    items=ShoppingBasketItems(items=[BASKET_ITEM_QUANTITY_TWO]),
)
DISCOUNTABLE_SHOPPING_BASKET: Final[ShoppingBasket] = ShoppingBasket(
    user_id=USER_ID,
    created_at=BASKET_CREATION_DATE,
    items=ShoppingBasketItems(items=[BASKET_ITEM_QUANTITY_FIVE]),
)

DISCOUNT: Final[Discount] = Discount(percentage=10, amount=15.5)
DISCOUNTED_SHOPPING_BASKET: Final[
    ShoppingBasket
] = DiscountedShoppingBasket.from_basket(
    basket=DISCOUNTABLE_SHOPPING_BASKET, discount=DISCOUNT
)
CATEGORIES = [ProductCategory.BOOK, ProductCategory.VIDEO]
STRATEGIES = [ThreeBooksDiscountStrategy(), MultiCategoryDiscountStrategy(CATEGORIES)]

ORDER_ID = OrderId("order-01")
UNPAID_ORDER = UnpaidOrder(user_id=USER_ID, shopping_basket=SHOPPING_BASKET)
PAID_ORDER = PaidOrder.from_unpaid_order(order_id=ORDER_ID, order=UNPAID_ORDER)
PAYMENT_DETAILS = PaymentDetails()
PAYMENT_REFERENCE = PaymentReference("payment-reference-01")
