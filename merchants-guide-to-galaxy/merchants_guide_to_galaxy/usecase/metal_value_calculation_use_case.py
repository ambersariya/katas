from functools import reduce

from merchants_guide_to_galaxy.domain.currency import Currency
from merchants_guide_to_galaxy.domain.symbol_repo import SymbolRepo
from merchants_guide_to_galaxy.domain.metal import Metal
from merchants_guide_to_galaxy.domain.roman_numerals_converter import roman_to_arabic


def credit_assignment(line: str):
    return line.lower().endswith("credits")


def metal_value_calculation_use_case(symbol_repo: SymbolRepo, raw_data: str) -> None:
    dataset = [
        line.replace(" is", "").replace(" Credits", "").split(" ")
        for line in raw_data.split("\n") if credit_assignment(line=line)
    ]

    def __extract_currency_values(c):
        if isinstance(c, Currency):
            return c.value

    for data in dataset:
        credit_value = int(data.pop())
        metal = data.pop()
        symbols = list(map(lambda curr: symbol_repo.find_symbol_value(symbol=curr), data))

        currency_symbol_values = map(__extract_currency_values, symbols)
        roman_symbol = ''.join(list(currency_symbol_values))
        arabic_value = roman_to_arabic(roman_symbol)
        credit_value /= arabic_value
        symbol_repo.add(symbol=Metal(value=credit_value, name=metal))
