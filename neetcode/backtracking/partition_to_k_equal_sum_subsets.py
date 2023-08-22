from typing import List
"""
Partition to K Equal Sum Subsets

Given an integer array nums and an integer k, return true if it is possible to divide 
this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums, k =[4,3,2,3,5,2,1], 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1,4), (2,3), (2,3) with equal 
sums.

Example 2:

Input: nums,k =[1,2,3,4],3
Output: false

sols
1) O(k^n) time complexity where n is the size of the nums array
2) O(k*2^n) time complexity (one of the trees is 2^n and we have to do that for k number
of trees) - solution below
"""

class Solution:

    def canPartitionKSubsets(self, nums: List[int], k:int)->bool:
        if sum(nums) % k:
            return False
        nums.sort(reverse=True)
        target = sum(nums) / k
        used =[False] * len(nums)

        # i -index we are in nums, 
        # k - how many k partitions are left that we need to build
        def backtrack(i, k, subsetSum): 
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k-1, 0) # k-1 additional subsets
            
            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                
                used[j] = True
                if backtrack(j+1, k, subsetSum + nums[j]):
                    return True
                used[j] =False
            return False
        return backtrack(0, k, 0)

sol = Solution()
print("expected::True, Actual:", sol.canPartitionKSubsets([4,3,2,3,5,2,1], 4))
print("expected::False, Actual:", sol.canPartitionKSubsets([1,2,3,4], 3))