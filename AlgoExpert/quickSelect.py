"""
Time & Space Complexity

The quickselect algorithm is a variation of the quicksort algorithm, tailored to efficiently find the kth smallest (or largest) element in an unsorted array. Here's the analysis of its time and space complexity:
Time Complexity:

    Best Case: O(n)
    Average Case: O(n)
    Worst Case: O(n^2)

In the best and average cases, the algorithm effectively reduces the search space by approximately half with each partition step, resulting in a linear time complexity of O(n). However, in the worst case, the partition process may not evenly divide the array, leading to unbalanced partitions and potentially degenerating into a worst-case time complexity of O(n^2). This occurs when the pivot is consistently chosen poorly, such as when the array is already sorted or nearly sorted.
Space Complexity:

 In the iterative implementation of the quickselect algorithm provided here, the space complexity is
 indeed O(1) because it doesn't utilize additional space proportional to the input size. 
 Instead, it operates directly on the input array without requiring any additional data structures 
 or recursion. 

"""
# O(n) time | O(1) space
# find kth samllest value in an input array in linear time on average
# (also find the kth largest value in the array)

def quick_select(array, k):
    """
    Selects the kth smallest element from the given array.
    
    Parameters:
        array (list): The input list of integers.
        k (int): The desired rank of the element to select (1-indexed).
        
    Returns:
        int: The kth smallest element in the array.
    """
    position = k - 1
    return quick_select_helper(array, 0, len(array) - 1, position)

def quick_select_helper(array, startIdx, endIdx, position):
    """
    Helper function for the quickselect algorithm.
    
    Parameters:
        array (list): The input list of integers.
        startIdx (int): The starting index of the subarray.
        endIdx (int): The ending index of the subarray.
        position (int): The desired rank of the element to select (0-indexed).
        
    Returns:
        int: The kth smallest element in the array.
    """
    while True:
        if startIdx > endIdx:
            return None
        pivotIdx = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx
        # Partition the array based on the pivot element
        while leftIdx <= rightIdx:
            # Move left index until finding an element greater than the pivot
            if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                swap(leftIdx, rightIdx, array)
            # Move left index if the element is less than or equal to the pivot
            if array[leftIdx] <= array[pivotIdx]:
                leftIdx += 1
            # Move right index if the element is greater than or equal to the pivot
            if array[rightIdx] >= array[pivotIdx]:
                rightIdx -= 1
        # Swap the pivot with the right index (partitioning step)
        swap(pivotIdx, rightIdx, array)
        # Check if the right index is the desired position
        if rightIdx == position:
            return array[rightIdx]
        # Update the indices for the next iteration based on the position of the right index
        elif rightIdx < position:
            startIdx = rightIdx + 1
        else:
            endIdx = rightIdx - 1


def swap(one, two, array):
    """
    Swaps two elements in the given array.
    
    Args:
        one (int): Index of the first element to swap.
        two (int): Index of the second element to swap.
        array (list): The input list of integers.
    """
    array[one], array[two] = array[two], array[one]

# Unit tests
import unittest

class TestQuickSelect(unittest.TestCase):
    def test_quickselect(self):
        self.assertEqual(quick_select_helper([8, 5, 2, 9, 7, 6, 3], 3), 5)  # expected output: 5
        self.assertEqual(quick_select_helper([], 3), None)  # expected output: 0
        
        # Add more test cases for edge cases, empty array, etc.

if __name__ == "__main__":
    unittest.main()


my_array = [8,5,2,9,7,6,3]
my_val =3
#expected =5
print(quick_select_helper(my_array, my_val))
