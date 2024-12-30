import unittest

# Assume the insertionsort function is defined in a module called `sorting`
from sorting import insertionsort


class TestInsertionSort(unittest.TestCase):
    def test_sorted_array(self):
        """Test if the function handles already sorted arrays."""
        arr = [1, 2, 3, 4, 5]
        insertionsort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        """Test if the function handles reverse sorted arrays."""
        arr = [5, 4, 3, 2, 1]
        insertionsort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        """Test if the function sorts a general unsorted array."""
        arr = [84, 21, 96, 15, 47]
        insertionsort(arr)
        self.assertEqual(arr, [15, 21, 47, 84, 96])

    def test_single_element_array(self):
        """Test if the function handles single-element arrays."""
        arr = [42]
        insertionsort(arr)
        self.assertEqual(arr, [42])

    def test_empty_array(self):
        """Test if the function handles empty arrays."""
        arr = []
        insertionsort(arr)
        self.assertEqual(arr, [])

    def test_array_with_duplicates(self):
        """Test if the function handles arrays with duplicate values."""
        arr = [4, 2, 4, 3, 2]
        insertionsort(arr)
        self.assertEqual(arr, [2, 2, 3, 4, 4])

    def test_array_with_negative_numbers(self):
        """Test if the function handles arrays with negative numbers."""
        arr = [-3, 1, -5, 7, -2]
        insertionsort(arr)
        self.assertEqual(arr, [-5, -3, -2, 1, 7])

    def test_array_with_mixed_types(self):
        """Test if the function raises an exception for arrays with mixed types."""
        arr = [1, "string", 3.14]
        with self.assertRaises(TypeError):
            insertionsort(arr)

    def test_large_array(self):
        """Test if the function handles a large array."""
        arr = list(range(1000, 0, -1))  # Reverse sorted array of 1000 elements
        expected = list(range(1, 1001))  # Sorted array
        insertionsort(arr)
        self.assertEqual(arr, expected)


if __name__ == "__main__":
    unittest.main()

"""
Explanation of Test Cases

    test_sorted_array: Verifies the function correctly identifies and handles an already sorted array.
    test_reverse_sorted_array: Tests the function's ability to sort a reverse-ordered array.
    test_unsorted_array: Ensures a general unsorted array is sorted correctly.
    test_single_element_array: Checks if the function can handle arrays with one element.
    test_empty_array: Ensures the function works correctly with an empty array.
    test_array_with_duplicates: Verifies that duplicate values are sorted correctly.
    test_array_with_negative_numbers: Ensures arrays with negative numbers are handled properly.
    test_array_with_mixed_types: Ensures that the function raises a TypeError for arrays with mixed types (e.g., integers and strings).
    test_large_array: Tests the performance and correctness of the function with a large array.

Running the Tests
python -m unittest test_sorting.py

"""