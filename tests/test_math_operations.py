# test_math_operations.py
import unittest
from src.math_operations import add_numbers

class TestMathOperations(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5, "Should be 5")
        self.assertEqual(add_numbers(-1, 1), 0, "Should be 0")
        self.assertEqual(add_numbers(0, 0), 0, "Should be 0")

if __name__ == '__main__':
    unittest.main()
