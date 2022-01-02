from typing import List
"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is
1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1 given height =[2,1,5,6,2,3]
The largest rectangle rectangle has an area of 10 units.

Example:
Input: [2,5,6,2,3]
Output: 10

"""
# O(n) Time | O(n) space - because of the stack

class Solution:

    def largestRectangleArea(self, heights: List[int])-> int:
        maxArea =0
        stack =[] # pair: (index,height)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height =stack.pop()
                maxArea =max(maxArea, height *(i -index))
                start =index
            stack.append((start, h))
        for i, h in stack:
            maxArea =max(maxArea,h *(len(heights) - i))
        return maxArea

nums =[2,5,6,2,3]
sol = Solution()
print(sol.largestRectangleArea(nums))