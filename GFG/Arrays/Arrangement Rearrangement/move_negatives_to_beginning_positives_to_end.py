"""
move all negative numbers to beginning and positive to end with constant extra space

nput: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5

Note: Order of elements is not important here

Approach 1:
Apply the partition process of quicksort

Time complexity: O(N) 
Auxiliary Space: O(1)

"""

def rearrange(arr):
    n = len(arr)
    j = 0
    for i in range(n):
    	if(arr[i] < 0):
            temp =arr[i]
            arr[i] =arr[j]
            arr[j] =temp
            j = j+1
    return arr

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
rearrange(arr)

"""
Two Pointer Approach:

The idea is to solve this problem with constant space and linear time using a two-pointer 
or two variable approach where we simply take two variables like left and right which
hold the 0 and N-1 indexes. 

check that:
- If the left and right pointer elements are negative then simply increment left pointer
- Otherwise, if the left element is positive and right element is negative then simply swap
   the elements, and simultaneously increment and decrement the left and right pointers.
- Else if the left element is positive and right element is also positive then simply
decrement the right pointer.
- Repeat the above steps until left pointer <= right pointer


This is an in-place rearranging algorithm for arranging the positive and negative numbers 
where the order of elements is not maintained.

Time Complexity: O(N)
Auxiliary Space: O(1)

The problem becomes difficult if we need to maintain the order of elements. 
Please refer to Rearrange positive and negative numbers with constant extra space for details.
"""

# function to shift all the negative elements to the left of the array
def shiftall(arr,left, right):
    
    # Loop to iterate while the left pointer is less than the right pointer
    while left <= right:
        # condition to check if the left and right pointer are negative
        if arr[left] < 0 and arr[right] < 0:
            left += 1

        # condition to check if the left pointer element is positive and the right pointer
        # element is negative
        elif arr[left] > 0 and arr[right] < 0:
            arr[left], arr[right] =arr[right], arr[left]
            left += 1
            right -=1
        
        # condition to check if the left pointer is positive and right pointer as well
        elif arr[left] > 0 and arr[right] > 0:
            right -=1
        else:
            left +=1
            right -=1

def display(arr):
  for i in range(len(arr)):
    print(arr[i], end=" ")
  print()
 
# Driver Code
if __name__ == "__main__":
  arr=[-12, 11, -13, -5, 6, -7, 5, -3, 11]
  n=len(arr)
  shiftall(arr,0,n-1)
  display(arr)

'''
Two pointer approach 2
'''
def move_negatives(arr):
	i =0
	j = len(arr)-1
	
	while i < j:
		if arr[i] <0 and arr[j]>0:
			i =i +1
			j =j -1
		elif arr[i] < 0 and arr[j] <0:
			i =i +1
		elif arr[i] > 0 and arr[j] > 0:
			j = j-1
		elif arr[i] > 0 and arr[j] < 0:
			arr[i],arr[j] =arr[j], arr[i]
			i +=1
			j =j-1
	return arr

	

    		
	
print("\n########################## move_negatives ##########################\n")
print("expected:,actual:[-12 -13 -5 -7 -3 -6 11 6 5]",move_negatives([-12, 11, -13, -5, 6, -7, 5, -3, -6]))
			

print("\n Approach 1: Modified Insertion Sort \n")

"""
Given an array of positive and negative numbers, arrange them such that all negative integers
appear before all the positive integers in the array without using any additional 
data structure like hash table, arrays, etc. The order of appearance should be maintained.

Examples:  

Input:  [12 11 -13 -5 6 -7 5 -3 -6]
Output: [-13 -5 -7 -3 -6 12 11 6 5]

A simple solution is to use another array. We copy all elements of original array to
new array. We then traverse the new array and copy all negative and positive elements back
in original array one by one. The problem with this approach is that it uses auxiliary array
and we're not allowed to use any data structure to solve this problem.

One approach that does not use any data structure is to use partition processs of Quicksort.
The idea is to consider 0 as pivot and divide the array arround it. The problem with this
approach is that it changes relative order of elements. 

Below are the methods which do not use any other data structure and also preverses relative
order of elements

Approach 1: Modified Insertion Sort
We can modify insertion sort to solve this problem.
Loop from i = 1 to n-1.
    a) If the current element is positive do nothing.
    b) If the current element arr[i] is negative, we
    insert it into sequence arr[0..i-1] such that all positive elements in arr[0..i-1]
    are shifted one position to their right and arr[i] is inserted at index of first 
    positive element.

Time complexity of above solution is O(n2) and auxiliary space is O(1). 
We have maintained the order of appearance and have not used any other data structure

"""

