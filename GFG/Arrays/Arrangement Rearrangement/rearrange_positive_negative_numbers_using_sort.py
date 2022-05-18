"""
Rearrange positive and negative numbers using inbuilt sort function

Given an array of positive and negative numbers, arrange them such that all 
negative integers appear before all the positive integers in the array without 
using any additional data structure like a hash table, arrays, etc.
The order of appearance should be maintained.
Examples:

Input :  arr[] = [12, 11, -13, -5, 6, -7, 5, -3, -6]
Output : arr[] = [-13, -5, -7, -3, -6, 12, 11, 6, 5]

Input :  arr[] = [-12, 11, 0, -5, 6, -7, 5, -3, -6]
Output : arr[] =  [-12, -5, -7, -3, -6, 0, 11, 6, 5]

approach 4:
we recursively traverse the array cutting it into two halves (array[start ..start] & 
array[(start+1)..end], and keep on splitting the arry till we reach the last element. Then
we starting merging it back. The idea is to, at any point, keep the array in the proper
sequence of negative and positive integers. The merging logic would be:
(I) if the array[start] is negative, merge the rest of the array as it is so that the
negative  number's order is maintained. The reason for this is that since we are tracing
back from the recursive calls, we start moving right to left through the array, thus,
naturally maintaining the original sequence.
(II) if the array[start] is positive, merge the rest of the array, but, after right-rotating
the half of the array[(start+1)..end]. The idea for the rotation is to merge the array so
that the positive array[start] is always merged with the positive elements. But, 
the only thing here is that the merged array will have all the positive elements on the left
and  negative elements on the right. So we reverse the sequence in each recursion to get back
the original sequence of negative elements and then positive elements subsequently.
It can be observed since we reverse the array while merging with a positive first element
in each recursion, so the sequence of positive elements, although coming
after the negative elements, are in reverse order. So, as a final step, we reverse only the 
positive half of the final array, and, subsequently getting the intended sequence.

array: [-12, -11, -13, -5, -6, 7, 5, 3, 6]
rearranged array: [-12, -11, -13, -5, -6, 7, 5, 3, 6]
 

Time complexity: O(N)

"""

def printArray(array, length):
    print("[", end ="")

    for i in range(length):
        print(array[i],end="")

        if(i< (length -1)):
            print(",", end=" ")

        else:
            print("]")

def reverse(array,start,end):
    while(start < end):
        temp =array[start]
        array[start] =array[end]
        array[end] = temp
        start += 1
        end -=1

# Rearrange the array with all negative integers on left and positive integers on right
# use recursion to split the array with first element as one half and the rest array as
# another and then merge it with head of the array in each step
def rearrange(array, start, end):
    # exit condition
    if(start == end):
        return
    
    # rearrange the array except the first element in each recursive call
    rearrange(array, (start+1), end)

    # if the first element of the array is positive, then right-rotate the array by 
    # one place first and then reverse the merged array.

    if(array[start] >=0):
        reverse(array, (start +1), end)
        reverse(array, start, end)

if __name__=='__main__':
    array =[12, 11, -13, -5, 6, -7, 5, -3, -6]
    length = len(array)
    countNegative = 0

    for i in range(length):
        if(array[i] < 0):
            countNegative += 1

    print("array: ", end=" ")
    printArray(array, length)
    rearrange(array, 0, (length-1))

    reverse(array, countNegative, (length - 1))

    print("reattanged array: ", end =" ")
    printArray(array, length)

"""
Approach 1: Modified Partition Process of Quick Sort

We can reverse the order of positive numbers whenever relative order is changed. This will happen if there
are more than one positive element between last negative number in left subarray and current 
negative element.

Current Array :- [Ln, P1, P2, P3, N1, .......]
Here, Ln is the left subarray(can be empty) that contains only negative elements. P1, P2, P3 are the positive numbers and N1
is the negative number that we want to move at correct place.
If difference of indices between positive number and negative number is greater than 1,
    1. Swap P1 and N1, we get [Ln, N1, P2, P3, P1, ......]
    2. Rotate array by one position to right, i.e. rotate array [P2, P3, P1], we get [Ln, N1, P1, P2, P3, ......]

"""
print("Approach 1: Modified Partition Process of Quick Sort")

# program for moving negative numbers to left while maintaining the order
class Solution:
    def rotateSubArray(self, arr, l, r):
        temp = arr[r]
        for j in range(r, l-1, -1):
            arr[j] = arr[j-1]
        arr[l] = temp

        return arr

    def moveNegative(self, arr):
        last_negative_index = -1

        for i in range(len(arr)):
            if arr[i] < 0:
                last_negative_index += 1
                arr[i], arr[last_negative_index] = arr[last_negative_index], arr[i]

                if i - last_negative_index >=2:
                    self.rotateSubArray(arr, last_negative_index+1, i)

        return arr
if __name__=='__main__':
    arr = [5, 5, -3, 4, -8, 0, -7, 3, -9, -3, 9, -2, 1]
    ob = Solution()
    ob.moveNegative(arr)
    for i in arr:
        print(i, end=' ')
    print()


"""
Approach 2: Modified Insertion Sort

We can modify insertion sort to solve this problem

Algorithm

Loop from i=1 to n-1
a) If the current element is positive, do nothing.
b) If the current element arr[i] is negative, we insert it into the sequence arr[0..i-1] such that all 
positive elements in arr[0..i-1] are shifted one position to their right and arr[i] is inserted at index of
first positive element.

Time complexity of above solution is O(n^2) and auxiliary space is O(1). We have maintained the order 
of appearance and have not used any other data structure.

Note: this method does not handle zeros

"""
# program to rearrange positive and negative numbers in a array

