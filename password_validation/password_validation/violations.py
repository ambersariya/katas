from dataclasses import dataclass
from typing import List


@dataclass(init=True, frozen=True)
class Violation:
    message: str


class Violations:
    def __init__(self, violations=None):
        if violations is None:
            violations = []
        self._violations = violations

    def add(self, violation: Violation):
        self._violations.append(violation)

    def __len__(self):
        return len(self._violations)

    def __iter__(self):
        return iter(self._violations)
