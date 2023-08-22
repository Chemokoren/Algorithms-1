"""
(OA) - Fair Indexes

You are given two arrays A and B consisting of N integers each.

Index K is named fair if the four sums (A[0] + ... + A[K-1]), (A[k] + ... + A[N-1]), (B[0] + ... + B[k-1]) 
and (B[K] + ... + B[N-1]) are all equal. 
In other words, K is the index where the two arrays, A and B, can be split (into two non-empty arrays 
each) in such a way that the sums of the resulting arrays' elements are equal.

write a function:

int fairIndexes(vector<int> &A, vector<int> &B);

which, given two arrays of integers A and B, returns the number of fair indexes.
Example 1:
Input: A = [4, -1, 0, 3], B = [-2, 5, 0, 3]
Output: 2
Explanation:

The fair indexes are 2 and 3. In both cases, the sums of elements the subarrays are equal to 3.

For index = 2;

4 + (-1) = 3; 0 + 3 = 3;

-2 + 5 = 3; 0 + 3 = 3;
Example 2:
Input: A = [2, -2, -3, 3], B = [0, 0, 4, -4]
Output: 1
Explanation:

The only fair index is 2.

"""
from typing import List
from collections import deque

def fairIndexes(A: List[int], B: List[int]) -> int:

    # GET A PREFIX SUM OF EACH ARRAY
    for i in range(1, len(A)):
        A[i] +=A[i -1]
        B[i] +=B[i -1]

    # TRY EACH INDEX
    fair = 0
    for k in range(1, len(A)):
        left_A, right_A =A[k -1], A[-1] - A[k -1]
        left_B, right_B =B[k -1], B[-1] - B[k -1]
        fair += int(left_A == right_A == left_B == right_B)
    return fair

if __name__=='__main__':
    A =[int(x) for x in input().split()]
    B = [int(y) for y in input().split()]
    print(fairIndexes(A, B))



