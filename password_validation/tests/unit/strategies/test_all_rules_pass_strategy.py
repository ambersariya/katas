from unittest import TestCase

from password_validation.rules.rules import HasMinPasswordLength, ContainsCapitalLetter, ContainsUnderscore
from password_validation.strategies.strategy import AllRulesPassStrategy
from password_validation.validation_result import ValidationResult


class AllRulesPassStrategyShould(TestCase):
    def test_iteration_1(self):
        password = "Codurance"
        rules = [HasMinPasswordLength(9), ContainsCapitalLetter()]
        strategy = AllRulesPassStrategy()
        result = strategy.validate(password, rules)

        self.assertIsInstance(result, ValidationResult)
        self.assertEqual(len(result.violations), 0)
        self.assertEqual(result.fail, False)

    def test_iteration_2(self):
        password = "Codurance"
        rules = [HasMinPasswordLength(9), ContainsCapitalLetter(), ContainsUnderscore()]
        strategy = AllRulesPassStrategy()
        result = strategy.validate(password, rules)
        self.assertEqual(len(result.violations), 1)
        self.assertEqual(result.fail, True)
