"""
K maximum sums of overlapping contiguous sub-arrays

Given an array of Integers and an Integer value k, find out k sub-arrays(may be overlapping),
which have k maximum sums.

Examples:

Input : arr = {4, -8, 9, -4, 1, -8, -1, 6}, k = 4
Output : 9 6 6 5

Input : arr = {-2, -3, 4, -1, -2, 1, 5, -3}, k= 3
Output : 7 6 5

Using Kadane's Algorithm, we can find the maximum contiguous subarray sum of an array.
But in this case Kadane's algorithm does not work. As whenever we hit a negative 
number in the array we set the max_ending_here variable to zero,
hence we miss the possibilities for second and so on maximums.


Approach 1:

computes the maximum sub-array-sum problem in O(n) time and k maximum sub-array sum 
problem in O(k * n) time

First, we look at the problem of only maximum sub-array sum using this approach

prerequisites:

- Prefix sum array
- Maximum subarray sum in O(n) using prefix sum

Method for k-maximum sub-arrays:

1) calculate the prefix sum of the input array.
2) take cand, maxi and mini as arrays of size k.
4) for each value of the prefix_sum[i] do
    i) update cand[j] value by prefix_sum[i] - mini[j]
    ii) maxi will be the maximum k elements of maxi and cand
    iii) If prefix_sum is less than all values of mini, then include it in mini and remove
    the maximum element from mini

# After the ith iteration mini holds k minimum prefix sum upto
# index i and maxi holds k maximum overlapping sub-array sums upto index i
5) return maxi


Time Complexity: The ‘insertMini’ and ‘maxMerge’ functions runs in O(k) time and it takes 
O(k) time to update the ‘cand’ array. We do this process for n times. Hence, the overall 
time complexity is O(k*n).

"""

# Throught this calculation method, we keep maxi in non-increasing and mini in non-decreasing
# order

# program to find out k maximum sum of overlapping sub-arrays

# Function to compute prefix-sum of the input array
def prefix_sum(arr, n):
    pre_sum = list()
    pre_sum.append(arr[0])
    for i in range(1, n):
        pre_sum.append(pre_sum[i-1]+arr[i])

    return pre_sum


# update maxi by k maximum values from maxi and cand
def maxMerge(maxi, cand):
    # Here cand and maxi arrays are in non-increasing order beforehand. Now, j is the 
    # index of the next cand element and i is the index of next maxi element. Traverse through
    # maxi array.
    # If cand[j] > maxi[i] insert cand[j] at the ith position in the maxi array and remove
    # the minimum element of the maxi array i.e. the last element and increase j by 1 i.e. take
    # the next element from cand .
    k = len(maxi)
    j = 0 
    for i in range(k):
        if(cand[j] > maxi[i]):
            maxi.insert(i, cand[j])
            del maxi[-1]
            j += 1

# Insert prefix_sum[i] to mini array if needed
def insertMini(mini, pre_sum):
    # Traverse the mini array from left to right. If prefix_sum[i] is less than any element 
    # then insert prefix_sum[i] at that position and delete maximum element of the mini array
    # i.e. the rightmost element from the array.
    k =len(mini)
    for i in range(k):
        if(pre_sum < mini[i]):
            mini.insert(i, pre_sum)
            del mini[-1]
            break

# Function to compute k maximum overlapping sub-array sums
def kMaxOvSubArray(arr, k):
    n =len(arr)
    
    # compute the prefix sum of the input array.
    pre_sum = prefix_sum(arr, n)

    # Set all the elements of mini as + infinite except 0th. Set the 0th element as 0
    mini = [float('inf') for i in range(k)]
    mini[0] = 0

    # Set all the elements of maxi as - infinite.
    maxi =[-float('inf') for  i in range(k)]

    # Initialize cand array.
    cand =[0 for i in range(k)]

    # For each element of the prefix_sum array do:
    # compute the cand array.
    # take k maximum values from maxi and cand using maxmerge function.
    # insert prefix_sum[i] to mini array if needed using insertMini function

    for i in range(n):
        for j in range(k):
            cand[j] = pre_sum[i] -mini[j]
        maxMerge(maxi, cand)
        insertMini(mini, pre_sum[i])

    # Elements of maxi array is the k maximum overlapping sub-array sums. 
    # Print out the elements of maxi array
    for ele in maxi:
        print(ele, end=' ')
    print()

arr1 = [4, -8, 9, -4, 1, -8, -1, 6]
k1 = 4
kMaxOvSubArray(arr1, k1)
  
# Test case 2
arr2 = [-2, -3, 4, -1, -2, 1, 5, -3]
k2 = 3
kMaxOvSubArray(arr2, k2) 


