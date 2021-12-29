"""
Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such
that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the 
target, where index1 must be less than index2.

Note:
- Your returned answers (both index1 and index2) are not zero-based.
- You may assume that each input would have exactly one solution and you may not use the same
element twice

Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 =1, index2 =2

"""

# # O(n) time
# def twoSum(nums, target):
#     dic ={}
#     for i in nums:
#         diff =target -i
#         if diff in dic:
#             return [diff, i]
#         else:
#             dic[diff]=i
#     return dic

# numbers,target = [2,7,11,15], 9
# print(twoSum(numbers,target))

def twoSum(nums, target):
    l,r=0, len(nums)-1
    while l< r:
        diff =nums[l]+ nums[r]
        if diff == target:
            return [l+1, r+1]
        elif diff > target:
            r -= 1
        else:
            l +=1

numbers,target = [2,7,11,15], 9
numbers,target = [1,3,4,5,7,10,11], 9
print(twoSum(numbers,target))


