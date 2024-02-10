"""
The Knapsack Problem involves selecting a combination of items to maximize the value while staying within the capacity constraint of the knapsack.

Problem Case:
Given a list of items, each with a value and weight, and a capacity constraint for the knapsack, the task is to determine the maximum value that can be obtained by selecting a subset of the items such that the total weight does not exceed the capacity.

Thought Process:

    Initialization: Initialize a 2D array knapsackValues of size (n+1) * (C+1), where n is the number of items and C is the capacity of the knapsack. Set all values to zero.
    Iterating over Items: Iterate over each item in the list.
    Updating Values: For each item, iterate over each possible capacity value from 0 to the total capacity.
        If the weight of the current item is greater than the current capacity, set the value in the knapsackValues array to the value of the previous item at the same capacity.
        Otherwise, set the value to the maximum of either the previous item's value at the same capacity or the value of the current item plus the value of the remaining capacity obtained by subtracting the current item's weight.
    Backtracking: After calculating all possible values, backtrack to determine which items were selected to achieve the maximum value while staying within the capacity constraint.
    Return: Return the maximum value and the indices of the selected items.

The solution leverages dynamic programming to efficiently solve the problem by breaking it down into smaller subproblems and storing their solutions to avoid redundant calculations.



The time complexity of the Knapsack Problem solution using dynamic programming is O(n * C), where n is the number of items and C is the capacity of the knapsack. This is because we have a nested loop iterating over each item and each possible capacity value.

The space complexity is also O(n * C) because we are creating a 2D array of size (n+1) * (C+1) to store the intermediate values of the knapsack problem.

"""
# O(nc) time | O(nc) space
def knapsackProblem(items, capacity):
    """
    Solves the 0/1 knapsack problem using dynamic programming.

    Args:
        items (List[Tuple[int, int]]): List of tuples representing items, where each tuple contains
                                        the value and weight of the item.
        capacity (int): The maximum weight capacity of the knapsack.

    Returns:
        Tuple[int, List[int]]: A tuple containing the maximum value that can be achieved with the given
                                capacity and a list of indices of the selected items.

    Time Complexity: O(n * c), where n is the number of items and c is the capacity of the knapsack.
    Space Complexity: O(n * c), where n is the number of items and c is the capacity of the knapsack.
    """
    # Initialize a 2D list to store knapsack values
    knapsackValues = [[0 for x in range(0, capacity + 1)] for y in range(0, len(items) + 1)]
    
    # Iterate over each item
    for i in range(1, len(items) + 1):
        currentWeight = items[i - 1][1]  # Get the weight of the current item
        currentValue = items[i - 1][0]   # Get the value of the current item
        
        # Iterate over each possible capacity
        for c in range(0, capacity + 1):
            # If the current weight exceeds the current capacity, use the value from the previous row
            if currentWeight > c:
                knapsackValues[i][c] = knapsackValues[i - 1][c]
            else:
                # Otherwise, take the maximum value between using the current item or not using it
                knapsackValues[i][c] = max(knapsackValues[i - 1][c], knapsackValues[i - 1][c - currentWeight] + currentValue)
    
    # Return the maximum value and the selected items
    return [knapsackValues[-1][-1], getKnapSackItems(knapsackValues, items)]

def getKnapSackItems(knapsackValues, items):
    """
    Retrieves the indices of the items selected for the knapsack based on the computed values.

    Args:
        knapsackValues (List[List[int]]): 2D list containing the computed knapsack values.
        items (List[Tuple[int, int]]): List of tuples representing items.

    Returns:
        List[int]: A list of indices of the selected items.

    Time Complexity: O(n), where n is the number of items.
    Space Complexity: O(n), where n is the number of items.
    """
    sequence = []   # Initialize a list to store the selected item indices
    i = len(knapsackValues) - 1   # Start from the last row of knapsackValues
    c = len(knapsackValues[0]) - 1   # Start from the last column of knapsackValues
    
    # Traverse the knapsackValues table to determine the selected items
    while i > 0:
        if knapsackValues[i][c] == knapsackValues[i - 1][c]:
            # If the current value is equal to the value above, move to the row above
            i -= 1
        else:
            # Otherwise, add the index of the current item to the sequence
            sequence.append(i - 1)
            c -= items[i - 1][1]   # Subtract the weight of the current item from the current capacity
            i -= 1   # Move to the row above
        
        # If the remaining capacity is 0, break out of the loop
        if c == 0:
            break
    
    # Return the reversed sequence of selected item indices
    return list(reversed(sequence))

my_items =[[1,2],[4,3],[5,6],[6,7]]
my_capacity =10

print(knapsackProblem(my_items,my_capacity))

import unittest

class TestKnapsackProblem(unittest.TestCase):

    def test_knapsack_problem(self):
        # Test case 1
        items = [(60, 5), (50, 3), (70, 4), (30, 2)]
        capacity = 5
        expected_result = (80, [1, 3])  # Max value = 120, Selected items: (50, 3) and (70, 4)
        self.assertEqual(tuple(knapsackProblem(items, capacity)), expected_result)

        # Test case 2
        items = [(40, 4), (30, 3), (50, 5), (10, 1)]
        capacity = 8
        expected_result = (80, [1, 2])  # Max value = 90, Selected items: (50, 5), (30, 3), and (10, 1)
        self.assertEqual(tuple(knapsackProblem(items, capacity)), expected_result)

        # Test case 3
        items = [(70, 7), (20, 3), (39, 4), (37, 5), (5, 1), (10, 2)]
        capacity = 10
        expected_result = (90, [0, 1])  # Max value = 107, Selected items: (5, 1), (37, 5), (20, 3), and (70, 7)
        self.assertEqual(tuple(knapsackProblem(items, capacity)), expected_result)

        # Test case 4 (Edge case: Empty items list)
        items = []
        capacity = 5
        expected_result = (0, [])  # Max value = 0, No items selected
        self.assertEqual(tuple(knapsackProblem(items, capacity)), expected_result)

        # Test case 5 (Edge case: Zero capacity)
        items = [(30, 3), (20, 2), (40, 4)]
        capacity = 0
        expected_result = (0, [])  # Max value = 0, No items selected
        self.assertEqual(tuple(knapsackProblem(items, capacity)), expected_result)

if __name__ == "__main__":
    unittest.main()

