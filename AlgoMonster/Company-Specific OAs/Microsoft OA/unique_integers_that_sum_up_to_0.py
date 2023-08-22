"""
(OA) - Unique Integers That Sum Up To 0

Given an integer n, return any array containing n unique integers such that they add up to 0.
Example 1:
Input:5
Output: [-4,-2,0,2,4]
Example 2:
Input:3
Output: [-2, 0, 2]
Example 1:
Input:1
Output: [0]

"""
from typing import List

def unique_sum(n: int) -> List[int]:
    res =[]
    for i in range(n):
        res.append(i * 2 - n + 1)
    return res

if __name__=='__main__':
    # n = int(input())
    n = 5
    res = unique_sum(n)
    print(' '.join(map(str, res)))
