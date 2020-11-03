# For a given array A of N integers and a sequence S of N integers from the set {−1, 1}, we define val(A, S) as follows:
#
# val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|
#
# (Assume that the sum of zero elements equals zero.)
#
# For a given array A, we are looking for such a sequence S that minimizes val(A,S).
#
# Write a function:
#
# def solution(A)
#
# that, given an array A of N integers, computes the minimum value of val(A,S) from all possible values of val(A,S) for all possible sequences S of N integers from the set {−1, 1}.
#
# For example, given array:
#
#   A[0] =  1
#   A[1] =  5
#   A[2] =  2
#   A[3] = -2
# your function should return 0, since for S = [−1, 1, −1, 1], val(A, S) = 0, which is the minimum possible value.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..20,000];
# each element of array A is an integer within the range [−100..100].


def solution(A):
    a = [abs(s) for s in A]
    su = sum(a)
    ta = su // 2

    dp = [[0 for _ in range(ta + 1)] for _ in range(len(a))]
    for i in range(a[0], ta + 1): dp[0][i] = a[0]
    for i in range(1, len(a)):
        for j in range(ta + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= a[i]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i]] + a[i])

    return su - dp[-1][-1] - dp[-1][-1]

my_array =[1, 5, 2, -2]

print(solution(my_array))