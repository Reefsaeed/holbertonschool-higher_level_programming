#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Max at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max in the middle."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max at the beginning."""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_one_element_list(self):
        """Only one element."""
        self.assertEqual(max_integer([8]), 8)

    def test_all_negative(self):
        """All numbers negative."""
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_positive_negative(self):
        """Mixed list of positives and negatives."""
        self.assertEqual(max_integer([-1, 3, -10, 2]), 3)

    def test_empty_list(self):
        """Empty list should return None."""
        self.assertIsNone(max_integer([]))

    def test_none_argument(self):
        """Passing None should raise TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_integer_values(self):
        """List containing non-integers should raise TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

    def test_list_of_floats(self):
        """Ensure function works with floats."""
        self.assertEqual(max_integer([1.5, 2.8, 0.3]), 2.8)

    def test_list_of_equal_values(self):
        """All elements equal."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_large_list(self):
        """Large list test."""
        self.assertEqual(max_integer(list(range(1000))), 999)


if __name__ == "__main__":
    unittest.main()
