from shopping_basket.basket.shopping_basket_items import ShoppingBasketItems
from shopping_basket.core.messagebus import MessageBus
from shopping_basket.product.product_id import ProductId
from shopping_basket.stock.event import StockIsLow
from shopping_basket.stock.stock import Stock
from shopping_basket.stock.stock_repository import StockRepository


class StockManagementService:
    def __init__(
        self, stock_repository: StockRepository, message_bus: MessageBus
    ) -> None:
        self.message_bus = message_bus
        self.stock_repository = stock_repository

    def reserve(self, product_id: ProductId, quantity: int) -> None:
        stock = self.stock_repository.find_by_id(product_id=product_id)
        updated_stock = stock.reserve(quantity=quantity)
        self.stock_repository.save_stock(stock=updated_stock)

    def save_stock(self, stock: Stock) -> None:
        self.stock_repository.save_stock(stock)

    def increase_stock(self, product_id: ProductId, quantity: int) -> None:
        stock = self.stock_repository.find_by_id(product_id=product_id)
        updated_stock = stock.increase_quantity(quantity=quantity)
        self.stock_repository.save_stock(stock=updated_stock)

    def update_stock(self, items: ShoppingBasketItems) -> None:
        for item in items.items():
            stock = self.stock_repository.find_by_id(product_id=item.id)
            stock = stock.reduce_reserved(quantity=item.quantity)
            self.stock_repository.save_stock(stock=stock)
            if not stock.is_enough_available():
                self.message_bus.handle(
                    event=StockIsLow(
                        product_id=stock.product_id,
                        order_quantity=stock.order_quantity(),
                    )
                )
