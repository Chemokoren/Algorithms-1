"""
(OA) - Maximum Length of a Concatenated String with Unique Characters

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have
unique characters. Return the maximum possible length of s.
Constraints:

    1 <= arr.length <= 16
    1 <= arr[i].length <= 26
    arr[i] contains only lower case English letters.

Example 1:
Input: ["un","iq","ue"]
Output: 4
Explanation:

All possible concatenations are "","un","iq","ue","uniq" and "ique".
Example 2:
Input: ["cha","r","act","ers"]
Output: 6
Explanation:

Possible solutions are "chaers" and "acters".
Example 3:
Input: ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation:

impossible to concatenate as letters wont be unique.

"""
from typing import List

def maxLength(arr: List[str]) ->int:
    maxlen = 0
    unique =['']

    def isvalid(s):
        return len(s) == len(set(s))

    for word in arr:
        for j in unique:
            tmp = word + j
            if isvalid(tmp):
                unique.append(tmp)
                maxlen = max(maxlen, len(tmp))
    return maxlen

if __name__ == '__main__':
    # word_list = input().split()
    word_list =["cha","r","act","ers"]
    print(maxLength(word_list))



