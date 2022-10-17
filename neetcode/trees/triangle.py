from typing import List
"""
Given a triangle array, return the minimum path sum from top to bottom. For each step, 
you may move to an adjacent number on the row below.

Example 1:

Input: triangle =[[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11

Explanation: The minimum path sum from top to bottom is 11 (i.e., 2+3+5+1 = 11).

Example 2:
Input: triangle =[[-10]]
Output: -10

Memory complexity is O(n) where n is the number of rows we have
Time complexity =O(n^2) where n is the number of elements we have
"""

class solution:
    def minimumTotal(self, triangle: List[List[int]])->int:
        """
        Return minimum path sum from top to bottom for a given triangle.
        
            Parameters:
                triangle(List[List[int]]): triangle array
            Returns:
                int:  minimum path sum from top to bottom
        
        """
        dp =[0] * (len(triangle)+ 1)

        for row in triangle[::-1]: # start from the last row
            for i, n in enumerate(row):
                dp[i] =n + min(dp[i], dp[i+1])
        return dp[0]

triangle =[[2],[3,4],[6,5,7],[4,1,8,3]]
sol =solution()
print(sol.minimumTotal(triangle))

def test(nums):
    res =0
    for r in nums:
        res +=min(r)
        
    return res
print("my tests::", test([[2],[3,4],[6,5,7],[4,1,8,3]]))
print("my tests::", test([[-10]]))
        
        