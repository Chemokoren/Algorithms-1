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
    
    # def find_target_sum_ways(self, nums: List[int], target : int)-> int:
    #     dp  ={} # (index, total) -> # of ways
    #     res =[]

    #     def backtrack(i, total, way):
    #         if i == len(nums):
    #             res.append(way)
    #             return res
    #         if (i, total) in dp:
    #             return dp[(i, total)]
    #         val1 =backtrack(i + 1, total + nums[i], way.append(nums[i]))
    #         val2 =backtrack(i + 1, total - nums[i], way.append(nums[i]))
    #         res.append(val1)
    #         res.append(val2)
    #         dp[(i, total)] =res
    #         return dp[(i, total)]
        
    #     return backtrack(0, 0, way=[])


    def find_target_sum_ways(self, nums: List[int], target: int) -> List[List[int]]:
        dp = {}  # (index, total) -> List of ways
        res = []

        def backtrack(i, total, way):
            if i == len(nums):
                if total == target:
                    res.append(way[:])  # Append a copy of the way list
                return

            if (i, total) in dp:
                return dp[(i, total)]

            # Create new lists for each branch of the recursion
            way_plus = way + [nums[i]]
            way_minus = way + [-nums[i]]

            backtrack(i + 1, total + nums[i], way_plus)
            backtrack(i + 1, total - nums[i], way_minus)

            dp[(i, total)] = res

        # Initialize the way list
        backtrack(0, 0, way = [])
        return res
    
    def find_target_sum_ways_2(self, nums: List[int], target: int) -> List[List[int]]:
        # dp = {}
        
        # def backtrack(i, total, way):
        #     if i == len(nums):
        #         if total == target:
        #             return [way]  # Return the way as a list
        #         else:
        #             return []
            
        #     if (i, total) in dp:
        #         return dp[(i, total)]
            
        #     ways_with_plus  = backtrack(i + 1, total + nums[i], way + [nums[i]])
        #     ways_with_minus = backtrack(i + 1, total - nums[i], way + [-nums[i]])
            
        #     result = ways_with_plus + ways_with_minus
        #     dp[(i, total)] = result
        #     return result
        
        def backtrack(i, total, way):
            if i == len(nums):
                if total == target:
                    return [way]  # Return the way as a list
                return []

            ways_with_plus = backtrack(i + 1, total + nums[i], way + [nums[i]])
            ways_with_minus = backtrack(i + 1, total - nums[i], way + [-nums[i]])

            return ways_with_plus + ways_with_minus

        return backtrack(0, 0, way=[])

nums = [1, 1, 1, 1, 1]
target = 1
solution = Solution()
ways = solution.find_target_sum_ways_2(nums, target)
for way in ways:
    print(" ".join(map(str, way)))
# print(ways)
    

    
# sol = Solution()
# print(sol.find_target_sum_ways([1,1,1,1,1], target=3))

# print("---")
# print(sol.findTargetSumWays([1,1,1,1,1], target=3))
# print("---")
# print("---")
# print(sol.find_target_sum_ways_2([1,1,1,1,1], target=3))