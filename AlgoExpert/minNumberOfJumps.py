"""
The problem tackled by the minNumberOfJumps function is finding the minimum number of jumps needed 
to reach the end of an array, where each element in the array represents the maximum number of steps 
that can be taken from that position.

Problem Case:
Given an array representing the maximum number of steps that can be taken from each position,
the task is to find the minimum number of jumps needed to reach the end of the array.


Thought Process for Solving:

    Initialization: Initialize an array jumps to store the minimum number of jumps needed to reach each position in the input array. Set jumps[0] to 0 since no jumps are needed to reach the starting position.
    Iterative Approach: Iterate through the array starting from index 1. For each position i, iterate backwards from index 0 to i - 1.
    Updating Jumps: For each position i, check if it's possible to reach position i from position j. If reachable, update jumps[i] to be the minimum of its current value and jumps[j] + 1, indicating the number of jumps needed to reach j plus one additional jump to reach i.
    Return Result: Return the value of jumps[-1], which represents the minimum number of jumps needed to reach the last index of the array.

By following this thought process, the function efficiently computes the minimum number of jumps required to reach the end of the array, providing a solution to the problem.


    Algorithm:
        - Initialize an array 'jumps' to store the minimum number of jumps needed
          to reach each position in the input array. Set jumps[0] to 0 since no jumps
          are needed to reach the starting position.
        - Iterate through the array starting from index 1:
            - For each position 'i', iterate backwards from index 0 to 'i - 1':
                - Check if it's possible to reach position 'i' from position 'j':
                    - If reachable, update jumps[i] to be the minimum of its current value
                      and jumps[j] + 1 (indicating the number of jumps needed to reach 'j'
                      plus one additional jump to reach 'i').
        - Return the value of jumps[-1], which represents the minimum number of jumps
          needed to reach the last index of the array.

    Complexity Analysis:
        - Time Complexity: O(n^2) where 'n' is the length of the input array.
          This is because for each element in the array, we potentially iterate
          through all previous elements to update the jumps array.
        - Space Complexity: O(n) for the jumps array, where 'n' is the length of the
          input array. We also use a constant amount of additional space for variables
          and loop indices.

"""
# O(n ^ 2) time | O(n) space
def minNumberOfJumps(array):
    """
    Finds the minimum number of jumps needed to reach the last index of the given array.

    Args:
        array (List[int]): The input array representing the maximum number of steps
                           that can be taken from each position.

    Returns:
        int: The minimum number of jumps needed to reach the last index.


    """
    jumps = [float("inf") for x in array]  # Initialize jumps array with infinite jumps
    jumps[0] = 0  # No jumps needed to reach the starting position
    for i in range(1, len(array)):  # Iterate through array starting from index 1
        for j in range(0, i):  # Iterate backwards from index 0 to i - 1
            if array[j] + j >= i:  # Check if it's possible to reach position i from j
                # Update jumps[i] to be the minimum of its current value and jumps[j] + 1
                jumps[i] = min(jumps[j] + 1, jumps[i])
    return jumps[-1]  # Return the minimum number of jumps needed to reach the last index



"""
The thought process behind this solution involves traversing the array and determining the minimum 
number of jumps needed to reach the end. Here's a breakdown of the steps:

    Initialization:
        Initialize jumps to 0, representing the total number of jumps needed.
        Initialize maxReach to the value of the first element in the array, indicating the farthest
         position that can be reached with the current number of jumps.
        Initialize steps to the value of the first element, representing the remaining steps that can
         be taken from the current position.

    Traversal:
        Iterate through the array starting from the second element.
        For each position i:
            Update maxReach to the maximum value between the current maxReach and the sum of i and the
              value at position i, which represents the farthest reachable position.
            Decrement steps by 1, indicating that one step is taken from the current position.
            If steps becomes 0, it means that no more steps can be taken from the current position 
            without jumping. In this case:
                Increment jumps by 1, as a jump is required to move further.
                Update steps to the difference between the current maxReach and i, representing the 
                remaining steps based on the farthest reachable position.

    Return:
        After traversing the entire array, return jumps + 1, where jumps represents the total number
          of jumps required. Adding 1 accounts for the final jump to reach the end of the array.

This approach efficiently calculates the minimum number of jumps needed to reach the end of the array
 by dynamically updating the farthest reachable position and the remaining steps at each iteration.


 The time and space complexity of the provided solution are as follows:

    Time Complexity:
        The solution traverses the input array once in a linear manner, which results in a time complexity of O(n), where n is the length of the input array.

    Space Complexity:
        The solution uses a constant amount of additional space for variables (jumps, maxReach, steps) and does not rely on any auxiliary data structures proportional to the input size.
        Therefore, the space complexity is O(1) (constant space complexity).

Overall, the solution is efficient, with linear time complexity and constant space complexity, making it suitable for handling large input arrays efficiently.

"""
# O(n) time | O(1) space
def min_NumberOfJumps(array):
    """
    Finds the minimum number of jumps required to reach the end of an array, where each element represents the maximum
    number of steps that can be taken from that position.

    Args:
        array (List[int]): The input array representing the maximum number of steps that can be taken from each position.

    Returns:
        int: The minimum number of jumps needed to reach the end of the array.

    Example:
        >>> minNumberOfJumps([2, 3, 1, 1, 2, 4, 2, 0, 1, 1])
        4
    """
    # If there is only one element in the array, no jumps are needed
    if len(array) == 1:
        return 0
    
    jumps = 0             # Initialize the number of jumps
    maxReach = array[0]   # Initialize the farthest position that can be reached with the current number of jumps
    steps = array[0]      # Initialize the remaining steps that can be taken from the current position
    
    # Iterate through the array starting from the second element
    for i in range(len(array)):
        # If the current index exceeds the farthest reachable position
        if i > maxReach:
            return -1  # Unable to reach the end of the array
        
        maxReach = max(maxReach, i + array[i])  # Update the farthest position that can be reached
        
        # If no more steps are left, a jump is required
        if steps == 0:
            jumps += 1                         # Increment the number of jumps
            steps = maxReach - i               # Update the remaining steps based on the farthest reachable position
        
        steps -= 1                             # Decrement the remaining steps
    
    return jumps  # Return the total number of jumps required to reach the end of the array




# Returns the number of arrangements to
# form 'n'
# def solve(n):
#     if n < 1:
#         return 0
#     if n == 1:
#         return 1
#     return (solve(n - 1) +
# 		solve(n - 3) +
# 		solve(n - 5))

# my_array =[1,3,5]
# print(solve(3))

import unittest

class TestMinNumberOfJumps(unittest.TestCase):

    def test_min_number_of_jumps(self):
        # Test case with a regular array
        self.assertEqual(minNumberOfJumps([2, 3, 1, 1, 2, 4, 2, 0, 1, 1]), 5)
        
        # Test case with a sorted array
        self.assertEqual(minNumberOfJumps([1, 2, 3, 4, 5]), 3)
        
        # Test case with a single element array
        self.assertEqual(minNumberOfJumps([0]), 0)
        
        # Test case with an empty array
        self.assertEqual(minNumberOfJumps([]), 0)
        
        # Test case with a large array
        self.assertEqual(minNumberOfJumps([1] * 10**6), 999999)
        
        # Test case with a decreasing array
        self.assertEqual(minNumberOfJumps([5, 4, 3, 2, 1]), 1)
        
        # Test case with a increasing array
        self.assertEqual(minNumberOfJumps([1, 2, 3, 4, 5]), 4)
        

if __name__ == "__main__":
    unittest.main()
