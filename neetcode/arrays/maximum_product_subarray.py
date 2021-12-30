from typing import List
"""
Given an integer array nums, find the contiguous subarray with an array(containing at least one 
number) which has the largest product.
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""
def maxProduct(nums):
    max_val=nums[0]
    curProd=1
    for i in nums:
        if i ==0:
            i =1
        curProd =i * curProd
        max_val=max(max_val, curProd, i)
    return max_val

nums =[0,2,3,-2,4]

print("freelance:",maxProduct(nums))

# using Dynamic Programming
class Solution:

    def maxProduct(self, nums: List[int])-> int:
        res = max(nums)
        curMin, curMax = 1,1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax *n
            curMax = max(n*curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res

nums =[0,2,3,-2,4]
sol =Solution()

print("DP:",sol.maxProduct(nums))