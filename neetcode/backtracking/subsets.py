from typing import List
"""
Subsets

Given an integer array nums, return all possible subsets (the power set)
The solution set must not contain duplicate subsets.

Example 1:

Input: nums =[1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

2^n = num of subsets where n is the length of the array nums

                                    [1, 2, 3]
                                    /         \
                                [1]             []
                               /  \           /     \
                            [1,2]  [1]       [2]      []
                           /   \    /  \     /   \     /  \
                    [1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []

"""

# O(n.2^n) time complexity where n is the size of the input
class Solution:
    """Takes array nums, & returns all possible subsets"""
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Subsets method accepts nums and returns a list of list containing integers.
        
            Parameters:
                nums(List[int]): List of integers
            
            Returns:
                res(List[List[int]]): List of of List containing integers
        """
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
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