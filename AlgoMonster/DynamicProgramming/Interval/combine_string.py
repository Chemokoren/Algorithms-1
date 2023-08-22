"""
Combine String

For this question, we give you 3 strings and we ask if it is possible to make the 3rd string by merging the 2 other strings. What we mean by merging is that we can cut up both strings into a series of substrings that can be combined to form a 3rd string. The relative order in which characters appear in the first 2 strings must be maintained. Furthermore, you cannot take parts of the first 2 strings to make the 3rd string, all characters must be used when merging.
Input

    s1: First string
    s2: Second string
    s3: Target string that the other 2 strings must be combined to make

Output

Whether or not the 3rd string can be made
Examples
Example 1:

Input:

s1 = abe

s2 = cdf

s3 = abcdef

Output: true

Explanation:

We can make abcdef by doing ab + cd + e + f = abcdef
Example 2:

Input:

s1 = abe

s2 = cdf

s3 = abcd

Output: false

Explanation:

We cannot use parts of the first 2 strings as stated in the problem description so therefore this is not possible.
Constraints

    1 <= s1.length, s2.length, s3.length <= 500

"""

def combine_string(s1: str, s2: str, s3: str) -> bool:
    return False

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    s3 = input()
    res = combine_string(s1, s2, s3)
    print('true' if res else 'false')
