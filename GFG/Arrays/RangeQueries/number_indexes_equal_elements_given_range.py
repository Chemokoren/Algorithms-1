"""
Number of indexes with equal elements in given range

Given N numbers and Q queries, every query consists of L and R, your task is to find 
number of such integers i(L<=i<R) such that Ai=Ai+1. Consider 0-based indexing.

Input : A = [1, 2, 2, 2, 3, 3, 4, 4, 4] 
        Q = 2 
        L = 1 R = 8 
        L = 0 R = 4 
Output : 5 
         2
Explanation: We have 5 index i which has 
Ai=Ai+1 in range [1, 8). We have 
2 indexes i which have Ai=Ai+1
in range [0, 4). 

Input :A = [3, 3, 4, 4] 
       Q = 2
       L = 0 R = 3
       L = 2 R = 3 
Output : 2 
         1

A naive approach is to traverse from L to R(Exclusive R) and count the number of index i
which satisfies the condition Ai = Ai+1 for every query seperately.

Time Complexity : O(R – L) for every query 

Auxiliary Space: O(1)

"""
# program to count the number of indexes in range L R such that Ai = Ai + 1
# function that answers every query O(r-l)
def answer_query(a,l,r):
    # traverse from l to r and count the required indexes
    count = 0
    for i in range(l, r):
        if(a[i] == a[i + 1]):
            count += 1
    return count



 
# 1-st query
print("expected: 5, actual:", answer_query([1, 2, 2, 2, 3, 3, 4, 4, 4], 1, 8))
print("expected: 2, actual:",answer_query([1, 2, 2, 2, 3, 3, 4, 4, 4],  0, 4))

# 2nd query
print("expected: 2, actual:", answer_query([3, 3, 4, 4] , 0, 3))
print("expected: 1, actual:",answer_query([3, 3, 4, 4],  2, 3))

"""
Efficient approach

-We can answer queries in O(1) time. The idea is to precompute a prefix array prefixans
such that prefixans[i] stores the total count of index from 0
to i that obeys the given condition. prefixans[R-1]-prefix[L-1] returns the total count
of an index in the range(L,r) for every query.

Time complexity: O(n)

Auxiliary Space: O(n)

"""
# program to count the number of indexes in range L R such that Ai = Ai+1
N =1000

# array to store count of index from 0 to i that obey condition
prefixans =[0] * N

# precomputing prefixans[] array
def countIndex(a):
    n = len(a)
    # global N, prefixans

    # traverse to compute the prefixans[] array
    for i in range(0, n-1):

        if(a[i] == a[i+1]):
            prefixans[i] = 1

        if( i != 0):
            prefixans[i] =(prefixans[i] +prefixans[i -1])

# def that answers every query in O(1)
def answer_query(l,r):
    # global N, prefixans
    if(l == 0):
        return prefixans[r-1]
    else:
        return (prefixans[r-1] - prefixans[l-1])



 
# pre-computation
countIndex([1, 2, 2, 2, 3, 3, 4, 4, 4])
 
# 1-st query 
print (answer_query(1, 8))
 
# 2nd query
print (answer_query(0, 4))