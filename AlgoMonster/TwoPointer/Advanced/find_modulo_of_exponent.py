"""
Find Modulo of Exponent

Calculate the value of n^(2^k) % m. This question must be solved using constant memory.
Parameters

    n: An integer representing the base of the exponent
    k: An integer representing the exponent of the exponent of 2.
    m: An integer representing the base of the modulo

Result

    The result of the expression.

Examples
Example 1

Input: n = 2, k = 3, m = 10

Output: 6

Explanation: 2^(2^3) % 10 == 2^8 % 10 == 256 % 10 == 6.
Example 2

Input: n = 2, k = 34, m = 21

Output: 16
Constraints

    1 <= n, m <= 30000
    1 <= k <= 2^31 - 1


"""
def modulo_of_exponent(n: int, k: int, m: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return 0

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    m = int(input())
    res = modulo_of_exponent(n, k, m)
    print(res)