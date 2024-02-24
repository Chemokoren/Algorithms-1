"""

The Problem

The problem being solved here is the "Maximum Sum Increasing Subsequence" problem. Given an array of integers, the task is to find a subsequence (not necessarily contiguous) of the array such that the sum of elements in the subsequence is maximum, subject to the condition that the elements in the subsequence are in increasing order.

In simpler terms, we want to find a sequence of numbers from the array where each number is greater than the previous one, and the sum of these numbers is as large as possible.

For example, given the array [8, 12, 2, 3, 15, 5, 7], the maximum sum increasing subsequence is [8, 12, 15], and the sum is 35. This algorithm efficiently finds both the maximum sum and the corresponding subsequence.

The thought process

The algorithm for finding the maximum sum increasing subsequence follows a dynamic programming approach. Here's the step-by-step thought process:

    Initialization:
        We initialize two arrays:
            sequences, which keeps track of the previous index forming the subsequence that ends at the current index.
            sums, which keeps track of the maximum sum of increasing subsequences ending at each index. Initially, it's set to the values of the array.

    Iterating through the array:
        We iterate through each element of the input array.
        For each element at index i, we compare it with all previous elements at indices [0, i).
        If the current element is greater than the previous element and adding it to the sum of the previous subsequence results in a higher sum than the current sum at index i, we update the sum and the corresponding previous index in the sequences array.

    Updating maximum sum index:
        While iterating, we also keep track of the index (maxSumIdx) with the maximum sum found so far.

    Building the subsequence:
        Once we've iterated through all elements, we have the index of the maximum sum subsequence.
        We use the sequences array to backtrack from this index to reconstruct the subsequence.

    Return the result:
        Finally, we return the maximum sum found and the subsequence that achieves this sum.

By following this approach, the algorithm efficiently identifies the maximum sum increasing subsequence by leveraging dynamic programming principles to store and update necessary information as it iterates through the array. This ensures that the solution is optimal in terms of both time and space complexity.


Time & Space Complexity

The time complexity of this solution is O(n2)O(n2), where nn is the length of the input array. This is because we have two nested loops:

    The outer loop runs nn times, iterating through each element of the input array.
    The inner loop runs up to ii times, where ii is the current index of the outer loop. In the worst case scenario, this loop also iterates through all previous elements.

As a result, the total number of iterations across both loops is 1+2+3+…+n−1=n(n−1)21+2+3+…+n−1=2n(n−1)​, which is proportional to n2n2.

The space complexity of this solution is O(n)O(n). This is because we use two additional arrays (sequences and sums), each of which has a length equal to the length of the input array. Hence, the space required is linear with respect to the size of the input array.

"""

# O(n ^ 2) time | O(n) space
def max_sum_increasing_subsequence(array):
    """
    Finds the maximum sum increasing subsequence within the given array.

    Args:
    array (list): The input array of integers.

    Returns:
    list: A list containing two elements:
          1. The maximum sum of the increasing subsequence.
          2. The increasing subsequence itself.

    """
    if not array:
        return [0, []]  # Return [0, []] for empty arrays
    
    # Initialize sequences to keep track of previous indices forming the subsequence
    sequences = [None for x in array]

    # Initialize sums to keep track of the sums of subsequences ending at each index
    sums = array[:]

    # Initialize the index of the maximum sum subsequence
    maxSumIdx = 0

    # Iterate through the array
    for i in range(len(array)):
        currentNum = array[i]

        # Compare with previous elements to find the increasing subsequence with maximum sum
        for j in range(0, i):
            otherNum = array[j]

            # If the current number forms an increasing subsequence with maximum sum
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j

        # Update the index of the maximum sum subsequence
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i

    # Return the maximum sum and the subsequence
    return [sums[maxSumIdx], build_sequence(array, sequences, maxSumIdx)]


def build_sequence(array, sequences, currentidx):
    """
    Builds the increasing subsequence given the array, previous indices, and current index.

    Args:
    array (list): The input array of integers.
    sequences (list): The list containing previous indices forming the subsequence.
    currentidx (int): The index of the current element in the subsequence.

    Returns:
    list: The increasing subsequence formed by the given indices.

    """
    sequence = []

    # Reconstruct the subsequence backwards starting from the current index
    while currentidx is not None:
        sequence.append(array[currentidx])
        currentidx = sequences[currentidx]

    # Reverse the sequence to obtain the correct order
    return list(reversed(sequence))

# Example usage
my_array = [8, 12, 2, 3, 15, 5, 7]
print(max_sum_increasing_subsequence(my_array))


import unittest

class TestMaxSumIncreasingSubsequence(unittest.TestCase):
    
    def test_max_sum_increasing_subsequence(self):
        # Test case with positive integers
        array1 = [8, 12, 2, 3, 15, 5, 7]
        self.assertEqual(max_sum_increasing_subsequence(array1), [35, [8, 12, 15]])
        
        # Test case with negative integers
        array2 = [-2, -3, 4, -1, -2, 1, 5, -3]
        self.assertEqual(max_sum_increasing_subsequence(array2), [9, [4, 5]])
        
        # Test case with all elements equal
        array3 = [1, 1, 1, 1, 1]
        self.assertEqual(max_sum_increasing_subsequence(array3), [1, [1]])
        
        # Test case with a single element
        array4 = [5]
        self.assertEqual(max_sum_increasing_subsequence(array4), [5, [5]])
        
        # Test case with an empty array
        array5 = []
        self.assertEqual(max_sum_increasing_subsequence(array5), [0, []])
        
        # Test case with descending sequence
        array6 = [5, 4, 3, 2, 1]
        self.assertEqual(max_sum_increasing_subsequence(array6), [5, [5]])
        
        # Test case with ascending sequence
        array7 = [1, 2, 3, 4, 5]
        self.assertEqual(max_sum_increasing_subsequence(array7), [15, [1, 2, 3, 4, 5]])
        
if __name__ == '__main__':
    unittest.main()

