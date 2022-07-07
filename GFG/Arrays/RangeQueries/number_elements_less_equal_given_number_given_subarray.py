"""
Number of elements less than or equal to a given number in a given subarray

Given an array 'a[]' and number of queries q. Each query can be represented by l,r,x.
Your task is to print the number of elements less than or equal to x in the subarray
represented by l to r. Examples:

Input: arr[] = {2,3,4,5}
        q = 2
        0   3   5
        0   2   2

Output :    4
            1
Number of elements less than or equal to 5 in arr[0..3] is 4(all elements)

Number of elements less than or equal to 2 in arr[0..2] is 1 (only 2)


Naive Approach

- The naive approach for each query is to traverse the subarray and count the number of 
elements which are in the given range.

Efficient Approach

- The idea is to use binary index Tree. Not in the following steps x is the number 
according to which you have to find the elements and the subarray is represented 
l,r. 
Step 1: Sort the array in ascending order. 
Step 2: Sort the queries according to x in ascending order, initialize bit array as 0.
Step 3: Start from the first query and traverse the array till the value in the array is
less than equal to x. For each such element, update the BIT with value equal to 1.
Step 4: Query the BIT array in the range l to r


"""

from dataclasses import dataclass
from typing import List

# program to answer queries to count number of elements smaller than or equal to x

class Query1():
    def __init__(self, l, r, x, idx):
        # original int l,r,x,idx
        self.l = l
        self.r = r
        self.x = x
        self.idx = idx

@dataclass
class Query:
    l: int
    r: int
    x: int
    idx: int

@dataclass
class ArrayElement:
    val: int
    idx: int

# bool function to sort queries according to k
def cmp1(q1: Query, q2: Query):
    return q1.x < q2.x

# bool function to sort array according to its value
def cmp2(x: ArrayElement, y: ArrayElement):
    return x.val < y.val

# updating the bit array
def update(bit: List[int], idx:int, val:int, n:int):
    for idx in range(n): # for (; idx<=n; idx +=idx&-idx)
        bit[idx] +=val   # bit[idx] += val;

# querying the bit array
def query(bit:List[int], idx:int, n:int):
    sum = 0
    for i in range(0,idx):  # for (; idx > 0; idx -= idx&-idx)
        sum +=bit[idx] # sum += bit[idx];
    return sum

def answerQueries(n:int, queries: List[Query], q:int,arr: List[ArrayElement]):
    # initialising bit array
    bit=[None] * (n+1)
    memset(bit, 0, len(bit))

    # sorting the array
    sort(arr, arr+n,cmp2)

    # sorting queries
    sort(queries, queries +q, cmp1)

    # current index of aray
    curr = 0

    # array to hold answer of each query
    ans =[None] * q

    # Looping through each query
    for i in range(0,q):
        # traversing the array value till it is less than equal to Query number
        while(arr[curr].val <= queries[i].x and curr < n):
            # updating the bit array for the array index
            update(bit, arr[curr].idx+1, 1, n)
            curr +=1

        # Answer for each Query will be number of values less than equal to x upto r minus
        # number of values less than equal to x upto l-1
        ans[queries[i].idx] = query(bit, queries[i].r+1,n) -query(bit,queries[i].l,n)

        # printing answer for each Query
        for i in range(0, q):
            print(ans[i])


if __name__=='__main__':

    # size of array
    n =4

    # initialising array value and index -   ArrayElement arr[n];
    arr =[0] *n

    arr[0].val = 2
    arr[0].idx = 0
    arr[1].val = 3
    arr[1].idx = 1
    arr[2].val = 4
    arr[2].idx = 2
    arr[3].val = 5
    arr[3].idx = 3
 
    # number of queries
    q =2

    queries = [0] * q #   Query queries[q];

    queries[0].l = 0
    queries[0].r = 2
    queries[0].x = 2
    queries[0].idx = 0
    queries[1].l = 0
    queries[1].r = 3
    queries[1].x = 5
    queries[1].idx = 1
 
    answerQueries(n, queries, q, arr);
 
    # return 0;



# expected output - 1 , 4

# p = Query(10,15,5,1)
# p1 = Query(10,15,12,1)
# print("do these data classes work: ",cmp1(p,p1))



'''
my tests

'''
def my_tests(arr,Q):
    l,r,n =Q
    arr =arr[l:r+1]
    count = 0
    for i in arr:
        if i <= n:
            count +=1
    return count

print("expected: 4, actual: ", my_tests([2,3,4,5], [0,3,5]))
print("expected: 1, actual: ", my_tests([2,3,4,5], [0,2,2]))