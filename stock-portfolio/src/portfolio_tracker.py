class PortfolioTracker:
    def add_purchase(self, number_of_shares, stock, purchase_date):
        raise NotImplementedError()

    def add_sale(self, number_of_shares, stock, sell_date):
        raise NotImplementedError()

    def update_value(self, stock, value):
        raise NotImplementedError()

    def print_portfolio(self):
        raise NotImplementedError()
