from password_validation.rules.rules import HasMinPasswordLength, ContainsUnderscore, ContainsNumber, \
    ContainsLowercaseLetter, ContainsCapitalLetter

PASSWORD_LENGTH = 8


class PasswordValidator:
    def validate(self, password: str) -> bool:
        return HasMinPasswordLength(min_length=PASSWORD_LENGTH).check(password) \
               and ContainsCapitalLetter().check(password) \
               and ContainsLowercaseLetter().check(password) \
               and ContainsNumber().check(password) \
               and ContainsUnderscore().check(password)
