from typing import List
"""
Maximum Subarray

Given an integer array nums, find the contiquous subarray (containing at least one number)
which has the largest sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum =6 .

"""

'''
that, given an array A consisting of N integers, returns the biggest value X, which occurs in
 A exactly X times. If there is no such value, the function should return 0
'''
class Solution:

    def maxSubArray(self, nums: List[int])->int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum +=n
            maxSub =max(maxSub, curSum)
        return maxSub

nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
print(sol.maxSubArray(nums))


"""
you are given a String S containing lowercase English letters. Your task is to calculate the
minimum number of letters that need to be removed in order to make it possible to build 
a palindrome from the remaining letters. When building the palindrome, you can rearrange 
the remaining letters in any way

"""