from typing import List
"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each
number sorted in non-decreasing order.

Example 1:
input: nums =[-4,-1,0,3,10]
Output: =[0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100]. After sorting it becomes 
[0,1,9,16,100]
"""
class Solution:
    def squaresOfSortedArray(self,nums:List[int])->List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        for i in range(1,len(nums)-1):
            if nums[i] < nums[i-1]:
                nums[i-1],nums[i] =nums[i],nums[i-1]
        return nums

    def sortedSquares(self, nums:List[int])->List[int]:
        res =[]
        l, r =0, len(nums)-1

        while l <= r:
            if nums[l] **2 > nums[r] ** 2:
                res.append(nums[l] **2)
                l +=1

            else:
                res.append(nums[r] **2)
                r -=1
        return res[::-1]

    # def sortedSquares(self, nums:List[int])->List[int]:
    #     res =[]
    #     l, r =0, len(nums)-1

    #     while l <= r:
    #         if nums[l] **2 < nums[r] ** 2:
    #             res.append(nums[l] **2)
    #             l +=1

    #         else:
    #             res.append(nums[r] **2)
    #             r -=1
    #     return res


nums =[-4,-1,0,3,10]
sol = Solution()
print(sol.sortedSquares(nums))

