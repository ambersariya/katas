from typing import List, Protocol

from password_validation.rules.rules import Rule
from password_validation.violations import Violation, Violations


class Strategy(Protocol):
    def validate(self, password: str, rules: List[Rule]) -> Violations:
        pass


class AllRulesPassStrategy(Strategy):

    def validate(self, password: str, rules: List[Rule]) -> Violations:
        if password is None:
            return Violations(violations=[Violation('Password cannot be empty')])

        violations = [rule.check(password=password) for rule in rules]

        violations = self._filter_out_None_values(violations)
        return Violations(violations=violations)

    def _filter_out_None_values(self, violations):
        return [violation for violation in violations if violation is not None]
