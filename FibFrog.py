"""
1. FibFrog
Count the minimum number of jumps required for a frog to get to the other side of a river.
Task Score
100%
Correctness
100%
Performance
100%
Task description
The Fibonacci sequence is defined using the following recursive formula:

    F(0) = 0
    F(1) = 1
    F(M) = F(M - 1) + F(M - 2) if M >= 2
A small frog wants to get to the other side of a river. The frog is initially located at one bank of the river (position −1) and wants to get to the other bank (position N). The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number. Luckily, there are many leaves on the river, and the frog can jump between the leaves, but only in the direction of the bank at position N.

The leaves on the river are represented in an array A consisting of N integers. Consecutive elements of array A represent consecutive positions from 0 to N − 1 on the river. Array A contains only 0s and/or 1s:

0 represents a position without a leaf;
1 represents a position containing a leaf.
The goal is to count the minimum number of jumps in which the frog can get to the other side of the river (from position −1 to position N). The frog can jump between positions −1 and N (the banks of the river) and every position containing a leaf.

For example, consider array A such that:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
The frog can make three jumps of length F(5) = 5, F(3) = 2 and F(5) = 5.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the minimum number of jumps by which the frog can get to the other side of the river. If the frog cannot reach the other side of the river, the function should return −1.

For example, given:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
"""



A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]


# Task Score 100%
# Correctness 100%
# Performance 100%

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Detected time complexity:
# O(N * log(N))

"""
The N*log(N) time complexity is given by the fact, that there are approximately log(N)
Fibonacci numbers up to N and you visit each position once.

As for the sequence hack: there are 26 Fibonacci numbers smaller than 100k,
 so I just preallocate an array of this size.
"""
def get_fib_seq_up_to_n(N):
    # there are 26 numbers smaller than 100k
    fib = [0] * (27)
    fib[1] = 1
    for i in range(2, 27):
        fib[i] = fib[i - 1] + fib[i - 2]
        if fib[i] > N:
            return fib[2:i]
        else:
            last_valid = i


def solution(A):
    # you can always step on the other shore, this simplifies the algorithm
    A.append(1)

    fib_set = get_fib_seq_up_to_n(len(A))

    # this array will hold the optimal jump count that reaches this index
    reachable = [-1] * (len(A))

    # get the leafs that can be reached from the starting shore
    for jump in fib_set:
        if A[jump - 1] == 1:
            reachable[jump - 1] = 1

    # iterate all the positions until you reach the other shore
    for idx in range(len(A)):
        # ignore non-leafs and already found paths
        if A[idx] == 0 or reachable[idx] > 0:
            continue

        # get the optimal jump count to reach this leaf
        min_idx = -1
        min_value = 100000
        for jump in fib_set:
            previous_idx = idx - jump
            if previous_idx < 0:
                break
            if reachable[previous_idx] > 0 and min_value > reachable[previous_idx]:
                min_value = reachable[previous_idx]
                min_idx = previous_idx
        if min_idx != -1:
            reachable[idx] = min_value + 1

    return reachable[len(A) - 1]


# second solution
# Task Score 100%
# Correctness 100%
# Performance 100%
# Time Spent 1 min
# Detected time complexity:
# O(N * log(N))

def fibonacciUpTo(n):
    fib = [0, 1]
    while True:
        new_fib = fib[-1] + fib[-2]
        if new_fib > n:
            break
        else:
            fib.append(new_fib)
    return fib[1:]  # slight modification to omit 0 - it would require additional checks later on


def solution1(A):
    A.append(1)  # the last 1 marks the other side of the river
    fib = fibonacciUpTo(len(A))

    reachable = [-1] * len(A)  # will mark in how many jumps we can get to specific point
    for jump in fib:
        reachable[
            jump - 1] = 1  # initialize reachable destinations by checking where we can get from initiali position of x=-1

    for x, leaf in enumerate(A):
        if reachable[x] > 0 and leaf == 1:  # if position is reachable and there is a leaf we can hop on
            for jump in fib:  # check where we can get from there
                if jump + x >= len(A):  # too far
                    break
                else:
                    if reachable[x + jump] < 0 or reachable[x + jump] > reachable[
                        x] + 1:  # if the place was unreachable before or if we found faster way there
                        reachable[x + jump] = reachable[x] + 1  # write down in how many jumps we can go there

    return reachable[-1]

# solution 2

def fibonacciDynamic(n):
    # Generate and return all the Fibonacci numbers,
    # less than or equal to n, in descending order.
    # n must be larger than or equal to one.
    fib = [0] * (n + 2)
    fib[1] = 1
    for i in range(2, n + 2):
        fib[i] = fib[i - 1] + fib[i - 2]
        if fib[i] > n:
            return fib[i-1: 1: -1]
        elif fib[i] == n:
            return fib[i: 1: -1]
