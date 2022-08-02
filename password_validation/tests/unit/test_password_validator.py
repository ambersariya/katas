from unittest import TestCase

from parameterized import parameterized

from password_validation.validator import PasswordValidator


class PasswordValidatorShould(TestCase):
    @parameterized.expand([
        ('', False),  # 0 length
        (None, False),  # 0 length
        ('password_to_check', False),  # no number or capital, underscore
        ('pass word', False),  # no number or capital, underscore
        ('password1', False),  # no capital
        ('Ab_cdef123', True),
    ])
    def test_iteration_1(self, password, expected_result):
        password_validator = PasswordValidator()

        self.assertEquals(password_validator.validate(password=password), expected_result)
