"""
Partition Equal Subset Sum

Given a non-empty array nums containing only positive integers, find if the array can be
partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:
Input: nums =[1, 5, 11, 5]
Output: True
Explanation: The array can be partitioned as [1,5,5] and [11].

Example 2:
Input: nums =[1,2,3,5]
Output: False
Explanation: The array cannot be partitioned into equal sum subsets.

"""
from typing import List
import unittest

class Solution:

    def partition_equal_subset_sum(self, arr):
        if sum(arr) % 2 ==0:
            return True
        else:
            return False
    def canPartition(self, nums: List[int])->bool:
        if sum(nums) % 2:
            return False
        dp =set()
        # we are guaranteed that we can add up to a sum of zero if we don't choose
        # any value from the input array nums
        dp.add(0) 
        target =sum(nums) //2

        for i in range(len(nums)-1, -1, -1):
            nextDP = set()
            for t in dp:
                # return it the first time we find the target to improve time complexity
                if(t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False

sol = Solution()
print(sol.partition_equal_subset_sum([1, 5, 11, 5]))
print(sol.partition_equal_subset_sum([1,2,3,5]))

print("------------------")
print(sol.canPartition([1, 5, 11, 5]))
print(sol.canPartition([1,2,3,5]))

class TestPartitionEqualSubsetSum(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_can_partition_equal_subset_sum(self):
        self.assertEqual(True, self.sol.canPartition([1, 5, 11, 5]))
        self.assertEqual(False, self.sol.canPartition([1,2,3,5]))

if __name__=="__main__":
    unittest.main()