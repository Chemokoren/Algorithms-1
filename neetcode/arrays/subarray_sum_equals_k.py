from typing import List
"""
Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of continuous subarrays
whose sum equals to k

Example 1:

Input: nums =[1,1,1], k=2
Output: 2

Example 2:

Input: nums =[1,2,3], k =3
Output: 2

Constratins:
- 1 <= nums.length <= 2*10^4
- 1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7
"""

def sumEquals(nums, target):
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            sum_val =nums[i] + nums[j]
            if sum_val==target:
                count +=1
    return count



class Solution:

    def subarraySum(self, nums: List[int],k:int)->int:
        res = 0
        curSum =0
        prefixSums ={0: 1}

        for n in nums:
            curSum += n
            diff = curSum -k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] =1 + prefixSums.get(curSum,0)
        return res

sol = Solution()
nums, k =[1,2,3],3
# nums, k=[1,1,1],2
print(sol.subarraySum(nums,k))