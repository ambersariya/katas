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
