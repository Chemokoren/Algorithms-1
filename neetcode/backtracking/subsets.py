from typing import List
"""
Subsets

Given an integer array nums, return all possible subsets (the power set)
The solution set must not contain duplicate subsets.

Example 1:
Input: nums =[1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

2^n = num of subsets where n is the length of the array nums

"""

class Solution:
    # O(n.2^n) time complexity
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                print(subset.copy())
                res.append(subset.copy())
                return 

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res

nums =[1,2,3]
sol = Solution()
print(sol.subsets(nums))