
"""
This code performs a binary search on a shifted sorted array to find the index of the target element. 
The shifted_binary_search function serves as a wrapper for the helper function 
shifted_binary_search_helper_iterative, which implements the actual search logic. 

The algorithm iteratively divides the search range in half until the target element is found or the 
search range is exhausted. The time complexity of this algorithm is O(log⁡n) and the space complexity 
is O(1), where n is the number of elements in the array.

"""
def shifted_binary_search(array, target):
    """
    Perform a binary search to find the index of the target element in a shifted sorted array.

    Args:
        array (List[int]): The shifted sorted array of integers.
        target (int): The target value to search for in the array.

    Returns:
        int: The index of the target element in the array if found, otherwise returns -1.
    """
    return shifted_binary_search_helper_recursive(array, target, 0, len(array) -1)

# Iterative approach
# O(log(n)) time | O(1) space
def shifted_binary_search_helper_iterative(array, target, left, right):
    """
        Perform an iterative binary search to find the index of the target element in a shifted sorted array.

        Args:
            array (List[int]): The shifted sorted array of integers.
            target (int): The target value to search for in the array.
            left (int): The left boundary index of the search range.
            right (int): The right boundary index of the search range.

        Returns:
            int: The index of the target element in the array if found, otherwise returns -1.
    """
    
    while left <=right:
        middle =(left + right) //2
        potentialMatch =array[middle]
        leftNum =array[left]
        rightNum =array[right]
        if target == potentialMatch:
            return middle
        elif leftNum <= potentialMatch:
            if target < potentialMatch and target >= leftNum:
                right =middle -1
            else:
                left =middle +1

        else:
            if target > potentialMatch and target <= rightNum:
                left = middle + 1
            else:
                right =middle - 1
    return -1


# Recursive approach
# O(log(n)) time | O(log(n)) space -because of frames in the callstack
def shifted_binary_search_helper_recursive(array, target, left, right):
    """
    Perform a recursive binary search to find the index of the target element in a shifted sorted array.

    Args:
        array (List[int]): The shifted sorted array of integers.
        target (int): The target value to search for in the array.
        left (int): The left boundary index of the current search range.
        right (int): The right boundary index of the current search range.

    Returns:
        int: The index of the target element in the array if found, otherwise returns -1.
    """
    # Base case: If left index exceeds right index, the target is not found.
    if left > right:
        return -1
    
    # Calculate the middle index of the current search range.
    middle = (left + right) // 2
    # Retrieve the potential match value at the middle index.
    potentialMatch = array[middle]
    # Retrieve the values at the left and right boundaries of the search range.
    leftNum = array[left]
    rightNum = array[right]

    # Check if the potential match equals the target value.
    if target == potentialMatch:
        return middle
    # If the leftNum is less than or equal to the potential match,
    # perform binary search on the appropriate subarray.
    elif leftNum <= potentialMatch:
        if target < potentialMatch and target >= leftNum:
            # Perform recursive search on the left subarray.
            return shifted_binary_search_helper_recursive(array, target, left, middle - 1)
        else:
            # Perform recursive search on the right subarray.
            return shifted_binary_search_helper_recursive(array, target, middle + 1, right)
    # If the rightNum is less than the potential match,
    # perform binary search on the appropriate subarray.
    else:
        if target > potentialMatch and target <= rightNum:
            # Perform recursive search on the right subarray.
            return shifted_binary_search_helper_recursive(array, target, middle + 1, right)
        else:
            # Perform recursive search on the left subarray.
            return shifted_binary_search_helper_recursive(array, target, left, middle - 1)

import unittest

class TestShiftedBinarySearch(unittest.TestCase):
    def test_regular_case(self):
        # Test case with a regular shifted sorted array
        array = [5, 6, 7, 8, 9, 10, 1, 2, 3]
        target = 3
        self.assertEqual(shifted_binary_search(array, target), 8)

    def test_target_not_found(self):
        # Test case where target is not found in the array
        array = [5, 6, 7, 8, 9, 10, 1, 2, 3]
        target = 4
        self.assertEqual(shifted_binary_search(array, target), -1)

    def test_target_at_beginning(self):
        # Test case where target is at the beginning of the array
        array = [5, 6, 7, 8, 9, 10, 1, 2, 3]
        target = 5
        self.assertEqual(shifted_binary_search(array, target), 0)

    def test_target_at_end(self):
        # Test case where target is at the end of the array
        array = [5, 6, 7, 8, 9, 10, 1, 2, 3]
        target = 3
        self.assertEqual(shifted_binary_search(array, target), 8)

    def test_empty_array(self):
        # Test case with an empty array
        array = []
        target = 5
        self.assertEqual(shifted_binary_search(array, target), -1)

    def test_single_element_array(self):
        # Test case with a single element array
        array = [5]
        target = 5
        self.assertEqual(shifted_binary_search(array, target), 0)

    def test_array_with_duplicate_elements(self):
        # Test case with an array containing duplicate elements
        array = [5, 5, 5, 5, 5]
        target = 5
        self.assertEqual(shifted_binary_search(array, target), 2)

if __name__ == "__main__":
    unittest.main()
