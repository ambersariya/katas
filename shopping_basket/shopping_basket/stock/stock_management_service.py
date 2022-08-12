from shopping_basket.product import ProductId


class StockManagementService:
    def reserve(self, product_id: ProductId, quantity: int):
        raise NotImplementedError()

