"""
Problem case
The problem is to find the total area of trapped rainwater between a series of walls represented by 
the given heights.

To solve this problem, we need to iterate through the list of heights twice.

    In the first pass, we calculate the maximum height encountered from the left side for each wall 
    and store it in an auxiliary list called maxes.
    In the second pass, we calculate the maximum height encountered from the right side for each wall.
    We also calculate the minimum height between the maximum height from the right and the maximum 
    height from the left for each wall. 
    If the height of the current wall is less than this minimum height, it means water can be trapped 
    at that position, and we add the trapped water height to the total water area.
    Finally, we return the sum of all trapped water heights.

This approach effectively calculates the trapped water area between the walls. By maintaining the maximum heights from both the left and right sides, we can determine how much water can be trapped at each wall position.

The thought process involves considering the properties of trapped water and how they relate to the given heights. By breaking down the problem into smaller steps and using auxiliary data structures to store intermediate results, we can efficiently solve the problem in linear time and space complexity.


Time & Space Complexity

The time complexity of the waterArea function is O(n), where n is the number of heights in the input 
list. This is because the function iterates through the list of heights twice, once from left to 
right and once from right to left, each iteration taking O(n) time.

The space complexity of the function is also O(n). This is because the function creates an additional
list maxes of the same length as the input list to store the maximum heights encountered from the 
left side. Therefore, the space required is proportional to the size of the input list.

Yes, further optimizations can be made to improve the efficiency of the solution. Here are some potential optimizations:

    Two-Pointer Approach: 
    Instead of storing the maximum heights from both the left and right sides in separate arrays, we 
    can use a two-pointer approach to calculate them on-the-fly as we traverse the heights array 
    from left to right and then from right to left. This reduces the space complexity from O(n) to O(1).
    

    Single Pass Solution: Instead of iterating through the heights array twice, we can perform the calculations in a single pass. This can be achieved by using two pointers starting from the left and right ends of the array and moving towards each other, calculating the trapped water area as we go.

    Stack-Based Solution: We can also solve this problem using a stack-based approach, which allows us to track potential areas where water can be trapped more efficiently. By maintaining a stack of indices of walls in non-decreasing order of height, we can easily calculate the trapped water area by considering the heights of walls and the distances between them.

    Dynamic Programming: We can apply dynamic programming techniques to optimize the solution further. By precomputing certain values or storing intermediate results, we can avoid redundant calculations and improve the overall runtime complexity.

These optimizations can significantly enhance the performance of the solution, making it more efficient, especially for large input sizes. However, they may require a deeper understanding of the problem and more complex implementation compared to the initial approach.



"""

# O(n ) time | O(n) space
def water_area(heights):
    """
    Calculate the total area of trapped water between the given heights.

    Args:
        heights (List[int]): A list of integers representing the heights of walls.

    Returns:
        int: The total area of trapped water.

    Example:
        water_area([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) => 6
    """
    res= [0] * len(heights)
    rights = [0] * len(heights)
    lefts = [0] * len(heights)
    leftMax = 0

    # Calculate the maximum height of walls to the left of each index
    for i in range(len(heights)):
        height = heights[i]
        lefts[i] = leftMax
        leftMax = max(leftMax, height)

    rightMax = 0

    # Calculate the maximum height of walls to the right of each index
    for i in reversed(range(len(heights))):
        height = heights[i]
        rights[i] =rightMax
        rightMax = max(rightMax, height)

    for i in range(len(heights)):
        height = heights[i]
        minHeight = min(lefts[i], rights[i])
        if height < minHeight:
            res[i] = minHeight - height
        else:
            res[i] = 0

    return sum(res)


