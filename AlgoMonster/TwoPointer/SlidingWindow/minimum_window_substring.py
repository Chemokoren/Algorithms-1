"""
Minimum Window Substring

Given two strings, original and check, return the minimum substring of original such that each 
character in check, including duplicates, are included in this substring. By "minimum", I mean 
the shortest substring. If two substrings that satisfy the condition has the same length, the 
one that comes lexicographically first are smaller.

Parameters

    original: The original string.
    check: The string to check if a window contains it.

Result

    The smallest substring of original that satisfy the condition.

Examples
Example 1

Input: original = "cdbaebaecd", check = "abc"

Output: baec

Explanation: baec is the shortest substring of original that contains all of a, b, and c.
Constraints

    1 <= len(check), len(original) <= 10^5
    original and check both contains only upper case and lower case characters in English. 
    The characters are case sensitive.

"""
def get_minimum_window(original: str, check: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    return ''

if __name__ == '__main__':
    original = input()
    check = input()
    res = get_minimum_window(original, check)
    print(res)
