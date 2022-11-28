from merchants_guide_to_galaxy.symbol_repo import SymbolRepo, Currency, CurrencyValue


def currency_assignment(line: str):
    return "is" in line and not line.lower().endswith("credits") and not line.endswith("?")


def currency_assignment_use_case(symbol_repo: SymbolRepo, raw_data: str) -> None:
    dataset = [line.split(" ") for line in raw_data.split("\n") if currency_assignment(line=line)]
    for data in dataset:
        currency_name, _, currency_value = data
        symbol_repo.add(symbol=Currency(name=currency_name, value=CurrencyValue[currency_value]))

