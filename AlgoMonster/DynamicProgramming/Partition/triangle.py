"""
Triangle

The problem is to find the minimum path sum from top to bottom if given a triangle. 
Each step you may move to adjacent numbers on the row below.

Input

    triangle: see example

Output

the minimum path sum

Examples
Example 1:

Input:

triangle = [

    [2],

    [3,4],

  [6,5,7],

  [4,1,8,3]

]


Output: 11

Explanation:

The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.

"""

from typing import List

def minimum_total(triangle: List[List[int]]) -> int:
    return 0

if __name__ == '__main__':
    triangle = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = minimum_total(triangle)
    print(res)