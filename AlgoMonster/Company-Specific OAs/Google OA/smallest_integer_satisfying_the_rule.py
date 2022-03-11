"""
(OA) 2021 | Smallest Integer Satisfying the Rule

You have a number written down on a piece of paper. Unfortunately, you are extremely clumsy and you 
knocked over a bottle of ink, which covered the paper. This causes some numbers to be completely 
illegible.

This number is very important to you, so you want to reconstruct the number. You don't remember the 
original number, but you distinctly remember that this number has two peculiar attributes: it has no 
zeros anywhere in the number, and each adjacent digits are distinct. With this information, it is not 
necessarily possible to guarantee a number, so you just want to find the lowest possible number given
the current information.

Parameter

    digits: A string of length n consisting of 1 ~ 9 and/or ? (which represents an illegible digit).

Result

    A string representing the lowest possible number that satisfy the conditions described above.

Examples

Example 1

Input: digits = "1??13"

Output: "12313"

Example 2

Input: digits = "?1???2??3???4?"

Output: "21213212312141"
Constraints:

    1 <= n <= 2000

"""
def min_possible_int(digits: str) -> str:
    return ''

if __name__ == '__main__':
    digits = input()
    res = min_possible_int(digits)
    print(res)
