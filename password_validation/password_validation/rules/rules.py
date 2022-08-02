class CheckPasswordLength:
    def __init__(self, length: int):
        self._length = length

    def check(self, password: str) -> bool:
        return (password is not None) \
               and (len(password) >= self._length)


class CheckCapitalLetter:
    def check(self, password: str) -> bool:
        return password.lower() != password


class CheckLowercaseLetter:
    def check(self, password: str):
        return password.upper() != password


class CheckContainsNumber:
    def check(self, password: str):
        for character in password:
            if character.isnumeric():
                return True
        return False
