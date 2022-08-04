from unittest import TestCase

from password_validation.strategies.strategy import AllRulesPassStrategy
from password_validation.validator import PasswordValidator
from password_validation.validator_builder import PasswordValidatorBuilder


class ValidatorBuilderShould(TestCase):
    def test_build_a_validator_with_no_rules(self):
        result = PasswordValidatorBuilder() \
            .with_strategy(AllRulesPassStrategy()) \
            .build()

        self.assertIsInstance(result, PasswordValidator)

    def test_build_a_validator_with_specific_rules(self):
        validator = PasswordValidatorBuilder() \
            .has_min_password_length(4) \
            .contains_capital_letter() \
            .with_strategy(AllRulesPassStrategy()) \
            .build()

        password_to_pass = "Danish"
        password_to_fail = "foo"

        self.assertEqual(len(validator.validate(password_to_pass)), 0)
        self.assertEqual(len(validator.validate(password_to_fail)), 2)
