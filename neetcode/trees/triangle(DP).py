from typing import List
"""
Given a triangle array, return the minimum path sum from top to bottom. For each step, 
you may move to an adjacent number on the row below.

Example 1:

Input: triangle =[[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
                       2
                      /  \
                    3      4
                  /  \   /   \
                6      5      4
               /  \   /  \  /   \
              4     1     8      3    

Explanation: The minimum path sum from top to bottom is 11 (i.e., 2+3+5+1 = 11).

Example 2:
Input: triangle =[[-10]]
Output: -10

Memory complexity is O(n) where n is the number of rows we have
Time complexity =O(n^2) where n is the number of elements we have
"""

class solution:
    """
    Bottom-up dynamic programming approach to efficiently calculate the minimum path sum
    by iteratively updating the optimal substructure.
    
    """

    def minimum_total(self, triangle: List[List[int]])->int:
        """
        Method returns the minimum path sum from top to bottom for a given triangle.
        
        Parameters:
            triangle(List[List[int]]): triangle array
        Returns:
            int:  minimum path sum from top to bottom
        
        """
        # initialize dp array with the length of the triangle plus 1
        dp =[0] * (len(triangle)+ 1)

        # iterates over the rows of the triangle in reverse order
        for row in triangle[::-1]: 
            for i, n in enumerate(row):
                # The minimum path sum to reach the current element n is calculated by 
                # adding n to the minimum of the adjacent elements in the next row, 
                # dp[i] and dp[i+1].
                dp[i] =n + min(dp[i], dp[i+1])
        # after the loop completes, the minimum path sum from the top to the bottom of the 
        # triangle is stored in dp[0]
        return dp[0]


sol =solution()
print(sol.minimum_total([[2],[3,4],[6,5,7],[4,1,8,3]]))
        
        