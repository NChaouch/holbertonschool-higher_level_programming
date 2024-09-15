#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function"""

    def test_max_at_start(self):
        self.assertEqual(max_integer([5, 2, 3]), 5)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 8]), 8)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 9, 3]), 9)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

if __name__ == '__main__':
    unittest.main()
