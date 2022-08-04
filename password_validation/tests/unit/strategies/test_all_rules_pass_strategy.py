from unittest import TestCase

from password_validation.rules.rules import HasMinPasswordLength, ContainsCapitalLetter, ContainsUnderscore
from password_validation.strategies.strategy import AllRulesPassStrategy


class AllRulesPassStrategyShould(TestCase):
    def test_iteration_1(self):
        password = "Codurance"
        rules = [HasMinPasswordLength(9), ContainsCapitalLetter()]
        strategy = AllRulesPassStrategy()
        result = strategy.validate(password, rules)
        self.assertEqual(len(result), 0)

    def test_iteration_2(self):
        password = "Codurance"
        rules = [HasMinPasswordLength(9), ContainsCapitalLetter(), ContainsUnderscore()]
        strategy = AllRulesPassStrategy()
        result = strategy.validate(password, rules)
        self.assertEqual(len(result), 1)