# A utility function to print an array of size n
def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

# function to rearrange positive and negative numbers in a array
def RearrangePosNeg(arr, n):

    for i in range(1, n):
        key = arr[i]

        # if current element is positive do nothing
        if(key > 0):
            continue
        '''
        if current element is negative, shift positive elements of arr[0..i-1], to one position to their
        right

        '''
        j = i -1
        while(j >= 0 and arr[j]>0):
            arr[j + 1] = arr[j]
            j = j-1
        # put negative element at its right position
        arr[j+1] = key

if __name__ == "__main__":
    arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    n = len(arr)
 
    RearrangePosNeg(arr, n)
    printArray(arr, n)

"""
Approach 3: Optimized Merge Sort

Merge method of standard merge sort algorithm can be modified to solve this problem. While merging two sorted
halves say left and right, we need to merge in such a way that the negative part of left and right sub-array
is copied first followed by positive part of left and right sub-array.

"""

# program to rearrange positive and negative numbers in a array
# Function to print an array
def printArray(A, size):
    for i in range(size):
        print(A[i], end=" ")
    print()

# Merge two subarrays of arr[].First subarray is arr[l..m]
# Second subarray is arr[m + 1 ..r]

def merge(arr, l, m, r):
    i, j, k = 0, 0, 0
    n1 = m - l +1
    n2 = r - m

    # create temp arrays
    L = [arr[l + i] for i in range(n1)]
    R = [arr[m + 1 + j] for j in range(n2)]

    # Merge the temp arrays back into arr[l..r]
    i = 0 # initial index of first subarray
    j = 0 # Initial index of second subarray
    k = l # Initial index of merged subarray

    # Note the order of appearance of elements
    # should be maintained - we copy elements
    # of left subarray first followed by that of right subarray

    # copy negative elements of left subarray
    while(i < n1 and L[i] < 0):
        arr[k] = L[i]
        k += 1
        i += 1

    # copy negative elements of right subarray
    while(j < n2 and R[j] < 0):
        arr[k] = R[j]
        k += 1
        j += 1

    # copy positive elements of left subarray
    while(i < n1):
        arr[k] = L[i]
        k += 1
        i += 1

    # copy positive elements of right subarray
    while(j < n2):
        arr[k] = R[j]
        k += 1
        j += 1

# Function to rearrange positive and negative numbers in a array
def RearrangePosNeg(arr, l, r):

    if(l < r):

        # same as (l + r) / 2, but avoids overflow for large l and h
        m = l +(r - l) // 2

        # Sort first and second halves
        RearrangePosNeg(arr, l, m)
        RearrangePosNeg(arr, m + 1, r)

        merge(arr, l, m, r)

arr = [0,-12, 11, -13, -5, 6, -7, 5, -3, -6]
arr_size = len(arr)
 
RearrangePosNeg(arr, 0, arr_size - 1)
 
printArray(arr, arr_size)

"""
The time complexity of above solution is O(n log n). The problem with this approach is we are using 
auxiliary array for merging but we’re not allowed to use any data structure to solve this problem. 
We can do merging in-place without using any data-structure. 
Let Ln and Lp denotes the negative part and positive part of left sub-array respectively. 
Similarly, Rn and Rp denote the negative and positive part of right sub-array respectively. 

Below are the steps to convert [Ln Lp Rn Rp] to [Ln Rn Lp Rp] without using extra space. 

1. Reverse Lp and Rn. We get [Lp] -> [Lp'] and [Rn] -> [Rn'] 
    [Ln Lp Rn Rp] -> [Ln Lp’ Rn’ Rp]

2. Reverse [Lp’ Rn’]. We get [Rn Lp].
    [Ln Lp’ Rn’ Rp] -> [Ln Rn Lp Rp]

The time complexity of above solution is O(n log n), O(Log n) space for recursive calls,
 and no additional data structure.

"""
# program to rearrange positive and negative numbers in an array

# function to print an array
def printArray(A, size):
 
    for i in range(0, size):
        print(A[i], end=" ")
    print()

# function to reverse an array. An array can be reversed in O(n) time and O(1) space.
def reverse(arr, l, r):
    if l< r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l + 1, r - 1
        reverse(arr, l, r)

# Merges two subarrays of arr[]. First subarray is arr[l..m]. Second subarray is arr[m+1..r]
def merge(arr, l, m, r):
    i = l # initial index of 1st subarray
    j = m +1 # Initial index of IInd

    while i <= m and arr[i] < 0:
        i += 1

    # arr[i..m] is positive
    while j <= r and arr[j] < 0:
        j += 1
    
    # arr[j..r] is positive
    # reverse positive part of left
    # sub-array (arr[i..m])
    reverse(arr, i, m)

    # reverse negative part of right
    # sub-array(arr[m +1 .. j-1])
    reverse(arr, m+1, j-1)

    # reverse arr[i..j-1]
    reverse(arr, i, j-1)

# Function to Rearrange positive and negative numbers in a array
def RearrangePosNeg(arr, l, r):
    if l < r:
        # same as (l + r) /2, but avoids overflow for large l and h
        m = l + (r-l) // 2

        # sort first and second halves
        RearrangePosNeg(arr, l, m)
        RearrangePosNeg(arr, m +1, r)

        merge(arr, l, m, r)

if __name__ == "__main__":
 
    arr = [0,-12, 11, -13, -5, 6, -7, 5, -3, -6]
    arr_size = len(arr)
 
    RearrangePosNeg(arr, 0, arr_size - 1)
 
    printArray(arr, arr_size)

