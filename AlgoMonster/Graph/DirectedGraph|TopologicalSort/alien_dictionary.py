"""
Alien Dictionary

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you.

You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language.

Derive the order of letters in this language.

Note:

    You may assume all letters are in lowercase.
    Every letter that appears in the input must also appear in the output, and your output cannot have characters not in the input.
    If no ordering of letters makes the dictionary sorted lexicographically, return an empty string.
    There may be multiple valid orders. If that's the case, return the smallest in normal lexicographical order.

Input

    words: A list of strings of size n, representing the dictionary words sorted lexicographically in the alien language.

Output

A string representing the smallest possible lexicographical order, or an empty string if no valid order exists.
Examples
Example 1:


Input:

words = ["wrt","wrf","er","ett","rftt"]

Output: wertf

Example 2:

Input:

words = ["z","x"]

Output: zx

Explanation:

From z and x，we can get z < x. So return zx.
Constraints

    2 <= n <= 10000
    1 <= words[i] <= 30

"""
from typing import List

def alien_order(words: List[str]) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    return ''

if __name__ == '__main__':
    words = input().split()
    res = alien_order(words)
    print(res)