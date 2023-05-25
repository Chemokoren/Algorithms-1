"""


A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

The answers to these M = 3 queries are as follows:

        The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
        The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
        The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.

Write a function:

    def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        M is an integer within the range [1..50,000];
        each element of arrays P, Q is an integer within the range [0..N − 1];
        P[K] ≤ Q[K], where 0 ≤ K < M;
        string S consists only of upper-case English letters A, C, G, T.


"""

"""
The idea is to hold an auxiliary array per nucleotide X, with position i (ignoring zero) is how many times X has occurred as of now. And so if we need the number of occurrences of 
X from position f to position t, we could take the following equation:
aux(t) - aux(f)
O(N+M)
"""
#
# Detected time complexity: O(N + M)
#
def solution(S, P, Q):
    n = len(S)
    m = len(P)

    aux = [[0 for i in range(n+1)] for i in [0,1,2]]

    for i,c in enumerate(S):
        aux[0][i+1] = aux[0][i] + ( c == 'A' )
        aux[1][i+1] = aux[1][i] + ( c == 'C' )
        aux[2][i+1] = aux[2][i] + ( c == 'G' )

    result = []

    for i in range(m):
        fromIndex , toIndex = P[i] , Q[i] +1
        if   aux[0][toIndex] - aux[0][fromIndex] > 0:
            r = 1
        elif aux[1][toIndex] - aux[1][fromIndex] > 0:
            r = 2
        elif aux[2][toIndex] - aux[2][fromIndex] > 0:
            r = 3
        else:
            r = 4

        result.append(r)

    return result

def solution1(S, P, Q):

    count = []
    for i in range(3):
        count.append([0]*(len(S)+1))

    for index, i in enumerate(S):
        count[0][index+1] = count[0][index] + ( i =='A')
        count[1][index+1] = count[1][index] + ( i =='C')
        count[2][index+1] = count[2][index] + ( i =='G')

    result = []

    for i in range(len(P)):
      start = P[i]
      end = Q[i]+1

      if count[0][end] - count[0][start]:
          result.append(1)
      elif count[1][end] - count[1][start]:
          result.append(2)
      elif count[2][end] - count[2][start]:
          result.append(3)
      else:
          result.append(4)

    return result
