import unittest

from password_validation.rules.rules import ContainsUnderscore, Violation


class CheckContainsUnderscoreShould(unittest.TestCase):
    def test_return_nothing_when_there_is_at_least_one_underscore(self):
        password_to_check = '_abc'
        checker = ContainsUnderscore()
        self.assertIsNone(checker.check(password=password_to_check))

    def test_return_a_violation_when_there_is_no_underscore(self):
        password_to_check = 'abc'
        checker = ContainsUnderscore()
        self.assertIsInstance(checker.check(password=password_to_check), Violation)
