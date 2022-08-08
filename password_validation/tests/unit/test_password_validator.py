from unittest import TestCase

from parameterized import parameterized

from password_validation.strategies.strategy import AllRulesPassStrategy
from password_validation.validation_result import ValidationResult
from password_validation.validator_builder import PasswordValidatorBuilder
from password_validation.violations import Violations


class PasswordValidatorShould(TestCase):
    @parameterized.expand([
        ('', 5),
        (None, 1),
        ('password_to_check', 2),
        ('pass word', 3),
        ('password1', 2),
        ('Ab_cdef123', 0),
    ])
    def test_iteration_1(self, password, expected_num_violations):
        password_validator = PasswordValidatorBuilder() \
            .has_min_password_length(8) \
            .contains_capital_letter() \
            .contains_lower_case_letter() \
            .contains_underscore() \
            .contains_number() \
            .with_strategy(AllRulesPassStrategy()) \
            .build()
        result = password_validator.validate(password=password)

        self.assertIsInstance(result, ValidationResult)
        self.assertIsInstance(result.violations, Violations)
        self.assertEqual(
            len(result.violations),
            expected_num_violations
        )

    @parameterized.expand([
        ('passw', 3),
        ('passwo', 2),
        ('password', 2),
        ('Cdef123', 0),
    ])
    def test_iteration_2_validation_2(self, password, expected_num_violations):
        password_validator = PasswordValidatorBuilder() \
            .has_min_password_length(6) \
            .contains_capital_letter() \
            .contains_lower_case_letter() \
            .contains_number() \
            .with_strategy(AllRulesPassStrategy()) \
            .build()
        result = password_validator.validate(password=password)

        self.assertIsInstance(result, ValidationResult)
        self.assertIsInstance(result.violations, Violations)
        self.assertEqual(
            len(result.violations),
            expected_num_violations
        )

    @parameterized.expand([
        ('passw', 3),
        ('passwo', 3),
        ('password', 3),
        ('Cdef123_', 1),
        ('Cdef12345678910_', 0),
    ])
    def test_iteration_2_validation_3(self, password, expected_num_violations):
        password_validator = PasswordValidatorBuilder() \
            .has_min_password_length(16) \
            .contains_capital_letter() \
            .contains_lower_case_letter() \
            .contains_underscore() \
            .with_strategy(AllRulesPassStrategy()) \
            .build()

        result = password_validator.validate(password=password)

        self.assertIsInstance(result, ValidationResult)
        self.assertIsInstance(result.violations, Violations)
        self.assertEqual(
            len(result.violations),
            expected_num_violations
        )
