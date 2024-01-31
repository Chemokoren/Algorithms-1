"""
Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at 
least one number) which has the largest product.

Example 1:

Input: [2, 3, -2, 4]
Output: 6
Explanation: [2, 3] has the largest product 6.

"""
from typing import List
import unittest

class Solution:


    # time complexity: O(n) | memory complexity: O(1)
    def max_product(self, nums: List[int])-> int:
        res = max(nums)

        curMin, curMax = 1, 1

        for n in nums:

            if n == 0:
                curMin, curMax  = 1, 1
                continue
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = max(tmp, n * curMin, n)
            res = max(res, curMax)
        return res
    
class TestMaximumProductSubarray(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_max_product_subarray(self):
        self.assertEqual(6, self.sol.max_product([2, 3, -2, 4]))
        self.assertEqual(4, self.sol.max_product([-1, -5, -2, -3, 0, 6]))

if __name__=="__main__":
    unittest.main()