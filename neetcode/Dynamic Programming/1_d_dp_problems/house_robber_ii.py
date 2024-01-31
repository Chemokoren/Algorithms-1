"""
House Robber II

You are a professional robber planning to rob houses along a street. Each house has a 
certain amount of money stashed. All houses at this places are arranged in a circle.
That means the first house is the neighbor of the last one. Meanwhile, adjacent houses
have a security system connected, and it will automatically contact the police if two
adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums =[2, 3, 2]
Ouput: 3
Explanation: You cannot rob house 1(money= 2) and then rob house 3( money =2), because 
they are adjacent

[2, 3, 2, 1]
"""
from typing import List

class Solution:


    # time complexity: O(n) | memory complexity: O(1)
    def rob_optimized(self, nums : List[int])->int:
            
            def dfs(nums):
                rob1, rob2 = 0, 0

                # [rob1, rob2, n, n + 1]
                for n in nums:
                    temp = max(n + rob1, rob2)
                    rob1 = rob2
                    rob2 = temp
                return rob2
            return max(nums[0],dfs(nums[1:]), dfs(nums[:-1]))
    
sol = Solution()
print(sol.rob_optimized([2]))
print(sol.rob_optimized([2, 3, 2]))
print(sol.rob_optimized([2, 3, 2, 1]))
print(sol.rob_optimized([1, 2, 3, 1, 5, 2, 7]))


        