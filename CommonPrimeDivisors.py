"""

1. CommonPrimeDivisors
Check whether two numbers have the same prime divisors.
Task Score
0%
Correctness
0%
Performance
0%
Task description

A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A prime D is called a prime divisor of a positive integer P if there exists a positive integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.

You are given two positive integers N and M. The goal is to check whether the sets of prime divisors of integers N and M are exactly the same.

For example, given:

        N = 15 and M = 75, the prime divisors are the same: {3, 5};
        N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is not equal to {2, 3, 5};
        N = 9 and M = 5, the prime divisors aren't the same: {3} is not equal to {5}.

Write a function:

    def solution(A, B)

that, given two non-empty arrays A and B of Z integers, returns the number of positions K for which the prime divisors of A[K] and B[K] are exactly the same.

For example, given:
    A[0] = 15   B[0] = 75
    A[1] = 10   B[1] = 30
    A[2] = 3    B[2] = 5

the function should return 1, because only one pair (15, 75) has the same set of prime divisors.

Write an efficient algorithm for the following assumptions:

        Z is an integer within the range [1..6,000];
        each element of arrays A, B is an integer within the range [1..2,147,483,647].


"""

sol_val =([15, 10, 9], [75, 30, 5])

def get_divisors(n):
    list_data=[]
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            list_data.append(i)

    return list_data

def solution(A, B):
    list_data=[]
    for i in range(len(A)):
        for j in range(len(B)):
            if(get_divisors(i)== get_divisors(j)):
                return i+1


# second solution
# takes like 11 min
# Detected time complexity:
# O(Z * log(max(A) + max(B))**2)
def gcd(x, y):
    ''' Compute the greatest common divisor.
    '''
    if x%y == 0:
        return y;
    else:
        return gcd(y, x%y)
def removeCommonPrimeDivisors(x, y):
    ''' Remove all prime divisors of x, which also exist in y. And
        return the remaining part of x.
    '''
    while x != 1:
        gcd_value = gcd(x, y)
        if gcd_value == 1:
            # x does not contain any more
            # common prime divisors
            break
        x /= gcd_value
    return x
def hasSamePrimeDivisors(x, y):
    gcd_value = gcd(x, y)   # The gcd contains all
                            # the common prime divisors
    x = removeCommonPrimeDivisors(x, gcd_value)
    if x != 1:
        # If x and y have exactly the same common
        # prime divisors, x must be composed by
        # the prime divisors in gcd_value. So
        # after previous loop, x must be one.
        return False
    y = removeCommonPrimeDivisors(y, gcd_value)
    return y == 1
def solution1(A, B):
    count = 0
    for x,y in zip(A,B):
        if hasSamePrimeDivisors(x,y):
            count += 1
    return count


# solution 3
# takes like 2 minutes
# Detected time complexity:
# O(Z * log(max(A) + max(B))**2)

# def gcd1(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
def solution3(A, B):
    # write your code in Python 2.7
    cnt = 0
    for i in range(len(A)):
        a, b = A[i], B[i]
        g = gcd(a, b)
        while True:
            d = gcd(a, g)
            if 1 == d:
                break
            a /= d
        while True:
            d = gcd(b, g)
            if 1 == d:
                break
            b /= d
        cnt += 1 if a == 1 and b == 1 else 0
    return cnt

print(solution3([15, 10, 9], [75, 30, 5]))
