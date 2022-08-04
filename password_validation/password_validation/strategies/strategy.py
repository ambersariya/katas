from abc import abstractmethod
from typing import List, Protocol, Final

from password_validation.rules.rules import Rule
from password_validation.validation_result import ValidationResult
from password_validation.violations import Violation, Violations


class Strategy(Protocol):
    @abstractmethod
    def validate(self, password: str, rules: List[Rule]) -> ValidationResult:
        pass


class AllRulesPassStrategy(Strategy):
    def validate(self, password: str, rules: List[Rule]) -> ValidationResult:
        if password is None:
            return Violations(violations=[Violation('Password cannot be empty')])

        violations = [rule.check(password=password) for rule in rules]

        violations = self._filter_out_None_values(violations)
        return Violations(violations=violations)

    def _filter_out_None_values(self, violations):
        return [violation for violation in violations if violation is not None]


class AllowOneFailureStrategy(Strategy):
    _NUM_ALLOWED_VIOLATION: Final[int] = 1

    def validate(self, password: str, rules: List[Rule]) -> ValidationResult:
        self._ensure_atleast_2_rules(rules)
        violations = [rule.check(password=password) for rule in rules]
        violations = self._remove_none_values(violations)
        return ValidationResult(
            violations=Violations(violations),
            fail=self._is_failure(violations))

    def _is_failure(self, violations: list) -> bool:
        num_violations = 0
        for v in violations:
            if isinstance(v, Violation):
                num_violations += 1

        return num_violations > self._NUM_ALLOWED_VIOLATION

    @staticmethod
    def _remove_none_values(violations):
        return [violation for violation in violations if violation is not None]

    @staticmethod
    def _ensure_atleast_2_rules(rules: list):
        if len(rules) < 2:
            raise ValueError("Provide at least 2 rules for password validation")
