"""
Find All Anagrams in a String

Given a string original and a string check, find the starting index of all substrings of
 original that is an anagram of check. The output must be sorted in ascending order.
Parameters

    original: A string
    check: A string

Result

    A list of integers representing the starting indices of all anagrams of check.

Examples
Example 1

Input: original = "cbaebabacd", check = "abc"

Output: [0, 6]

Explanation: The substring from 0 to 2, "cba", is an anagram of "abc", and so is the substring 
from 6 to 8, "bac".
Example 2

Input: original = "abab", check = "ab"

Output: [0, 1, 2]

Explanation: All substrings with length 2 from "abab" is an anagram of "ab".
Constraints

    1 <= len(original), len(check) <= 10^5
    Each string consists of only lowercase characters in standard English alphabet.


"""
from typing import List

def find_all_anagrams(original: str, check: str) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    return []

if __name__ == '__main__':
    original = input()
    check = input()
    res = find_all_anagrams(original, check)
    print(' '.join(map(str, res)))