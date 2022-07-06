"""
We have an array arr[]. We need to find the sum of all the elements in the range L and R
where 0<=L<=R<=n-1. Consider a situation when there are many range queries.

Examples:

Input: 3 7 2 5 8 9

    query(0, 5)
    query(3, 5)
    query(2, 4)

Output: 34
        22
        15

Note : array is 0 based indexed and queries too.

since there are no updates/modifications, we use the Sparse table to answer queries 
efficiently. In a sparse table, we break queries in powers of 2.

suppose we are asked to compute sum of elements from arr[i] to arr[i+12].
We do the following:

// Use sum of 8(or 2^3) elements
table[i][3] = sum(arr[i], arr[i+1], ... arr[i+7])

// use sum of 4 elements
table[i+8][2] = sum(arr[i+8], arr[i+9],..arr[i+11]).

// Use sum of single element
table[i+12][0] = sum(arr[i+12]).

our result is sum of above values.

Notice that it took only 4 actions to compute the result over a subarray of size 13.


This algorithm for answering queries with Sparse Table works in O(k), which is O(log(n))
because we choose minimal k such that 2^k+1 > n.

Time complexity of sparse table construction :
Outer loop runs in O(k), inner loop runs in O(n). Thus, in total we get
O(n * k) = O(n * log(n)) 

"""

# program to find the sum in a given range in an array using sparse table.
# Because 2^17 is larger than 10^5
k =16

# maximum value of array
n = 100000

# k + 1 because we need to access table[r][k]

table =[[0 for j in range(k + 1)] for i in range(n)]

# it builds sparse table
def buildSparseTable(arr, n):
    global table, k

    for i in range(n):
        table[i][0] = arr[i]

    for j in range(1, k+1):
        for i in range(0, n-(1<<j)+1):
            table[i][j] = table[i][j-1] + table[i + (1 << (j-1))][j-1]

# Returns the sum of the elements in the range L and R.
def query(L, R):
    global table, k

    # boundaries of next query, 0 - indexed
    answer = 0
    for j in range(k, -1, -1):
        if( L +(1 << j)-1 <=R):
            answer = answer + table[L][j]

            # instead of having L ', we increment L directly
            L += 1<< j

    return answer


if __name__ == '__main__':
    arr = [3, 7, 2, 5, 8, 9]
    n = len(arr)
 
    buildSparseTable(arr, n)
    print(query(0,5))
    print(query(3,5))
    print(query(2,4))

'''
my tests
'''

def my_test(arr, ran):
    l,r =ran
    return sum(arr[l:r+1])

print("expected: 34, actual:", my_test([3, 7, 2, 5, 8, 9],[0,5]))
print("expected: 22, actual:", my_test([3, 7, 2, 5, 8, 9],[3,5]))
print("expected: 15, actual:", my_test([3, 7, 2, 5, 8, 9],[2,4]))

