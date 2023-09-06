"""
Target Sum

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before
each integer in nums and then concatenate all the integers.

- For example, if nums =[2, 1], you can add a '+' before 2 and a '-' before 1 and 
concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.

Example 1

Input: nums =[1,1,1,1,1], target =3

Output = 5

Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3


"""
from typing import List
from collections import defaultdict
class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) ->int:

        dp ={} # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            
            if (i, total) in dp:
                return dp[(i, total)]
            """
            Two recursive calls are made, one adds the current item, the other subtracts it. 
            Each of these choices creates a new path to explore, but eventually when that path has 
            been fully explored, 
            it will return a value (if there is no way to use any of the numbers after i, that can 
            make the current total == target, then it returns 0. 
            But if there were one or more ways, it would return that value). 
            Now imagine this has happened from the very bottom, all the way back to the top,
            and we're back to our very first call, that means every other node in the tree except
            the very first one has been evaluated, 
            therefore we can just add the results of both choices.
            """
            dp[(i, total)] =(backtrack(i + 1, total + nums[i]) +
                             backtrack(i + 1, total -nums[i]))
            return dp[(i, total)]
        return backtrack(0, 0)
    
    def findTargetSumWaysTwo(self, nums, target):
        dp = defaultdict(int)
        dp[0] = 1


        for num in nums:
            new_dp = defaultdict(int)
            for n in dp:
                new_dp[n+num] += dp[n]
                new_dp[n-num] += dp[n]

            dp = new_dp


        return dp[target]
    
    def findTargetSumWaysThree(self, nums: List[int], target: int) -> int:
        dp = {}
        dp[0] = 1
        for n in nums:
            newdp = {}
            for key in dp:
                if (key + n) in newdp:
                    newdp[key + n] += dp[key]
                else:
                    newdp[key + n] = dp[key]
                if (key - n) in newdp:
                    newdp[key - n] += dp[key]
                else:
                    newdp[key - n] = dp[key]
            dp = newdp
        return dp.get(target, 0)


    def findTargetSumWaysFour(self, nums: List[int], target: int) -> int:
        # the key is the current sum, the value is the number of possible expressions
        dp: dict[int, int] = {0: 1}

        for num in reversed(nums):
            dp_next: dict[int, int] = {}
            for cur_sum, count in dp.items():
                dp_next[cur_sum + num] = dp_next.get(cur_sum + num, 0) + count
                dp_next[cur_sum - num] = dp_next.get(cur_sum - num, 0) + count
            dp = dp_next

        return dp.get(target, 0)

nums, target =[1,1,1,1,1], 3

sol = Solution()
print(sol.findTargetSumWays(nums, target))
print("Example 2::", sol.findTargetSumWaysTwo(nums, target))
print("Example 3::", sol.findTargetSumWaysThree(nums, target))
print("Example 4::", sol.findTargetSumWaysFour(nums, target))
