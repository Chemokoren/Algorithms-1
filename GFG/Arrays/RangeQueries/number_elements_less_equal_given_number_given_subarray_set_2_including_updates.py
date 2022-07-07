"""
Number of elements less than or equal to a given number in a given subarray | set 2 

(including updates)

Given an array 'a[]' and number of queries q there will be two types of queries

    Query 0 update(i, v) : Two integers i and v which means set a[i] = v
    Query 1 count(l, r, k): We need to print number of integers less than equal to k in 
    the subarray l to r.

Given a[i], v <= 10000 Examples :

Input : arr[] = {5, 1, 2, 3, 4}
        q = 6
        1 1 3 1  // First value 1 means type of query is count()
        0 3 10   // First value 0 means type of query is update()
        1 3 3 4
        0 2 1
        0 0 2
        1 0 4 5
Output :
1
0
4
For first query number of values less than equal to 1 in 
arr[1..3] is 1(1 only), update a[3] = 10
There is no value less than equal to 4 in the a[3..3]
and similarly other queries are answered       

We have discussed a solution that handles only count() queries in below post.
Number of elements less than or equal to a given number in a given subarray Here update()
query also needs to be handled. 

Naive Approach 
---------------
The naive approach is whenever there is update operation update the array and whenever
type 2 query is there traverse the subarray and count the valid elements. 

Efficient Approach 
------------------
The idea is to use square root decomposition 

    Step 1 : Divide the array in sqrt(n) equal sized blocks. For each block keep a binary
    index tree of size equal to 1 more than the maximum possible element in the array of 
    the elements in that block.
    Step 2: For each element of the array find out the block to which it belongs and 
    update the bit array of that block with the value 1 at arr[i].
    Step 3: Whenever there is a update query, update the bit array of the corresponding 
    block at the original value of the array at that index with value equal to -1 and 
    update the bit array of the same block with value 1 at the new value of the array at 
    that index.
    Step 4: For type 2 query you can make a single query to the BIT (to count elements 
    less than or equal to k) for each complete block in the range, and for the two 
    partial blocks on the end, just loop through the elements.


The question is know why not to use this method when there were no update operations the 
answer lies in space complexity in this method 2-d bit array is used as well as its size 
depends upon the maximum possible value of the array but when there was no update 
operation our bit array was only dependent on the size of array. 

"""
# number of elements less than or equal to a given number in a given subarray 
# and allowing update operations
MAX = 10001

# updating the bit array of a valid block
def update(idx, blk, val, bit):
    while idx < MAX:
        bit[blk][idx] += val

        idx += (idx & -idx)

# answering the query
def query(l, r, k, arr, blk_sz, bit):

    # traversing the first block in range
    summ = 0
    while l<r and l % blk_sz !=0 and l != 0:
        if arr[l] <= k:
            summ +=1
        l += 1
    # Traversing completely overlapped blocks in range for such blocks bit array of
    # that block is queried
    while l + blk_sz <=r:
        idx = k
        while idx > 0:
            summ += bit[l // blk_sz][idx]
            idx -= (idx & -idx)
        
        l += blk_sz

    # Traversing the last block
    while l<= r:
        if arr[l]  <= k:
            summ += 1
        l += 1
    return summ

# Preprocessing the array
def preprocess(arr, blk_sz, n, bit):
    for i in range(n):
        update(arr[i], i//blk_sz, 1, bit)

def preprocessUpdate(i, v, blk_sz, arr, bit):
    # updating the bit array at the original and new value of array
    update(arr[i], i // blk_sz, -1, bit)
    update(v, i//blk_sz, 1, bit)
    arr[i] = v

if __name__=="__main__":
    arr =[5,1,2,3,4]
    n = len(arr)

    # size of block size will be equal to square root of n
    from math import sqrt
    blk_sz = int(sqrt(n))

    # Initialising bit array of each block as elements of array cannot exceed 10^4
    # so size of bit array is accordingly
    bit =[[0 for j in range(MAX)] for j in range(blk_sz +1)]

    preprocess(arr, blk_sz, n, bit)
    print(query(1,3,1,arr,blk_sz, bit))

    preprocessUpdate(3, 10, blk_sz, arr, bit)
    print(query(3,3,4,arr,blk_sz, bit))
    preprocessUpdate(2,1, blk_sz,arr,bit)
    preprocessUpdate(0, 2, blk_sz, arr, bit)
    print(query(0, 4, 5, arr, blk_sz, bit))