"""
Partition Equal Subset Sum

Given a non-empty array nums containing only positive integers, find if the array can be
partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums =[1, 5, 11, 5]
Output: True
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums =[1, 2, 3, 5]
Output: False
Explanation: The array cannot be partitioned into equal sum subsets.

"""
from typing import List
import unittest

class Solution:

    def can_partition(self, nums: List[int])->bool:

        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)-1, -1, -1):
            nextDP =set()
            for t in dp:
                if(t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False
    
class TestPartitionEqualSubsetSum(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_partition_equal_subset_sum_false(self):
        self.assertEqual(False, self.sol.can_partition([1, 2, 3, 5]))

    def test_partition_equal_subset_sum_true(self):
        self.assertEqual(True, self.sol.can_partition([1, 5, 11, 5]))

if __name__=="__main__":
    unittest.main()