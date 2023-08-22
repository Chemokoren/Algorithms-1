"""
Minimum swaps required to bring all elements less than or equal to k together

Given an array of n positive integers and a number k. Find the minimum number of swaps required to bring all
numbers less than or equal to k together.


Input:  arr[] = {2, 1, 5, 6, 3}, k = 3
Output: 1

Explanation: 
To bring elements 2, 1, 3 together, swap 
element '5' with '3' such that final array
will be-
arr[] = {2, 1, 3, 6, 5}

Input:  arr[] = {2, 7, 9, 5, 8, 7, 4}, k = 5
Output: 2

A simple solution is to first count all elements less than or equals to k(say'good'). Now traverse for
every sub-array and swap those elements whose value is greater than k. 
The Time complexity of this approach is O(n^2)
An efficient approach is to use two ponter technique and sliding window. Time complexity of this approach
is O(n)

1. Find count of all elements which are less than or equals to 'k'. Let's say the count is 'cnt'
2. Using two pointer technique for window of length 'cnt', each time keep track of how many elements in 
this range are greater than 'k'. Let's say the total count is 'bad'.
3. Repeat step 2, for every window of length 'cnt' and take minimum of count 'bad' among them. This will 
be the final answer.


"""
# program to find minimum swaps required to club all elements less than or equals to k together

# Utility function to find minimum swaps required to club all elements less than or equals to k together

def minSwap(arr, n, k):

    # find count of elements which are less than or equals to k
    count =0
    for i in range(0,n):
        if(arr[i] <=k):
            count = count +1

    # find unwanted elements in current window of size 'count'
    bad = 0
    for i in range(0, count):
        if(arr[i] > k):
            bad = bad +1

    # Initialize answer with 'bad' value of current window
    ans = bad
    j = count
    for i in range(0, n):
        if(j == n):
            break

        # Decrement count of previous window
        if(arr[i] > k):
            bad = bad - 1

        # Increment count of current window
        if(arr[j] > k):
            bad = bad + 1

        # update ans if count of 'bad' is less in current window
        ans = min(ans, bad)

        j = j + 1
    return ans

arr = [2, 1, 5, 6, 3]
n = len(arr)
k = 3
print("expected 1, actual:", minSwap(arr, n, k))
 
arr1 = [2, 7, 9, 5, 8, 7, 4]
n = len(arr1)
k = 5
print ("expected 2, actual:", minSwap(arr1, n, k))