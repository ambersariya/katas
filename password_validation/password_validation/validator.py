from typing import List

from password_validation.rules.rules import Rule
from password_validation.strategies.strategy import Strategy


class PasswordValidator:
    def __init__(self, rules: List[Rule], strategy: Strategy):
        """"""
        self._rules = rules
        self._strategy = strategy

    def validate(self, password: str):
        return self._strategy.validate(password, self._rules)
