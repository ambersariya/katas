from dataclasses import dataclass

from merchants_guide_to_galaxy.domain.currency import Currency
from merchants_guide_to_galaxy.domain.currency import CurrencyValue
from merchants_guide_to_galaxy.domain.error import NonExistingCurrency
from merchants_guide_to_galaxy.domain.intergalactic_symbols import IntergalacticSymbol
from merchants_guide_to_galaxy.domain.metal import Metal
from merchants_guide_to_galaxy.domain.roman_numerals_converter import roman_to_arabic
from merchants_guide_to_galaxy.domain.symbol_repo import SymbolRepo


@dataclass(init=True, frozen=True)
class Answer:
    query: str
    outcome: str


def __extract_currency_values(syms) -> list[CurrencyValue]:
    return [c.value for c in syms if isinstance(c, Currency)]


def __extract_metal_value(intergalactic_syms: list[IntergalacticSymbol]) -> int:
    metal_values = [sym for sym in intergalactic_syms if isinstance(sym, Metal)]
    return 1 if len(metal_values) == 0 else metal_values[0].value


def __format_answer_with_credits(query: str, syms: list[IntergalacticSymbol], answer_value: int) -> Answer:
    concatenated_query_symbols = ' '.join(list(map(lambda s: s.name, syms)))
    outcome_message = f"{concatenated_query_symbols} is {float(answer_value)}"
    outcome_message = f"{outcome_message} Credits" if 'Credits' in query else outcome_message
    return Answer(query=query, outcome=outcome_message)


def __answer_query(raw_data: str, symbol_repo: SymbolRepo) -> Answer:
    try:
        cleaned_query = __clean_query(raw_data)
        symbols: list[Currency | Metal] = list(map(
            lambda sym: symbol_repo.find_symbol_value(symbol=sym),
            cleaned_query
        ))
        currency_symbol_values = __extract_currency_values(symbols)
        metal_value = __extract_metal_value(symbols)
        roman_symbol = ''.join(currency_symbol_values)
        arabic_value = roman_to_arabic(roman_symbol) * metal_value
        return __format_answer_with_credits(
            query=raw_data,
            syms=symbols,
            answer_value=arabic_value
        )
    except NonExistingCurrency:
        return Answer(outcome="I have no idea what you are talking about", query=raw_data)


def __clean_query(raw_data) -> list[str]:
    return raw_data \
        .replace("how much is ", "") \
        .replace("how many Credits is ", "") \
        .replace(" ?", "") \
        .split(" ")


def __is_query(raw_query: str) -> bool:
    return raw_query.endswith("?")


def answer_queries_use_case(raw_data: str, symbol_repo: SymbolRepo) -> list[Answer]:
    return [
        __answer_query(raw_data=raw_query, symbol_repo=symbol_repo)
        for raw_query in raw_data.split("\n") if __is_query(raw_query)
    ]
