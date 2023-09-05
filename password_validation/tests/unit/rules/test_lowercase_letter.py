from unittest import TestCase

from password_validation.rules.rules import ContainsLowercaseLetter, Violation


class CheckLowercaseLetterShould(TestCase):
    def test_return_nothing_when_password_contains_lowercase_letters(self):
        password_to_check = 'a'
        checker = ContainsLowercaseLetter()
        self.assertIsNone(checker.check(password=password_to_check))

    def test_return_violation_when_password_does_not_contain_lowercase_letters(self):
        password_to_check = 'A'
        checker = ContainsLowercaseLetter()
        self.assertIsInstance(checker.check(password=password_to_check), Violation)
