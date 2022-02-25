"""
Subarray Sum Divisible by K

Prefix Sum
Subarray Sum Divisible by K

Given an array of integers and an integer K, find the number of subarrays which are divisible 
by K.

Input: [3,1,2,5,1], 3

Output: 6

Explanation: the six subarrays are[3], [3,1,2], [1,2],[5,1], [3,1,2,5,1,], [1,2,5,1]
"""

def subarray_sum_divisible(nums, k): 
    left, right = 0, 0 
    count = 0 
    n = len(nums)

    while left < n:
        while right < n:
            total_sum = sum(nums[left:right+1])
            if total_sum % k == 0:
                count += 1
            right += 1
        right = left + 1
        left = right
    return count

nums = [3,1,2,5,1]
k =3
print(subarray_sum_divisible(nums, k))
