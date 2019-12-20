import unittest

from day04.main import password, password_extra


class Tests(unittest.TestCase):
    def test_password(self):
        self.assertTrue(password(111111))
        self.assertFalse(password(223450))
        self.assertFalse(password(123789))

    def test_password_extra(self):
        self.assertTrue(password_extra(112233))
        self.assertFalse(password_extra(123444))
        self.assertTrue(password_extra(111122))
