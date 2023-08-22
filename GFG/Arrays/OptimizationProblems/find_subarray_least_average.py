"""
Find the subarray with least average

Given an array arr[] of size n and integer k such that k <=n

Examples:

Input:  arr[] = {3, 7, 90, 20, 10, 50, 40}, k = 3
Output: Subarray between indexes 3 and 5

The subarray {20, 10, 50} has the least average 
among all subarrays of size 3.

Input:  arr[] = {3, 7, 5, 20, -10, 0, 12}, k = 2
Output: Subarray between [4, 5] has minimum average

A simple solution is to consider every element as beginning of subarray of size k and
compute sum of subarray starting with this element. Time complexity of this solution is
O(nk)

Time Complexity: O(n*k) where n is the size of array.
Auxiliary Space: O(1)

"""
# program to find minium average subarray
# Prints beginning and ending indexes of subarray of size k with minimum average
def findsubarrayleast(arr, k):
    min = 999999
    minindex  =0
    

    for i in range(len(arr)-k):
        sum = 0
        j =i
        for j in range(i, i+k):
            sum += arr[j]
        if sum < min :
            min = sum
            minindex =i

    return arr[minindex:minindex + k]


print("expected: [20, 10, 50], actual ", findsubarrayleast([3, 7, 90, 20, 10, 50, 40], 3))


"""
An Efficient solution is to solve the above problem in O(n) time and O(1) extra space. The
idea is to use sliding window of size k. Keep track of sum of current k elements. To
compute sum of current window, remove first element of previous window and add current
element(last element of current window)

1) Initialize res_index = 0 // Beginning of result index
2) Find sum of first k elements. Let this sum be 'curr_cum'
3) Initialize min_sum = sum
4) Iterate from (k+1)'th to n'th element, do the following for every element arr[i]
    a) curr_sum = curr_sum + arr[i] - arr[i-k]
    b) If curr_sum < min_sum
            res_index = (i - k+1)
5) Print res_index and res_index+k-1 as beginning and ending indexes of resultant 
subarray.

"""

# program to find minimum average  subarray
# Prints beginning and ending indexes of subarray of size k with minimum average
def findMinAvgSubarray(arr, k):
    n = len(arr)

    # k must be smaller than or equal to n
    if(n < k) : return 0

    # initialize beginning index of result
    res_index = 0

    # compute sum of first subarray of size k
    curr_sum = 0
    for i in range(k):
        curr_sum += arr[i]

    # Initialize minimum sum as current sum
    min_sum = curr_sum

    # Traverse from (k + 1) 'th element to n'th element
    for i in range(k, n):

        # Add current item and remove first item of previous subarray
        curr_sum += arr[i] -arr[i-k]

        # update result if needed
        if(curr_sum < min_sum):
            min_sum = curr_sum
            res_index =(i -k +1)
    return [res_index,(res_index + k - 1)]



print("Expected: [3, 5], actual: ", findMinAvgSubarray([3, 7, 90, 20, 10, 50, 40], 3))




print("\n my tests \n")
'''
my tests

'''
def my_tests(a, size):
    start = 0
    end = 0
    max_so_far = float("inf")
    i = 0
    j = 0

    while end < len(a)-1:
        end = start + size
        curr_average = sum(a[start:end]) / size
        if curr_average < max_so_far:
            max_so_far =curr_average
            i= start
            j= end
        start +=1
    return [i,j-1], a[i:j]

print("Expected: [3, 5], actual: ", my_tests([3, 7, 90, 20, 10, 50, 40], 3))
print("Expected: [4, 5], actual: ", my_tests([3, 7, 5, 20, -10, 0, 12], 2))

