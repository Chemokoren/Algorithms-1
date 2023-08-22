"""
Maximum sum of i*arr[i] among all
rotations of a given array

Given an array arr[] of n integers, find the maximum that maximizes
the sum of the value of i*arr[i] where i varies from 0 to n-1.

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

Method 1: This method discusses the Naive Solution which takes O(n2) amount of time. 
The solution involves finding the sum of all the elements of the array in each rotation
and then deciding the maximum summation value. 

Approach:A simple solution is to try all possible rotations. 
Compute sum of i*arr[i] for every rotation and return maximum sum.

Algorithm:
Rotate the array for all values from 0 to n.
Calculate the sum for each rotations.
Check if the maximum sum is greater than the current sum then update the maximum sum.

Time Complexity : O(n2)
Auxiliary Space : O(1)

"""

# program to find maximum sum rotation
import sys

# Returns maximum value of i*arr[i]
def maxSum(arr, n):
    # Initialize result
    res =-sys.maxsize

    # consider rotation beginning with i for all possible values of i
    for i in range(0,n):

        # Initialize sum of current rotation
        curr_sum = 0

        # Compute sum of all values. We don't acurately rotate the array, but compute
        # sum by finding indexes when arr[i] is first element

        for j in range(0, n):
            index =int((i+j)% n)
            curr_sum += j * arr[index]

        # update result if required
        res =max(res, curr_sum)
    return res

arr = [8, 3, 1, 2]
n = len(arr)
 
print(maxSum(arr, n))


"""
Method 2: This method discusses the efficient solution which solves the problem in 
O(n) time. In the naive solution, the values were calculated for every rotation. 
So if that can be done in constant time then the complexity will decrease.



Approach: The basic approach is to calculate the sum of new rotation from the 
previous rotations. This brings up a similarity where only the multipliers of 
first and last element change drastically and the multiplier of every other 
element increases or decreases by 1. 
So in this way, the sum of next rotation can be calculated from the sum of present rotation.

Algorithm: 

The idea is to compute the value of a rotation using values of previous rotation.
When an array is rotated by one, following changes happen in sum of i*arr[i]. 
Multiplier of arr[i-1] changes from 0 to n-1, i.e., arr[i-1] * (n-1) is added to current value.
Multipliers of other terms is decremented by 1. i.e., (cum_sum – arr[i-1]) is subtracted
from current value where cum_sum is sum of all numbers.
next_val = curr_val - (cum_sum - arr[i-1]) + arr[i-1] * (n-1);

next_val = Value of ∑i*arr[i] after one rotation.
curr_val = Current value of ∑i*arr[i] 
cum_sum = Sum of all array elements, i.e., ∑arr[i].

Lets take example {1, 2, 3}. Current value is 1*0+2*1+3*2= 8. 
Shifting it by one will make it {2, 3, 1} and next value
will be 8 - (6 - 1) + 1*2 = 5 which is same as 2*0 + 3*1 + 1*2

Time Complexity: O(n). 
Since one loop is needed from 0 to n to check all rotations and the sum of the present rotation is calculated from the previous rotations in O(1) time).
Auxiliary Space: O(1). 
As no extra space is required so the space complexity will be O(1)

"""

# program to compute maximum sum of i*arr[i]

def maxSum(arr, n):

    # compute sum of all array elements
    cum_sum =0

    for i in range(0,n):
        cum_sum +=arr[i]

    # Compute sum of i * arr[i] for initial configuration
    curr_val =0

    for i in range(0,n):
        curr_val +=i*arr[i]

    # Initialize result
    res = curr_val

    # Compute values for other iterations
    for i in range(1, n):
        
        # compute next value using previous value in O(1) time
        next_val =(curr_val - (cum_sum -arr[i-1])+arr[i-1]*(n-1))

        # update current value
        curr_val =next_val

        # update result if required
        res =max(res, next_val)

    return res

arr = [8, 3, 1, 2]
n = len(arr)
 
print(maxSum(arr, n))


"""
Method 3: The method discusses the solution using pivot in O(n) time. 
The pivot method can only be used in the case of a sorted or a rotated sorted array.
For example: {1, 2, 3, 4} or {2, 3, 4, 1}, {3, 4, 1, 2} etc.

Approach: Let’s assume the case of a sorted array. As we know for an array the maximum sum
will be when the array is sorted in ascending order.
In case of a sorted rotated array, we can rotate the array to make it in ascending order.
So, in this case, the pivot element is needed to be found following which the maximum sum 
can be calculated.

Algorithm: 
Find the pivot of the array: if arr[i] > arr[(i+1)%n] then it is the pivot element. 
(i+1)%n is used to check for the last and first element.
After getting pivot the sum can be calculated by finding the difference with the pivot
which will be the multiplier and multiply it with the current element while 
calculating the sum


Time Complexity : O(n) 
As only one loop was needed to traverse from 0 to n to find the pivot.
To find the sum another loop was needed, so the complexity remains O(n).
Auxiliary Space : O(1). 
We do not require extra space to so the Auxiliary space is O(1)

"""
    
# program to find maximum sum of all rotation of i*arr[i] using pivot

def maxSum(arr, n):
    
    sum = 0
    pivot =findPivot(arr,n)

    # difference in pivot and index of last element of array
    diff =n -1 - pivot
    for i in range(n):
        sum = sum +((i + diff) % n) * arr[i]

    return sum


# function to find pivot
def findPivot(arr, n):
    for i in range(n):
        if(arr[i] > arr[(i + 1) % n]):
            return i

if __name__ == "__main__" :
 
    # rotated input array
    arr = [8, 3, 1, 2]
    n= len(arr)
     
    max= maxSum(arr, n)
    print(max)