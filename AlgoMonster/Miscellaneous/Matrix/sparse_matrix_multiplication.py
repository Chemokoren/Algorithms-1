"""

Sparse Matrix Multiplication

Given two sparse integer matrices A and B. Return the result of AB.

Review the rules of multiple two matrices here(https://www.mathsisfun.com/algebra/matrix-multiplying.html)

Below is a graphical demonstration of matrix multiplication:

A "sparse" matrix is a matrix where most entries are zero. You may assume that the number of columns in A is equal to that of the number of rows in B.
Input

    a: an integer matrix.
    b: an integer matrix.

Output

An integer matrix represent the product of the above matrices.
Examples
Example 1:

Input:

a = [[1, 0, 3], [0, 1, 2]]

b = [[0, 1], [1, 3], [0, 0]]

Output: [[0, 1], [1, 3]]

Explanation:

"""

from typing import List

def multiply_matrix(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    return []

if __name__ == '__main__':
    a = [[int(x) for x in input().split()] for _ in range(int(input()))]
    b = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = multiply_matrix(a, b)
    for row in res:
        print(' '.join(map(str, row)))