"""
Maximal Square

Given a binary matrix, find out the largest size square sub-matrix with all 1's and 
return its area.

Input

    matrix: a binary matrix

Output

the area of the largest square in the input matrix
Examples
Example 1:

Input:

matrix = 

[[1, 0, 1, 0, 0],

 [1, 0, 1, 1, 1],

 [1, 1, 1, 1, 0],

 [1, 0, 0, 1, 0]]


Output: 4

Explanation:

The largest square is of size 2x2 and area 4.

from typing import List

def maximal_square(matrix: List[List[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return 0

if __name__ == '__main__':
    matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = maximal_square(matrix)
    print(res)
"""