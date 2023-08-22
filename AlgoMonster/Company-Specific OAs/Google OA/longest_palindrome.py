"""
2021 (OA) - Longest Palindrome

A string is a palindrome if it reads the same backward as forwards. For example, "madam" and "racecar"
are palindromes, but "milk" is not.

We are given an array of N strings in which each string consist of two lowercase English letters. 
We would like to join as many strings together as possible in order to obtain a palindrome.

Input

    arr: an array of length N containing two-letter strings

Output

the length of longest palindrome that can be created by joining as many strings together as possible 
form arr

Examples

Example 1:

Input:

arr = ['ck', 'kc', 'ho', 'kc']

Output: 4

Explanation:

The longest palindrome are "ckkc" and "kcck", and their lengths are both equal to 4.

"""

from typing import List

def solution(arr: List[str]) -> int:
    return 0

if __name__ == '__main__':
    arr = [input() for _ in range(int(input()))]
    res = solution(arr)
    print(res)