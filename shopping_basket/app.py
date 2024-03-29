from typing import Any

from fastapi import FastAPI
from starlette import status

from shopping_basket.api.requests import AddItem
from shopping_basket.basket.infrastructure.in_memory_shopping_basket_repository import (
    InMemoryShoppingBasketRepository,
)
from shopping_basket.basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.core.value_objects import UserId
from shopping_basket.core.date_provider import DateProvider
from shopping_basket.core.email_gateway import FakeEmailGateway
from shopping_basket.core.messagebus import HANDLERS
from basket.shopping_basket_item_logger import ItemLogger
from shopping_basket.basket.discount.discount_calculator import DiscountCalculator
from shopping_basket.basket.discount.discount_strategy import (
    MultiCategoryDiscountStrategy,
    ThreeBooksDiscountStrategy,
)
from shopping_basket.order.handler import OrderConfirmedHandler
from shopping_basket.order.notification.order_confirmation import OrderConfirmation
from shopping_basket.payment.event import OrderConfirmed
from shopping_basket.product.infrastructure.in_memory_product_repository import (
    InMemoryProductRepository,
)
from shopping_basket.product.product import Product
from shopping_basket.product.product_category import ProductCategory
from shopping_basket.product.product_id import ProductId
from shopping_basket.product.product_service import ProductService
from shopping_basket.purchase.event import StockPurchased
from shopping_basket.purchase.handler import OrderMoreHandler
from shopping_basket.purchase.purchase_system import PurchaseSystem
from shopping_basket.stock.event import StockIsLow
from shopping_basket.stock.handler import StockUpdateHandler, StockPurchasedHandler
from shopping_basket.stock.infrastructure.in_memory_stock_repository import InMemoryStockRepository
from shopping_basket.stock.stock import Stock
from shopping_basket.stock.stock_management_service import StockManagementService

app = FastAPI()
PRODUCT_CATEGORIES = [ProductCategory.BOOK, ProductCategory.VIDEO]
DISCOUNT_STRATEGIES = [
    ThreeBooksDiscountStrategy(),
    MultiCategoryDiscountStrategy(PRODUCT_CATEGORIES),
]

date_provider = DateProvider()
shopping_basket_repository = InMemoryShoppingBasketRepository(date_provider=date_provider)
stock_repository = InMemoryStockRepository()
stock_management_service = StockManagementService(stock_repository=stock_repository)
product_repository = InMemoryProductRepository()
discount_calculator = DiscountCalculator([])
product_service = ProductService(
    product_repository=product_repository,
    stock_management_service=stock_management_service,
)
item_logger = ItemLogger()
shopping_basket_service = ShoppingBasketService(
    product_service=product_service,
    shopping_basket_repository=shopping_basket_repository,
    item_logger=item_logger,
    discount_calculator=discount_calculator,
)
purchase_system = PurchaseSystem()
stock_handler = StockUpdateHandler(stock_management_service=stock_management_service)
order_more_handler = OrderMoreHandler(purchase_system=purchase_system)
stock_purchase_handler = StockPurchasedHandler(stock_management_service=stock_management_service)
email_gateway = FakeEmailGateway()
order_confirmation = OrderConfirmation(email_gateway=email_gateway)
order_confirmed_handler = OrderConfirmedHandler(order_confirmation=order_confirmation)
HANDLERS[OrderConfirmed] = [stock_handler]
HANDLERS[StockIsLow] = [order_more_handler]
HANDLERS[StockPurchased] = [stock_purchase_handler]

# Add some products to repo
product_service.add_product(
    product=Product(
        id=ProductId("10002"),
        name="The Hobbit",
        price=5,
        category=ProductCategory.BOOK,
    ),
    stock=Stock(product_id=ProductId("10002"), available=5, reserved=0, min_available=5),
)
product_service.add_product(
    product=Product(
        id=ProductId("20001"),
        name="Game of Thrones",
        price=9,
        category=ProductCategory.VIDEO,
    ),
    stock=Stock(product_id=ProductId("20001"), available=5, reserved=0, min_available=5),
)
product_service.add_product(
    product=Product(
        id=ProductId("20110"),
        name="Breaking Bad",
        price=7,
        category=ProductCategory.VIDEO,
    ),
    stock=Stock(product_id=ProductId("20110"), available=5, reserved=0, min_available=5),
)


@app.get("/")
async def root() -> Any:
    return {"message": "Hello World"}


@app.post("/items/{user_id}/add-item", status_code=status.HTTP_204_NO_CONTENT)
async def add_item(user_id: str, item: AddItem) -> Any:
    shopping_basket_service.add_item(
        user_id=UserId(user_id), product_id=ProductId(item.product_id), quantity=item.quantity
    )


@app.get("/baskets/{user_id}", status_code=status.HTTP_200_OK)
async def basket_for(user_id: str) -> Any:
    return {"basket": shopping_basket_service.basket_for(user_id=UserId(user_id))}
