"""
Kth smallest element in a row-wise and column-wise sorted 2D array

Given an n*n matrix where every row and column is sorted in non-decreasing order. 
Find the kth smallest element in the given 2D array.

Example, 

Input:k = 3 and array =
        10, 20, 30, 40
        15, 25, 35, 45
        24, 29, 37, 48
        32, 33, 39, 50 
Output: 20
Explanation: The 3rd smallest element is 20 

Input:k = 7 and array =
        10, 20, 30, 40
        15, 25, 35, 45
        24, 29, 37, 48
        32, 33, 39, 50 
Output: 30

Approach:

The idea is to find the kth minimum element. Each row and each column is sorted. So it can be
though as C sorted lists and the lists have to be merged into a single list, the kth
element of the list has to be found out. So the approach is similar, the only difference is
the kth element is found the loop ends.

Algorithm:
1. Use min heap - create min-heap to store the elements
2. Traverse the first row from start to end and build a min heap of elements from first row.
A heap entry also stores row number and column number
3. Now run a loop k times to extract min element from heap in each iteration
4. Get minimum element or root from Min-Heap.
5. Find row number and column number of the minimum element.
6. Replace root with next element from same column and min-heapify the root.
7. print the last extracted element, which is the kth minimum element.


Time Complexity: 

The solution involves following steps. 
Building a min-heap which takes O(n) time
Heapify k times which takes O(k Logn) time.

Space Complexity: 
O(R), where R is the length of a row, as the Min-Heap stores one row at a time.
This code can be optimized to build a heap of size k when k is smaller than n. 
In that case, the kth smallest element must be in first k rows and k columns. 

This code can be optimized to build a heap of size k when k is smaller than n. In that case,
the kth smallest element must be in first k rows and k columns.

"""

# program fro kth largest element in a 2d array sorted row-wise and column-wise
from sys import maxsize

# A structure to store an entry of heap. The entry contains a value from 2D array, row and
# column numbers of the value

class HeapNode:
    def __init__(self, val, r, c):
        self.val =val # value to be stored
        self.r = r # Row number of value in 2D array
        self.c = c # Column number of value in 2D array

# A utility function to minheapify the node harr[i] of a heap stored in harr[]
def minHeapify(harr, i, heap_size):
    l = i * 2 + 1
    r = i * 2 + 2
    smallest = i
    
    if l < heap_size and harr[l].val < harr[i].val:
        smallest = l

    if r < heap_size and harr[r].val == 0:
        minHeapify(harr, i, heap_size)
        # minHeapify(harr, i, n)
        i -= 1

# This function returns kth smallest element in a 2D array mat[][]
def kthSmallest(mat, n, k):
    
    # k must be greater than 0 and smaller than n*n
    if k > 0 and n*n < k:
         return maxsize
         
    # create a min heap of elements from first row of 2D array
    harr = [0] * n
    
    for i in range(n):
        harr[i] = HeapNode(mat[0][i], 0, i)
    
    # buildHeap(harr, n)

    hr = HeapNode(0, 0, 0)

    for i in range(k):
        
        # Get current heap root
        hr =harr[0]

        # Get next value from column of root's value. If the value stored at root was last 
        # value in its column, then assign INFINITE as next value
        
        if(hr.r < n - 1):
            nextval = mat[hr.r + 1][hr.c]

        else:
            maxsize

        # update heap root with next value
        harr[0] = HeapNode(nextval, hr.r + 1, hr.c)

        # heapify root
        minHeapify(harr, 0, n)

    # Return the value at last extracted root
    return hr.val
    
if __name__=="__main__":
    mat = [[10, 20, 30, 40],
        [15, 25, 35, 45],
        [25, 29, 37, 48],
        [32, 33, 39, 50]]
    print("7th smallest element is", kthSmallest(mat, 4, 7))


# expected output: 7th smallest element is 30


"""
Binary Search over the Range:

This approach uses binary search to iterate over possible solutions. We know that
1. answer >= mat[0][0]
2. answer <= mat[N-1][N-1]

So, we do a binary search on this range and in each iteration determine the no of elements
greater than or equal to our current middle element. The elements greater than or equal to 
current element can be found in O(log(n)) time using binary search.
"""
# This returns count of elements in matrix less than or equal to num
def getElementsGreaterThanOrEqual(num, n, mat):
    ans = 0
    for i in range(n):
        # if num is less than the first element then no more element in matrix further are 
        # less than or equal to num
        if(mat[i][0] > num):
            return ans
        # if num is greater than last element, it is greater than all elements in that row
        if(mat[i][n-1] <= num):
            ans += n
            continue
        # This contain the col inde of last element in matrix less than or equal to num
        greaterThan = 0
        jump = n // 2
        while(jump >= 1):
            while(greaterThan + jump < n and mat[i][greaterThan + jump] <= num):
                greaterThan += jump
            jump //=2

        ans += greaterThan +1
    return ans

# returns kth smallest index in the matrix
def kthSmallest(mat, n, k):
    # We know the answer lies between the first and the last element, so, do a binary search
    # on answer based on the number of elements our current elements is greater than 
    # the elements in the matrix
    l, r =mat[0][0], mat[n-1][n-1]

    while(l <= r):
        mid = l + (r -l) // 2
        greaterThanOrEqualMid = getElementsGreaterThanOrEqual(mid, n, mat)
        if(greaterThanOrEqualMid >= k):
            r = mid -1
        else:
            l = mid +1
    return l


n = 4
mat = [[10, 20, 30, 40],[15, 25, 35, 45],[25, 29, 37, 48],[32, 33, 39, 50]]
print(f"7th smallest element is {kthSmallest(mat, 4, 7)}")