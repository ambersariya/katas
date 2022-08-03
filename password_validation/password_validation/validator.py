from typing import List

from password_validation.rules.rules import Rule
from password_validation.violations import Violations, Violation

PASSWORD_LENGTH = 8


class PasswordValidator:
    def __init__(self, rules: List[Rule]):
        """"""
        self._rules = rules

    def validate(self, password: str):
        if password is None:
            return Violations(violations=[Violation('Password cannot be empty')])

        violations = [rule.check(password=password) for rule in self._rules]
        violations = self._filter_out_None_values(violations)
        return Violations(violations=violations)

    def _filter_out_None_values(self, violations):
        return [violation for violation in violations if violation is not None]
