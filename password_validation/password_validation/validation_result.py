from dataclasses import dataclass

from password_validation.violations import Violations, Violation


@dataclass(init=True)
class ValidationResult:
    violations: Violations
    allowed_violations: int

    @property
    def fail(self):
        num_violations = 0
        for v in self.violations:
            if isinstance(v, Violation):
                num_violations += 1

        return num_violations > self.allowed_violations
