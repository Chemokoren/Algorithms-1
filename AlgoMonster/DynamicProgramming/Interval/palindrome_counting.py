"""
Palindrome Counting

Count the number of palindromes that exist in a particular string. Duplicates are allowed 
so long as they cover distinct intervals of the string. Empty strings do not count 
towards this total.

Example 1:

Input: abab
Output: 6
Explanation:

The following intervals are palindromes(0-indexed), [0,0],[1,1],[2,2],[3,3],[0,2],[1,3]

"""

def palindrome_counting(s: str) -> int:
    return 0

if __name__ == '__main__':
    s = input()
    res = palindrome_counting(s)
    print(res)
