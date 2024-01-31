"""
Split Array Largest Sum

Given an array nums which consists of non-negative integers and an integer m, you can 
split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Example 1:
Input; nums =[7, 2, 5, 10, 8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays. The best way is to split it into 
[7,2,5] and [10, 8],
Where the largest sum among the two subarrays is only 18.

Example 2:

Input: nums =[1,2,3,4,5], m=2
Output: 9


"""
from typing import List
import unittest

class Solution:

    # time complexity n^2 * m
    def split_array_backtracking(self, nums: List[int], m:int)-> int:
        dp ={}

        def dfs(i, m):
            if m == 1:
                return sum(nums[i:])
            if (i, m) in dp:
                return dp[(i, m)]
            
            res, curSum = float("inf"), 0
            for j in range(i,len(nums) - m + 1):
                curSum += nums[j]
                maxSum =max(curSum, dfs(j + 1, m-1))
                res = min(res, maxSum)
                if curSum > res:
                    break
            dp[(i, m)] = res
            return res
        return dfs(0, m)
    

    # n.log s where s is the sum of input arrays
    def splitArray(self, nums: List[int], m:int)-> int:
        l, r = max(nums), sum(nums)

        def canSplit(largest):
            subarray = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n
            return subarray + 1 <= m

        res = r
        while l <= r:
            mid = l + ((r - l) // 2)
            if canSplit(mid):
                res = mid
                r = mid -1
            else:
                l = mid + 1
        return res

        

class TestSplitArrayLargestSum(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol =Solution()

    def test_split_array_largest_sum(self):
        self.assertEqual(18, self.sol.split_array_backtracking([7, 2, 5, 10, 8], m = 2))
        self.assertEqual(9, self.sol.split_array_backtracking([1,2,3,4,5], m=2))

    def test_split_array(self):
        self.assertEqual(18, self.sol.splitArray([7, 2, 5, 10, 8], m = 2))
        self.assertEqual(9, self.sol.splitArray([1,2,3,4,5], m=2))

if __name__=="__main__":
    unittest.main()