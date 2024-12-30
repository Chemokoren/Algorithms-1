import unittest

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from mergesort import mergesort


class TestMergeSort(unittest.TestCase):
    def test_empty_list(self):
        """Test sorting an empty list."""
        A = []
        mergesort(A)
        self.assertEqual(A, [])

    def test_single_element_list(self):
        """Test sorting a list with a single element."""
        A = [42]
        mergesort(A)
        self.assertEqual(A, [42])

    def test_already_sorted_list(self):
        """Test sorting a list that is already sorted."""
        A = [1, 2, 3, 4, 5]
        mergesort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        """Test sorting a reverse-sorted list."""
        A = [5, 4, 3, 2, 1]
        mergesort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5])

    def test_list_with_duplicates(self):
        """Test sorting a list with duplicate values."""
        A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        mergesort(A)
        self.assertEqual(A, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_list_with_negative_numbers(self):
        """Test sorting a list with negative numbers."""
        A = [-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]
        mergesort(A)
        self.assertEqual(A, [-9, -6, -5, -5, -5, -4, -3, -3, -2, -1, -1])

    def test_list_with_mixed_positive_and_negative(self):
        """Test sorting a list with mixed positive and negative numbers."""
        A = [3, -1, 4, -1, 5, -9, 2, -6, 5, 3, -5]
        mergesort(A)
        self.assertEqual(A, [-9, -6, -5, -1, -1, 2, 3, 3, 4, 5, 5])

    def test_large_list(self):
        """Test sorting a large list."""
        A = list(range(1000, 0, -1))  # Reverse order
        expected = list(range(1, 1001))  # Sorted order
        mergesort(A)
        self.assertEqual(A, expected)

    def test_list_with_floats(self):
        """Test sorting a list with floating-point numbers."""
        A = [3.14, 2.71, 1.41, -3.14, 0.0, -2.71]
        mergesort(A)
        self.assertEqual(A, [-3.14, -2.71, 0.0, 1.41, 2.71, 3.14])

    def test_list_with_repeated_same_element(self):
        """Test sorting a list with all elements being the same."""
        A = [7, 7, 7, 7, 7, 7, 7]
        mergesort(A)
        self.assertEqual(A, [7, 7, 7, 7, 7, 7, 7])

if __name__ == '__main__':
    unittest.main()


"""
Explanation of the Tests

    Empty List: Verifies that the function correctly handles an empty list without errors.
    Single-Element List: Ensures the function returns the same list since it's already sorted.
    Already Sorted List: Confirms that the function recognizes the sorted order and does not alter it.
    Reverse-Sorted List: Tests the function's ability to completely sort a list in descending order.
    Duplicates: Ensures the function can handle lists with duplicate elements and sort them correctly.
    Negative Numbers: Verifies the function can sort lists containing negative values.
    Mixed Positive and Negative Numbers: Checks the function's performance with a mix of positive and negative integers.
    Large List: Tests scalability by sorting a large list of integers.
    Floating-Point Numbers: Ensures the function works with decimal numbers.
    Repeated Same Element: Verifies that the function handles lists where all elements are identical.

How to Run

python -m unittest test_mergesort.py
"""