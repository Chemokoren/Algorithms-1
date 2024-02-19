"""
Largest Range

Find the largest range of numbers contained in this array wherethe range of numbers is a set of 
numbers that come after one another in the set of real integers for instance the range from
2-5 consists of numbers 2,3,4,5

A range does not necessarily need to have all the numbers next to each other in the array. It's
just that the numbers need to be contained somewhere in the array.

Given the array, [1,11,3,0,15,5,2,4,10,7,12,6], here are the sample ranges we can create.
1) [0,1,2,3,4,5,6,7]
2) [10,11,12]
3) [5]

The thought process

The thought process behind the largestRange function is to find the longest consecutive sequence of numbers in a given array. Here's a breakdown of the approach:

First, I will look at the three main steps before subsequently breaking them into sub-steps that are 
easier to understand.

- Iterate through the array once and put everything in the hash table with each value initialized to True.
- Go through all the numbers a second time and expanded outwards where necessary and marked them as False.
- We store the range using pointers to the first and last value and the length of the range in a variable
leading to constant space utilization

    Initialize Variables:
        bestRange: Store the start and end indices of the longest consecutive sequence found so far.
        longestLength: Store the length of the longest consecutive sequence found so far.
        nums: Use a dictionary to keep track of whether each number in the array has been visited.

    Mark Numbers as Visited:
        Iterate through the array and mark each number as visited in the nums dictionary.

    Iterate Through Numbers:
        For each number in the array:
            If it has already been visited, skip to the next number.
            Otherwise, mark it as visited and start counting the length of the consecutive sequence.
            Initialize the left and right boundaries of the current sequence.

    Extend Sequence:
        Extend the sequence to the left and right as long as consecutive numbers are found.
        Mark each visited number in the nums dictionary and update the length of the current sequence.

    Update Longest Sequence:
        If the length of the current sequence is longer than the longest sequence found so far, update longestLength and bestRange accordingly.

    Return Result:
        After iterating through all numbers, return the bestRange, which represents the start and end of the longest consecutive sequence.

The key idea behind this solution is to use a dictionary to efficiently keep track of visited numbers and to iterate through each number in the array, extending consecutive sequences to the left and right. By updating longestLength and bestRange whenever a longer sequence is found, the function eventually returns the longest consecutive sequence in the array.

Time Complexity
- O(N) Because we loop through the array twice in two seperate iterations. In the first iteration,
we map the values as True while adding them to a hashtable.
- In the second iteration, we expanded outwards of the given number while doing constant operations and
marking the value as False.

Space Complexity
- O(N) because we created a hashtable to store every single element in the array.
- We also store the start and end values of the array in constant time and the longest length of
range encountered in constant time.

Let's analyze the time and space complexity of the largestRange function:

    Time Complexity:
        The function iterates through the input array twice: once to mark each number as visited and once to find the longest consecutive sequence.
        Inside the second loop, there are two nested while loops that extend the consecutive sequence to the left and right as long as consecutive numbers are found.
        The worst-case time complexity is O(n), where n is the length of the input array. This is because each number in the array is visited only once, and the while loops inside the second loop also contribute to linear time complexity.
    Space Complexity:
        The function uses a dictionary nums to keep track of visited numbers. The space required for this dictionary is proportional to the number of unique elements in the input array.
        In the worst case, where all numbers in the input array are unique, the space complexity is O(n), where n is the length of the input array.
        Additionally, the space complexity of other variables (bestRange, longestLength) is constant and does not depend on the size of the input array.

In summary, the time complexity of the largestRange function is O(n) and the space complexity is also O(n), where n is the length of the input array. This solution is efficient and should work well for arrays of moderate size. However, if the input array is extremely large, the space complexity could become a concern due to the dictionary used to track visited numbers.

"""

# O(n) time | O(n) space
def largestRange(array):
    """
    Finds the largest range of consecutive numbers in the given array.

    Args:
    - array: A list of integers.

    Returns:
    - A list containing the start and end of the largest range found.
    """
    bestRange = []          # Store the best range found so far
    longestLength = 0       # Store the length of the longest range found so far
    nums = {}               # Dictionary to store if a number has been visited

    # Mark all numbers in the array as unvisited
    for num in array:
        nums[num] = True

    # Iterate through each number in the array
    for num in array:
        # Skip if the number has already been visited
        if not nums[num]:
            continue

        nums[num] = False   # Mark the current number as visited
        currentLength = 1   # Initialize the length of the current range
        left = num - 1      # Initialize left boundary of the range
        right = num + 1     # Initialize right boundary of the range

        # Extend the range to the left as long as consecutive numbers are found
        while left in nums:
            nums[left] = False      # Mark the number as visited
            currentLength += 1      # Increment the length of the current range
            left -= 1              # Move to the left

        # Extend the range to the right as long as consecutive numbers are found
        while right in nums:
            nums[right] = False     # Mark the number as visited
            currentLength += 1      # Increment the length of the current range
            right += 1             # Move to the right

        # Check if the current range is the longest found so far
        if currentLength > longestLength:
            longestLength = currentLength   # Update the length of the longest range
            bestRange = [left + 1, right - 1]   # Update the best range found so far

    return bestRange

# Example usage:
my_range = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(largestRange(my_range))


"""
some unit tests written using Python's built-in unittest module to test the largestRange function

In these tests:

    test_empty_array: Tests the function with an empty array.
    test_single_element: Tests the function with an array containing only one element.
    test_no_consecutive_sequence: Tests the function with an array that has no consecutive sequence.
    test_all_consecutive_sequence: Tests the function with an array where all elements form a consecutive sequence.
    test_mixed_consecutive_sequence: Tests the function with an array containing a mixed consecutive sequence.
    test_duplicate_numbers: Tests the function with an array containing duplicate numbers.
    test_negative_numbers: Tests the function with an array containing negative numbers.
    test_large_input: Tests the function with a large input array to check performance and correctness.

These tests cover various scenarios to ensure that the largestRange function behaves as expected. You can run these tests using the unittest module by executing the script, or you can integrate them into your test suite if you're using a testing framework like pytest.


"""

import unittest

class TestLargestRange(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(largestRange([]), [])

    def test_single_element(self):
        self.assertEqual(largestRange([5]), [5, 5])

    def test_no_consecutive_sequence(self):
        self.assertEqual(largestRange([4, 2, 10, 6]), [4, 4])

    def test_all_consecutive_sequence(self):
        self.assertEqual(largestRange([1, 2, 3, 4, 5]), [1, 5])

    def test_mixed_consecutive_sequence(self):
        self.assertEqual(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]), [0, 7])

    def test_duplicate_numbers(self):
        self.assertEqual(largestRange([1, 1, 1, 1, 1]), [1, 1])

    def test_negative_numbers(self):
        self.assertEqual(largestRange([-1, -3, -2, -4]), [-4, -1])

    def test_large_input(self):
        # Test with a large input array
        large_input = list(range(1000000))
        self.assertEqual(largestRange(large_input), [0, 999999])

if __name__ == '__main__':
    unittest.main()

