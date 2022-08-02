from unittest import TestCase

from password_validation.rules.rules import ContainsLowercaseLetter


class CheckLowercaseLetterShould(TestCase):
    def test_return_true_when_password_is_lowercase(self):
        password_to_check = 'a'
        checker = ContainsLowercaseLetter()
        self.assertTrue(checker.check(password=password_to_check))

    def test_return_false_when_password_is_not_lowercase(self):
        password_to_check = 'A'
        checker = ContainsLowercaseLetter()
        self.assertFalse(checker.check(password=password_to_check))
