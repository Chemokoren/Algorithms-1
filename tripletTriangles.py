"""
Tasks Details
easy
1. CountTriangles
Count the number of triangles that can be built from a given set of edges.
Task Score
N/A
Correctness
Not assessed
Performance
Not assessed
Task description

An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if it is possible to build a triangle with sides of lengths A[P], A[Q] and A[R]. In other words, triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].

For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12

There are four triangular triplets that can be constructed from elements of this array, namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).

Write a function:

    def solution(A)

that, given an array A consisting of N integers, returns the number of triangular triplets in this array.

For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12

the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..1,000];
        each element of array A is an integer within the range [1..1,000,000,000].


"""

def solution(A):
    # write your code in Python 3.6
    count =0
    len_arr =len(A)
    for j in range(len_arr - 2):
        # if j== len_arr-2:
        #     return
        if ((A[j +1] + A[j] > A[j + 2]) or (A[j+1] + A[j+2] > A[j]) or (A[j] + A[j+2] > A[j+1])):
                count = count + 1

    return count

"""

Detected time complexity:
O(N**3)
 Task Score 63% Correctness 100% Performance 0%

"""
def solution2(arr):
    # Count of triangles
    count = 0

    # The three loops select three
    # different values from array
    n =len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (arr[i] + arr[j] > arr[k] and
                        arr[i] + arr[k] > arr[j] and
                        arr[k] + arr[j] > arr[i]):
                    count += 1
    return count

A =[10, 2, 5, 1, 8, 12]
# A =[4, 6, 3, 7]
print(solution2(A))
