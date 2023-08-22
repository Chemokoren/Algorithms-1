"""

AOA 2021 (OA) - Split String Into Unique Primes

Given a string made up of integers 0 to 9, count the number of ways to split the string into prime numbers in the range of 2 to 1000 inclusive, using up all the characters in the string.

Each prime number, pn, must not contain leading 0s, and 2 <= pn <= 1000.
Constraints

The input string does not contain any leading 0s.
Examples
Example 1:
Input: "31173"
Output: 6
Explanation:

The string "31173" can be split into prime numbers in 6 ways:

    [3, 11, 7, 3]
    [3, 11, 73]
    [31, 17, 3]
    [31, 173]
    [311, 7, 3]
    [311, 73]

"""

def split_primes(input_str: str) -> int:
    return 0

if __name__ == '__main__':
    input_str = input()
    res = split_primes(input_str)
    print(res)