print(" ---------------------------- updated ----------------------------\n")
# O(n ) time | O(n) space
def water_area_updated(heights):
    """
    Calculate the total area of trapped water between the given heights.

    Args:
        heights (List[int]): A list of integers representing the heights of walls.

    Returns:
        int: The total area of trapped water.

    Example:
        water_area([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) => 6
    """
    maxes = [0] * len(heights)
    leftMax = 0

    # Calculate the maximum height of walls to the left of each index
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax, height)
    print(f"left maxes:: {maxes}")

    rightMax = 0

    # Calculate the trapped water area for each index
    for i in reversed(range(len(heights))):
        height = heights[i]
        minHeight = min(rightMax, maxes[i])
        if height < minHeight:
            maxes[i] = minHeight - height
        else:
            maxes[i] = 0
        rightMax = max(rightMax, height)

    return sum(maxes)


print("------------------------- two pointer approach --------------------------")
"""
This implementation uses two pointers (left and right) starting from the left and right ends of the
array, respectively. 
As they move towards each other, the algorithm calculates the trapped water area between the walls 
represented by the heights array. 
It updates the maximum height encountered from the left and right sides (leftMax and rightMax) and 
calculates the water trapped at each position based on the minimum height of the two walls.


The time complexity of this solution is O(N), where N is the number of elements in the heights array. This is because we iterate through the array once using the two-pointer approach, and each iteration takes constant time.

The space complexity is O(1) because we only use a constant amount of extra space for variables like left, right, leftMax, rightMax, and water, regardless of the size of the input array. We don't use any additional data structures that grow with the input size.

"""
def water_area(heights):
    """
    Calculate the total area of water trapped between the bars based on their heights.

    Args:
        heights (List[int]): A list representing the heights of bars.

    Returns:
        int: The total area of water trapped between the bars.

    Explanation:
        This function utilizes the Two-Pointer Approach to calculate the water area trapped between 
        bars.
        It starts with two pointers at the left and right ends of the array and moves them towards 
        each other.
        At each step, it calculates the water trapped based on the minimum height of the walls and 
        updates the maximum height encountered from the left and right sides.
    """
    # Handle empty input case
    if not heights:
        return 0
    
    # Initialize pointers and maximum heights
    left = 0
    right = len(heights) - 1
    leftMax = heights[left]
    rightMax = heights[right]
    water = 0
    
    # Main loop using two-pointer approach
    while left < right:
        # Process the shorter bar first
        if heights[left] < heights[right]:
            # If the current bar is taller than the leftMax, update leftMax
            if heights[left] >= leftMax:
                leftMax = heights[left]
            # Calculate water trapped between bars
            else:
                water += leftMax - heights[left]
            # Move left pointer
            left += 1
        else:
            # If the current bar is taller than the rightMax, update rightMax
            if heights[right] >= rightMax:
                rightMax = heights[right]
            # Calculate water trapped between bars
            else:
                water += rightMax - heights[right]
            # Move right pointer
            right -= 1
    
    # Return the total water area
    return water

# Test cases
print(water_area([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output should be 6
print(water_area([4,2,0,3,2,5]))              # Output should be 9


import unittest

class TestWaterArea(unittest.TestCase):

    def test_water_area(self):
        self.assertEqual(water_area([0,8,0,0,5,0,0,10,0,0,1,1,0,3]), 48)

    def test_num_water_area_1(self):
        self.assertEqual(water_area([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_water_area_empty(self):
        # Test case with empty input
        heights = []
        self.assertEqual(water_area(heights), 0)

    def test_water_area_single_height(self):
        # Test case with single height
        heights = [5]
        self.assertEqual(water_area(heights), 0)

    def test_water_area_equal_heights(self):
        # Test case with equal heights
        heights = [3, 3, 3, 3, 3]
        self.assertEqual(water_area(heights), 0)

    def test_water_area_descending_heights(self):
        # Test case with descending heights
        heights = [5, 4, 3, 2, 1]
        self.assertEqual(water_area(heights), 0)

    def test_water_area_ascending_heights(self):
        # Test case with ascending heights
        heights = [1, 2, 3, 4, 5]
        self.assertEqual(water_area(heights), 0)

    def test_water_area_symmetric_heights(self):
        # Test case with symmetric heights
        heights = [2, 1, 1, 2]
        self.assertEqual(water_area(heights), 2)

if __name__=="__main__":
    unittest.main()