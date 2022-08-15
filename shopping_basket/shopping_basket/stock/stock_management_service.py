from shopping_basket.product import ProductId
from shopping_basket.stock.stock_repository import StockRepository


class StockManagementService:
    def __init__(self, stock_repository: StockRepository):
        self.stock_repository = stock_repository

    def reserve(self, product_id: ProductId, quantity: int):
        stock = self.stock_repository.find_by_id(product_id=product_id)
        updated_stock = stock.reserve(quantity)
        self.stock_repository.save_stock(updated_stock)

    def save_stock(self, stock):
        self.stock_repository.save_stock(stock)