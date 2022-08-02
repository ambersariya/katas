import unittest

from password_validation.rules.rules import CheckContainsUnderscore


class CheckContainsUnderscoreShould(unittest.TestCase):
    def test_return_true_when_there_is_at_least_one_underscore(self):
        password_to_check = '_'
        checker = CheckContainsUnderscore()
        self.assertTrue(checker.check(password=password_to_check))
