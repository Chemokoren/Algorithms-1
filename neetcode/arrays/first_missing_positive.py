"""
First Missing Positive

Given an unsorted integer array nums, find the smallest missing positive integer.

Example 1:

Input: nums =[1,2,0]
Output: 3

Example 2:

Input: nums = [3,4,-1,1]
Output: 2

Example 3:

Input: nums =[7,8,9,11,12]
Output: 1

* There are various solutions 
- O(nlogn)
- O(n) time | O(n) space
- O(n) time | O(1) space

"""
from typing import List

class Solution:

    # O(n) time | O(1) memory
    def firstMissingPositive(self, A: List[int])->int:
        for i in range(len(A)):
            if A[i] < 0:
                A[i] = 0
        for i in range(len(A)):
            val = abs(A[i])
            if 1<= val <= len(A):
                if A[val -1] > 0:
                    A[val - 1] *= -1
                elif A[val -1] == 0:
                    A[val -1] =-1 *(len(A) + 1)

        for i in range(1, len(A)+1):
            if A[i -1] >= 0:
                return i
        return len(A) + 1

nums = [3,4,-1,1]
nums =[7,8,9,11,12]
nums =[1,2,0]
sol = Solution()
print(sol.firstMissingPositive(nums))