# utility function to print an array of size n
def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

# function to rearrange positive and negative numbers in a array
def RearrangePosNeg(arr, n):
    for i in range(1, n):
        key = arr[i]

        # if current element is positive do nothing
        if( key > 0):
            continue

        ''' If current element is negative, shift positive elements of arr[0 ..i-1],
            to one position to their right
        '''
        j = i - 1
        while(j >=0 and arr[j]> 0):
            arr[j + 1] = arr[j]
            j = j-1

        # Put negative element at its right position
        arr[j + 1] =key

if __name__=="__main__":
    
    arr = [ -12, 11, -13, -5, 6, -7, 5, -3, -6 ]
    n = len(arr)
 
    RearrangePosNeg(arr, n)
    printArray(arr, n)


print("\n Approach 2: Optimized Merge Sort\n")
"""
Approach 2: Optimized Merge Sort

Merge method of standard merge sort algorithm cab be modified to solve this problem. 
While merging two sorted halves say left and right, we need to merge in such a way that 
negative part of left and right sub-array is copied first followed by positive part of left
and right sub-array.

The time complexity of above solution is O(n log n). The problem with this approach 
is we are using auxiliary array for merging but we’re not allowed to use any data structure
to solve this problem.

"""

# Function to pran array
def printArray(A, size):
 
    for i in range(size):
        print(A[i], end = " ")
    print()
 
# Merges two subarrays of arr[], First subarray is arr[l..m], Second subarray is arr[m + 1..r]
def merge(arr, l, m, r):
    i, j, k = 0, 0, 0
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays */
    L = [arr[l + i] for i in range(n1)]
    R = [arr[m + 1 + j] for j in range(n2)]
 
    # Merge the temp arrays back into arr[l..r]*/
    i = 0 # Initial index of first subarray
    j = 0 # Initial index of second subarray
    k = l # Initial index of merged subarray
 
    # Note the order of appearance of elements should be maintained - we copy elements
    # of left subarray first followed by that of right subarray
 
    # copy negative elements of left subarray
    while (i < n1 and L[i] < 0):
        arr[k] = L[i]
        k += 1
        i += 1
 
    # copy negative elements of right subarray
    while (j < n2 and R[j] < 0):
        arr[k] = R[j]
        k += 1
        j += 1
 
    # copy positive elements of left subarray
    while (i < n1):
        arr[k] = L[i]
        k += 1
        i += 1
 
    # copy positive elements of right subarray
    while (j < n2):
        arr[k] = R[j]
        k += 1
        j += 1

# Function to Rearrange positive and negative numbers in a array
def RearrangePosNeg(arr, l, r):

    if(l < r):
        # same as (l + r) / 2, but avoids overflow for large l and h
        m = l + (r - l) // 2

        # sort first and second halves
        RearrangePosNeg(arr, l, m)
        RearrangePosNeg(arr, m+1, r)

        merge(arr, l, m, r)

    
arr = [ -12, 11, -13, -5, 6, -7, 5, -3, -6 ]
arr_size = len(arr)
 
RearrangePosNeg(arr, 0, arr_size - 1)
 
printArray(arr, arr_size)

"""
Let Ln and Lp denotes the negative part and positive part of left sub-array respectively. 

Similarly, Rn and Rp denote the negative and positive part of right sub-array respectively. 

Below are the steps to convert [Ln Lp Rn Rp] to [Ln Rn Lp Rp] without using extra space. 

1. Reverse Lp and Rn. We get [Lp] -> [Lp'] and [Rn] -> [Rn'] 
    [Ln Lp Rn Rp] -> [Ln Lp’ Rn’ Rp]

2. Reverse [Lp’ Rn’]. We get [Rn Lp].
    [Ln Lp’ Rn’ Rp] -> [Ln Rn Lp Rp]

The time complexity: O(n log n),
space complexity:  O(Log n) space for recursive calls, 

No additional data structure.
"""

