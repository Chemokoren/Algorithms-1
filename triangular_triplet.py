"""


An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].

For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

Triplet (0, 2, 4) is triangular.

Write a function:

    class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

the function should return 1, as explained above. Given array A such that:
  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1

the function should return 0.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].


"""
# P Q R
# A =[0, 2, 4]
# A =[10, 50, 5, 1]
# A= [10, 2, 5, 1, 8, 20]
A = [10, 14, 5, 1]
def solution(A):
    final_val =0
    for i in range(len(A)):
        if i==0:
            if A[i] + A[i+1] > A[i+2] and  A[i+1] + A[i+2] > A[i] and  A[i+2] + A[i] > A[i+1]:
                final_val= 1
        if i==len(A):
            if A[i-2] + A[i-1] > A[i] and  A[i-1] + A[i] > A[i-2] and  A[i] + A[i-2] > A[i-1]:
                final_val= 1
        if i !=0 and i !=len(A)-1:
            if A[i] + A[i-1] > A[i+1] and  A[i-1] + A[i+1] > A[i] and  A[i+1] + A[i] > A[i-1]:
                final_val= 1
        return final_val

# solution 1
# Detected time complexity: O(N*log(N))

def solution1(A):
    A_len = len(A)
    if A_len < 3:
         # N is an integer within the range [0..1,000,000]
        # if the list is too short, it is impossible to
        # find out a triangular.
        return 0
    A.sort()
    for index in range(0, A_len-2):
        if A[index]+A[index+1] > A[index+2]:
            return 1
        # The list is sorted, so A[index+i] >= A[index+2]
        # where i>2. If A[index]+A[index+1] <= A[index+2],
        # then A[index]+A[index+1] <= A[index+i], where
        # i>=2. So there is no element in A[index+2:] that
        # could be combined with A[index] and A[index+1]
        # to be a triangular.
    # No triangular is found
    return 0

#solution 2  O(n*log(n)).   ---it should be  O(N).
def solution2(A):
    # write your code in Python 2.7
    if A==[]:
        return 0
    N=len(A)
    if N<3:
        return 0
    if (2*max(A))<sum(A):
        return 1
    else:
        return 0
print(solution2(A))
