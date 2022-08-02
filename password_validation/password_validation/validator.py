from typing import List

from password_validation.rules.rules import Rule

PASSWORD_LENGTH = 8


class PasswordValidator:
    def __init__(self, rules: List[Rule]):
        """"""
        self._rules = rules

    def validate(self, password: str):
        if password is None:
            return False
        results = [rule.check(password=password) for rule in self._rules]
        return False not in results
