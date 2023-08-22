"""
Array range queries for elements with frequency same as value

Given an array of N numbers, the task is to answer Q queries of the following type:

query(start, end) = Number of times a number x occurs exactly x times in a subarray 
from start to end.

Input : arr = {1, 2, 2, 3, 3, 3} 
Query 1: start = 0, end = 1, 
Query 2: start = 1, end = 1, 
Query 3: start = 0, end = 2, 
Query 4: start = 1, end = 3, 
Query 5: start = 3, end = 5, 
Query 6: start = 0, end = 5 
Output : 1 0 2 1 1 3 
Explanation 
In Query 1, Element 1 occurs once in subarray [1, 2]; 
In Query 2, No Element satisfies the required condition is subarray [2]; 
In Query 3, Element 1 occurs once and 2 occurs twice in subarray [1, 2, 2]; 
In Query 4, Element 2 occurs twice in subarray [2, 2, 3]; 
In Query 5, Element 3 occurs thrice in subarray [3, 3, 3]; 
In Query 6, Element 1 occurs once, 2 occurs twice and 3 occurs thrice in subarray [1, 2, 2, 3, 3, 3] 

Method 1: Brute Force

Calculate frequency of every element in the subarray under each query. If any number x has
frequency x in the subarray covered under each query, we increment the counter.

Time Complexity of this method is O(Q * N)

"""

# program to answer Q queries to find number of times an element x appears x times in a
# Query subarray
from dataclasses import dataclass
import math as mt

# Returns the count of number x with frequency x in the subarray from start to end
def solveQuery(start, end, arr):

    # map for frequency of elements
    frequency = dict()

    # store frequency of each element in arr[start end]
    for i in range(start, end + 1):
        if arr[i] in frequency.keys():
            frequency[arr[i]] += 1
        else:
            frequency[arr[i]] = 1

    # count elements with same frequency as value
    count = 0
    for x in frequency:
        if x == frequency[x]:
            count += 1
    return count


# Driver code
A = [1, 2, 2, 3, 3, 3 ]
n = len(A)
 
# 2D array of queries with 2 columns
queries = [[ 0, 1 ], [ 1, 1 ],
           [ 0, 2 ], [ 1, 3 ],
           [ 3, 5 ], [ 0, 5 ]]
 
# calculating number of queries
q = len(queries)
 
for i in range(q):
    start = queries[i][0]
    end = queries[i][1]
    print("Answer for Query ", (i + 1), " = ", solveQuery(start,end, A))

"""
Method 2(Efficient)
We can solve this problem using MO's Algorithm.
We assign starting index, ending index and query number to each query. Each query takes
the following form:-

Starting Index(L): Starting Index of the subarray covered under the query
Ending Index(R): Ending index of the subarray covered under the query
Query Number(Index): Since queries are sorted, this tells us original position of the 
query so that we answer the queries in the original order.

Firstly, we divide the queries into blocks and sort the queries using a custom comparator.
Now we process the queries offline where we keep two pointers i.e. MO_RIGHT and MO_LEFT
with each incoming query,we move these pointers forward and backward and insert and delete
elements according to the starting and ending indices of the current query.

Let the current running anser be current_ans.
Whenever we insert an element we increment the frequency of the included element, if this 
frequency is equal to the element we just included, we increment the current_ans.
If the frequency of this element becomes(current element + 1) this means that earlier
this element was counted in the current_ans when it was equal to its frequency, thus we 
need to decrement current_ans in this case.

Whenever we delete/remove an element we decrement the frequency of the excluded element,
if this frequency is equal to the element we just excluded, we increment the current_ans.
If the frequency of this element becomes(current element -1) this means that earlier this
element was counted in the current_ans when it was equal to its frequency, thus we need
to decrement current_ans in this case.

Time Complexity of this approach using MO’s Algorithm is O(Q * sqrt(N) * logA) where logA 
is the complexity to insert an element A into the unordered_map for each query.

"""
import math
# Program to answer Q queries to find number of times an element x appears x times 
# in a Query subarray 


