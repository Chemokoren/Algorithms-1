"""
Given an array of integers nums sorted in ascending order, find the starting and 
ending position of a given target value.

if target is not found in the array, return [-1, -1].

You must write an algorithm with 0(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

"""

class Solution:

    def getLeftPosition(self, nums, target):
        left = 0
        right = len(nums) -1
        while(left <= right):
            mid = left+(right-left)// 2
            if(nums[mid] == target):
                if(mid-1 >= 0 and nums[mid-1] != target or mid ==0):
                    return mid
                right = mid -1

            elif(nums[mid]>target):
                right = mid-1
            else:
                left = mid + 1
        return -1

    def getRightPosition(self,nums,target):
        left =0
        right =len(nums)-1
        while(left <= right):
            mid = left+(right-left)//2
            if(nums[mid] == target):
                if(mid+1 < len(nums) and nums[mid+1] != target or mid ==len(nums)-1):
                    return mid
                left =mid +1
            elif(nums[mid]>target):
                right = mid-1
            else:
                left = mid+1
        return -1

    def searchRange(self, nums, target:int):
        left =self.getLeftPosition(nums, target)
        right=self.getRightPosition(nums, target)
        return [left,right]


nums,target = [5,7,7,8,8,10], 8
# nums,target = [5,7,7,8,8,10], 6
# nums,target = [], 0

sol = Solution()
print(sol.searchRange(nums, target))
                
