from password_validation.rules.rules import HasMinPasswordLength

PASSWORD_LENGTH = 8


class PasswordValidator:
    def validate(self, password_string) -> bool:
        return HasMinPasswordLength(length=PASSWORD_LENGTH).check(password_string)
