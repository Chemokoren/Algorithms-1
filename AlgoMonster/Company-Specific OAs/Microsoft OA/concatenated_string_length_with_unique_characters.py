"""
(OA) - Concatenated String Length with unique Characters

Given an Array A consisting of N Strings, calculate the length of the longest string S such that:

    S is a concatenation of some of the Strings from A.
    every letter in S is different.
    N is [1..8]
    A consists of lowercase English letters
    Sum of length of strings in A does not exceed 100.

Example 1:
Input: ["co","dil","ity"]
Output: 5
Explanation:

String S could be codil, dilco, coity, ityco
Example 2:
Input: ["abc","kkk","def","csv"]
Output: 6
Explanation:

Strings S could be abcdef , defabc, defcsv , csvdef
Example 3:
Input: ["abc","ade","akl"]
Output: 0
Explanation:

impossible to concatenate as letters wont be unique.

"""
from typing import List

def max_length(arr: List[str])->int:
    dp =[set(x) for x in arr if len(set(x)) == len(x)]
    for v in arr:
        a = set(v)
        if len(a) == len(v):
            for b in dp:
                if a & b:
                    continue
                dp.append(a | b)
    for x in arr:
        tmp = set(x)
        if tmp in dp:
            dp.remove(tmp)
    return max(len(x) for x in dp) if dp else 0


if __name__=='__main__':
    arr = input().split()
    res = max_length(arr)
    print(res)


