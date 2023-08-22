"""
XOR of numbers that appeared even number of times in given range

Given an array of numbers of size N and queries. Each query or a range can be represented 
by L(LeftIndex) and R(RightIndex). Find XOR -sum of the numbers that appeared even number
of times in the given range.

Prerequisite: Queries for number of distinct numbers in given range | Segment Tree for 
range query

Examples:


Input : arr[] = { 1, 2, 1, 3, 3, 2, 3 }
        Q = 5
        L = 3,  R = 6
        L = 3,  R = 4
        L = 0,  R = 2
        L = 0,  R = 6
        L = 0,  R = 4
Output : 0
         3
         1
         3
         2

Explanation of above example: 
In Query 1, there are no numbers which appeared even number of times. 
Hence the XOR-sum is 0. 
In Query 2, {3} appeared even number of times. XOR-sum is 3. 
In Query 3, {1} appeared even number of times. XOR-sum is 1. 
In Query 4, {1, 2} appeared even number of times. XOR-sum is 1 xor 2 = 3. 
In Query 5, {1, 3} appeared even number of times. XOR-sum is 1 xor 3 = 2.

Segment Trees or Binary Indexed Trees can be used to solve this problem efficiently.

Approach:

Firstly, it is easy to note that the answer for the query is the XOR-sum of all elements in
the query range xor-ed with XOR-sum of distinct elements in the query range(since
taking XOR of an element with itself results into a null value). Find the XOR-sum of all 
numbers in query range using prefix XOR-sums.
To find the XOR-sum of distinct elements in range: Number of distinct elements in a 
subarray of given range.

Now, returning back to our main problem, just change the assignment BIT[i] = 1 to
BIT[i] = arri(i is subscript) and count the XOR-sum instead of sum.


Time Complexity: O(Q * Log(N)), where N is the size of array, Q is the total number of
queries.

Space complexity: O(N) where N is size of array
 
"""

# Program to Find the XOR-sum of elements that appeared even
#  number of times within a range


''' structure to store queries
L --> Left Bound of Query
R --> Right Bound of Query
idx --> Query Number '''
from dataclasses import dataclass


@dataclass
class que:
    L:int
    R:int
    idx:int

#  cmp function to sort queries according to R

def cmp(a: que, b:que):
    if (a.R != b.R):
        return a.R < b.R;
    else:
        return a.L < b.L;

''' 
N --> Number of elements present in input array. BIT[0..N] --> Array that
represents Binary Indexed Tree
'''

# Returns XOR-sum of arr[0..index]. This
# function assumes that the array is
# preprocessed and partial sums of array
# elements are stored in BIT[].
# BIT is an array of type int
def getSum(BIT:int,index:int):

	# Initialize result
	xorSum = 0

	# index in BITree[] is 1 more than
	# the index in arr[]
	index = index + 1

	# Traverse ancestors of BIT[index]
	while (index > 0):
		# Take XOR of current element of BIT to xorSum
		xorSum ^= BIT[index]

		# Move index to parent node
		# in getSum View
		index -= index & (-index)
	return xorSum

# Updates a node in Binary Index Tree
# (BIT) at given index in BIT. The
# given value 'val' is xored to BIT[i]
# and all of its ancestors in tree.
# BIT is an array of type int
def updateBIT(BIT, N: int,index:int, val:int):
	# index in BITree[] is 1 more than
	# the index in arr[]

	index = index + 1

	# Traverse all ancestors and
	# take xor with 'val'
	while (index <= N):

		# Take xor with 'val' to
		# current node of BIT
		BIT[index] ^= val

		# Update index to that of
		# parent in update View
		index += index & (-index)


# Constructs and returns a Binary Indexed
# Tree for given array of size N.
# arr: array of type int
def constructBITree(arr:int, N: int):
    # Create and initialize BITree[] as 0
	#int* BIT = new int[N + 1]
    BIT = int[N + 1]

    for i in range(1, N):
        BIT[i] = 0
    return BIT

# Function to answer the Queries
# arr - array of type int
# queries - array of type que
# BIT is an array of type int
def answeringQueries(arr: int, N:int, queries, Q:int,BIT):
	# Creating an array to calculate
	# prefix XOR sums
	# int* prefixXOR = new int[N + 1];
    prefixXOR = int[N + 1]


	# map for coordinate compression
	# as numbers can be very large but we
	# have limited space
	# map<int, int> mp
    mp ={}
    
    for i  in range(0,N):
        
        # If A[i] has not appeared yet
        if (not mp[arr[i]]):
            mp[arr[i]] = i
            
        # calculate prefixXOR sums
        if (i == 0):
            prefixXOR[i] = arr[i]
        else:
            prefixXOR[i] =prefixXOR[i - 1] ^ arr[i]
            
    
    # Creating an array to store the
	# last occurrence of arr[i]
	# int lastOcc[1000001];
    lastOcc =[1,0,0,0,0,0,1]
    
    memset(lastOcc, -1, len(lastOcc))
    
    # sort the queries according to comparator
    sort(queries, queries + Q, cmp)
    
    # answer for each query, int res[Q];
    int(res[Q])
    
    # Query Counter
    
    j = 0
    
    for i in range(0, Q):
        
        while (j <= queries[i].R):
            
            # If last visit is not -1 update
			# arr[j] to set null by taking
			# xor with itself at the idx
			# equal lastOcc[mp[arr[j]]]
            if (lastOcc[mp[arr[j]]] != -1):
                updateBIT(BIT, N,lastOcc[mp[arr[j]]], arr[j])
            
            # Setting lastOcc[mp[arr[j]]] as j and
			# updating the BIT array accordingly   
            updateBIT(BIT, N, j, arr[j])
            lastOcc[mp[arr[j]]] = j
            j +=1
        
        # get the XOR-sum of all elements within
		# range using precomputed prefix XORsums
        allXOR = prefixXOR[queries[i].R] ^	prefixXOR[queries[i].L - 1]
        
        # get the XOR-sum of distinct elements
		# within range using BIT query function
        distinctXOR = getSum(BIT, queries[i].R) ^ getSum(BIT, queries[i].L - 1)
        # store the final answer at the numbered query
        res[queries[i].idx] = allXOR ^ distinctXOR
    
    # Output the result
    for i in range(0, Q):
        print(res[i])


# Driver program to test above functions
if __name__=='__main__0':
    
    arr = [ 1, 2, 1, 3, 3, 2, 3 ]
    N = len(arr) / len(arr[0])

    # int* BIT = constructBITree(arr, N)
    BIT = constructBITree(arr, N)

	# structure of array for queries
	# que queries[5]
    queries = [5] * que
    
    #  Initializing values (L, R, idx) to queries 
    
    queries[0].L = 3 
    queries[0].R = 6
    queries[0].idx = 0
    queries[1].L = 3 
    queries[1].R = 4
    queries[1].idx = 1
    queries[2].L = 0
    queries[2].R = 2
    queries[2].idx = 2
    queries[3].L = 0
    queries[3].R = 6
    queries[3].idx = 3
    queries[4].L = 0
    queries[4].R = 4
    queries[4].idx = 4
    
    Q = len(queries) / len(queries[0])
    
    # answer Queries
    answeringQueries(arr, N, queries, Q, BIT)