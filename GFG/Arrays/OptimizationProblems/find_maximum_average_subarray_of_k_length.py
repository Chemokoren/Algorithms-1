"""

Find maximum average subarray of k length

Given an array with positive and negative numbers, find the maximum average
subarray of the given length.

Input:  arr[] = {1, 12, -5, -6, 50, 3}, k = 4
Output: Maximum average subarray of length 4 begins
        at index 1.
Maximum average is (12 - 5 - 6 + 50)/4 = 51/4

A simple solution is to run two loops. The outer loop picks starting point, and the inner
loop goes to length 'k' from the starting point and computes the average of elements.

Time Complexity: O(n *k) as we are using nexted loops to traverse n*k times
Auxiliary Space: O(1), as we are not using any extra space.

A Better solution is to create an auxiliary array of size n. Store cumulative sum of
elements in this array. Let the array be csum[]. csum[i] stores sum of elements from arr[0]
to arr[i]. Once we have the csum[] array  with us, we can compute the sum between two 
indexes in O(1) time.

One observation is, that a subarray of a given length has a maximum average if it has
a maximum sum. So we can avoid floating-point arithmetic by just comparing sums.


Time Complexity: O(n), as we are using a loop to traverse n times. Where n is the number 
of elements in the array. Auxiliary Space: O(n), as we are using extra space for 
the array csum.

"""

# program to find maximum average subarray of given length.
# Returns beginning index of maximum average subarray of length 'k'
def findMaxAverage(arr,  k):
    n = len(arr)
    # check if 'k' is valid
    if k > n:
        return -1

    # Create and fill aarray to store cumulative sum. csum[i] stores sum of arr[0] 
    # to arr[i]
    csum =[0]*n
    csum[0] = arr[0]
    for i in range(1, n):
        csum[i] = csum[i-1] + arr[i]

    # Initialize max_sm as sum of first subarray
    max_sum = csum[k-1]
    max_end = k-1

    # Find sum of other subarrays and update max_sum if required.
    for i in range(k, n):
        curr_sum = csum[i] - csum[i-k]
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_end = i

    # Return starting index
    return max_end - k + 1

print("Expected:, Actual:",findMaxAverage([1, 12, -5, -6, 50, 3],4))

"""
Efficient Method. 

    Compute sum of first ‘k’ elements, i.e., elements arr[0..k-1]. Let this sum be ‘sum’.
    Initialize ‘max_sum’ as ‘sum’ 

    Do the following for every element arr[i] where i varies from ‘k’ to ‘n-1’ 
        Remove arr[i-k] from sum and add arr[i], i.e., do sum += arr[i] – arr[i-k] 
        If new sum becomes more than max_sum so far, update max_sum. 
    Return ‘max_sum’

Time Complexity: O(n), as we are using a loop to traverse n times. Where n is the number
of elements in the array.
Auxiliary Space: O(1), as we are not using any extra space.

"""

# program to find maximum average subarray of given length
# Returns beginning index of maximum average subarray of length 'k'
def findMaxAverage(arr, k):
    n = len(arr)
    # Check if 'k' is valid
    if(k > n):
        return -1

    # Compute sum of first 'k' elements
    sum = arr[0]

    for i in range(1, k):
        sum += arr[i]

    max_sum =sum
    max_end = k-1

    #compute sum of remaining subarrays
    for i in range(k,n):
        sum = sum + arr[i] - arr[i-k]

        if(sum > max_sum):
            max_sum = sum
            max_end =i
    # return starting index
    start_idx =max_end - k+1
    return [start_idx, max_end]


print("Expected :, Actual:",  findMaxAverage([1, 12, -5, -6, 50, 3], 4))

















print("\n my tests \n")
'''
my tests

'''
def my_tests(arr,k):

    max_val = -float('inf')
    start_idx =0
    end_idx =0

    for i in range(len(arr) - k):
        end = i+k

        sum_val =sum(arr[i:end])/k

        if sum_val > max_val:
            max_val = sum_val
            start_idx = i
            end_idx = end
    return max_val,(start_idx, end_idx)


print("Expected:, Actual: ", my_tests([1, 12, -5, -6, 50, 3], 4))

