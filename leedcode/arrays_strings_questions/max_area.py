"""

"""
class Solution:
    def maxArea(self, height: int)->int:
        maxarea = 0
        l = 0
        r = len(height) - 1
        while(l < r):
            maxarea = max(maxarea, min(height[l], height[r])* (r-l))
            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1
        return maxarea

my_vals = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.maxArea(my_vals))