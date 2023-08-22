"""
Rearrange positive and negative numbers in O(n) time and O(1) extra space

An array contains both positive and negative numbers in random order. Rearrange the array 
elements so that positive and negative numbers are placed alternatively. Number of positive 
and negative numbers need not be equal. If there are more positive numbers they appear at 
the end of the array. If there are more negative numbers, they too appear in the end of the
array.
For example, if the input array is [-1, 2, -3, 4, 5, 6, -7, 8, 9], then the output should 
be [9, -7, 8, -3, 5, -1, 2, 4, 6]
Note: The partition process changes relative order of elements. I.e. the order of the 
appearance of elements is not maintained with this approach. See this for maintaining 
order of appearance of elements in this problem.
The solution is to first separate positive and negative numbers using partition process
of QuickSort. In the partition process, consider 0 as value of pivot element so that 
all negative numbers are placed before positive numbers. Once negative and positive numbers 
are separated, we start from the first negative number and first positive number
and swap every alternate negative number with next positive number. 

Time Complexity: O(n) where n is number of elements in given array. 
Auxiliary Space: O(1)

"""

# program to put positive numbers at even indexes(0, // 2, 4, ...) and
# negative numbers at odd indexes (1, 3, 5, ..)

# The main function that rearranges elements of given array.
# It puts positive elements at even indexes (0, 2, ..) and negative numbers 
# at odd indexes (1, 3, 5, ..)
# The main function that rearranges elements of given array.
# It puts positive elements at even indexes (0, 2, ..) and negative numbers 
# at odd indexes (1, 3, ..).
def rearrange(arr, n):
    # The following few lines are similar to partition process of QuickSort. The idea is
    # to consider 0 as pivot and divide the array around it.
    i = -1
    for j in range(n):
        if(arr[j] < 0):
            i += 1
            # swapping of arr
            arr[i], arr[j] = arr[j], arr[i]

    # Now all positive numbers are at end and the negative numbers at the beginning of array.
    # Initialize indexes for starting point of positive and negative numbers to be swapped
    pos, neg = i + 1, 0

    #Increment  the negative index by 2 and positive index by 1 i.e., swap every alternative
    # negative number with next positive number
    while (pos < n and neg < pos and arr[neg] < 0):
        # swapping of arr
        arr[neg], arr[pos] = arr[pos],arr[neg]
        pos += 1
        neg += 2

# A utility function to print an array
def printArray(arr, n):

    for i in range(n):
        print(arr[i], end=" ")

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
rearrange(arr, n)
printArray(arr, n)



"""
Rearrange array in alternating positive & negative items with O(1) extra space | Set 1

Given an array of positive and negative numbers, arrange them in an alternate fashion 
such that every positive number is followed by negative and vice-versa maintaining the
order of appearance. 
Number of positive and negative numbers need not be equal. If there are more positive 
numbers they appear at the end of the array. If there are more negative numbers,
 they too appear in the end of the array.

Examples : 

Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}

output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}

Naive Approach : 
The above problem can be easily solved if O(n) extra space is allowed. It becomes interesting
due to the limitations that O(1) extra space and order of appearances. 
The idea is to process array from left to right. While processing, find the first out of place
element in the remaining unprocessed array. 
An element is out of place if it is negative and at odd index, or it is positive and at even
index. Once we find an out of place element, we find the first element after it with opposite
sign. We right rotate the subarray between these two elements (including these two).

Time Complexity : O(N^2)

Space Complexity : O(1)

"""

# rotates the array to right by once from index 'outOfPlace to cur'
def rightRotate(arr, n, outOfPlace, cur):
    temp = arr[cur]
    for i in range(cur, outOfPlace, -1):
        arr[i] = arr[i - 1]
    arr[outOfPlace] =temp
    return arr

def rearrange(arr,n):
    outOfPlace =-1
    for index in range(n):
        if(outOfPlace >= 0):
            # if element at outOfPlace place in negative and if element at index is positive
            # we can rotate the array to right or if element at outOfPlace place in positive
            # and if element at index is negative we can rotate the array to right
            if((arr[index] >= 0 and arr[outOfPlace] < 0) or
              (arr[index] < 0 and arr[outOfPlace] >=0)):
              arr =rightRotate(arr, n, outOfPlace, index)
              
              if(index-outOfPlace > 2):
                  outOfPlace +=2
              else:
                  outOfPlace =- 1

        if(outOfPlace == -1):
            
            # conditions for A[index] to be in out of place
            if((arr[index] >= 0 and index % 2 == 0) or (arr[index] < 0 and index % 2 == 1)):
                outOfPlace = index
    return arr


arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
 
print("\nGiven Array is:")
print(arr)
 
print("\nRearranged array is:")
print(rearrange(arr, len(arr)))

print("Efficient Approach : \n")
"""
Efficient Approach : 

We first sort the array in non-increasing order.Then we will count the number of poitive 
and negative integers. Then we will swap the one negative and one positive

number till we reach our condition. 

This will rearrange the array elements because we are sorting the array and accessing
the element from left to right according to our need.

Time Complexity: O(N*logN)

Space Complexity: O(1)

"""

