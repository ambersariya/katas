from unittest import TestCase

from password_validation.rules.rules import HasMinPasswordLength


class TestPasswordLengthShould(TestCase):
    def test_check_password_matches_given_length_or_longer(self):
        password_length = HasMinPasswordLength(length=6)
        password_to_check = '123454'
        self.assertTrue(password_length.check(password_to_check))
