import unittest

from password_validation.violations import Violations, Violation


class ViolationsListShould(unittest.TestCase):
    def test_be_instantiable_with_a_list_of_violations(self):
        violations = Violations([Violation('message first testcase')])
        self.assertEqual(len(violations), 1)

    def test_return_1_violation_it_is_holding(self):
        violations = Violations()
        violations.add(Violation('some message second testcase'))
        self.assertEqual(len(violations), 1)

    def test_return_2_violations_it_is_holding(self):
        violations = Violations()
        violations.add(Violation('some message 1: third testcase'))
        violations.add(Violation('some message 2: third testcase'))
        self.assertEqual(len(violations), 2)
