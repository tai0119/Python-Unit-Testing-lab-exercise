import unittest
from leap_year import is_leap_year

class TestLeapYear(unittest.TestCase):
# 1. Expand Test Coverage
#  Add tests for edge cases and error conditions. Aim for comprehensive test coverage that exercises all code paths.
    def test_leap_year_0(self):
        self.assertTrue(is_leap_year(0))  # Edge case: year zero

    def test_leap_year_negative(self):
        self.assertTrue(is_leap_year(-400))  # Historical calendar years (valid in logic)

    def test_not_leap_year_negative(self):
        self.assertFalse(is_leap_year(-500))  # Not divisible by 4

    def test_string_input(self):
        with self.assertRaises(TypeError):
            is_leap_year("2020")
        # self.assertFalse(is_leap_year("2020"))  # This will likely raise TypeError in modern Python

    def test_float_input(self):
        self.assertTrue(is_leap_year(2020.0))  # This will pass in current logic since 2020.0 % 4 == 0

# 2. Implement Test Fixtures
#  Use setUp() and tearDown() methods to prepare test environments and clean up after tests run.
# This proves that setUp() and tearDown() run before and after each individual test method, not once for the whole class.

    def setUp(self):
        # Setup actions before each test
        print(f"Running {self._testMethodName}...")

    def tearDown(self):
        # Cleanup actions after each test
        print(f"Finished {self._testMethodName}.\n")

    def test_leap_year_0(self):
        self.assertTrue(is_leap_year(0))

    def test_leap_year_negative(self):
        self.assertTrue(is_leap_year(-400))

    def test_not_leap_year_negative(self):
        self.assertFalse(is_leap_year(-500))

    def test_string_input(self):
        with self.assertRaises(TypeError):
            is_leap_year("2020")

    def test_float_input(self):
        self.assertTrue(is_leap_year(2020.0))
        
if __name__ == '__main__':
    unittest.main()
