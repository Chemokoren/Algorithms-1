"""
You are a professional robber planning to rob houses along a street. Each house has a 
certain amount of money stashed, the only contraint stopping you from robbing each one 
of them is that adjacent houses have security system connected and it will automatically
contact the police if two adjacent houses were broken into  on the same night.


Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums =[1, 2, 3, 1]
Output: 4
Explanation: Rob house 1(money=1) and then rob house 3(money=3)
Total amount you can rob = 1+3 = 4
[1, 2, 3, 1, 5, 2, 7]


"""
from typing import List

class Solution:

    def house_robber(self, nums):
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[n-1]
    def rob_optimized(self, nums : List[int])->int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n + 1]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

sol = Solution()
print(sol.house_robber([1, 2, 3, 1]))
print(sol.house_robber([1, 2, 3, 1, 5, 2, 7]))


print(sol.rob_optimized([1, 2, 3, 1]))
print(sol.rob_optimized([1, 2, 3, 1, 5, 2, 7]))