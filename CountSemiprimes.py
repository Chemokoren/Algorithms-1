#
"""
Task description
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
The number of semiprimes within each of these ranges is as follows:

(1, 26) is 10,
(4, 10) is 4,
(16, 20) is 0.
Write a function:

def solution(N, P, Q)

that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.

For example, given an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
the function should return the values [10, 4, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
M is an integer within the range [1..30,000];
each element of arrays P, Q is an integer within the range [1..N];
P[i] ≤ Q[i].
Copyright 2009–2020 by Cod
"""


# solution 1
# O(N * log(log(N)) + M)
def solution(N, P, Q):
    A = len(P) * [0]
    if N < 4:
        return A
    # Minimum prime factor of n stored in Factor[n]
    Factor = [0] * (N + 1)
    i = 2
    while (i * i <= N):
        if (Factor[i] == 0):
            k = i * i
            while (k <= N):
                if (Factor[k] == 0):
                    Factor[k] = i;
                k += i
        i += 1

    # Count semi prime numbers and store
    # sum scan in array Incluse_scan
    Incluse_scan = [0] * (N + 1)
    cnt_semi = 0
    for k in range(4, N + 1):
        if Factor[k] != 0:
            d = int(k / Factor[k])
            if Factor[d] == 0:
                cnt_semi += 1
        Incluse_scan[k] = cnt_semi
    # Do the difference of semi prime counters
    for r in range(0, len(P)):
        if (P[r] <= 4):
            min_inclusive = 0
        else:
            min_inclusive = P[r] - 1
        A[r] = Incluse_scan[Q[r]] - Incluse_scan[min_inclusive]
    return A



# solution 1
# Detected time complexity:
# O(N * log(log(N)) + M)
def sieve(N):
    semi = set()
    sieve = [True]* (N+1)
    sieve[0] = sieve[1] = False

    i = 2
    while (i*i <= N):
        if sieve[i] == True:
            for j in range(i*i, N+1, i):
                sieve[j] = False
        i += 1

    i = 2
    while (i*i <= N):
        if sieve[i] == True:
            for j in range(i*i, N+1, i):
                if (j % i == 0 and sieve[j//i] == True):
                    semi.add(j)
        i += 1

    return semi


def solution1(N, P, Q):

    semi_set = sieve(N)

    prefix = []

    prefix.append(0) # 0
    prefix.append(0) # 1
    prefix.append(0) # 2
    prefix.append(0) # 3
    prefix.append(1) # 4

    for idx in range(5, max(Q)+1):
        if idx in semi_set:
            prefix.append(prefix[-1]+1)
        else:
            prefix.append(prefix[-1])

    solution = []

    for idx in range(len(Q)):
        solution.append(prefix[Q[idx]] - prefix[P[idx]-1])

    return solution


print(solution1(26, [1, 4, 16], [26, 10, 20]))





# # solution 2
# # the actual solution
# def Solution(N, P, Q):
#     # main idea:
#     # using "sieve of Eratosthenes"
#     # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
#
#     boolean[]
#     primeArray = new
#     boolean[N + 1];  # note: plus one for "0"
#
#     # initial settting (sieve of Eratosthenes)
#     Arrays.fill(primeArray, true);  # initial setting: all primes
#     primeArray[0] = false;  # not prime
#     primeArray[1] = false;  # not prime
#     int
#     sqrtN = (int)
#     Math.sqrt(N);
#     # sieve of Eratosthenes
#     for (int i =1; i < sqrtN; i++){
#     if (primeArray[i] == true)  # prime
#     {
#     int j = i + i;
#     for (j=j; j <= N; j=j+i){
#     primeArray[j] = false;  # not prime
#     }
#     }
#     }
#
#     # store all primes in "List"
#     List < Integer > primeList = new
#     ArrayList <> ();
#     for (int i=2; i <= N; i++){
#     if (primeArray[i] == true){
#     primeList.add(i);  # "i" is prime
#     }
#     }
#
#     # find "semiprimes"
#     boolean[]
#     semiprimeArray = new
#     boolean[N + 1];  # note: plus one for "0"
#     Arrays.fill(semiprimeArray, false);  # initial setting: all "not" semiprimes
#     long
#     semiprimeTemp;  # using "long" (be careful)
#     # for "primeList.size()"
#     for (int i=0; i < primeList.size(); i++){
#     for (int j=i; j < primeList.size(); j++){
#     semiprimeTemp = (long) primeList.get(i) * (long) primeList.get(j);  # semiprimes
#     if (semiprimeTemp > N){
#     break;
#     }
#     else {
#     semiprimeArray[(int)
#     semiprimeTemp] = true;  # semiprimes
#
# }
# }
# }
#
# # compute "cumulative Count of semiprimes"
# int[]
# semiprimeCumulateCount = new
# int[N + 1];  # note: plus one for "0"
# for (int i=1; i <= N; i++)
# {
#     semiprimeCumulateCount[i] = semiprimeCumulateCount[i - 1];  # cumulative
# if (semiprimeArray[i] == true)
# {
#     semiprimeCumulateCount[i] + +;  # semiprimes
# }
# }
#
# # compute "results" (for each query)
# int
# numQuery = Q.length;
# int[]
# result = new
# int[numQuery];
# for (int i=0; i < numQuery; i++)
# {
#     result[i] = semiprimeCumulateCount[Q[i]] - semiprimeCumulateCount[P[i] - 1];  # note: "P[i]-1" (not included)
# }
# return result;
