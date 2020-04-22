"""


Write a function:

    def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A ≤ B.


"""

def solution(A, B, K):
    if B < A or K <= 0:
        raise Exception("Invalid Input")
    count =0;
    for i in range(A-1,B):
        if i%K == 0:
            count +=1
    return count

def solution1(A, B, K):
    d = B - A
    if A%K==0:
        return int(d//K) + 1
    else:
        rest = A % K
    return (d+rest)//K

def solution2(A,B, K):
     diffs = B//K - A//K
     if A % K == 0:
         diffs += 1
     return diffs

print(solution2(6,11,2))
print(solution2(11,345,17))
print(solution2(101,123000000,10000))

#
#Test Values
#
# A = 11, B = 345, K = 17 - 0.036 s
# A = B in {0,1}, K = 11
# A = B in {0,1}, K = 11
# A = 10, B = 10, K in {5,7,20}
# A = 100, B=123M+, K=2
# A = 101, B = 123M+, K = 10K
# A = 0, B = MAXINT, K in {1,MAXINT}
# A, B, K in {1,MAXINT}



