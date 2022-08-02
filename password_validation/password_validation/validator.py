from password_validation.rules.rules import HasMinPasswordLength

PASSWORD_LENGTH = 8


class PasswordValidator:
    def validate(self, password: str) -> bool:
        return HasMinPasswordLength(min_length=PASSWORD_LENGTH).check(password)
