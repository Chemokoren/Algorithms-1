from typing import List
"""
Trapping Rain Water

Givn n non-negative integers representing an elevation map where the width of each bar is 1, compute
how much water it can trap after raining.

Example 1:

Input height: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map(black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]
In this case, 6 units of rain water (blue section) are being trapped.
"""

# O(n) time | O(1) space
class Solution:

    def trap(self,height: List[int])->int:

        if not height: return 0

        l, r = 0, len(height) -1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax =max(leftMax, height[l])
                res += leftMax -height[l]
            else:
                r -= 1
                rightMax =max(rightMax, height[r])
                res += rightMax -height[r]
        return res

sol = Solution()
arr =[0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(arr))