"""
(OA) - Max Inserts to Obtain String Without 3 Consecutive 'a'

Given a string S, returns the maximum number of letters a that can be inserted into S (including at 
the front and end of S) so that the resulting string doesn’t contain three consecutive letters a. 
If string S already contains the substring aaa, then your function should return -1.

Example 1:
Input: aabab
Output: 3
Explanation:

A string aabaabaa can be made
Example 2:
Input: dog
Output: 8
Explanation:

A string aadaaoaagaa can be made
Example 3:
Input: aa
Output: 0
Explanation:

No longer string can be made.
Example 4:
Input: baaaa
Output: -1
Explanation:

There is a substring aaa

"""

from itertools import groupby

def max_inserts(s: str) -> int:
    ans, last =0, '#'
    for c, g in groupby(s):
        L = len(list(g))
        if c == 'a':
            if L < 3:
                ans += 2 - L
            else:
                return -1
        else:
            ans += 2 * (L - (last == 'a'))
        last = c
    ans += 2 * (s[-1] != 'a')
    return ans

if __name__=='__main__':
    s = input()
    res = max_inserts(s)
    print(res)
