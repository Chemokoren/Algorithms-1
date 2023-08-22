"""

We have briefly discussed sparse table in Range Minimum Query (Square Root Decomposition 
and Sparse Table)
Sparse table concept is used for fast queries on a set of static data (elements do not 
change). It does preprocessing so that the queries can be answered efficiently.
 
 

Example Problem 1 : Range Minimum Query

We have an array arr[0 . . . n-1]. We need to efficiently find the minimum value from 
index L (query start) to R (query end) where 0 <= L <= R <= n-1. 
Consider a situation when there are many range queries. 

Example: 

Input:  arr[]   = {7, 2, 3, 0, 5, 10, 3, 12, 18};
        query[] = [0, 4], [4, 7], [7, 8]

Output: Minimum of [0, 4] is 0
        Minimum of [4, 7] is 3
        Minimum of [7, 8] is 12

The idea is to precompute minimum of all subarrays of size 2^j where j varies from 0 
to Log n. We make a table lookup[i][j] such that lookup[i][j] contains minimum of range 
starting from i and of size 2^j. 
For example lookup[0][3] contains minimum of range [0, 7] (starting with 0 and of size 2^3)


How to fill this lookup or sparse table? 
The idea is simple, fill in a bottom-up manner using previously computed values. 
We compute ranges with current power of 2 using values of lower power of two. 
For example, to find a minimum of range [0, 7] (Range size is a power of 3), 
we can use the minimum of following two. 

a) Minimum of range [0, 3] (Range size is a power of 2) 
b) Minimum of range [4, 7] (Range size is a power of 2)

Based on above example, below is formula, 

// Minimum of single element subarrays is same
// as the only element.
lookup[i][0] = arr[i]

// If lookup[0][2] <=  lookup[4][2], 
// then lookup[0][3] = lookup[0][2]
If lookup[i][j-1] <= lookup[i+2^(j-1])[j-1]
   lookup[i][j] = lookup[i][j-1]

// If lookup[0][2] >  lookup[4][2], 
// then lookup[0][3] = lookup[4][2]
Else 
   lookup[i][j] = lookup[i+2^(j-1)][j-1] 


For any arbitrary range [l, R], we need to use ranges which are in powers of 2. 
The idea is to use the closest power of 2. We always need to do at most one comparison
(compare the minimum of two ranges which are powers of 2). One range starts with L and 
ends with “L + closest-power-of-2”. 
The other range ends at R and starts with “R – same-closest-power-of-2 + 1”. For example,
if the given range is (2, 10), we compare the minimum of two ranges (2, 9) and (3, 10).

Based on above example, below is formula, 

// For (2, 10), j = floor(Log2(10-2+1)) = 3
j = floor(Log(R-L+1))

// If lookup[2][3] <=  lookup[3][3], 
// then RMQ(2, 10) = lookup[2][3]
If lookup[L][j] <= lookup[R-(int)pow(2, j)+1][j]
   RMQ(L, R) = lookup[L][j]

// If lookup[2][3] >  arr[lookup[3][3], 
// then RMQ(2, 10) = lookup[3][3]
Else 
   RMQ(L, R) = lookup[R-(int)pow(2, j)+1][j]

Since we do only one comparison, the time complexity of query is O(1).


 
"""

# program to do range minimm query using sparse table
import math

# fills lookup array lookup[][] in bottom up manner
def buildSparseTable(arr, n):

    # Initialize M for the intervals with length 1
    for i in range(0, n):
        lookup[i][0] = arr[i]

    j = 1

    # compute values from smaller to bigger intervals
    while(1 << j) <= n:

        # compute minimum value for all intervals with size 2^j
        i =0
        while(i +(1 << j) -1) < n:
            
             # For arr[2][10], we compare arr[lookup[0][7]] and arr[lookup[3][10]]
            if(lookup[i][j-1] < lookup[i + (1 << (j-1))][j-1]):
                    lookup[i][j] = lookup[i][j-1]

            else:
                lookup[i][j]= lookup[i +(1 << (j-1))][j - 1]
            i += 1
        j += 1

