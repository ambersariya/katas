from typing import Protocol


class Rule(Protocol):
    def check(self, password: str) -> bool:
        pass


class HasMinPasswordLength(Rule):
    def __init__(self, length: int):
        self._length = length

    def check(self, password: str) -> bool:
        return (password is not None) \
               and (len(password) >= self._length)


class CheckCapitalLetter(Rule):
    def check(self, password: str) -> bool:
        return password.lower() != password


class CheckLowercaseLetter(Rule):
    def check(self, password: str) -> bool:
        return password.upper() != password


class CheckContainsNumber(Rule):
    def check(self, password: str) -> bool:
        for character in password:
            if character.isnumeric():
                return True
        return False


class CheckContainsUnderscore(Rule):
    def check(self, password: str) -> bool:
        return '_' in password