# Variable to represent block size.
# This is made global so compare() of sort can use it.
block: int

# Structure to represent a query range
@dataclass
class Query :
    L: int 
    R: int 
    index: int 


''' Function used to sort all queries
so that all queries of same block
are arranged together and within
a block, queries are sorted in
increasing order of R values. 
'''
def compare(x:Query, y:Query):
    # Different blocks, sort by block.
    if (x.L / block != y.L / block):
        return x.L / block < y.L / block
        
    # Same block, sort by R value
    return x.R < y.R

# Inserts element (x) into current range and updates current answer
# int& currentAns,	unordered_map<int, int>& freq
def add(x:int, currentAns,	freq):
    # increment frequency of this element
    freq[x] +=1
    
    # if this element was previously contributing to the currentAns, decrement currentAns 
    if (freq[x] == (x + 1)):
        currentAns -=1

	# if this element has frequency equal to its value, increment currentAns
    elif (freq[x] == x):
        currentAns +=1

# Removes element (x) from current range btw L and R and updates current Answer 
# unordered_map<int, int>& freq
def remove(x:int, currentAns:int, freq):
    
    # decrement frequency of this element
    freq[x] -=1

	# if this element has frequency equal to its value, increment currentAns
    if (freq[x] == x):
        currentAns +=1

	# if this element was previously contributing to the currentAns decrement currentAns
    elif (freq[x] == (x - 1)):
        currentAns -=1

# Utility Function to answer all queries and build the ans array in the original
# order of queries 
# queryResultsUtil(int a[], Query q[],int ans[], int m)
def  queryResultsUtil(a, q, ans, m):
    
    # map to store freq of each element 
	# unordered_map<int, int> freq;
   freq ={}
   
   # Initialize current L, current R and current sum
   currL = 0
   currR:int = 0
   currentAns:int = 0
   
   # Traverse through all queries
   for i in range(0, m):
		# L and R values of current range
        L = q[i].L, R = q[i].R
        index = q[i].index
        
        #Remove extra elements of previous
        # range. For example if previous
        # range is [0, 3] and current range
        #  is [2, 5], then a[0] and a[1] are
        #  removed
        
        while (currL < L):
            remove(a[currL], currentAns, freq)
            currL +=1
            
        # Add Elements of current Range
        
        while (currL > L):
            currL-=1
            add(a[currL], currentAns, freq)
            
        while (currR <= R):
            add(a[currR], currentAns, freq)
            currR +=1
            
        # Remove elements of previous range. For example # when previous range is 
        # [0, 10] and current range is [3, 8], then a[9] and a[10] are Removed
        
        while (currR > R + 1):
            currR -=1
            remove(a[currR], currentAns, freq)
            
        # Store current ans as the Query ans for Query number index
        ans[index] = currentAns


# Wrapper for queryResultsUtil() and outputs the ans array constructed by answering all
# queries queryResults(int a[], int n, Query q[], int m)
def queryResults(a, n, q, m):
    # Find block size
    block = int(math.sqrt(n))
    
    # Sort all queries so that queries of same blocks are arranged together.
    sort(q, q + m, compare)
    
    # int* ans = new int[m];
    ans = [0] *m
    queryResultsUtil(a, q, ans, m)
    
    for i in range(0, m):
        # << (i + 1) << " = " << ans[i] << endl;
        print("Answer for Query " , (i + 1) , " = " , ans[i])
        
#Driver program
if __name__=="__main__":
    
    A= [ 1, 2, 2, 3, 3, 3 ]
    
    n = len(A) / A[0]
    
    # 2D array of queries with 2 columns
    queries = [ [ 0, 1, 0 ],
						[ 1, 1, 1 ],
						[ 0, 2, 2 ],
						[ 1, 3, 3 ],
						[ 3, 5, 4 ],
						[ 0, 5, 5 ] ]

	# calculating number of queries
    q = len(queries) / len(queries[0])
    
    # Print result for each Query 
    queryResults(A, n, queries, q)