def printArray(A, size):
    for i in range(0,size):
        print(A[i], end=" ")
    print()


# Function to reverse an array. An array can be reversed in O(n) time and O(1) space.
def reverse(arr, l, r):
 
    if l < r:
     
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l + 1, r - 1
        reverse(arr, l, r)
    
# Merges two subarrays of arr[], first subarray is arr[l..m], second subarray is arr[m + 1..r]
def merge(arr, l, m, r):
 
    i = l # Initial index of 1st subarray
    j = m + 1 # Initial index of 2nd subarray
 
    while i <= m and arr[i] < 0:
        i += 1
 
    # arr[i..m] is positive
 
    while j <= r and arr[j] < 0:
        j += 1
 
    # arr[j..r] is positive
 
    # reverse positive part of left sub-array (arr[i..m])
    reverse(arr, i, m)
 
    # reverse negative part of right sub-array (arr[m + 1..j-1])
    reverse(arr, m + 1, j - 1)
 
    # reverse arr[i..j-1]
    reverse(arr, i, j - 1)
 

# Function to Rearrange positive & negative numbers in a array
def RearrangePosNeg(arr, l, r):
 
    if l < r:
     
        # Same as (l + r)/2, but avoids overflow for large l and h
        m = l + (r - l) // 2
 
        # Sort first and second halves
        RearrangePosNeg(arr, l, m)
        RearrangePosNeg(arr, m + 1, r)
 
        merge(arr, l, m, r)

if __name__ == "__main__":
 
    arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    arr_size = len(arr)
 
    RearrangePosNeg(arr, 0, arr_size - 1)
 
    printArray(arr, arr_size)


print("\n Approach 4: Using Two Pointer Algorithm: \n")

"""
Approach 4: Using Two Pointer Algorithm

"""

def RearrangePosNeg(arr, n):
    i = 0
    j = n-1

    while(True):
        # Loop until arr[i] < 0 and  still inside the array
        while(i < n and arr[i] < 0):
            i += 1

        # Loop until arr[j] > 0 and still inside the array
        while (j >=0 and arr[j]> 0):
            j -= 1

        # if i is less than j
        if (i < j):
            arr[i],arr[j] = arr[j], arr[i]

        else:
            break

arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
n = len(arr)
RearrangePosNeg(arr, n)
print(*arr)
 

# O(n) time complexity & O(1) space complexity
def move_negatives1(arr):
	i =0
	j =0
	k =len(arr)-1
	while j<len(arr)-1:
		if(arr[j] < 0):
			arr[i] =arr[j]
			i +=1
		else:
			if(arr[k] < 0):
				arr[k],arr[j] =arr[j],arr[k]
				k =k-1
				j =j+1
		j =j+1
	
	return arr
	
'''
sorting the elements
'''
# O(n*log(n)) time complexity & O(1) space complexity
def move_negatives2(arr):
	arr.sort(reverse=False)
	return arr

'''
Here we will use the famous Ductch National FlagAlgorithm for two "colors". The first color will be for all
negative integers and the second color will be for all positive integers. We will divide the array into 
three partitions with the help of two pointers, low and high.

1. ar[1...low-1] negative integers
2. ar[low...high] unknown
3. ar[high+1...N] positive integers

Now, we explore the array with the help of low pointer, shrinking the unknown partition, and moving
elements to their correct partition in the process. We do this until we have explored all the elements,
and size of the unknown partition shrinks to zero.

'''
def reArrangeDutch(arr):
    n = len(arr)
    low, high = 0, n-1
    while(low < high):
        if(arr[low] < 0):
            low +=1
        elif(arr[high]>0):
            high -=1
        else:
            arr[low],arr[high]=arr[high],arr[low]
    return arr

arr = [1, 2,  -4, -5, 2, -7, 3, 2, -6, -8, -9, 3, 2,  1]

print("##################################### Dutch National FlagAlgorithm #####################################")
print(reArrangeDutch(arr))