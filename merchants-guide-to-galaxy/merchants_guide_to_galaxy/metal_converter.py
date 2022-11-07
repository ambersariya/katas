from merchants_guide_to_galaxy.currency_repo import CurrencyRepo


class MetalConverter:

    def __init__(self, currency_repo: CurrencyRepo):
        self.currency_repo = currency_repo

    def calculate_metal_value(self, numeral, metal, credit) -> int:
        pass
