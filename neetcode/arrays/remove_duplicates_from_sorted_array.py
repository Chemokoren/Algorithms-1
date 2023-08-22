"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that 
each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have
the result be placed in the first part of the array nums. More formally, if there are  k elements after 
removing the duplicates, then the first k elements of nums should hold the final result. It does not
matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place
with O(1) memory.

Example:
input: nums =[0,0,1,1,1,2,2,3,3,4]
Output: 5, nums =[0,1,2,3,4,_,_,_,_,_]
Explanation: your function should return k=5, with the first five elements of nums being 0,1,2,3,and
4 respectively. 
It does not matter what you leave beyond the returned k(hence they are underscores)
"""

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int])->int:
        l =1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] =nums[r]
                l += 1

        for i in range(l,len(nums)):
            nums[i] ='_'
        return l, nums

nums =[0,0,1,1,1,2,2,3,3,4]
sol = Solution()
print(sol.removeDuplicates(nums))