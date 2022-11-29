from merchants_guide_to_galaxy.usecase.answer_printer import AnswerPrinter
from merchants_guide_to_galaxy.usecase.answer_queries_use_case import answer_queries_use_case
from merchants_guide_to_galaxy.usecase.metal_value_calculation_use_case import metal_value_calculation_use_case
from merchants_guide_to_galaxy.usecase.currency_assignment_use_case import currency_assignment_use_case
from merchants_guide_to_galaxy.domain.symbol_repo import SymbolRepo
from merchants_guide_to_galaxy.domain.error import NonExistingCurrency


class IntergalacticCurrencyConverter:

    def __init__(self, symbol_repo: SymbolRepo, answer_printer: AnswerPrinter):
        self.answer_printer = answer_printer
        self.symbol_repo = symbol_repo

    def execute_conversion(self, raw_data: str) -> None:
        currency_assignment_use_case(symbol_repo=self.symbol_repo, raw_data=raw_data)
        metal_value_calculation_use_case(symbol_repo=self.symbol_repo, raw_data=raw_data)
        answers = answer_queries_use_case(symbol_repo=self.symbol_repo, raw_data=raw_data)
        self.answer_printer.print(answers=answers)

    def __parse_data(self, data: list[str]) -> list[str | int]:
        result = []
        for element in data:
            try:
                currency = self.currency_repo.find_symbol_value(element)
                result.append(currency)
            except NonExistingCurrency:
                result.append(element)
