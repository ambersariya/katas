from abc import abstractmethod
from typing import List, Protocol, Final

from password_validation.rules.rules import Rule
from password_validation.validation_result import ValidationResult
from password_validation.violations import Violation, Violations


def _remove_none_values(violations: list) -> list:
    return [violation for violation in violations if violation is not None]


class Strategy(Protocol):
    @abstractmethod
    def validate(self, password: str, rules: List[Rule]) -> ValidationResult:
        pass


class AllRulesPassStrategy(Strategy):
    _NUM_ALLOWED_VIOLATION: Final[int] = 0

    def validate(self, password: str, rules: List[Rule]) -> ValidationResult:
        if password is None:
            return ValidationResult(
                allowed_violations=self._NUM_ALLOWED_VIOLATION,
                violations=Violations(violations=[Violation('Password cannot be empty')])
            )

        violations = [rule.check(password=password) for rule in rules]
        violations = _remove_none_values(violations)

        return ValidationResult(
            allowed_violations=self._NUM_ALLOWED_VIOLATION,
            violations=Violations(violations)
        )


class AllowOneFailureStrategy(Strategy):
    _NUM_ALLOWED_VIOLATION: Final[int] = 1

    def validate(self, password: str, rules: List[Rule]) -> ValidationResult:
        self._ensure_has_atleast_2_rules(rules)
        violations = [rule.check(password=password) for rule in rules]
        violations = _remove_none_values(violations)

        return ValidationResult(
            allowed_violations=self._NUM_ALLOWED_VIOLATION,
            violations=Violations(violations)
        )

    @staticmethod
    def _ensure_has_atleast_2_rules(rules: list):
        if len(rules) < 2:
            raise ValueError("Provide at least 2 rules for password validation")
