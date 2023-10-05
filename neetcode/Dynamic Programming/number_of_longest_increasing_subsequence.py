"""
Number of Longest Increasing Subsequence

Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

Example 1:

Input: nums =[1, 3, 5, 4, 7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7]

Example 2:

Input: nums =[2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5
subsequences' length is 1, so output 5.
"""
from typing import List
import unittest

class Solution:

    def findNumberOfLIS(self, nums: List[int])-> int:

        dp ={} # key = index, value =[length of LIS, count]
        lenLIS, res=0, 0 # length of LIS, count of LIS

        # i = start of subseq
        for i in range(len(nums)-1, -1, -1):
            maxLen, maxCnt =1, 1 # len, cnt of LIS start from i

            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]: # make sure increasing order
                    length, count = dp[j] # len, cnt of LIS start from
                    if length + 1 > maxLen:
                        maxLen, maxCnt = length + 1, count
                    elif length + 1 == maxLen:
                        maxCnt += count
            
            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCnt
            elif maxLen == lenLIS:
                res += maxCnt
            dp[i] =[maxLen, maxCnt]
        return res
    
sol = Solution()
print(sol.findNumberOfLIS([1, 3, 5, 4, 7]))
print(sol.findNumberOfLIS([2,2,2,2,2]))