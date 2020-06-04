"""
Problem
An array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days. If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].
For example, consider the following array A consisting of six elements such that:
  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.
Write a function,

def solution(A)
that, given an array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days, returns the maximum possible profit from one transaction during this period. The function should return 0 if it was impossible to gain any profit.
For example, given array A consisting of six elements such that:
  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
the function should return 356, as explained above.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [0..400,000];
each element of array A is an integer within the range [0..200,000].
"""

A = [23171, 21011, 21123, 21366, 21013, 21367]


# Detected time complexity: O(N)
def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 0

    start = 0
    end = len(A) - 1
    min_val = A[start]
    max_val = A[end]
    while start <= end:
        min_val = min(min_val, A[start])
        max_val = max(max_val, A[end])

        gap_l = min_val - A[start + 1]
        gap_r = A[end - 1] - max_val

        if gap_l > gap_r:
            start += 1
        else:
            end -= 1
    return max_val - min_val


def solution1(A):
    # write your code in Python 3.6

    for i in range(len(A) - 1):
        if i == 0:
            max_profit = 0
        if (A[i + 1] - A[i]) > max_profit:
            max_profit = A[i + 1] - A[i]

    return max_profit


def solution2(A):
    min = A[0]
    max_profit = 0
    profit = 0
    min_index = 0
    max_index = 0
    i = 1

    while i < len(A):
        if A[i] < min:
            min = A[i]
            min_index = i
            profit = A[i] - min
        if profit > max_profit:
            max_profit = profit
            max_index = i
        i += 1
    return max_profit

#solution 3
def solution3(A):
    if len(A) == 1 or len(A) == 0:
        return 0;

    maxSoFar = 0;
    maxEndingHere = 0;
    minPrice = A[0];

    for i in range(len(A)):
        maxEndingHere = max(0, A[i] - minPrice)
        minPrice = min(minPrice, A[i])
        maxSoFar = max(maxEndingHere, maxSoFar)

    return maxSoFar;


print(solution(A))
