"""
Maximum Occurrence in a Given Range

Given an array of n integers in non-decreasing order. Find the number of occurrences 
of the most frequent value within a given range:

Input : arr[] = {-5, -5, 2, 2, 2, 2, 3, 7, 7, 7}
        Query 1: start = 0, end = 9
        Query 2: start = 4, end = 9
Output : 4
         3
Explanation:  
Query 1: '2' occurred the most number of times
with a frequency of 4 within given range.
Query 2: '7' occurred the most number of times
with a frequency of 3 within given range.

Segment Trees can eb used to solve this problem efficiently.
The key idea behind this problem is that the given array is non-decreasing order which
means that all occurrences of a number are consecutively placed in the array as the array
is in sorted order.

A segment tree can be constructed where each node would store the maximum count of its
respective range[i,j]. For that we will build the frequency array and call RMQ 
(Range Maximum Query) on this array. 

arr[] =  {-5, -5, 2, 2, 2, 2, 3, 7, 7, 7}
freq_arr[] = {2, 2, 4, 4, 4, 4, 1, 3, 3, 3}
where, freq_arr[i] = frequency(arr[i])

Now there are two cases to be considered,

Case 1: The value of the numbers at index i and j for the given range are same, i.e. 
arr[i] = arr[j].
Solving this cases is very easy. Since arr[i] = arr[j], all numbers between these indices
are same(since the array is non-decreasing). Hence answer for this case is simply count
of all numbers between i and j(inclusive of both) i.e. (j-1+1)

arr[] =  {-5, -5, 2, 2, 2, 2, 3, 7, 7, 7}
if the given query range is [3, 5], answer would 
be (5 - 3 + 1) = 3, as 2 occurs 3 times within  given range


Case 2: The value of the numbers at index i and j for the given range are different, i.e. 
arr[i] != arr[j] 
If arr[i] != arr[j], then there exists an index k where arr[i] = arr[k] and
arr[i] != arr[k + 1]. This may be a case of partial overlap where some occurrences of a
particular number lie in the leftmost part of the given range and some lie just before 
range starts. 
Here simply calling RMQ would result into an incorrect answer. 

For e.g. 
 

arr[] =  {-5, -5, 2, 2, 2, 2, 3, 7, 7, 7}
freq_arr[] = {2, 2, 4, 4, 4, 4, 1, 3, 3, 3}
if the given query is [4, 9], calling RMQ on 
freq_arr[] will give us 4 as answer which 
is incorrect as some occurrences of 2 are 
lying outside the range. Correct answer is 3.


Similar situation can happen at the rightmost part of the given range where some 
occurrences of a particular number lies inside the range and some lies just after the 
range ends. 
Hence for this case, inside the given range we have to count the leftmost same numbers 
upto some index say i and rightmost same numbers from index say j to the end of the range.
And then calling RMQ (Range Maximum Query) between indices i and j and taking maximum of 
all these three. 
For e.g. 

arr[] =  {-5, -5, 2, 2, 2, 2, 3, 7, 7, 7}
freq_arr[] = {2, 2, 4, 4, 4, 4, 1, 3, 3, 3}
if the given query is [4, 7], counting leftmost
same numbers i.e 2 which occurs 2 times inside 
the range and rightmost same numbers i.e. 3 
which occur only 1 time and RMQ on [6, 6] is 
1. Hence maximum would be 2.


Further Optimization: For the partial overlapping case we have to run a loop to calculate 
the count of same numbers on both sides. To avoid this loop and perform this operation in 
O(1), we can store the index of the first occurrence of every number in the given array 
and hence by doing some precomputation we can find the required count in O(1).

Time Complexity: 
Time Complexity for tree construction is O(n). Time complexity to query is O(Log n).
"""

# Python 3 Program to find the occurrence
# of the most frequent number within
# a given range
from collections import defaultdict
import math

# A utility function to get the middle index
# from corner indexes.
def getMid(s, e):
	return s + (e - s) // 2

''' A recursive function to get the maximum value in
	a given range of array indexes. The following
	are parameters for this function.

	st --> Pointer to segment tree
	index --> Index of current node in the segment
			tree. Initially 0 is passed as root is
			always at index 0
	ss & se --> Starting and ending indexes of the
				segment represented by current node,
				i.e., st[index]
	qs & qe --> Starting and ending indexes of query
				range '''
def RMQUtil(st, ss, se, qs, qe, index):
	
	# If segment of this node is a part of given range
	# then return the min of the segment
	if (qs <= ss and qe >= se):
		return st[index]
		
	# If segment of this node is outside the
	# given range
	if (se < qs or ss > qe):
		return 0

	# If a part of this segment overlaps
	# with the given range
	mid = getMid(ss, se)
	return max(RMQUtil(st, ss, mid, qs, qe, 2 * index + 1),
			RMQUtil(st, mid + 1, se, qs, qe, 2 * index + 2))


