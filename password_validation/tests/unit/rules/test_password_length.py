from unittest import TestCase

from password_validation.rules.rules import HasMinPasswordLength, Violation


class TestPasswordLengthShould(TestCase):
    def test_should_return_violation_when_password_is_shorter_than_required(self):
        password_length = HasMinPasswordLength(min_length=6)
        password_to_check = '12345'
        self.assertIsInstance(password_length.check(password_to_check), Violation)

    def test_should_return_nothing_when_password_is_longer_than_required(self):
        password_length = HasMinPasswordLength(min_length=6)
        password_to_check = '123456'
        self.assertIsNone(password_length.check(password_to_check))
