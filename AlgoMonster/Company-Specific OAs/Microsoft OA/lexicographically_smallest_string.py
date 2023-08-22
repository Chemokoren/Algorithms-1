"""
(OA) - Lexicographically Smallest String

Given a string str, the task is to find the lexicographically smallest string that can be formed by 
removing at most one character from the given string.

Example 1:
Input: abczd
Output: abcd
Example 2:
Input: abcda
Output: abca
Explanation:

One can remove d to get abca which is the lexicographically smallest string possible.
"""

def smallest_string(s: str)->str:
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            break
    return s[:i] + s[i +1:]

if __name__=='__main__':
    s = input()
    res = smallest_string(s)
    print(res)
