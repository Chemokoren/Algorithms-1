"""
Count Number of Nice Subarrays

We define a "nice" array as an array that contains exactly k odd numbers, where k is a 
user-defined number. In that case, given an array arr, find the number of "nice" continuous 
subarrays of that array (the array itself is its own subarray). Duplicate subarrays are counted 
as different subarrays as long as their index range is different.

Parameters

    k: An integer required for the definition of a "nice" array.
    arr: A list of integers representing the array.

Result

    An integer representing the number of nice subarrays of arr.

Examples
Example 1

Input: k = 3, arr = [1, 1, 2, 1, 1]

Output: 2

Explanation: The nice subarrays are [1, 1, 2, 1] and [1, 2, 1, 1].
Example 2

Input: k = 1, arr = [2, 4, 6, 8, 10]

Output: 0

Explanation: There are no odd integer in arr, so there are no odd subarrays.
Constraints

    1 <= k <= len(arr) <= 50000
    0 <= arr[i] <= 10^5

"""

from typing import List

def count_nice_subarrays(k: int, arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return 0

if __name__ == '__main__':
    k = int(input())
    arr = [int(x) for x in input().split()]
    res = count_nice_subarrays(k, arr)
    print(res)