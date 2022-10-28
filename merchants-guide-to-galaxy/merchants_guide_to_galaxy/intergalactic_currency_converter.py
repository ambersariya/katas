from merchants_guide_to_galaxy.currency_repo import CurrencyRepo, Currency, CurrencyValue


class IntergalacticCurrencyConverter:

    def __init__(self, currency_repo: CurrencyRepo):
        self.currency_repo = currency_repo

    def execute_conversion(self, raw_data: str) -> None:
        dataset = [line for line in raw_data.split("\n") if len(line) > 0]
        for data in dataset:
            split_data = data.split(" ")
            self.currency_repo.add(currency=Currency(name=split_data[0], value=CurrencyValue[split_data[2]]))
