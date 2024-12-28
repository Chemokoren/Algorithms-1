import unittest

# Assuming the quicksort functions are in a module named quicksort_module.
# from quicksort_module import quicksort_recursive, quicksort, partition

def quicksort_recursive(A):
    low, high = 0, len(A) - 1
    def rec_quick_sort(A, low, high):
        if low < high:
            p = partition(A, low, high)
            rec_quick_sort(A, low, p - 1)
            rec_quick_sort(A, p + 1, high)
        return A
    return rec_quick_sort(A, low, high)

def quicksort(A, low, high):
    if low < high:
        p = partition(A, low, high)
        quicksort(A, low, p - 1)
        quicksort(A, p + 1, high)

def partition(A, low, high):
    i = low - 1
    pivot = A[high]
    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1


class TestQuickSort(unittest.TestCase):

    def test_quicksort_recursive_sorted(self):
        """
        Test for quicksort_recursive with an already sorted list.
        The list should remain sorted.
        """
        A = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(quicksort_recursive(A), expected)

    def test_quicksort_recursive_reverse_sorted(self):
        """
        Test for quicksort_recursive with a reverse sorted list.
        The list should be sorted in ascending order after sorting.
        """
        A = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(quicksort_recursive(A), expected)

    def test_quicksort_recursive_empty(self):
        """
        Test for quicksort_recursive with an empty list.
        An empty list should remain empty after sorting.
        """
        A = []
        expected = []
        self.assertEqual(quicksort_recursive(A), expected)

    def test_quicksort_recursive_single_element(self):
        """
        Test for quicksort_recursive with a single element list.
        A single element list should remain the same after sorting.
        """
        A = [42]
        expected = [42]
        self.assertEqual(quicksort_recursive(A), expected)

    def test_quicksort_sorted(self):
        """
        Test for quicksort with an already sorted list.
        The list should remain sorted.
        """
        A = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        quicksort(A, 0, len(A) - 1)
        self.assertEqual(A, expected)

    def test_quicksort_reverse_sorted(self):
        """
        Test for quicksort with a reverse sorted list.
        The list should be sorted in ascending order after sorting.
        """
        A = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        quicksort(A, 0, len(A) - 1)
        self.assertEqual(A, expected)

    def test_quicksort_empty(self):
        """
        Test for quicksort with an empty list.
        An empty list should remain empty after sorting.
        """
        A = []
        expected = []
        quicksort(A, 0, len(A) - 1)
        self.assertEqual(A, expected)

    def test_quicksort_single_element(self):
        """
        Test for quicksort with a single element list.
        A single element list should remain the same after sorting.
        """
        A = [42]
        expected = [42]
        quicksort(A, 0, len(A) - 1)
        self.assertEqual(A, expected)

    def test_partition(self):
        """
        Test for the partition function to ensure the pivot is placed in the correct position.
        """
        A = [3, 2, 5, 1, 4]
        pivot_index = partition(A, 0, len(A) - 1)
        # After partition, pivot should be in position 3, so the array should look like this:
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(A, expected)
        self.assertEqual(pivot_index, 3)

    def test_quicksort_large_input(self):
        """
        Test for quicksort with a large input to ensure performance.
        The list should be sorted correctly.
        """
        A = list(range(1000, 0, -1))  # A reverse sorted list of 1000 elements
        expected = list(range(1, 1001))  # The expected sorted list
        quicksort(A, 0, len(A) - 1)
        self.assertEqual(A, expected)

    def test_quicksort_recursive_large_input(self):
        """
        Test for quicksort_recursive with a large input to ensure performance.
        The list should be sorted correctly.
        """
        A = list(range(1000, 0, -1))  # A reverse sorted list of 1000 elements
        expected = list(range(1, 1001))  # The expected sorted list
        self.assertEqual(quicksort_recursive(A), expected)


if __name__ == '__main__':
    unittest.main()
