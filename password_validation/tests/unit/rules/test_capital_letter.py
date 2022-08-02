from unittest import TestCase

from password_validation.rules.rules import CheckCapitalLetter


class CapitalLetterCheckShould(TestCase):
    def test_return_true_when_there_is_atleast_one_capital_letter(self):
        password_to_check = 'A'
        checker = CheckCapitalLetter()

        self.assertTrue(checker.check(password=password_to_check))

    def test_return_false_when_an_integer_is_passed_as_string(self):
        password_to_check = '1'
        checker = CheckCapitalLetter()

        self.assertFalse(checker.check(password=password_to_check))
