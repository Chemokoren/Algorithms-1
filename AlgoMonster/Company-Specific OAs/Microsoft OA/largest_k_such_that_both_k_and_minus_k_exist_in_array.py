"""
(OA) - Largest K such that both K and -K exist in array

Given an array A of N integers, returns the largest integer K > 0 such that both values K and -K 
exist in array A. If there is no such integer, the function should return 0.

Example 1:
Input:[3, 2, -2, 5, -3]
Output: 3
Example 2:
Input:[1, 2, 3, -4]
Output: 0

"""
from typing import List

def largest_k(nums: List[int])->int:
    result = 0
    for i in nums:
        if i < 0 and -i in nums:
            result = max(result, -i)
    return result

if __name__=='__main__':
    # nums = [int(x) for x in input().split()]
    # vals =[1, 2, 3, -4]
    vals =[3, 2, -2, 5, -3]
    nums1 = vals
    nums = [int(x) for x in nums1]
    res = largest_k(nums)
    print(res)
