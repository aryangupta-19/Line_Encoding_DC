"""
Unit tests for data_generator.py
"""

import unittest
from data_generator import (
    generate_random_sequence,
    generate_fixed_zero_sequence,
    find_longest_palindrome,
    find_longest_palindrome_details,
    is_palindrome,
)


class TestDataGenerator(unittest.TestCase):

    def test_generate_random_sequence(self):
        length = 20
        seq = generate_random_sequence(length)
        self.assertEqual(len(seq), length)
        self.assertTrue(all(bit in "01" for bit in seq))

    def test_generate_random_sequence_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_random_sequence(0)
        with self.assertRaises(ValueError):
            generate_random_sequence(-5)

    def test_generate_fixed_zero_sequence_4(self):
        seq = generate_fixed_zero_sequence(length=16, zero_count=4)
        self.assertEqual(len(seq), 16)
        self.assertIn("0000", seq)
        self.assertTrue(all(bit in "01" for bit in seq))

    def test_generate_fixed_zero_sequence_8(self):
        seq = generate_fixed_zero_sequence(length=24, zero_count=8)
        self.assertEqual(len(seq), 24)
        self.assertIn("00000000", seq)
        self.assertTrue(all(bit in "01" for bit in seq))

    def test_generate_fixed_zero_sequence_invalid(self):
        with self.assertRaises(ValueError):
            # zero_count must be 4 or 8
            generate_fixed_zero_sequence(length=16, zero_count=5)

        with self.assertRaises(ValueError):
            # length smaller than zero_count
            generate_fixed_zero_sequence(length=3, zero_count=4)

    def test_find_longest_palindrome_example(self):
        # In the prompt's sequence "1011010010110":
        # "101101" is a palindrome of length 6 at index 0..5,
        # but the true longest palindromic substring is "011010010110" of length 12 at index 1..12!
        seq = "1011010010110"
        pal = find_longest_palindrome(seq)
        self.assertEqual(pal, "011010010110")
        self.assertTrue(is_palindrome(pal))
        self.assertEqual(len(pal), 12)

        # Also verify that "101101" is recognized as a palindrome
        self.assertTrue(is_palindrome("101101"))

    def test_find_longest_palindrome_where_101101_is_longest(self):
        # A sequence where "101101" is strictly the longest palindrome (len 6)
        seq = "10110101"
        pal = find_longest_palindrome(seq)
        self.assertEqual(pal, "101101")
        self.assertEqual(len(pal), 6)

    def test_find_longest_palindrome_details(self):
        seq = "1011010010110"
        details = find_longest_palindrome_details(seq)
        self.assertEqual(details["palindrome"], "011010010110")
        self.assertEqual(details["start_index"], 1)
        self.assertEqual(details["end_index"], 12)
        self.assertEqual(details["length"], 12)

    def test_find_longest_palindrome_edge_cases(self):
        # Empty string
        self.assertEqual(find_longest_palindrome(""), "")

        # Single character
        self.assertEqual(find_longest_palindrome("0"), "0")
        self.assertEqual(find_longest_palindrome("1"), "1")

        # Entire string is palindrome
        self.assertEqual(find_longest_palindrome("01010"), "01010")
        self.assertEqual(find_longest_palindrome("1001"), "1001")

        # Consecutive identical characters
        self.assertEqual(find_longest_palindrome("00000"), "00000")


if __name__ == "__main__":
    unittest.main()
