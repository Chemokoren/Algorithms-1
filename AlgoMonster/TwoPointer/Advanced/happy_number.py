"""
Happy Number

A "Happy Number" is defined as a number that after finite number of "steps" - where we sum the square of each digit each time - the result is a 1. Given a number n, determine whether it is a happy number.

As a challenge, complete this question under constant space.
Parameters

    n: The number to check.

Result

    true or false, depending on whether this number is a happy number.

Examples
Example 1

Input: n = 19

Output: true

Explanation:

1^2 + 9^2 = 82

8^2 + 2^2 = 68

6^2 + 8^2 = 100

1^2 + 0^2 + 0^2 = 1

Example 2

Input: n = 2

Output: false

Explanation:

2^2 = 4

4^2 = 16

1^2 + 6^2 = 37

3^2 + 7^2 = 58

5^2 + 8^2 = 89

8^2 + 9^2 = 145

1^2 + 4^2 + 5^2 = 42

4^2 + 2^2 = 20

2^2 + 0^2 = 4

...

Constraints

    1 <= n < 2^31



"""
def is_happy_number(n: int) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    return False

if __name__ == '__main__':
    n = int(input())
    res = is_happy_number(n)
    print('true' if res else 'false')
