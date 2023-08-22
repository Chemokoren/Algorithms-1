"""
Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending 
position of a given target value.

if target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:
Input: nums =[5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums =[5,7,7,8,8,10], target = 6
Output: [-1, -1]
"""

# O(n) solution
def linearSolution(nums, target):
    result=[]
    if target not in nums:
        return [-1, -1]

    for i in range(len(nums)):   
        if nums[i] ==target:
            result.append(i)
    
    return result


print("Expected: [3,4], actual:", linearSolution([5,7,7,8,8,10],8) )
print("Expected: [-1, -1], actual:", linearSolution([5,7,7,8,8,10],6) )

# O(log(n))
class Solution:
    def searchRange(self, nums, target):
        left = self.binSearch(nums, target, True)
        right =self.binSearch(nums, target, False)
        return [left, right]

    # leftBias=[True/False], if false res is rightBiased
    def binSearch(self, nums, target, leftBias):
        l, r =0, len(nums)-1
        i = -1
        while l<=r:
            m = (l+r)//2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m-1
            else:
                i =m
                if leftBias:
                    r =m-1
                else:
                    l = m+1
        return i

sol =Solution()

print("Expected: [3, 4], actual:", sol.searchRange([5,7,7,8,8,10],8) )
print("Expected: [-1, -1], actual:", sol.searchRange([5,7,7,8,8,10],6) )