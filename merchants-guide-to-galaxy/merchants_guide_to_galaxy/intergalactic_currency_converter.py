from merchants_guide_to_galaxy.metal_value_calculation_use_case import metal_value_calculation_use_case
from merchants_guide_to_galaxy.currency_assignment_use_case import currency_assignment_use_case
from merchants_guide_to_galaxy.currency_repo import SymbolRepo
from merchants_guide_to_galaxy.error import NonExistingCurrency


class IntergalacticCurrencyConverter:

    def __init__(self, currency_repo: SymbolRepo):
        self.currency_repo = currency_repo

    def execute_conversion(self, raw_data: str) -> None:
        currency_assignment_use_case(symbol_repo=self.currency_repo, raw_data=raw_data)
        metal_value_calculation_use_case(symbol_repo=self.currency_repo, raw_data=raw_data)
        # dataset = [line for line in raw_data.split("\n") if len(line) > 0]
        # for data in dataset:
        #     # We have logic that decides on whether the data in dataset has a ?
        #     if data.lower().endswith('credits'):
        #         # the entire sentence gets passed to met converter
        #         self.metal_converter.calculate_metal_value(data=data)
        #         continue
        #
        #     split_data = data.split(" ")
        #     if not data.lower().endswith('?'):
        #         self.currency_repo.add(currency=Currency(name=split_data[0], value=CurrencyValue[split_data[2]]))
        #     # the entire sentance gets passed in to something if it has a ?

    def __parse_data(self, data: list[str]) -> list[str | int]:
        result = []
        for element in data:
            try:
                currency = self.currency_repo.symbol_value(element)
                result.append(currency)
            except NonExistingCurrency:
                result.append(element)
