import unittest

from password_validation.rules.rules import HasMinPasswordLength, ContainsCapitalLetter
from password_validation.strategies.strategy import AllowOneFailureStrategy
from password_validation.validation_result import ValidationResult


class AllowOneFailureStrategyShould(unittest.TestCase):
    def test_raise_error_when_list_of_rules_is_less_than_two(self):
        password = "codurance"
        rules = []
        with self.assertRaises(ValueError):
            strategy = AllowOneFailureStrategy()
            strategy.validate(password, rules)

    def test_return_list_of_violations_with_one_failure(self):
        password = "codurance"
        rules = [HasMinPasswordLength(9), ContainsCapitalLetter()]
        strategy = AllowOneFailureStrategy()
        result = strategy.validate(password, rules)

        self.assertIsInstance(result, ValidationResult)
        self.assertEqual(1, len(result.violations))
        self.assertEqual(False, result.fail)
