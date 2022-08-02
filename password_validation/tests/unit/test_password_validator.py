from unittest import TestCase

from parameterized import parameterized

from password_validation.rules.rules import HasMinPasswordLength, ContainsCapitalLetter, ContainsLowercaseLetter, \
    ContainsNumber, ContainsUnderscore
from password_validation.validator import PasswordValidator


class PasswordValidatorShould(TestCase):
    @parameterized.expand([
        ('', False),  # 0 length
        (None, False),  # 0 length
        ('password_to_check', False),  # no number or capital, underscore
        ('pass word', False),  # no number or capital, underscore
        ('password1', False),  # no capital
        ('Ab_cdef123', True),
    ])
    def test_iteration_1(self, password, expected_result):
        rules = [
            HasMinPasswordLength(min_length=8),
            ContainsCapitalLetter(),
            ContainsLowercaseLetter(),
            ContainsNumber(),
            ContainsUnderscore()
        ]
        password_validator = PasswordValidator(rules=rules)

        self.assertEquals(password_validator.validate(password=password), expected_result)

    @parameterized.expand([
        ('passw', False),  # no number or capital, underscore
        ('passwo', False),  # no number or capital, underscore
        ('password', False),  # no capital
        ('Cdef123', True),
    ])
    def test_iteration_2_validation_2(self, password, expected_result):
        """
        Validation 2:

        Have more than 6 characters
        Contains a capital letter
        Contains a lowercase
        Contains a number
        """
        rules = [
            HasMinPasswordLength(min_length=6),
            ContainsCapitalLetter(),
            ContainsLowercaseLetter(),
            ContainsNumber()
        ]
        password_validator = PasswordValidator(rules=rules)

        self.assertEquals(password_validator.validate(password=password), expected_result)
