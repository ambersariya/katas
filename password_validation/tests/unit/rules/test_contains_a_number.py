from unittest import TestCase

from password_validation.rules.rules import ContainsNumber


class CheckContainsNumberShould(TestCase):
    def test_return_true_when_password_contains_numbers(self):
        password_to_check = '1'
        checker = ContainsNumber()
        self.assertTrue(checker.check(password=password_to_check))

    def test_return_false_when_password_doesnt_contains_numbers(self):
        password_to_check = 'a'
        checker = ContainsNumber()
        self.assertFalse(checker.check(password=password_to_check))

    def test_return_true_when_password_contains_alphanumeric_values(self):
        password_to_check = 'a1'
        checker = ContainsNumber()
        self.assertTrue(checker.check(password=password_to_check))