# Return minimum of elements in range from
# index qs (query start) to
# qe (query end). It mainly uses RMQUtil()
def RMQ(st, n, qs, qe):

	# Check for erroneous input values
	if (qs < 0 or qe > n - 1 or qs > qe):
		prf("Invalid Input")
		return -1

	return RMQUtil(st, 0, n - 1, qs, qe, 0)

# A recursive function that constructs Segment Tree
# for array[ss..se]. si is index of current node in
# segment tree st
def constructSTUtil(arr, ss, se, st,
					si):
	
	# If there is one element in array, store it in
	# current node of segment tree and return
	if (ss == se):
		st[si] = arr[ss]
		return arr[ss]
		
	# If there are more than one elements, then
	# recur for left and right subtrees and store
	# the minimum of two values in this node
	mid = getMid(ss, se)
	st[si] = max(constructSTUtil(arr, ss, mid, st, si * 2 + 1),
				constructSTUtil(arr, mid + 1, se, st, si * 2 + 2))
	return st[si]

''' Function to construct segment tree from given
array. This function allocates memory for segment
tree and calls constructSTUtil() to fill the
allocated memory '''
def constructST(arr, n):

	# Allocate memory for segment tree
	# Height of segment tree
	x = (math.ceil(math.log2(n)))
	
	# Maximum size of segment tree
	max_size = 2 * pow(2, x) - 1
	st = [0]*max_size

	# Fill the allocated memory st
	constructSTUtil(arr, 0, n - 1, st, 0)
	
	# Return the constructed segment tree
	return st

def maximumOccurrence(arr, n, qs, qe):

	# Declaring a frequency array
	freq_arr = [0]*(n + 1)
	
	# Counting frequencies of all array elements.
	cnt = defaultdict(int)
	for i in range(n):
		cnt[arr[i]] += 1

	# Creating frequency array by replacing the
	# number in array to the number of times it
	# has appeared in the array
	for i in range(n):
		freq_arr[i] = cnt[arr[i]]

	# Build segment tree from this frequency array
	st = constructST(freq_arr, n)
	maxOcc = 0 # to store the answer
	# Case 1: numbers are same at the starting
	# and ending index of the query
	if (arr[qs] == arr[qe]):
		maxOcc = (qe - qs + 1)
		
	# Case 2: numbers are different
	else:
		leftmost_same = 0
		righmost_same = 0
		
		# Partial Overlap Case of a number with some
		# occurrences lying inside the leftmost
		# part of the range and some just before the
		# range starts
		while (qs > 0 and qs <= qe and arr[qs] == arr[qs - 1]):
			qs += 1
			leftmost_same += 1

		# Partial Overlap Case of a number with some
	# occurrences lying inside the rightmost part of
		# the range and some just after the range ends
		while (qe >= qs and qe < n - 1 and arr[qe] == arr[qe + 1]):
			qe -= 1
			righmost_same += 1

		# Taking maximum of all three
		maxOcc = max([leftmost_same, righmost_same,
					RMQ(st, n, qs, qe)])

		return maxOcc

# Driver Code
if __name__ == "__main__":

	arr = [-5, -5, 2, 2, 2, 2, 3, 7, 7, 7]
	n = len(arr)

	qs = 0 # Starting index of query range
	qe = 9 # Ending index of query range

	# Print occurrence of most frequent number
	# within given range
	print("Maximum Occurrence in range is = ",
		maximumOccurrence(arr, n, qs, qe))

	qs = 4 # Starting index of query range
	qe = 9 # Ending index of query range

	# Print occurrence of most frequent number
	# within given range
	print("Maximum Occurrence in range is = ",
		maximumOccurrence(arr, n, qs, qe))

    



'''
my tests

'''
def my_tests(arr, q):
    l, r =q
    dic ={}
    new_arr=arr[l:r+1]

    for i in new_arr:
        if i in dic:
            dic[i] +=1
        else:
            dic[i] =1

    largest=-float('inf')
    num =None
    for key,val in dic.items():
        if val > largest:
            largest =val
            num =key
    return "\'"+str(num) +"\' occurred the most no. of times with a frequency of " +str(largest)

print("expected [2,4]", my_tests([-5, -5, 2, 2, 2, 2, 3, 7, 7, 7], [0,9]))
print("expected [7,3]", my_tests([-5, -5, 2, 2, 2, 2, 3, 7, 7, 7], [4,9]))