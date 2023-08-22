"""
(OA) - Pick Up Coupons

You are given a scratchcard consists of a row of non-negative integers. To win the scratch game, you
need to scratch at least 2 numbers of the same value. You can only scratch consecutive numbers from 
the card. Scratching each number costs 1 dollar. Return the minimum cost to win the game, or -1 if 
winning is not possible.

Examples
Example 1:
Input:

[1, 3, 4, 2, 3, 4, 5]
Output: 4
Explanation:

You can scratch either [3, 4, 2, 3] or [4, 2, 3, 4].
Example 2:
Input:

[2, 5, 0, 3, 7]
Output: -1
Explanation:

There are no numbers of the same value.
"""

from typing import List

def min_cost_to_win(nums: List[int]) -> int:
    return 0

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = min_cost_to_win(nums)
    print(res)
