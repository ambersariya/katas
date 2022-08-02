from unittest import TestCase

from password_validation.validator import PasswordValidator


class PasswordValidatorShould(TestCase):
    def test_return_true_when_password_string_is_validated(self):
        password_validator = PasswordValidator()

        self.assertTrue(password_validator.validate("some string"))

    def test_return_false_when_password_string_is_empty(self):
        password_validator = PasswordValidator()

        self.assertFalse(password_validator.validate(''))
        self.assertFalse(password_validator.validate(None))

    def test_return_true_when_there_is_atleast_one_capital_letter(self):
        password_validator = PasswordValidator()

        self.assertTrue(password_validator.validate('Easdfghj'))
