"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+'
and '-' before each integer in nums and then concatenate all the integers.

For exaample, if nums =[2, 1], you can add a '+' before 2 and a '-' before 1 and 
concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums =[1,1,1,1,1], target=3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3



"""
from typing import List
class Solution:

    def findTargetSumWays(self, nums: List[int], target : int)-> int:
        dp ={} # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) +
                                backtrack(i +1, total - nums[i]))
            return dp[(i, total)]
        return backtrack(0, 0)
    
sol = Solution()
print(sol.findTargetSumWays([1,1,1,1,1], target=3))