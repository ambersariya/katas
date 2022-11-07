from merchants_guide_to_galaxy.currency_repo import SymbolRepo
from merchants_guide_to_galaxy.metal import Metal


def roman_to_arabic(roman_symbol):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(roman_symbol):
        if i + 1 < len(roman_symbol) and roman_symbol[i:i + 2] in roman:
            num += roman[roman_symbol[i:i + 2]]
            i += 2
        else:
            num += roman[roman_symbol[i]]
            i += 1
    return num


class MetalConverter:
    def __init__(self, currency_repo: SymbolRepo):
        self.currency_repo = currency_repo

    def calculate_metal_value(self, data: str) -> None:
        metal = self.__calculate_value_from(data=data)
        self.currency_repo.add(symbol=metal)

    def __calculate_value_from(self, data) -> Metal:
        split_data = list(filter(lambda u: u.lower() not in ['is', 'credits'], data.split(' ')))
        credit_value = int(split_data.pop())
        metal = split_data.pop()
        roman_symbol = list(map(
            lambda curr: self.currency_repo.symbol_value(symbol=curr),
            split_data
        ))

        roman_symbol = ''.join(roman_symbol)
        arabic_value = roman_to_arabic(roman_symbol)
        credit_value /= arabic_value
        return Metal(value=credit_value, name=metal)
