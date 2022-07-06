"""
Constant time range add operation on an array

Given an array of size N which is initialized with all zeros. We are given many ranges
add queries, which should be applied to this array. We need to print the final updated 
array as our result.

Examples: 

N = 6
Arr = [0, 0, 0, 0, 0, 0]
rangeUpdate1 [0, 2], add 100
Arr = [100, 100, 100, 0, 0, 0]
rangeUpdate1 [1, 5], add 100
Arr = [100, 200, 200, 100, 100, 100]
rangeUpdate1 [2, 3], add 100
Arr = [100, 200, 300, 200, 100, 100]
Which is the final updated array.

This problem can be solved using segment tree with lazy updates in O(log N) time per
query but we can do better here, as update operation is not given. 
We can process each query in constant time using this logic when a query to add V is 
given in range [a, b] we will add V to arr[a] and –V to arr[b+1] now if we want to get 
the actual values of the array we will convert the above array into prefix sum array.

Arr = [0, 0, 0, 0, 0, 0]

rangeUpdate1 [0, 2], add 100
Arr = [100, 0, 0, -100, 0, 0]

rangeUpdate1 [1, 5], add 100. 
Arr = [100, 100, 0, -100, 0, 0]
Note: You can not add -100 at 6th index because array length is 6.

rangeUpdate1 [2, 3], add 100
Arr = [100, 100, 100, -100, -100, 0]    

Now we will convert above operation array to prefix sum array as shown below,
Arr = [100, 200, 300, 200, 100, 100]

Which is the final updated array.

So in effect, when we add a value V to specific index of the array, It represents adding V
to all elements right to this index, that is why we add –V after range to remove its 
effect after its range of add query. 
Please note in below code, if range spans till the last index, the addition of –V is 
omitted to be in memory limit of the array. 

Time Complexity: O(n) 
Auxiliary Space: O(1)

"""

# program to get updated array after many array range add operation

# Utility method to add value val, to range [lo, hi]
def add(arr,N, lo, hi, val):

    arr[lo] += val
    if(hi != N-1):
        arr[hi + 1] -= val

# Utility method to get actual array from operation array
def updateArray(arr, N):
    # convert array into prefix sum array
    for i in range(1, N):
        arr[i] += arr[i -1]

# method to print final updated array
def printArr(arr, N):
    updateArray(arr, N)
    for i in range(N):
        print(arr[i], end=" ")
    print()

N = 6
arr =[0 for i in range(N)]

# Range add Queries
add(arr,N, 0, 2, 100)
add(arr,N, 1, 5, 100)
add(arr,N, 2, 3, 100)

printArr(arr, N)




'''
my tests
'''

def rangeUpdate(arr, Q, val):
    l, r = Q
    for i in range(l, r+1):
        arr[i] += val
    return arr

N = 6
arr =[0 for i in range(N)]
print("expected:[100, 100, 100, 0, 0, 0], actual: ", rangeUpdate(arr,[0, 2], 100))
print("expected:[100, 200, 200, 100, 100, 100], actual: ", rangeUpdate(arr,[1, 5], 100))
print("expected:[100, 200, 300, 200, 100, 100], actual: ", rangeUpdate(arr,[2, 3], 100))