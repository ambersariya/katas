from typing import List

from password_validation.rules.rules import Rule, HasMinPasswordLength, ContainsCapitalLetter, ContainsLowercaseLetter, \
    ContainsNumber, ContainsUnderscore
from password_validation.strategies.strategy import Strategy
from password_validation.validator import PasswordValidator


class PasswordValidatorBuilder:
    _rules: List[Rule]
    _strategy: Strategy

    def __init__(self):
        self._rules = []

    def has_min_password_length(self, required_length: int):
        self._rules.append(HasMinPasswordLength(required_length))
        return self

    def contains_capital_letter(self):
        self._rules.append(ContainsCapitalLetter())
        return self

    def contains_lower_case_letter(self):
        self._rules.append(ContainsLowercaseLetter())
        return self

    def contains_number(self):
        self._rules.append(ContainsNumber())
        return self

    def contains_underscore(self):
        self._rules.append(ContainsUnderscore())
        return self

    def with_strategy(self, strategy: Strategy):
        self._strategy = strategy
        return self

    def build(self):
        return PasswordValidator(self._rules, self._strategy)
