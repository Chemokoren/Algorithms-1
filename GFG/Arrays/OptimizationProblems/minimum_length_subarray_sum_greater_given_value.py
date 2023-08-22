"""
Smallest subarray with sum greater than a given value

Given an array of integers and a number x, find the smallest subarray with sum greater 
than given value.

Examples:
arr[] = {1, 4, 45, 6, 0, 19}
   x  =  51
Output: 3
Minimum length subarray is {4, 45, 6}

arr[] = {1, 10, 5, 2, 7}
   x  = 9
Output: 1
Minimum length subarray is {10}

arr[] = {1, 11, 100, 1, 0, 200, 3, 2, 1, 250}
    x = 280
Output: 4
Minimum length subarray is {100, 1, 0, 200}

arr[] = {1, 2, 4}
    x = 8
Output : Not Possible
Whole array sum is smaller than 8.


A simple solution is to use two nested loops. The outer loop picks a starting element,
the inner loop considers all elements(on the right side of current start)as
ending element. Whenever sum of elements between current start and end becomes more than
the given number, update the result if current length is smaller than the smallest length 
so far.

Time Complexity: O(n2).
Auxiliary Space: O(1)

"""
# program to find smallest subarray with sum greater than a given value
# Returns length of smallest subaray with sum greater than x. If there is no subarray
#  with given sum, then returns n+1
def smallestSubWithSum(arr,x):

    n = len(arr)
 
    # Initialize length of smallest subarray as n+1
    min_len = n + 1
 
    # Pick every element as starting point
    for start in range(0,n):
     
        # Initialize sum starting with current start
        curr_sum = arr[start]
 
        # If first element itself is greater
        if (curr_sum > x):
            return 1
 
        # Try different ending points for current start
        for end in range(start+1,n):
         
            # add last element to current sum
            curr_sum += arr[end]
 
            # If sum becomes more than x and length of this subarray
            # is smaller than current smallest length, update the smallest
            # length (or result)
            if curr_sum > x and (end - start + 1) < min_len:
                min_len = (end - start + 1)
        

    # return min_len
    if min_len == n+1:
        return("Not Possible")
    else:
        return min_len


print("Expected:4, Actual:", smallestSubWithSum([1, 4, 45, 6, 10, 19], 51))
print("Expected:1, Actual:", smallestSubWithSum([1, 10, 5, 2, 7], 9))
print("Expected:4, Actual:", smallestSubWithSum([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280))


print("\n Efficient Solution \n")
"""
Efficient Solution

This problem can be solved in O(n) time using the idea used in this post. 

Time Complexity: O(n).
Auxiliary Space: O(1)

How to handle negative numbers? 

The above solution may not work if input array contains negative numbers. 
For example arr[] = {- 8, 1, 4, 2, -6}. To handle negative numbers, add a condition to 
ignore subarrays with negative sums. 
We can use the solution discussed in Find subarray with given sum with negatives allowed
in constant space 
(https://www.geeksforgeeks.org/find-subarray-with-given-sum-with-negatives-allowed-in-constant-space/)

"""
# O(n) solution for finding smallest subarray with sum greater than x
# Returns length of smallest subarray with sum greater than x. If there is no subarray
# with given sum, then returns n+1

def smallestSubWithSumOpt(arr,x):
    # Initialize current su and minimum length
    n = len(arr)
    curr_sum = 0
    min_len = n+1

    # Initialiaze starting and ending indexes
    start = 0
    end = 0

    while( end < n):

        # keep adding array elements while current sum is smaller than or equal to x
        while(curr_sum <=x and end < n):
            curr_sum += arr[end]
            end += 1

        # if current sum becomes greater than x
        while(curr_sum > x and start < n):

            # update minimum length if needed
            if(end - start < min_len):
                min_len = end -start

            # remove starting elements
            curr_sum -= arr[start]
            start += 1

    if (min_len == n + 1):
        return ("Not possible")
    else:
        return (min_len)


print("Expected: 3 ,Actual: ",smallestSubWithSumOpt([1, 4, 45, 6, 10, 19], 51))
print("Expected: 1 ,Actual: ",smallestSubWithSumOpt([1, 10, 5, 2, 7], 9))
print("Expected: 4 ,Actual: ",smallestSubWithSumOpt([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280))