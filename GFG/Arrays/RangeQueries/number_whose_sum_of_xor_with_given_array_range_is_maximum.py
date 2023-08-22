"""
Number whose sum of XOR with given array range is maximum

you are given a sequence of N integers and Q queries. In each query, you are given two
parameters L and R. You have to find the smallest integer X such that 0<=X<2^31 and the
sum of XOR of x with all elements is range[L,R]is maximum possible.

Input  : A = {20, 11, 18, 2, 13}
         Three queries as (L, R) pairs
         1 3
         3 5
         2 4
Output : 2147483629
         2147483645
         2147483645

Approach
- The binary representation of each element and X, we can observe that each bit is 
independent and the problem can be solved by iterating over each bit. Now basically 
for each bit we need to count the number of 1's and 0's in the given range, if the 
number of 1's are more then you have to set that bit of X to O so that the sum is 
maximum after xor with X else if number of 0's are more then you have to set that bit 
of X to 1. If the number of 1's and 0's are equal then we can set that bit of X to any
one of 1 or 0 because it will not affect the sum, but we have to maximize the value of X
so we will take that bit 0.
Now, to optimize the solution we can pre-calculate the count of 1's at each bit position
of the numbers up to that position by making a prefix array this will take O(n) time.
Now for each query number of 1's will be the number of 1's up to Rth posision -number
of 1's up to(L-1)th position.

Time complexity: O(n)

Auxiliary Space: O(n)

"""
# program to find smallest integer X such that sum of its XOR with range is maximum
import math

one =[[0 for x in range(32)]for y in range(100001)]
MAX =2147483647

# Function to make prefix array which counts 1's of each bit up to that number
def make_prefix(A, n):
    global one, MAX

    for j in range(0, 32):
        one[0][j] = 0

    # Making a prefix array which sums number of 1's up to that position
    for i in range(1, n+1):
        a = A[i -1]
        for j in range(0,32):
            x = int(math.pow(2,j))

            # if j-th bit of a number is set then add one to previously counted 1's
            if(a & x):
                one[i][j] = 1 + one[i -1][j]

            else:
                one[i][j] = one[i-1][j]

# Function fo tind X
def Solve(L, R):
    global one, MAX
    l = L
    r = R
    tot_bits =r -l+1

    # initially taking maximum value all bits 1
    X = MAX

    # Iterating over each bit
    for i in range(0, 31):
        # get 1's at ith bit between the range L-R by subtracting 1's till
        # Rth number -1's till L-1th number

        x = one[r][i] -one[l -1][i]

        # if 1's are more than or equal to 0's then unset the ith bit from answer
        if(x >=(tot_bits-x)):
            ith_bit = pow(2,i)

            # set ith bit to 0 by doing Xor with 1
            X = X^ith_bit
    return X

n = 5
q = 3
A = [ 210, 11, 48, 22, 133 ]
L = [ 1, 4, 2 ]
R = [ 3, 14, 4 ]

make_prefix(A, n)
 
for j in range(0, q) :
    print (Solve(L[j], R[j]),end="\n")


print("\n Approach 2 \n")
"""
Approach 2
From the below table, you can see that if we are given a number n, our answer would 
be "N-n", where N is all 1s.

And we can get n(which is sum of all integers from A[i] to A[j]) using "prefixSum[i] -
prefixSum[i]"

Number (n)	1	0	0	1	0	0	1
All 1s (N)	1	1	1	1	1	1	1
N-n	0	1	1	0	1	1	0

Time complexity: O(n)

Auxiliary Space: O(n)

"""
from typing import List

# program to find smallest integer X such that sum of its XOR with range is maximum
#  MAX is (1 << 31) -1 or in other terms 2^31 - 1

#define MAX 2147483647
MAX = 2147483647

prefixSum=[]

# prefixSum[0] =[100001]

prefixSum =[1,0,0,0,0,1]

# Function to make prefix Sum array which
# A -arry of type int
def make_prefix(A,n:int):
    prefixSum[0] = A[0]
    for i in range(1,n):
        prefixSum[i] = prefixSum[i - 1] + A[i];


# Function to find X
# A - array of type int
def Solve(A, L:int,R:int):
    n = prefixSum[R] - prefixSum[L] + A[L]
    return MAX - n

# Driver program
if __name__ =='__main__':
    
    n = 5
    q = 3
    A = [ 210, 11, 48, 22, 133 ]
    L = [ 1, 4, 2 ]
    R = [ 3, 4, 4 ]
    
    make_prefix(A, n)

    for j in range(0,q):
        print(Solve(A, L[j], R[j]))
