import unittest
from leap_year import is_leap_year

class TestLeapYear(unittest.TestCase):
    
    def test_leap_year_2020(self):
        self.assertTrue(is_leap_year(2020))

    def test_not_leap_year_1900(self):
        self.assertFalse(is_leap_year(1900))

    def test_leap_year_2000(self):
        self.assertTrue(is_leap_year(2000))

    def test_not_leap_year_2019(self):
        self.assertFalse(is_leap_year(2019))

if __name__ == '__main__':
    unittest.main()
