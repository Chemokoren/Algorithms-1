"""
Range Minimum Query (Square Root Decomposition and Sparse Table)

We have an array arr[0 . . . n-1]. We should be able to efficiently find the minimum 
value from index L (query start) to R (query end) where 0 <= L <= R <= n-1. Consider a 
situation when there are many range queries. 

Example: 

Input:  arr[]   = {7, 2, 3, 0, 5, 10, 3, 12, 18};
        query[] = [0, 4], [4, 7], [7, 8]

Output: Minimum of [0, 4] is 0
        Minimum of [4, 7] is 3
        Minimum of [7, 8] is 12

A simple solution is to run a loop from L to R and find the minimum element in the given 
range. This solution takes O(n) time to query in the worst case.
Another approach is to use Segment tree. With segment tree, preprocessing time is O(n) 
and time to for range minimum query is O(Logn). The extra space required is O(n) to 
store the segment tree. Segment tree allows updates also in O(Log n) time. 

Can we do better if we know that the array is static?

How to optimize query time when there are no update operations and there are many range 
minimum queries?

Below are different methods.

Method 1 (Simple Solution) 
--------------------------

A Simple Solution is to create a 2D array lookup[][] where an entry lookup[i][j] stores 
the minimum value in range arr[i..j]. The minimum of a given range can now be calculated 
in O(1) time.

"""


# program to do range minimum query in O(1) time with O(n*n) extra space and O(n*n)
# preprocessing time
from cgitb import lookup


MAX =500

# lookup[i][j] is going to store index of minimum value in arr[i..j]
lookup =[[0 for j in range(MAX)] for i in range(MAX)]

# structure to represent a query range
class Query:

    def __init__(self, L, R):
        self.L = L
        self.R = R

# Fills lookup array lookup[n][n] for all possible values of query ranges
def preprocess(arr, n):

    # Initialize lookup[][] for the intervals with length 1
    for i in range(n):
        lookup[i][i] = i

    # Fill rest of the entries in bottom manner
    for i in range(n):
        for j in range(i + 1, n):

            # To find minimum of [0,4],
            # We compare minimum
            # of arr[lookup[0][3]] with arr[4]
            if(arr[lookup[i][j - 1]] < arr[j]):
                lookup[i][j] = lookup[i][j-1]

            else:
                lookup[i][j] = j

# prints minimum of given m query ranges in arr[0..n-1]
def RMQ(arr, n, q, m):

    # fill lookup table for all possible input queries
    preprocess(arr, n)

    # one by one compute sum of all queries
    for i in range(m):
        # Left and right boundaries of current range
        L = q[i].L
        R = q[i].R

        # print sum of current query range
        print("Minimum of ["+str(L) +" , " +str(R)+"]" +str(arr[lookup[L][R]]))
    
if __name__ == "__main__":
     
    a = [7, 2, 3, 0, 5, 10, 3, 12, 18]
    n = len(a)   
    q = [Query(0, 4), Query(4, 7), Query(7, 8)]   
    m = len(q)   
    RMQ(a, n, q, m)

  
print("\n Here are my tests \n")


