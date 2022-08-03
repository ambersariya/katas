from typing import Protocol, Optional

from password_validation.violations import Violation


class Rule(Protocol):
    def check(self, password: str) -> Optional[Violation]:
        pass


class HasMinPasswordLength(Rule):
    def __init__(self, min_length: int):
        self._violation_message = f"Password length needs to be at least {min_length} characters long"
        self._min_length = min_length

    def check(self, password: str) -> Optional[Violation]:
        if len(password) < self._min_length:
            return Violation(self._violation_message)


class ContainsCapitalLetter(Rule):
    def check(self, password: str) -> Optional[Violation]:
        if password.lower() == password:
            return Violation("Password should contain at least one capital letter")


class ContainsLowercaseLetter(Rule):
    def check(self, password: str) -> Optional[Violation]:
        if password.upper() == password:
            return Violation("Password should contain at least one lowercase letter")


class ContainsNumber(Rule):
    def check(self, password: str) -> Optional[Violation]:
        for character in password:
            if character.isnumeric():
                return
        return Violation("Password should contain at least one number")


class ContainsUnderscore(Rule):
    def check(self, password: str) -> Optional[Violation]:
        if '_' not in password:
            return Violation("Password should contain at least one underscore")
