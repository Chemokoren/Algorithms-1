"""
Perfect Squares 2

    Prereq: Knapsack Intro

This problem is similar to Perfect Squares, except a number can only be used once. 
Again we ask you to output the minimum number of numbers in order to sum to the desired
number. Output -1 if the number can't be reached.

Examples
Example 1:
Input: 12
Output: -1
Explanation:

You cannot make 12 with any combination of 1, 4, 9
Example 2:
Input: 13
Output: 2
Explanation:

13 = 4 + 9

"""

def perfect_squares_2(n: int) -> int:
    return 0

if __name__ == '__main__':
    n = int(input())
    res = perfect_squares_2(n)
    print(res)
