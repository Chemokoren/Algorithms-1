"""
Queries on Left and Right Circular shift on array

Given an array A of N integers. There are three types of commands:

1: x - Right Circular shift array x times. If an array is a[0], a[1],..a[n-1],
        then after one right circular shift the array will vecome a[n-1], a[0], a[1],...,a[n-2]

2: y - Left Circular Shift the array y times. If an array is a[0], a[1], ..., a[n-1], then after
        one right circular shift they array will become a[1], ..., a[n-2], a[n-1],a[0]
3: lr -print the sum of all integers in the subarray a[l ... r] l and r are inclusive

Given Q queries, the task is execute each query.

Examples:

Input : n = 5, arr[] = { 1, 2, 3, 4, 5 }
        query 1 = { 1, 3 }
        query 2 = { 3, 0, 2 }
        query 3 = { 2, 1 }
        query 4 = { 3, 1, 4 }
Output : 12
         11

Initial array arr[] = { 1, 2, 3, 4, 5 }
After query 1, arr[] = { 3, 4, 5, 1, 2 }.
After query 2, sum from index 0 to index 
               2 is 12, so output 12.
After query 3, arr[] = { 4, 5, 1, 2, 3 }.
After query 4, sum from index 1 to index 
               4 is 11, so output 11.

Method 1: (Brute Force)
implement three function rotateR(arr, k) which will right rotate array arr by k times,
rotateL(arr, k) which will rotate array arr by k times, sum(arr,l,r) which will output
sum of array arr from index l to index r. On the input of value 1,2,3 call the appropriate
function.

Method 2: (Efficient Approach)
Initially, there are no rotations and we have many queries asking for sum of integers present 
in a range od indexes.
We can evaluate the prefix sum of all elements in the array, prefixsum[i] will denote the sum
of all the integers upto ith index.
Now, if we want to find sum of elements between two indexes i.e l and r, we compute it in 
constant time by just calculating prefixsum[r] -prefixsum[l-r].
Now for rotations, if we are rotating the array for every query, that will be highly
inefficient.
We just need to track the net rotation. If the tracked number is negative, it means
left rotation has dominated else right rotation has dominated. When we are tracking the 
net rotations, we need to do mod n. As after every n rotation, array will return to
its original state.
We need to observe it in sucn a way that every time we rotate the array, 
only its indexes are changing.
If we need to answer any query of third type and we have l and r. We need to find
what l and r were in the original order. We can easily find it out by adding the net 
rotations to the index and taking mod n.
Every command can be executed in O(1) time.

"""


# Program to solve queries on Left and Right Circular shift on array


# Function to solve query of type 1 x.
def querytype1(toRotate, times, n):
	# Decreasing the absolute rotation
	(toRotate) = ((toRotate) - times) % n


# Function to solve query of type 2 y.
def  querytype2(toRotate, times, n):
	#Increasing the absolute rotation.
	(toRotate) = ((toRotate) + times) % n


# Function to solve queries of type 3 l r.
def querytype3(toRotate, l, r,preSum,n):
    # Finding absolute l and r.
    l = (l + toRotate + n) % n
    r = (r + toRotate + n) % n
    
    # if l is before r.
    if (l <= r):
        print(preSum[r + 1] - preSum[l])
    # If r is before l.
    else:
        print(preSum[n] + preSum[r + 1] - preSum[l])

# Wrapper Function solve all queries.
def wrapper(a, n,preSum):
    preSum[n + 1]
    preSum[0] = 0
    
    # Finding Prefix sum
    for i in range(1, n):
        preSum[i] = preSum[i - 1] + a[i - 1]
    
    toRotate = 0
    
    # Solving each query
    querytype1(toRotate, 3, n)
    querytype3(toRotate, 0, 2, preSum, n)
    querytype2(toRotate, 1, n)
    querytype3(toRotate, 1, 4, preSum, n)

# Driver Program
if __name__=='__main__':
	a = { 1, 2, 3, 4, 5 }
	n = len(a) / list(a)[0]
	wrapper(a, n,0)
    # return 0
