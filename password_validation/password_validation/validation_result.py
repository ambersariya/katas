from dataclasses import dataclass

from password_validation.violations import Violations


@dataclass(init=True)
class ValidationResult:
    violations: Violations
    fail: bool
