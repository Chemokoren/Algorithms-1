"""
Delete String

Given 2 strings determine the minimum cost required to delete characters from either 
string to make them equal. We also assign a particular cost to each character so that in 
order to remove one instance of that character from either string it will inccur that 
cost. Only lower-case English letters will be used. The answer is guarenteed to fit in a 
32-bit integer.

Input

    costs: An array of size 26 that contains the cost for each character in the order of 
    a-z
    s1: First string
    s2: Second string

Output

Minimum cost to make the strings equal
Examples
Example 1:

Input:

costs = [1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

s1 = abb

s2 = bba

Output: 2

Explanation:

We can remove a from both string to make bb in both strings with only a cost of 2.
"""

from typing import List

def delete_string(costs: List[int], s1: str, s2: str) -> int:
    return 0

if __name__ == '__main__':
    costs = [int(x) for x in input().split()]
    s1 = input()
    s2 = input()
    res = delete_string(costs, s1, s2)
    print(res)