"""


A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

        0 represents a car traveling east,
        1 represents a car traveling west.

The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

    class Solution { public int solution(int[] A); }

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer that can have one of the following values: 0, 1.


"""
def solution(A):
    # write your code in Python 3.6
    if len(A) > 1000000000:
        return -1
    return len(A)

A = [0,1,0,1,1]


# Detected time complexity:O(N)
def solution1(A):
    west_cars =  0
    cnt_passings = 0
    for idx in range(len(A)-1, -1, -1):
        if A[idx] == 0:
            cnt_passings += west_cars
            if cnt_passings > 1000000000:
                return -1
        else:
            west_cars += 1
    return cnt_passings
#


# Count all 1 in the array
def solution2(A):
    count = 0
    count_of_0 = 0
    A_sum = sum(A)
    for index,value in enumerate(A):
        if value==0:
            count_of_0 += 1
            count += A_sum - (index + 1 - count_of_0)
            if count>1000000000:
                return -1
    return count

# solution 3
def solution3(A):
    count = 0
    count_of_0 = 0
    for value in A:
        if value==0:
            count_of_0 += 1
        else:
            count += count_of_0
            if count>1000000000:
                return -1
    return count
print(solution3(A))
