import unittest

from src.my_arithmetic_ethan.gcd import gcd

class TestGCD(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(101, 103), 1)

    def test_negative_numbers(self):
        self.assertEqual(gcd(-48, 18), 6)
        self.assertEqual(gcd(48, -18), 6)
        self.assertEqual(gcd(-48, -18), 6)

    def test_zeros(self):
        self.assertEqual(gcd(0, 18), 18)
        self.assertEqual(gcd(48, 0), 48)
        self.assertEqual(gcd(0, 0), 0)

    def test_equal_numbers(self):
        self.assertEqual(gcd(42, 42), 42)

    def test_large_numbers(self):
        self.assertEqual(gcd(123456789, 987654321), 9)

if __name__ == "__main__":
    unittest.main()
