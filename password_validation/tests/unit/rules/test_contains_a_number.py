from unittest import TestCase

from password_validation.rules.rules import ContainsNumber, Violation


class CheckContainsNumberShould(TestCase):
    def test_return_nothing_when_password_contains_a_number(self):
        password_to_check = '1'
        checker = ContainsNumber()
        self.assertIsNone(checker.check(password=password_to_check))

    def test_return_a_violation_when_password_does_not_contain_a_number(self):
        password_to_check = 'a'
        checker = ContainsNumber()
        self.assertIsInstance(checker.check(password=password_to_check), Violation)

    def test_return_nothing_when_password_contains_alphanumeric_values(self):
        password_to_check = 'a1'
        checker = ContainsNumber()
        self.assertIsNone(checker.check(password=password_to_check))
