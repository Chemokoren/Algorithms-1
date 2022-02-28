"""
Longest Increasing Subsequence

Input

    nums: the integer sequence

Output

the length of longest subsequence
Examples
Example 1:

Input:

nums = [50, 3, 10, 7, 40, 80]

Output: 4

Explanation:

The longest subsequence is [3, 7, 40, 80] which has length 4.
Example 2:

Input:

nums = [1, 2, 4, 3]

Output: 3

Explanation:

Both [1, 2, 4] and [1, 2, 3] are longest subsequences which have length 3.


"""
from typing import List

def longest_sub_len(nums: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return 0

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = longest_sub_len(nums)
    print(res)