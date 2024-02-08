"""
The problem this solution is trying to solve is to find the three largest numbers in a given array of integers. The solution iterates through the array and maintains a list threeLargest to store the three largest numbers encountered so far.

It does this by updating the threeLargest list whenever it encounters a number larger than any of the current three largest numbers. The update_largest function is responsible for updating the threeLargest list with the new number, and the shift_and_update function helps shift the existing numbers in the list to accommodate the new number.

Overall, the goal is to efficiently find and return the three largest numbers in the array while traversing through it only once.


This code finds the three largest numbers in an array by iterating through each number and updating 
the three largest numbers accordingly. 
The update_largest function is responsible for updating the three largest numbers with a new number,
while the shift_and_update function is used to shift the elements in the array when updating.

Time & Space Complexity

The time complexity of this solution is O(n), where n is the number of elements in the input array. This is because the solution iterates through the array once to update the three largest numbers.

The space complexity is O(1) because the solution maintains a fixed-size list threeLargest to store the three largest numbers, regardless of the size of the input array. Therefore, the space used by the algorithm does not increase with the size of the input array.

"""

# O(n) time | O(1) space
def find_three_largest_numbers(array):
    """
    Find the three largest numbers in the given array.

    Args:
        array (list): The input array of integers.

    Returns:
        list: A list containing the three largest numbers found in the array.

    Example:
        >>> find_three_largest_numbers([10, 5, 9, 10, 12])
        [10, 10, 12]
    """
    # Initialize an array to store the three largest numbers
    threeLargest = [None, None, None]
    
    # Iterate through each number in the input array
    for num in array:
        # Update the three largest numbers with the current number
        update_largest(threeLargest, num)
    
    # Return the three largest numbers found
    return threeLargest

def update_largest(threeLargest, num):
    """
    Update the three largest numbers with a new number.

    Args:
        threeLargest (list): A list containing the three largest numbers.
        num (int): The new number to be considered for updating the three largest numbers.

    Returns:
        None

    Example:
        >>> update_largest([10, 10, 12], 9)
        [10, 10, 12]
    """
    # Check if the new number is greater than the third largest number
    if threeLargest[2] is None or num > threeLargest[2]:
        # Shift the numbers and update the third largest number
        shift_and_update(threeLargest, num, 2)
    # Check if the new number is greater than the second largest number
    elif threeLargest[1] is None or num > threeLargest[1]:
        # Shift the numbers and update the second largest number
        shift_and_update(threeLargest, num, 1)
    # Check if the new number is greater than the first largest number
    elif threeLargest[0] is None or num > threeLargest[0]:
        # Shift the numbers and update the first largest number
        shift_and_update(threeLargest, num, 0)

def shift_and_update(array, num, idx):
    """
    Shift the elements in the array to update the specified index with a new number.

    Args:
        array (list): The array containing the elements to be shifted.
        num (int): The new number to be inserted into the array.
        idx (int): The index where the new number should be inserted.

    Returns:
        None

    Example:
        >>> shift_and_update([10, 10, 12], 9, 2)
        [10, 10, 9]
    """
    # Iterate through the array up to the specified index
    for i in range(idx + 1):
        # If the current index is the specified index, update it with the new number
        if i == idx:
            array[i] = num
        # Otherwise, shift the element to the right
        else:
            array[i] = array[i + 1]



import unittest

class TestThreeLargestNumbers(unittest.TestCase):

    def test_three_largest_numbers(self):
        """
        Test for finding the three largest numbers in an array.
        """
        self.assertListEqual(find_three_largest_numbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])

    def test_empty_array(self):
        """
        Test for an empty input array.
        """
        self.assertListEqual(find_three_largest_numbers([]), [None, None, None])

    def test_duplicate_numbers(self):
        """
        Test for an input array with duplicate numbers.
        """
        self.assertListEqual(find_three_largest_numbers([5, 5, 2, 9, 10]), [5, 9, 10])

    def test_negative_numbers(self):
        """
        Test for an input array with negative numbers.
        """
        self.assertListEqual(find_three_largest_numbers([-5, -10, -2, -9, -7]), [-7, -5, -2])

    def test_single_element_array(self):
        """
        Test for an input array with only one element.
        """
        self.assertListEqual(find_three_largest_numbers([100]), [None, None, 100])

    def test_all_negative_numbers(self):
        """
        Test for an input array with all negative numbers.
        """
        self.assertListEqual(find_three_largest_numbers([-5, -10, -2, -9, -7]), [-7, -5, -2])

if __name__ == "__main__":
    unittest.main()
