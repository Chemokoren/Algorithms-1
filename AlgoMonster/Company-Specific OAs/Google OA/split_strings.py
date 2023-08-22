"""
(OA) 2021 | Split Strings

Given a string s with length n, how many ways can you split it into two substrings s_1 and s_2 such 
that the number of unique characters in s_1 and s_2 are the same?

Parameter

    s: A string with length n.

Result

    The number of ways you can split it into two substrings that satisfy the condition.

Examples
Example 1:

Input: s = "aaa"

Output: 2

Explanation: It can be split in two ways: "a", "aa" and "aa", "a".
Example 2:

Input: s = "bac"

Output: 0

Explanation: There is no way to split this string into two substrings with equal unique elements.
Constraints

    0 <= n <= 10^5
    Characters in this string may consist of any alphanumeric character. The characters are case 
    sensitive. That is, same letters with different cases count as different characters.

"""
def total_ways_to_split_strings(s: str) -> int:
    return 0

if __name__ == '__main__':
    s = input()
    res = total_ways_to_split_strings(s)
    print(res)
