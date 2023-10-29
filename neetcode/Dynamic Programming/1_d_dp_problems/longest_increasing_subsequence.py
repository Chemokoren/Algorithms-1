"""
Longest Increasing Subsequence

Given an integer array nums, return the length of the longest increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no 
elements without changing the order of the remaining elements. For example, [3, 6, 2, 7] is 
a subsequence of the array [0, 3, 1, 6, 2, 2, 7].

Example 1:

Input: nums =[10, 9, 2, 5,3,7,101, 18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is
4.

Example 2:
Input: nums =[0, 1, 0, 3, 2, 3]
Output: 4
"""
from typing import List

class Solution:

    def longest_increasing_subsequence(self, arr):
        res =[]
        for i in range(len(arr)):
            
            sub =[]
            sub.append(arr[i])
            j = i +1

            while j < len(arr):
                if arr[j] > arr[i] and arr[j-1] < arr[j]:
                    sub.append(arr[j])
                j +=1
                
            if len(sub) > len(res):
                res =sub
        return res, len(res)
    
    def longest_increasing_subsequence_two(self, arr):
        if not arr:
            return [], 0

        n = len(arr)
        lis_lengths = [1] * n
        prev_indices = [-1] * n

        for i in range(1, n):
            for j in range(0, i):
                if arr[i] > arr[j] and lis_lengths[i] < lis_lengths[j] + 1:
                    lis_lengths[i] = lis_lengths[j] + 1
                    prev_indices[i] = j

        max_length = max(lis_lengths)
        max_length_index = lis_lengths.index(max_length)

        lis = [0] * max_length
        lis_index = max_length - 1
        i = max_length_index

        while i >= 0:
            lis[lis_index] = arr[i]
            lis_index -= 1
            i = prev_indices[i]

        return lis, max_length
    
    def lengthOfLIS(self, nums: List[int])-> int:
        LIS =[1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)

sol = Solution()
print(sol.longest_increasing_subsequence([0, 1, 0, 3, 2, 3]))
print(sol.longest_increasing_subsequence([10, 9, 2, 5,3,7,101, 18]))

print("------------------")

print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(sol.lengthOfLIS([10, 9, 2, 5,3,7,101, 18]))