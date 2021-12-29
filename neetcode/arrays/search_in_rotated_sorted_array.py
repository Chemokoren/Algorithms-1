from typing import List
"""
Suppose an array sorted in ascending order is rotated at some pivot unkown to you beforehand.
(i.e., [0,1,2,4,5,6,7]) might become [4,5,6,7,0,1,2])

You are given a target value to search. If found in the array return its index, otherwise
return -1.
You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n)

Example 1 : 
Input nums =[4, 5, 6,7,0, 1, 2] = target = 0
Output: 4

Example 2: 
Input: nums =[4,5,6,7,0,1,2], target = 3
output =-1

"""

class Solution:

    def search(self, nums: List[int], target: int)->int:
        l, r = 0, len(nums) -1

        while l<= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid


            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target <nums[l]:
                    l = mid +1
                else:
                    r = mid -1
            
            # right sorted portion
            else:
                if target < nums[mid] or target >nums[r]:
                    r = mid -1
                else:
                    l = mid + 1

        return -1

nums,target =[4, 5, 6,7,0, 1, 2], 0
nums, target =[4,5,6,7,0,1,2], 3
sol = Solution()
print(sol.search(nums, target))