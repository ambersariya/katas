from password_validation.rules.rules import CheckPasswordLength

PASSWORD_LENGTH = 8


class PasswordValidator:
    def validate(self, password_string) -> bool:
        return CheckPasswordLength(length=PASSWORD_LENGTH).check(password_string)