def rearrange(arr, n):
    arr.sort()

    # initialize two pointers - one pointing to the negative number, one pointing to
    # the positive number

    i, j = 1, 1
    while j < n:
        if arr[j] > 0:
            break
        j  += 1

    # swap the numbers until the given conditions gets satisfied
    while(arr[i] < 0) and (j < n):
        arr[i], arr[j] = arr[j], arr[i]

        # increment i by 2 coz a negative number is followed by a positive number
        i += 2
        j += 1

    return arr

arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
 
ans = rearrange(arr, len(arr))
for num in ans:
    print(num, end = " ")


print("\nApproach 1: \n")
"""
Rearrange array in alternating positive & negative items with O(1) extra space | Set 2

Examples: 

Input :
arr[] = {-2, 3, 4, -1}
Output :
arr[] = {-2, 3, -1, 4} OR {-1, 3, -2, 4} OR ..

Input :
arr[] = {-2, 3, 1}
Output :
arr[] = {-2, 3, 1} OR {-2, 1, 3} 

Input : 
arr[] = {-5, 3, 4, 5, -6, -2, 8, 9, -1, -4}
Output :
arr[] = {-5, 3, -2, 5, -6, 4, -4, 9, -1, 8} 

Approach 1:

First, sort the array in non-increasing order. Then we will count the number of positive 
and negative integers.
Then swap the one negative and one positive number in the odd positions till we reach our
condition.
This will rearrange the array elements because we are sorting the array and accessing 
the element from left to right according to our need.

Time Complexity: O(N*logN)

Space Complexity: O(1)

"""


class Main:
    
    # function which works in the condition when number of negative numbers are lesser or
    #  equal than positive numbers
    def fill1(self,a, neg, pos):
        if (neg % 2 == 1):
            for i in range(1, neg,2):
                c = a[i]
                d = a[i + neg]
                temp = c
                a[i] = d
                a[i + neg] = temp
        else:
            for i in range(1,neg, 2):
                c = a[i]
                d = a[i + neg - 1]
                temp = c
                a[i] = d
                a[i + neg - 1] = temp
                
    # Function which works in the condition when number of negative numbers are greater 
    # than positive numbers
    def fill2(self,a, neg, pos):
        if (pos % 2 == 1):
            for i in range(1,pos, 2):
                c = a[i]
                d = a[i + pos]
                temp = c
                a[i] = d
                a[i + pos] = temp
        else:
            for i in range(1,pos, 2):
                c = a[i]
                d = a[i + pos - 1]
                temp = c
                a[i] = d
                a[i + pos - 1] = temp
                
    
	# Reverse the array
    def reverse(self,a, n):
        # i, k, t =0,0,0
        for i in range(0, n / 2):
            t = a[i]
            a[i] = a[n - i - 1]
            a[n - i - 1] = t
    
    # Print the array
    def print(self,a, n):
        for i in range(0, n):
            print(a[i] + " ")
            print()

if __name__=='__main__':
    
    arr = [2, 3, -4, -1, 6, -9 ]
    n = len(arr)
    print("Given array is ")
    print(arr, n)

    m =Main()
    
    neg, pos = 0, 0
    for i in range(0, n):
        if (arr[i] < 0):
            neg +=1
        else:
            pos +=1
            
    # Sort the array
    arr.sort()
    
    if (neg <= pos):
        m.fill1(arr, neg, pos)
    else:
        # reverse the array in this condition
        m.reverse(arr, n)
    m.fill2(arr, neg, pos)
    print("Rearranged array is ")
    print(arr, n)

# Expected: -9 3 -1 2 -4 6

"""
Efficient Approach : 
We have already discussed a O(n2) solution that maintains the order of appearance in the 
array here. 
If we are allowed to change order of appearance, we can solve this problem in O(n) time 
and O(1) space.
The idea is to process the array and shift all negative values to the end in O(n) time. 
After all negative values are shifted to the end,
we can easily rearrange array in alternating positive & negative items.
We basically swap next positive element at even position from next negative element in
this step. 

Time Complexity : O(N)

Space Complexity : O(1)

"""

# program to rearrange array in alternativing positive & negative items with O(1) space
# solution does not maintain the original order of elements
def rearrange(arr, n):
    i =0
    j = n-1
    
    # shift all negative values to the end
    while(i < j):
        while( i<= n-1 and arr[i] > 0):
            i+=1
        while(j >= 0 and arr[j] < 0):
            j -=  1
        
        if( i< j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] =temp

    # i has index of leftmost negative element
    if(i == 0 or i == n):
        return 0

    # start with first positive element at index 0
    # rearrange array in alternating positive & negative items
    k = 0
    while( k < n and i < n):
        # swap next positive element at even
        # position from next negative element.
        temp = arr[k]
        arr[k] = arr[i]
        arr[i] =temp
        i = i+ 1
        k = k+ 2

# Utility function to print an array
def printArray(arr, n):
    for i in range(n):
        print(arr[i], end =" ")

    print("\n")

arr = [2,3, -4, -1, 6, -9 ]
 
n = len(arr)
 
print( "Given array is")
printArray(arr, n)
 
rearrange(arr, n)
 
print( "Rearranged array is")
printArray(arr, n)