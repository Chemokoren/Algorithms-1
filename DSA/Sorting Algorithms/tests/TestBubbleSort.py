import unittest
from ..bubblesort import bubblesort

class TestBubbleSort(unittest.TestCase):
    """
    Unit tests for the Bubble Sort function.
    """

    def test_sorted_array(self):
        """Test Bubble Sort on an already sorted array."""
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        bubblesort(arr)
        self.assertEqual(arr, expected)

    def test_reverse_sorted_array(self):
        """Test Bubble Sort on a reverse-sorted array."""
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        bubblesort(arr)
        self.assertEqual(arr, expected)

    def test_unsorted_array(self):
        """Test Bubble Sort on an unsorted array."""
        arr = [84, 21, 96, 15, 47]
        expected = [15, 21, 47, 84, 96]
        bubblesort(arr)
        self.assertEqual(arr, expected)

    def test_array_with_duplicates(self):
        """Test Bubble Sort on an array with duplicate elements."""
        arr = [3, 1, 2, 3, 1]
        expected = [1, 1, 2, 3, 3]
        bubblesort(arr)
        self.assertEqual(arr, expected)

    def test_empty_array(self):
        """Test Bubble Sort on an empty array."""
        arr = []
        expected = []
        bubblesort(arr)
        self.assertEqual(arr, expected)

    def test_single_element_array(self):
        """Test Bubble Sort on an array with a single element."""
        arr = [42]
        expected = [42]
        bubblesort(arr)
        self.assertEqual(arr, expected)

    def test_array_with_negative_numbers(self):
        """Test Bubble Sort on an array with negative numbers."""
        arr = [-3, -1, -7, -4, -2]
        expected = [-7, -4, -3, -2, -1]
        bubblesort(arr)
        self.assertEqual(arr, expected)

    def test_mixed_numbers(self):
        """Test Bubble Sort on an array with both positive and negative numbers."""
        arr = [-3, 5, -1, 7, 0]
        expected = [-3, -1, 0, 5, 7]
        bubblesort(arr)
        self.assertEqual(arr, expected)

    def test_floats_and_integers(self):
        """Test Bubble Sort on an array with both floats and integers."""
        arr = [3.2, 1.5, 2.1, 0, -1]
        expected = [-1, 0, 1.5, 2.1, 3.2]
        bubblesort(arr)
        self.assertEqual(arr, expected)

if __name__ == "__main__":
    unittest.main()


"""
Edge Cases Covered

    Already Sorted Array:
        Ensures the algorithm performs correctly without unnecessary changes.

    Reverse-Sorted Array:
        Validates handling of the worst-case scenario.

    Unsorted Array:
        Confirms the algorithm works on a typical case.

    Array with Duplicates:
        Tests stability and correctness with duplicate elements.

    Empty Array:
        Handles the edge case of an empty list gracefully.

    Single Element Array:
        Confirms correct behavior when the input has only one element.

    Array with Negative Numbers:
        Ensures sorting works with negative values.

    Mixed Numbers:
        Validates sorting when the array contains both positive and negative numbers.

    Floats and Integers:
        Checks for proper sorting of arrays with mixed numeric types.

Running the Tests
python -m unittest test_bubblesort.py

"""