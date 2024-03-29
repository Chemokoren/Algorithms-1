"""
Given a sorted array, and a target number e.g. 45, find the range of indices in the input array in 
between which you can find the target value.

In this case the range is [4,9] because 4 is the first index where you can find the first target value 45 and 
9 is the last index you can find the value 45.
"""
# recursive approach
# O(log(n)) time | O(log(n)) space
def search_for_range(array, target):
    """
    Returns the range of indices in the array that contain the target value.

    Args:
        array: A sorted list of integers.
        target: An integer to search for in the array.

    Returns:
        list: A list of two integers representing the leftmost and rightmost indices of the target value in the array.
        If the target value is not found in the array, returns [-1, -1].
    """
    final_range = [-1, -1]
    altered_binary_search(array, target, 0, len(array)-1, final_range, True)
    altered_binary_search(array, target, 0, len(array)-1, final_range, False)
    return final_range

def altered_binary_search(array, target, left, right, final_range, go_left):
    """
    Searches for the leftmost and rightmost indices of the target value in the array.

    Args:
        array: A sorted list of integers.
        target: An integer to search for in the array.
        left: The leftmost index of the search range.
        right: The rightmost index of the search range.
        final_range: A list of two integers representing the leftmost and rightmost indices of the target value in the array.
        go_left: A boolean indicating whether the function is searching for the leftmost or rightmost index.

    Returns:
        None.
    """
    # If the left pointer is greater than the right pointer, return
    if left > right:
        return
    # Calculate the mid index
    mid = (left + right) // 2
    # If the element at the mid index is less than the target, search the right half of the array
    if array[mid] < target:
        altered_binary_search(array, target, mid + 1, right, final_range, go_left)
    # If the element at the mid index is greater than the target, search the left half of the array
    elif array[mid] > target:
        altered_binary_search(array, target, left, mid - 1, final_range, go_left)
    # If the element at the mid index is equal to the target    
    else:
        # If we are searching for the leftmost index
        if go_left:
            # If the mid index is the first index or the element before the mid index is not equal to the target
            if mid == 0 or array[mid - 1] != target:
                 # Update the leftmost index in the final range
                final_range[0] = mid
            # Otherwise, search the left half of the array
            else:
                altered_binary_search(array, target, left, mid - 1, final_range, go_left)
        else:
            # If the mid index is the last index or the element after the mid index is not equal to the target
            if mid == len(array) - 1 or array[mid + 1] != target:
                 # Update the rightmost index in the final range
                final_range[1] = mid
            # Otherwise, search the right half of the array
            else:
                altered_binary_search(array, target, mid + 1, right, final_range, go_left)


# iterative approach
# O(log(n)) time | O(1) space
def search_for_range_iterative(array, target):
    """
    Find the range of indices in the sorted array that contains the target value.

    Args:
        array (List[int]): The sorted array of integers.
        target (int): The target value to search for in the array.

    Returns:
        List[int]: A list containing the start and end indices of the range that contains the target value.
                   If the target is not found in the array, returns [-1, -1].
    """
    # Initialize the final range list to store the start and end indices of the target range.
    finalRange =[-1, -1]
    
    # Perform two altered binary searches to find the left and right bounds of the target range.
    altered_binary_search_iterative(array, target, 0, len(array)-1, finalRange, True)
    altered_binary_search_iterative(array, target, 0, len(array)-1, finalRange, False)
    
    # Return the final range list containing the start and end indices of the target range.
    return finalRange

def altered_binary_search_iterative(array, target, left,right, finalRange, goLeft):
    """
    Perform an altered binary search to find the left and right bound of the target range.

    Args:
        array (List[int]): The sorted array of integers.
        target (int): The target value to search for in the array.
        left (int): The left boundary index of the search range.
        right (int): The right boundary index of the search range.
        finalRange (List[int]): A list containing the start and end indices of the target range.
        goLeft (bool): A boolean indicating whether to find the left or right bound of the target range.

    Returns:
        None
    """
    while left <= right:
        
        # Calculate the middle index of the current search range using integer division.
        mid =(left + right)
        
        # Perform binary search to find the left or right bound of the target range.
        if array[mid] < target:
            left =mid + 1
        elif array[mid] > target:
            right =mid -1
        else:
            # If the target value is found, update the finalRange list with the left or right bound.
            if goLeft:
                if mid ==0 or array[mid -1] != target:
                    finalRange[0] =mid
                    return
                else:
                    right = mid -1
            else:
                if mid == len(array) -1 or array[mid + 1] != target:
                    finalRange[1] =mid
                    return
                else:
                    left =mid+1


import unittest
class TestSearchForRange(unittest.TestCase):

    def test_recursive_search_range(self):
        # recursive approach test
        self.assertListEqual(search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45), [4,9])

    def test_iterative_search_range(self):
        # iterative approach test
        self.assertListEqual(search_for_range_iterative([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45), [4,9])

if __name__=="__main__":
    unittest.main()