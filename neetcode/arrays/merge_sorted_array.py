"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
- The number of elements initialized in nums1 and nums2 are m and n respectively.
- You may assume that nums1 has enough space(size that is equal to m+n) to hold additional 
  elements from nums2.

  Example:

  Input:
  nums1 =[1,2,3,0,0,0], m=3
  nums2 =[2,5,6], n=3

  Output: [1,2,2,3,5,6]
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m:int, nums2: list, n:int):
        # last index nums1
        last = m + n -1

        # merge in reverse order
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n -1]:
                nums1[last] =nums1[m-1]
                m -= 1
            else:
                nums1[last] =nums2[n-1]
                n -= 1
            last -= 1

        # fill nums1 with leftover nums2 elements 
        while n > 0:
            nums1[last] =nums2[n-1]
            n, last =n-1, last-1

        return nums1

nums1, m =[1,2,3,0,0,0], 3
nums2, n =[2,5,6], 3
sol = Solution()
print(sol.merge(nums1,m,nums2,n))


'''
my_tests 
'''
def my_tests(arr1, arr2):
    start = 0
    for i in range(len(arr1)):
        
        if arr1[i] ==0:
            arr1[i] =arr2[start]
            start +=1
    arr1.sort()
    return arr1

print("Expected:[1,2,2,3,5,6], Actual: ", my_tests([1,2,3,0,0,0], [2,5,6] ))


def my_tests_two(arr1, arr2):
    start =0
    for i in range(len(arr1)):
        if arr1[i] >0:
            continue
        arr1[i] =arr2[start]
        start +=1
        
    for i in range(1, len(arr1)-2):
        if arr1[i-1] > arr1[i]:
            arr1[i-1], arr1[i]= arr1[i], arr1[i-1]
    return arr1

print("My Test Two Expected:[1,2,2,3,5,6], Actual: ", my_tests_two([1,2,3,0,0,0], [2,5,6] ))