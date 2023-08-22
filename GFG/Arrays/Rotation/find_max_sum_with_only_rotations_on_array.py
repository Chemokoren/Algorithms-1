"""
Find maximum value of Sum(i*arr[i]) with only rotations on given array allowed

Given an array, only rotation operation is allowed on array. We can rotate the array as many times as we want.
Return the maximum possible summation of i*arr[i].

Input: arr[] = {1, 20, 2, 10}
Output: 72
We can get 72 by rotating array twice.
{2, 10, 1, 20}
20*3 + 1*2 + 10*1 + 2*0 = 72

Input: arr[] = {10, 1, 2, 3, 4, 5, 6, 7, 8, 9}
Output: 330
We can get 330 by rotating array 9 times.
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
0*1 + 1*2 + 2*3 ... 9*10 = 330


A Simple Solution is to find all rotations one by one, check sum of every rotation 
and return the maximum sum. Time complexity of this solution is O(n^2). 

We can solve this problem in O(n) time using an Efficient Solution. 
Let Rj be value of i*arr[i] with j rotations. The idea is to calculate next 
rotation value from previous rotation, i.e., calculate Rj from Rj-1. 
We can calculate initial value of result as R0, then keep calculating next 
rotation values. 

How to efficiently calculate Rj from Rj-1? 

This can be done in O(1) time. Below are details.


Let us calculate initial value of i*arr[i] with no rotation

R0 = 0*arr[0] + 1*arr[1] +...+ (n-1)*arr[n-1]

After 1 rotation arr[n-1], becomes first element of array, arr[0] becomes second element, arr[1] becomes 
third element and so on.

R1 = 0*arr[n-1] + 1*arr[0] +...+ (n-1)*arr[n-2]

R1 - R0 = arr[0] + arr[1] + ... + arr[n-2] - (n-1)*arr[n-1]

After 2 rotations arr[n-2], becomes first element of array, 
arr[n-1] becomes second element, arr[0] becomes third element
and so on.
R2 = 0*arr[n-2] + 1*arr[n-1] +...+ (n-1)*arr[n-3]

R2 - R1 = arr[0] + arr[1] + ... + arr[n-3] - (n-1)*arr[n-2] + arr[n-1]

If we take a closer look at above values, we can observe below pattern

Rj - Rj-1 = arrSum - n * arr[n-j]

Where arrSum is sum of all array elements, i.e., 

arrSum = ∑ arr[i]
        0<=i<=n-1 

1) Compute sum of all array elements. Let this sum be 'arrSum'.

2) Compute R0 by doing i*arr[i] for given array. Let this value be currVal.

3) Initialize result: maxVal = currVal // maxVal is result.

// This loop computes Rj from  Rj-1 
4) Do following for j = 1 to n-1
......a) currVal = currVal + arrSum-n*arr[n-j];
......b) If (currVal > maxVal)
            maxVal = currVal   

5) Return maxVal

Time complexity: O(n)
Auxiliary space: O(1)

"""

# returns max possible value of Sum(i*arr[i])
def maxSum(arr):
    # stores sum of arr[i]
    arrSum =0

    # stores sum of i*arr[i]
    currVal =0

    n = len(arr)

    for i in range(0, n):
        arrSum =arrSum+arr[i]
        currVal =currVal + (i*arr[i])

    # initialize result
    maxVal =currVal

    # try all rotations one by one and find the maximum rotation sum
    for j in range(1,n):
        currVal =currVal + arrSum-n*arr[n-j]
        if currVal > maxVal:
            maxVal=currVal


    return maxVal

# arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [8, 3, 1, 2]
print("Max sum is: ", maxSum(arr))



'''
Given an array arr[] of n integers, find the maximum that maximizes the sum of the value of
i*arr[i] where i varies form 0 to n-1.

Examples: 

Input: arr[] = {8, 3, 1, 2}
Output: 29
Explanation: Lets look at all the rotations,
{8, 3, 1, 2} = 8*0 + 3*1 + 1*2 + 2*3 = 11
{3, 1, 2, 8} = 3*0 + 1*1 + 2*2 + 8*3 = 29
{1, 2, 8, 3} = 1*0 + 2*1 + 8*2 + 3*3 = 27
{2, 8, 3, 1} = 2*0 + 8*1 + 3*2 + 1*3 = 17

Input: arr[] = {3, 2, 1}
Output: 7
Explanation: Lets look at all the rotations,
{3, 2, 1} = 3*0 + 2*1 + 1*2 = 4
{2, 1, 3} = 2*0 + 1*1 + 3*2 = 7
{1, 3, 2} = 1*0 + 3*1 + 2*2 = 7


Naive solution: O(n^2)
----------------------

- The solution involves finding the sum of all the elements of the array in each rotation and then
deciding the maximum summation value.

Approach:

A simple solution is to try all possible rotations. Compute the sum of i*arr[i] for every rotation
return maximum sum.

Algorithm:
- Rotate the array for all values from 0 to n
- Calculate the sum of each rotations.
- Check if the maximum sum is greater than the current sum then update the maximum sum.

Time Complexity : O(n2)
Auxiliary Space : O(1)

'''