"""
This approach supports queries in O(1), but preprocessing takes O(n^2) time. Also, this 
approach needs O(n^2) extra space which may become huge for large input arrays.

Method 2 (Square Root Decomposition) 

We can use Square Root Decompositions to reduce space required in the above method.

Preprocessing: 
1) Divide the range [0, n-1] into different blocks of √n each. 
2) Compute the minimum of every block of size √n and store the results.
Preprocessing takes O(√n * √n) = O(n) time and O(√n) space.

[ 7   2   3   0   5   10  3   12  18 ]
  0   1   2   3   4    5  6   7   8

lookup[0] is index of minimum in arr[0..2]
lookup[1] is index of minimum of arr[3..5]
lookup[2] is index minimum of arr[6..8]

[1, 3, 6]

Query: 
1) To query a range [L, R], we take a minimum of all blocks that lie in this range. 
For left and right corner blocks which may partially overlap with the given range, 
we linearly scan them to find the minimum. 
The time complexity of the query is O(√n). Note that we have a minimum of the middle block
directly accessible and there can be at most O(√n) middle blocks. 
There can be at most two corner blocks that we may have to scan, so we may have to scan
2*O(√n) elements of corner blocks. Therefore, the overall time complexity is O(√n).

Method 3 (Sparse Table Algorithm) 

The above solution requires only O(√n) space but takes O(√n) time to query. 
The sparse table method supports query time O(1) with extra space O(n Log n).
The idea is to precompute a minimum of all subarrays of size 2^j where j varies from 0 to
Log n. Like method 1, we make a lookup table. Here lookup[i][j] contains a minimum of 
range starting from i and of size 2^j. For example lookup[0][3] contains a minimum of range
[0, 7] (starting with 0 and of size 2^3)


Preprocessing: 

How to fill this lookup table? The idea is simple, fill in a bottom-up manner using 
previously computed values. 

For example, to find a minimum of range [0, 7], we can use a minimum of the following two.

a) Minimum of range [0, 3] 
b) Minimum of range [4, 7]

Based on the above example, below is the formula, 

// If arr[lookup[0][2]] <=  arr[lookup[4][2]], 
// then lookup[0][3] = lookup[0][2]
If arr[lookup[i][j-1]] <= arr[lookup[i+2^(j-1)][j-1]]
   lookup[i][j] = lookup[i][j-1]

// If arr[lookup[0][2]] >  arr[lookup[4][2]], 
// then lookup[0][3] = lookup[4][2]
Else 
   lookup[i][j] = lookup[i+2^(j-1)][j-1] 

[7  2   3   0   5   10  3   12  18]
 0  1   2   3   4   5   6   7   8

 lookup [i][j] contains index of minimum in range from arr[i] to arr[i + 2^(j -1)]

Query: 

For any arbitrary range [l, R], we need to use ranges that are in powers of 2. The idea 
is to use the closest power of 2. We always need to do at most one comparison (compare a 
minimum of two ranges which are powers of 2). 
One range starts with L and ends with “L + closest-power-of-2”. 
The other range ends at R and starts with “R – same-closest-power-of-2 + 1”. 
For example, if the given range is (2, 10), we compare a minimum of two ranges (2, 9) and 
(3, 10).

Based on the above example, below is the formula,

// For (2,10), j = floor(Log2(10-2+1)) = 3
j = floor(Log(R-L+1))

// If arr[lookup[0][3]] <=  arr[lookup[3][3]], 
// then RMQ(2,10) = lookup[0][3]

If arr[lookup[L][j]] <= arr[lookup[R-(int)pow(2,j)+1][j]]
   RMQ(L, R) = lookup[L][j]

// If arr[lookup[0][3]] >  arr[lookup[3][3]], 
// then RMQ(2,10) = lookup[3][3]
Else 
   RMQ(L, R) = lookup[R-(int)pow(2,j)+1][j]


Since we do only one comparison, the time complexity of the query is O(1).

So sparse table method supports query operation in O(1) time with O(n Log n) preprocessing
time and O(n Log n) space.

"""
print("\n Method 3 (Sparse Table Algorithm)  \n")

# Python3 program to do range minimum query
# in O(1) time with O(n Log n) extra space
# and O(n Log n) preprocessing time
from math import log2

MAX = 500

# lookup[i][j] is going to store index of
# minimum value in arr[i..j].
# Ideally lookup table size should
# not be fixed and should be determined
# using n Log n. It is kept constant
# to keep code simple.
lookup = [[0 for i in range(500)]
    for j in range(500)]

# Structure to represent a query range


class Query:
  def __init__(self, l, r):
    self.L = l
    self.R = r

# Fills lookup array lookup[][]
# in bottom up manner.


def preprocess(arr: list, n: int):
  global lookup

  # Initialize M for the
  # intervals with length 1
  for i in range(n):
    lookup[i][0] = i

  # Compute values from
  # smaller to bigger intervals
  j = 1
  while (1 << j) <= n:

    # Compute minimum value for
    # all intervals with size 2^j
    i = 0
    while i + (1 << j) - 1 < n:

      # For arr[2][10], we compare
      # arr[lookup[0][3]] and
      # arr[lookup[3][3]]
      if (arr[lookup[i][j - 1]] <
          arr[lookup[i + (1 << (j - 1))][j - 1]]):
        lookup[i][j] = lookup[i][j - 1]
      else:
        lookup[i][j] = lookup[i +
                  (1 << (j - 1))][j - 1]

      i += 1
    j += 1

# Returns minimum of arr[L..R]


def query(arr: list, L: int, R: int) -> int:
  global lookup

  # For [2,10], j = 3
  j = int(log2(R - L + 1))

  # For [2,10], we compare
  # arr[lookup[0][3]] and
  # arr[lookup[3][3]],
  if (arr[lookup[L][j]] <=
      arr[lookup[R - (1 << j) + 1][j]]):
    return arr[lookup[L][j]]
  else:
    return arr[lookup[R - (1 << j) + 1][j]]

# Prints minimum of given
# m query ranges in arr[0..n-1]


def RMQ(arr: list, n: int, q: list, m: int):

  # Fills table lookup[n][Log n]
  preprocess(arr, n)

  # One by one compute sum of all queries
  for i in range(m):

    # Left and right boundaries
    # of current range
    L = q[i].L
    R = q[i].R

    # Print sum of current query range
    print("Minimum of [%d, %d] is %d" %
      (L, R, query(arr, L, R)))


# Driver Code
if __name__ == "__main__":
  a = [7, 2, 3, 0, 5, 10, 3, 12, 18]
  n = len(a)
  q = [Query(0, 4), Query(4, 7),
    Query(7, 8)]
  m = len(q)

  RMQ(a, n, q, m)


'''
my tests

'''

def my_tests(arr, Q):
    result =[]
    for q in Q:
        l, r = q
        result.append(min(arr[l:r+1]))
    return result



print("expected: [0, 3, 12], actual:", my_tests([7, 2, 3, 0, 5, 10, 3, 12, 18], [[0, 4], [4, 7], [7, 8]]))