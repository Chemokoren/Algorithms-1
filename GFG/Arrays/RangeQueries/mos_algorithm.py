"""
MO's Algorithm(Query Square Root Decomposition) | Set 1 (Introduction)

We are given an array and a set of query ranges, we are required to find the sum of every
query range.

Input:  arr[]   = {1, 1, 2, 1, 3, 4, 5, 2, 8};
query[] = [0, 4], [1, 3] [2, 4]
"""

def test(arr,lst):
    start =lst[0]
    end = lst[1]
    return sum(arr[start:end+1])


print("expected: 8, actual: ", test([1, 1, 2, 1, 3, 4, 5, 2, 8],[0, 4] ))
print("expected: 4, actual: ", test([1, 1, 2, 1, 3, 4, 5, 2, 8],[1, 3] ))
print("expected: 6, actual: ", test([1, 1, 2, 1, 3, 4, 5, 2, 8],[2, 4]))


def new_test(arr,Q):
    result =[]
    for q in Q:
        l,r =q
        result.append(sum(arr[l:r+1]))
    return result

print(new_test([1, 1, 2, 1, 3, 4, 5, 2, 8],[[0, 4], [1, 3], [2, 4]]))

"""
The idea of MO's algorithm is to pre-process all queries so that result of one query
can be used in next qery. Below are the steps.

Let a[0...n-1] be input array and q[0..m-1] be array of queries.
1. Sort all queries in a way that queries with L values from 0 to square root(n-1) are put
together, then all queries from square root(n) to 2*square root(n-1), and so on. 
All queries within a block are sorted in increasing order of R vales.

2. Process all queries one by one in a way that every query uses sum computed in the 
previous query.
    - Let 'sum' be sum of previous query.
    - Remove extra elements of previous query. For example if previous query is [0,8] and
    current query is[3,9] then we subtract a[0], a[1] and a[2] from sum.
    - Add new elements of current query. In the same example as above, we add a[9] to sum.

The great thing about this algorithm is, in step 2, index variable for R change at most
O(n * square root(n)) times throght the run and same for L changes its value at most 
O(m * square root(n)) times.
All these bounds are possible only because the queries are sorted first in blocks of size
square root(n) size.

The preprocessing part takes O(m Log m) time.

Processing all queries takes 
O(n*square root(n)) + O(m * square root(n)) = O((m+n)*square root(n)) time.



"""

# compute sum of ranges for different range queries
import math

# function accepts array and list of queries and print sm of each query
def queryResults(arr, Q):
    # sort all queries so that all queries are in the increasing order of R values
    Q.sort(key=lambda x:x[1])

    # Initialize current L, current R and current sum
    currL, currR, currSum =0,0,0

    # Traverse throgh all queries
    for i in range(len(Q)):
        L, R = Q[i] # L and R values of current range

        # Remove extra elements from previous range
        # if previous range is[0,3] and current range is [2,5], then a[0] and a[1] are 
        # subtracted
        while currL < L:
            currSum -= arr[currL]
            currL +=1

        # Add elements of current range
        while currL > L:
            currSum += arr[currL -1]
            currL -=1
        while currR <= R:
            currSum += arr[currR]
            currR +=1

        # Remove elements of previous range
        # When previous range is[0,10] and current range is[3,8], then a[9] and a[10] are
        # subtracted
        while currR > R +1:
            currSum -= arr[currR -1]
            currR -=1
        # print the sum of current range
        print("Sum of", Q[i], "is", currSum)

arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
Q = [[0, 4], [1, 3], [2, 4]]
queryResults(arr,Q)
        

"""
The output of above program doesn’t print results of queries in same order as input,
because queries are sorted. The program can be easily extended to keep the same order.

Important Observations: 

    - ll queries are known beforehead so that they can be preprocessed
    - It cannot work for problems where we have update operations also mixed with sum 
    queries.
    - MO’s algorithm can only be used for query problems where a query can be computed 
    from results of the previous query. One more such example is maximum or minimum.

Time Complexity Analysis: 

The function mainly runs a for loop for all sorted queries. Inside the for loop, 
there are four while queries that move ‘currL’ and ‘currR’.

How much currR is moved? For each block, queries are sorted in increasing order of R. 
So, for a block, currR moves in increasing order. 
In worst case, before beginning of every block, currR at extreme right and current block 
moves it back the extreme left. 
This means that for every block, currR moves at most O(n). 
Since there are O(√n) blocks, total movement of currR is O(n * √n). 

How much currL is moved? 
Since all queries are sorted in a way that L values are grouped by blocks, 
movement is O(√n) when we move from one query to another quert. 
For m queries, total movement of currL is O(m * √n)
Please note that a Simple and more Efficient solution to solve this problem is to compute 
prefix sum for all elements from 0 to n-1. Let the prefix sum be stored in an array 
preSum[] (The value of preSum[i] stores sum of arr[0..i]). Once we have built preSum[], 
we can traverse through all queries one by one. For every query [L, R], 
we return value of preSum[R] – preSum[L]. Here processing every query takes O(1) time. 

Auxiliary Space: O(1)


"""