import sys

def maxSumNaive(arr):
    n =len(arr)

    # initialize result
    res =- sys.maxsize

    # Consider rotation beginning with i for all possible values of i.
    for i in range(0, n):

        # Initialize sum of current rotation

        curr_sum = 0

        # computer sum of all values. 
        for j in range(0,n):

            index = int((i + j) % n)
            curr_sum +=j * arr[index]

        # update result if need be
        res =max(res, curr_sum)
    return res

print("Naive Solution::")
# arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [8, 3, 1, 2]

print("Max sum is: ", maxSumNaive(arr))


'''

Method 2: Efficient solution

Approach:
---------
The basic approach is to calculate the sum of new rotation from the previous rotations. This brings 
up a similarity where only the multipliers of first and last element change drastically and 
the multiplier of every other element increases or decreases by 1. So in this way, the sum of next
rotation can be calculated from the sum of present rotation.

Algorithm:
The idea is to compute the value of a rotation using values of previous rotation. 
When an array is rotated by one, following changes happen in sum of i*arr[i].

1. Multiplier of arr[i-1] changes from 0 to n-1, i.e., arr[i-1] *(n-1) is added to current value.
2. Multipliers of other terms is decremented by 1 i.e., (cum_sum -arr[i-1]) is subtracted from 
current value where cum_sum is sum of all numbers.

next_val =curr_val -(cum_sum -arr[i-1]) + arr[i-1] * (n-1)

next_val = Value of sum(i*arr[i]) after one rotation.
curr_val = Current value of sum(i*arr[i])
cum_sum = of of all array elements, i.e., sum(arr[i])


Lets take example {1, 2, 3}. Current value is 1*0+2*1+3*2
= 8. Shifting it by one will make it {2, 3, 1} and next value
will be 8 - (6 - 1) + 1*2 = 5 which is same as 2*0 + 3*1 + 1*2

Time Complexity: O(n). 
Since one loop is needed from 0 to n to check all rotations and the sum of the present rotation is 
calculated from the previous rotations in O(1) time).

Auxiliary Space: O(1). 
As no extra space is required to so the space complexity will be O(1)

'''

def maxSumEfficient(arr, n):

    # compute sum of all array elements
    cum_sum = 0

    for i in range(0, n):
        cum_sum += arr[i]

    # compute sum of i * arr[i] for 
    # initial configuration.
    curr_val = 0

    for i in range(0, n):
        curr_val += i* arr[i]

    # initialize result
    res = curr_val

    # compute values for other iterations
    for i in range(1, n):

        # compute next value using previous value in O(1) time
        # value in O(1) time
        next_val =(curr_val - (cum_sum - arr[i-1]) + arr[i-1] * (n-1))

        # update current value
        curr_val = next_val

        # update result if required
        res =max(res, next_val)
    return res

print(" Efficient Code ")
arr = [8, 3, 1, 2]
n = len(arr)
 
print(maxSumEfficient(arr, n))

'''
Method 3: The method discusses the solution using pivot in O(n) time. The pivot method can 
only be used in the case of a sorted or a rotated array for example:
{1, 2, 3, 4} or {2, 3, 4, 1}, {3, 4, 1, 2}

Approach 
--------
Let's assume the case of a sorted array. As we know for an array the maximum sum will be
when the array is sorted in ascending order.
In case of a sorted rotated array, we can rotate the array to make it in ascending order. So, 
in this case, the pivot element is needed to be found following which the maximum sum can be 
calculated.

Algorithm:
1. Find the pivot of the array: if arr[i] > arr[i+1]%n then it is the pivot element. (i+1)%n is used 
to check for the last and first element.
2. After getting the pivot, the sum can be calculated by finding the difference with the pivot which
will be the multiplier and multiply it with the current element while calculating the sum.

Time Complexity : O(n) 
As only one loop was needed to traverse from 0 to n to find the pivot. To find the sum another loop was needed,
so the complexity remains O(n).

Auxiliary Space : O(1). 
We do not require extra space to so the Auxiliary space is O(1)


'''
print("maxSumUsingPivot")

# maximum sum of all rotation of i*arr[i] using the pivot.
def maxSumUsingPivot(arr, n):

    sum = 0
    pivot =findPivot(arr, n)
    
    # difference in pivot and index of last element of array
    diff = n- 1 - pivot
    for i in range(n):
        sum = sum +((i + diff) % n) * arr[i]
    return sum

# function to find pivot
def findPivot(arr, n):
    for i in range(n):
        if(arr[i] > arr[(i+1) % n]):
            return i

if __name__=='__main__':
    # rotated input array
    arr = [8, 3, 1, 2]
    n= len(arr)
     
    max= maxSumUsingPivot(arr, n)
    print(max)
