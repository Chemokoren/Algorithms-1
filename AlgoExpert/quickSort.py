# O(nlog(n)) time | O(log(n)) space
def quick_sort(array):
    """
    Sorts the given array in ascending order using the quicksort algorithm.

    Parameters:
        array (list): The input list of integers to be sorted.

    Returns:
        list: The sorted list.
    """
    quick_sort_helper(array, 0, len(array) - 1)
    return array

def quick_sort_helper(array, startIdx, endIdx):
    """
    Helper function for the quicksort algorithm.

    Parameters:
        array (list): The input list of integers.
        startIdx (int): The starting index of the subarray.
        endIdx (int): The ending index of the subarray.
    """
    # Base case: if the subarray has one or fewer elements, it is already sorted
    if startIdx >= endIdx:
        return
    
    # Selecting the pivot and initializing left and right pointers
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    
    # Partitioning the subarray
    while rightIdx >= leftIdx:
        # Move the left index until encountering an element greater than the pivot
        # and simultaneously move the right index until encountering an element smaller than the pivot.
        # Once both indices have found elements violating the partition rule,
        # swap them to correct the partition.
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    
    # Swap the pivot with the right index to place it in its final sorted position
    swap(pivotIdx, rightIdx, array)
    
    # Recursively sort the left and right subarrays
    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
    if leftSubarrayIsSmaller:
        quick_sort_helper(array, startIdx, rightIdx - 1)
        quick_sort_helper(array, rightIdx + 1, endIdx)
    else:
        quick_sort_helper(array, rightIdx + 1, endIdx)
        quick_sort_helper(array, startIdx, rightIdx - 1)

def swap(i, j, array):
    """
    Swaps the elements at the specified indices in the given array.

    Parameters:
        i (int): The index of the first element to swap.
        j (int): The index of the second element to swap.
        array (list): The input list of integers.
    """
    array[i], array[j] = array[j], array[i]



import unittest

class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        # Test case with a randomly shuffled array
        array1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(quick_sort(array1), sorted(array1))

        # Test case with an already sorted array
        array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(quick_sort(array2), sorted(array2))

        # Test case with a reverse-sorted array
        array3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(quick_sort(array3), sorted(array3))

        # Test case with an empty array
        array4 = []
        self.assertEqual(quick_sort(array4), [])

        # Test case with a single-element array
        array5 = [42]
        self.assertEqual(quick_sort(array5), [42])

        # Test case with an array containing duplicate elements
        array6 = [5, 2, 1, 4, 2, 3, 5, 1]
        self.assertEqual(quick_sort(array6), sorted(array6))

        self.assertEqual(quick_sort([8,5,9,5,6,3]), sorted([8,5,9,5,6,3]))

if __name__ == "__main__":
    unittest.main()