def solution2(A):
    class Status(object):
        # Object to store the status of attempts
        __slots__ = ('position', 'moves')
        def __init__(self, pos, moves):
            self.position = pos
            self.moves = moves
            return
    lenA = len(A)                        # Array length
    fibonacci = fibonacciDynamic(lenA+1) # Fibonacci numbers
    statusQueue = [Status(-1,0)]    # Initially we are at position
                                    # -1 with 0 move.
    nextTry = 0     # We are not going to delete the tried attemp.
                    # So we need a pointer to the next attemp.
    accessed = [False] * len(A) # Were we in this position before?
    while True:
        if nextTry == len(statusQueue):
            # There is no unprocessed attemp. And we did not
            # find any path yet. So no path exists.
            return -1
        # Obtain the next attemp's status
        currentStatus = statusQueue[nextTry]
        nextTry += 1
        currentPos = currentStatus.position
        currentMoves = currentStatus.moves
        # Based upon the current attemp, we are trying any
        # possible move.
        for length in fibonacci:
            if currentPos + length == lenA:
                # Ohhh~ We are at the goal position!
                return currentMoves + 1
            elif currentPos + length > lenA or A[currentPos + length] == 0 or accessed[currentPos + length]:
                # Three conditions are moving too far, no
                # leaf available for moving, and being here
                # before respectively.
                # PAY ATTENTION: we are using Breadth First
                # Search. If we were here before, the previous
                # attemp must achieved here with less or same
                # number of moves. With completely same future
                # path, current attemp will never have less
                # moves to goal than previous attemp. So it
                # could be pruned.
                continue
            # Enqueue for later attemp.
            statusQueue.append(
                Status(currentPos + length, currentMoves+1))
            accessed[currentPos + length] = True


# solution 3
def get_jumps(N):
    f = [1, 1]
    while f[-1] < N:
        f.append(f[-1] + f[-2])
    return f[1:-1]  # strip fisrt and last element
def solution3(A):
    # add frog's starting position to A
    A.insert(0, 1)
    # add frog's destination position to A
    A.append(1)
    n = len(A)
    # store avaliable fibonacci jumps
    steps = get_jumps(n)
    # we _can_ do at most n-1 jumps, so let ‘infinity’ := n,
    oo = n
    # S[i] <-- minimal jumps count to get to the position i
    S = [oo] * n
    S[0] = 0
    # dynamic programming...
    for position in range(1, len(S)):
        s_min = oo
        for jump in steps:
            prev_leaf = position - jump
            if prev_leaf >= 0:
                if A[prev_leaf] == 1 and S[prev_leaf] + 1 < s_min:
                    s_min = S[prev_leaf] + 1
            else:
                break
        S[position] = s_min
    return S[-1] if S[-1] != oo else -1


# solution 4
def F_upto_A(L):
    # Fibonacci sequence up to the
    # length of A (include starting and destination position)
    F = []
    F.append(0)
    F.append(1)
    while F[-1] <= L:
        F.append(F[-1]+F[-2])
    return F[1:-1]
def solution4(A):
    # add starting position to A
    A.insert(0, 1)
    # add destination position to A
    A.append(1)#[1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1]
    n = len(A)#13
    # store available fibonacci jumps
    F = F_upto_A(n)#[1, 1, 2, 3, 5, 8, 13]
    # S mapping A in position
    # and storing the minimum step count to every "1" position
    S = [n] * n
    S[0] = 0 #[0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
    for i in range(1, n):
        # check if the position is 1 in A
        if A[i] == 1 :
            #loop the Fibonacci sequence
            for x in F:
                # previous position
                prev = i - x
                if prev >= 0:
                    # (the minimum step count of the previous position)
                    # plus
                    # (one more step to the existing position)
                    # if less than the step count of the existing position
                    # update the step count of the existing position
                    if S[prev] + 1 < S[i]:
                        S[i] = S[prev] + 1
                else:
                    break
    # return the last position of S, if S[-1]==n ,
    # means destination can'tbe reached
    # S:[0, 13, 13, 13, 13, 1, 13, 2, 13, 13, 13, 13, 3]
    return S[-1] if S[-1] < n else -1

# solution 5
# convert java code to python
# class Solution {
#     public int solution(int[] A) {
#         if (A.length == 0) {
#             return 1;
#         }
#         int[] dp = new int[A.length + 2];
#         dp[0] = 1;
#         dp[A.length + 1] = -1;
#         for (int i = 1; i < A.length + 2; i++) {
#             int step = 1;
#             int previous = 1;
#             int min = Integer.MAX_VALUE;
#             while (step <= i) {
#                 // System.out.format("step: %d\n", step);
#                 if ((i == A.length + 1 || A[i - 1] == 1) && (i - step - 1 == -1 || A[i - step - 1] == 1) && dp[i - step] > 0) {
#                     min = Math.min(min, dp[i - step] + 1);
#                     // System.out.format("new min: %d\n", min);
#                 }
#                 int tmp = step;
#                 step = step + previous;
#                 previous = tmp;
#             }
#             if (min < Integer.MAX_VALUE) {
#                 dp[i] = min;
#             }
#             // System.out.format("i: %d, dp: %s\n", i, java.util.Arrays.toString(dp));
#         }
#         // System.out.format("dp: %s\n", java.util.Arrays.toString(dp));
#         return dp[A.length + 1] == -1 ? -1 : dp[A.length + 1] - 1;
#     }
# }

print(solution4(A))
