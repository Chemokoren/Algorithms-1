"""
    def solution(A)

that, given an array A consisting of N integers, returns the number of distinct values in array A.

For example, given array A consisting of six elements such that:
 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1

the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].


"""

#
# Detected time complexity: O(N**2)

A = [2, 1, 1, 2, 3, 1]


def solution(A):
    output = []
    for x in A:
        if x not in output:
            output.append(x)
    return len(output)


# Detected time complexity: O(N*log(N)) or O(N)

def solution1(A):
    myset = set(A)
    return len(myset)


#
# solution 3
#
def solution3(A):
    n = len(A)
    # Pick all elements one by one
    for i in range(0, n):

        # Check if the picked element
        # is already printed
        d = 0
        for j in range(0, i):
            if (A[i] == A[j]):
                d = 1
                break

            # If not printed earlier,
            # then print it
        if (d == 0):
            print (A[i])


print(solution3(A))
