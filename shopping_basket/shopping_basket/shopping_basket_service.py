class ShoppingBasketService:
    def basket_for(self, user_id):
        raise NotImplementedError()

    def add_item(self, user_id, product_id, quantity):
        raise NotImplementedError()
