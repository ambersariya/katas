from unittest import TestCase

from parameterized import parameterized

from password_validation.rules.rules import HasMinPasswordLength, ContainsCapitalLetter, ContainsLowercaseLetter, \
    ContainsNumber, ContainsUnderscore
from password_validation.validator import PasswordValidator
from password_validation.violations import Violations


class PasswordValidatorShould(TestCase):
    @parameterized.expand([
        ('', 5),  # 0 length
        (None, 1),  # 0 length
        ('password_to_check', 2),  # no number or capital, underscore
        ('pass word', 3),  # no number or capital, underscore
        ('password1', 2),  # no capital
        ('Ab_cdef123', 0),
    ])
    def test_iteration_1(self, password, expected_num_violations):
        rules = [
            HasMinPasswordLength(min_length=8),
            ContainsCapitalLetter(),
            ContainsLowercaseLetter(),
            ContainsNumber(),
            ContainsUnderscore()
        ]
        password_validator = PasswordValidator(rules=rules)
        result = password_validator.validate(password=password)

        self.assertIsInstance(result, Violations)
        self.assertEquals(
            len(result),
            expected_num_violations
        )

    @parameterized.expand([
        ('passw', 3),  # no number or capital, underscore
        ('passwo', 2),  # no number or capital, underscore
        ('password', 2),  # no capital
        ('Cdef123', 0),
    ])
    def test_iteration_2_validation_2(self, password, expected_num_violations):
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
        result = password_validator.validate(password=password)

        self.assertIsInstance(result, Violations)
        self.assertEquals(
            len(result),
            expected_num_violations
        )

    @parameterized.expand([
        ('passw', 3),  # no number or capital, underscore
        ('passwo', 3),  # no number or capital, underscore
        ('password', 3),  # no capital
        ('Cdef123_', 1),
        ('Cdef12345678910_', 0),
    ])
    def test_iteration_2_validation_3(self, password, expected_num_violations):
        """
        Validation 3:

        Have more than 16 characters
        Contains a capital letter
        Contains a lowercase
        Contains an underscore
        """
        rules = [
            HasMinPasswordLength(min_length=16),
            ContainsCapitalLetter(),
            ContainsLowercaseLetter(),
            ContainsUnderscore()
        ]
        password_validator = PasswordValidator(rules=rules)

        result = password_validator.validate(password=password)

        self.assertIsInstance(result, Violations)
        self.assertEquals(
            len(result),
            expected_num_violations
        )