# returns minimum of arr[L..R]
def query(L, R):
    # Find highest power of 2 that is smaller than or equal to count of element in
    # given range. For [2,10], j=3
    j = int(math.log2(R - L + 1))

    # compute minimum of last 2^j elements with first 2^j elements in range.
    # For [2,10], we compare arr[lookup[0][3]]
    # and arr[lookup[3][3]]

    if lookup[L][j] <= lookup[R -(1 << j) + 1][j]:
        return lookup[L][j]

    else:
        return lookup[R - (1 << j) + 1][j]


if __name__ =="__main__":
    a =[7,2,3,0,5,10,3,12,18]
    n = len(a)
    MAX = 500


    # lookup[i][j] is going to store minimum
    # value in arr[i..j]. Ideally lookup table
    # size should not be fixed and should be
    # determined using n Log n. It is kept
    # constant to keep code simple.

    lookup =[[0 for j in range(MAX)] for j in range(MAX)]

    buildSparseTable(a, n)
    print(query(0,4))
    print(query(0, 4))
    print(query(4, 7))
    print(query(7, 8))


"""

Example Problem 2 : Range GCD Query

We have an array arr[0 . . . n-1]. We need to find the greatest common divisor in the 
range L and R where 0 <= L <= R <= n-1. Consider a situation when there are many range 
queries.

Examples: 
 

Input : arr[] = {2, 3, 5, 4, 6, 8}
        queries[] = {(0, 2), (3, 5), (2, 3)}
Output : 1
         2
         1

We use below properties of GCD:

    - GCD function is associative [ GCD(a, b, c) = GCD(GCD(a, b), c) = GCD(a, GCD(b, c))], 
    we can compute GCD of a range using GCDs of subranges.
    If we take GCD of an overlapping range more than once, then it does not change answer.
    For example GCD(a, b, c) = GCD(GCD(a, b), GCD(b, c)). 
    Therefore like minimum range query problem, we need to do only one comparison to find 
    GCD of given range.

We build a sparse table using the same logic as above. After building the sparse table, 
we can find all GCDs by breaking given range in powers of 2 and add GCD of every piece to 
the current answer.
 

Time Complexity: O(n*Logn)

Auxiliary Space: O(n*Logn)

"""

# program to do range minimum query using sparse table
import math

# fills lookup array lookup[][] in bottom up manner
def buildSparseTableTwo(arr, n):

    # GCD of single element is element itself
    for i in range(0,n):
        table[i][0] = arr[i]

    # build sparse table
    j = 1
    while(1 << j) <=n:
        i = 0
        while i <= n -(1 << j):
            table[i][j] = math.gcd(table[i][j-1], table[i + (1 << (j-1))][j-1])
            
            i += 1
        j += 1
    
# Returns minimum of arr[L..R]
def query(L, R):
    # Find highest power of 2 that is smaller
    # than or equal to count of elements in the given range. For[0,10], j =3
    j = int(math.log2(R-L +1))

    # Compute GCD of last 2^j elements with
    # first 2^j elements in range.
    # For [2,10], we find GCD of arr[lookup[0][3]]
    # and arr[lookup[3][3]]

    return math.gcd(table[L][j], table[R- (1 << j) + 1][j])

if __name__=="__main__":
    a =[7,2,3,0,5,10,3,12,18]
    n = len(a)

    MAX = 500

    # lookup[i][j] is going to store minimum
    # value in arr[i..j]. Ideally lookup table
    # size should not be fixed and should be
    # determined using n Log n. It is kept
    # constant to keep code simple.

    table =[[0 for i in range(MAX)] for j in range(MAX)]

    buildSparseTableTwo(a, n)

    print(query(0, 2))
    print(query(1, 3))
    print(query(4, 5))
        


'''

my tests
'''

def test(arr, Q):
    result =[]
    for q in Q:
        l, r =q
        result.append(min(arr[l:r+1]))
        
    return result
print("expected: [0, 3, 12]","actual: ",test([7, 2, 3, 0, 5, 10, 3, 12, 18], [[0, 4], [4, 7], [7, 8]]) )


