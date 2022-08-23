from shopping_basket.stock.stock_repository import StockRepository
from .event import StockIsLow
from ..basket.shopping_basket_items import ShoppingBasketItems
from ..core.messagebus import MessageBus
from ..product.event import ProductLowOnStock

from ..product.product_id import ProductId
from .stock import Stock


class StockManagementService:
    def __init__(self, stock_repository: StockRepository, message_bus: MessageBus) -> None:
        self.message_bus = message_bus
        self.stock_repository = stock_repository

    def reserve(self, product_id: ProductId, quantity: int) -> None:
        stock = self.stock_repository.find_by_id(product_id=product_id)
        updated_stock = stock.reserve(quantity)
        self.stock_repository.save_stock(updated_stock)

    def save_stock(self, stock: Stock) -> None:
        self.stock_repository.save_stock(stock)

    def update_stock(self, items: ShoppingBasketItems) -> None:
        for item in items.items():
            stock = self.stock_repository.find_by_id(product_id=item.id)
            stock = stock.reduce_reserved(quantity=item.quantity)
            self.stock_repository.save_stock(stock=stock)
            if not stock.is_enough_available():
                self.message_bus.handle(
                    event=StockIsLow(
                        product_id=stock.product_id,
                        order_quantity=stock.order_quantity()
                    )
                )
