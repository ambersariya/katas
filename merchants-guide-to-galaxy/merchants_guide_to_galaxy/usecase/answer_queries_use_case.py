from dataclasses import dataclass

from merchants_guide_to_galaxy.domain.symbol_repo import SymbolRepo
from merchants_guide_to_galaxy.domain.roman_numerals_converter import roman_to_arabic


@dataclass(init=True, frozen=True)
class Answer:
    query: str
    outcome: str


def answer_queries_use_case(raw_data: str, symbol_repo: SymbolRepo) -> list[Answer]:
    intergalactic_gibberish = raw_data.replace("how much is ", "").replace(" ?", "")
    roman_symbol = list(map(
        lambda curr: symbol_repo.symbol_value(symbol=curr),
        intergalactic_gibberish.split(" ")
    ))
    roman_symbol = ''.join(roman_symbol)
    arabic_value = roman_to_arabic(roman_symbol)
    return [Answer(query=raw_data, outcome=f"{intergalactic_gibberish} is {arabic_value}")]
