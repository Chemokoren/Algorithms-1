"""

Queries for GCD of all numbers of an array except elements in a given range

Given an array of n numbers and a number of queries are also given. Each query will be
represented by two integers l, r. The task is to find out the GCD of all the numbers of 
the array excluding the numbers given in the range l, r(both inclusive) for each query.

Examples:

Input : arr[] = {2, 6, 9}
        Ranges [0 0], [1 1], [1 2]
Output : 3
         1
         2 
GCD of numbers excluding [0 0] or 
first element is GCD(6, 9) = 3
GCD of numbers excluding the [1 1] or
second element is GCD(2, 9) = 1
GCD of numbers excluding [1 2] is 
equal to first element = 2

Note: We use 1 basd indexing in below explanation
We start from the very basic question how to calclate GCD of two numbers the best choice
is Euclid's algorithm. Now, how to calculate GCD of more than one numbers, the solution
is simple to suppose there are three numbers a,b and c. GCD(a,b,c) = GCD(GCD(a,b,c)). In
this way, we can easily find out GCD of any number of numbers.
One simple way to solve the question for each query suppose the range given is l and r.
Take GCD of the numbers from 1 to l-1 sppose it is x then take GCD of the numbers
from the range r+1 to n let it be y the output of each query will be GCD(x,y).
An efficient solution is to use two arrays, one as a prefix array and the second one as
suffix array. The i-th index of the prefix array will store GCD of the numbers from 1 to
i and the ith index of suffix array will denote the GCD of the numbers from i to n. Now 
suppose in a particlar query range given is l, r, it is obvious that  the output for that 
query will be GCD(prefix[l-1], suffix[r+1])


Time Complexity: O(nlogn) 
Auxiliary Space: O(n)
"""

# program for queries of GCD excluding given range of elements.

# Calculating GCD using euclid algorithm
def GCD(a,b):
    if(b == 0):
        return a
    return GCD(b, a%b)

# Filling the prefix and suffix array
def FillPrefixSuffix(prefix, arr, suffix, n):
    # Filling the prefix array following relation
    # prefix(i) = GCD(prefix(i-1), arr(i))
    prefix[0] =arr[0]
    for i in range(1,n):
        prefix[i] = GCD(prefix[i-1], arr[i])
        
    # Filling the suffix array following the relation 
    # suffix(i) = GCD(suffix(i+1), arr(i))
    suffix[n-1] = arr[n-1]

    for i in range(n-2, -1, -1):
        suffix[i] =GCD(suffix[i+1],arr[i])

# To calculate gcd of the numbers outside range
def GCDoutsideRange(l,r,prefix, suffix, n):
    # If l=0, we need to tell GCD of numbers from r+1 to n
    if(l==0):
        return suffix[r+1]
    # if r=n-1 we need to return the gcd of numbers from 1 to l
    if(r==n-1):
        return prefix[l-1]
    return GCD(prefix[l-1], suffix[r+1])


arr =[2,6,9]
n = len(arr)
prefix =[]
suffix=[]

for i in range(n+1):
    prefix.append(0)
    suffix.append(0)

FillPrefixSuffix(prefix, arr, suffix, n)
l =0
r = 0
print(GCDoutsideRange(l,r, prefix, suffix, n))

l = 1
r = 1
print(GCDoutsideRange(l,r,prefix, suffix, n))
l = 1
r = 2
print(GCDoutsideRange(l,r,prefix, suffix, n))
