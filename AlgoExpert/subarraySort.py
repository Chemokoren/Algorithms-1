"""
Problem

The problem being addressed by this algorithm is to find the shortest subarray within a given array
 such that sorting just this subarray would make the entire array sorted in ascending order.

In other words, we're looking for the smallest segment of the array that needs to be sorted in order
to have the entire array sorted. This can be useful in various scenarios, such as identifying a
minimal set of changes needed to correct the order of data in a dataset or finding the extent of
disorder in a sequence of values.

The thought Process

The thought process behind this algorithm revolves around identifying the minimum and maximum elements
that are out of order in the array. Once we determine these elements, we can find their correct
positions within the sorted array. This allows us to locate the smallest subarray that needs to be 
sorted to ensure the entire array is sorted.

Here's the step-by-step thought process:

    Finding Out-of-Order Elements:
        We iterate through the array and check each element to determine if it's out of order. 
        An element is considered out of order if it's greater than the next element or less than the 
        previous element. We store the minimum and maximum out-of-order elements along with their 
        indices.

    Identifying the Subarray Range:
        Once we have the minimum and maximum out-of-order elements, we determine their correct 
        positions in the sorted array.
        We find the leftmost index where the minimum out-of-order element should be placed, and the 
        rightmost index where the maximum out-of-order element should be placed.

    Returning the Result:
        Finally, we return the range of indices representing the smallest subarray that needs to be
        sorted to ensure the entire array is sorted.

By following this approach, the algorithm efficiently identifies the subarray that requires sorting 
to achieve a fully sorted array. It does so by leveraging the properties of out-of-order elements 
to determine the minimum and maximum extent of the subarray.

Complexity Analysis
-------------------

The time complexity of this algorithm is O(n), where nn is the length of the input array. Here's the 
breakdown:

    Finding Out-of-Order Elements:
        In the first loop, we iterate through the entire array once. This loop has a time complexity 
        of O(n), where nn is the length of the array.

    Identifying the Subarray Range:
        After finding the minimum and maximum out-of-order elements, we perform two additional loops 
        to find their correct positions in the sorted array. These loops also have a time complexity 
        of O(n), where nn is the length of the array.

Overall, the time complexity of the algorithm is dominated by the linear iteration through the input
array. Therefore, the time complexity is O(n).

The space complexity of this algorithm is O(1) because it only uses a constant amount of 
additional space regardless of the size of the input array. This constant space is used for variables
like min_out_of_order, max_out_of_order, left_idx, and right_idx, which store information about the 
minimum and maximum out-of-order elements and their indices. Therefore, the space complexity is 
independent of the size of the input array.

"""

# O(n) time | O(1) space
def subarray_sort(array):
    """
    Finds the shortest subarray that needs to be sorted in order for the entire array to be sorted in ascending order.

    Args:
    array (list): The input array of integers.

    Returns:
    list: A list containing two elements:
          1. The leftmost index of the subarray to be sorted.
          2. The rightmost index of the subarray to be sorted.

    """
    # if len(array) < 2:
    #     return [-1, -1]
    min_out_of_order = float("inf")
    max_out_of_order = float("-inf")
    
    # Iterate through the array to find the minimum and maximum elements that are out of order
    for i in range(len(array)):
        num = array[i]
        if is_out_of_order(i, num, array):
            min_out_of_order = min(min_out_of_order, num)
            max_out_of_order = max(max_out_of_order, num)
    
    # If the array is already sorted, return [-1, -1]
    if min_out_of_order == float("inf"):
        return [-1, -1]
    
    # Find the leftmost index of the subarray to be sorted
    left_idx = 0
    while min_out_of_order >= array[left_idx]:
        left_idx += 1
    
    # Find the rightmost index of the subarray to be sorted
    right_idx = len(array) - 1
    while max_out_of_order <= array[right_idx]:
        right_idx -= 1
    
    return [left_idx, right_idx]

def is_out_of_order(i, num, array):
    """
    Checks if a given number is out of order at a specific index in the array.

    Args:
        i (int): The index of the current number.
        num (int): The current number.
        array (list): The input array of integers.

    Returns:
        bool: True if the number is out of order, False otherwise.

    """
    # Check if the number is greater than the next number or less than the previous number
    if i == 0:
        return num > array[i + 1] if len(array) > 1 else False
    if i == len(array) - 1:
        return num < array[i - 1] if len(array) > 1 else False
    return num > array[i + 1] or num < array[i - 1]

print(subarray_sort([1,2,4,7,10,11,7,12,6,7,16,18,19]))

"""

These tests cover various scenarios including arrays with elements in ascending order, 
descending order, a single element, an empty array, and arrays with elements out of order in different
positions. They ensure that the function behaves correctly under different conditions and provide
robustness to the solution.
"""
import unittest

class TestSubarraySort(unittest.TestCase):

    def test_subarray_sort(self):
        self.assertEqual(subarray_sort([1,2,4,7,10,11,7,12,6,7,16,18,19]), [3, 9])
        self.assertEqual(subarray_sort([1,2,3,4,5]), [-1, -1])
        self.assertEqual(subarray_sort([5,4,3,2,1]), [0, 4])
        self.assertEqual(subarray_sort([1]), [-1, -1])
        self.assertEqual(subarray_sort([]), [-1, -1])
        self.assertEqual(subarray_sort([1,3,2,2,2]), [1, 4])
        self.assertEqual(subarray_sort([1,2,3,2,1]), [1, 4])
        self.assertEqual(subarray_sort([1,2,4,5,3]), [2, 4])

if __name__ == '__main__':
    unittest.main()
