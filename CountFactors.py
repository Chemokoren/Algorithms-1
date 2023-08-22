"""
1. CountFactors
Count factors of given number n.
Task Score
57%
Correctness
100%
Performance
0%
Task description
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):

    count = 0
    for i in range(1, N+1):
        if N % i == 0:
            count =count +1
    return count

def solution1(N):

    count = 0
    for i in range(N+1):
        if i == 0:
            count= 0
        else:
            if N % i == 0:
                count =count +1
    return count

def solution2(N):
    count = 2
    for i in range(2,(N//2)+1):
        if N%i==0:
            count =count+1
    return count;

#Detected time complexity: O(sqrt(N))
#Task Score 100% Correctness 100% Performance 100%
def solution3(N):
    result = 0
    for i in range(1,N+1):
        if i*i > N:
            break
        if i*i == N:
            result += 1
            break
        if N % i == 0:
            result += 2
    return result

def solution4(N):
    candidate = 1
    result = 0
    while candidate * candidate < N:
        # N has two factors: candidate and N // candidate
        if N % candidate == 0:
          result += 2

        candidate += 1

    # If N is square of some value.
    if candidate * candidate == N:  result += 1

    return result

print(solution4(240000000000000))
