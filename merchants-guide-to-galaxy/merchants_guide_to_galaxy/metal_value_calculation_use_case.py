from merchants_guide_to_galaxy.currency_repo import SymbolRepo
from merchants_guide_to_galaxy.metal import Metal
from merchants_guide_to_galaxy.roman_numerals_converter import roman_to_arabic


def credit_assignment(line: str):
    return line.lower().endswith("credits")


def metal_value_calculation_use_case(symbol_repo: SymbolRepo, raw_data: str) -> None:
    dataset = [line.replace(" is", "").replace(" Credits", "").split(" ") for line in raw_data.split("\n") if
               credit_assignment(line=line)]
    for data in dataset:
        credit_value = int(data.pop())
        metal = data.pop()
        roman_symbol = list(map(
            lambda curr: symbol_repo.symbol_value(symbol=curr),
            data
        ))
        roman_symbol = ''.join(roman_symbol)
        arabic_value = roman_to_arabic(roman_symbol)
        credit_value /= arabic_value
        symbol_repo.add(symbol=Metal(value=credit_value, name=metal))
