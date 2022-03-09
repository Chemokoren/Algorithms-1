"""
(OA) - String Without 3 Identical Consecutive Letters

Given a string S having lowercase English letters, returns a string with no instances of three 
identical consecutive letters, obtained from S by deleting the minimum possible number of letters.

Example 1:
Input: eedaaad
Output: eedaad
Explanation:

One occurrence of letter a is deleted.
Example 2:
Input: xxxtxxx
Output: xxtxx
Explanation:

Note that letter x can occur more than three times in the returned string if the occurrences are not
consecutive.

Example 3:
Input: uuuuxaaaaxum
Output: uuxaaxum

"""
def filter_string(s: str) -> str:
    news =s[0:2]
    for i in range(2, len(s)):
        # Do not append if the previous chars are the same
        if s[i] != s[i -1] or s[i] != s[i -2]:
            news += s[i]
    return news

if __name__ == '__main__':
    s = input()
    res = filter_string(s)
    print(res)
    