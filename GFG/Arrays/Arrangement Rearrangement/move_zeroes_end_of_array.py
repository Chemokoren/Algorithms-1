"""
Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).
Example: 
 

Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
Output : arr[] = {1, 2, 4, 3, 5, 0, 0, 0};

Input : arr[]  = {1, 2, 0, 0, 0, 3, 6};
Output : arr[] = {1, 2, 3, 6, 0, 0, 0};

Traverse the given array ‘arr’ from left to right. While traversing, maintain count of
non-zero elements in array. Let the count be ‘count’. For every non-zero element arr[i], 
put the element at ‘arr[count]’ and increment ‘count’. After complete traversal, 
all non-zero elements have already been shifted to front end and ‘count’ is set as 
index of first 0. Now all we need to do is that run a loop which makes all elements zero 
from ‘count’ till end of the array.

Time Complexity: O(n) where n is number of elements in input array.
Auxiliary Space: O(1)

"""
# code to move all zeroes at the end of the array
def pushZerosToEnd(arr, n):
    count =0 # count of non-zero elements

    # Traverse the array. If element encountered is non-zero, then replace the element at
    # index 'count ' with this element
    for i in range(n):

        if arr[i] != 0:
            # here count is incremented
            arr[count] = arr[i]
            count +=1

    # Now all non-zero elements have been shifted to front and 'count' is set as index of 
    # first 0. Make all elements 0 from count to end.
    while count < n:
        arr[count] =0
        count += 1

arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)

print(" approach 2:")

"""
Approach 2:

moveZerosToEnd(arr, n)
    Initialize count = 0
    for i = 0 to n-1
        if (arr[i] != 0) then
            swap(arr[count++], arr[i])

Time Complexity: O(n). 
Auxiliary Space: O(1).

"""

def moveZerosToEnd(arr, n):
    # Count of non-zero elements
    count = 0

    # Traverse the array. If arr[i] is non-zero, the  swap the element at index 'count'
    # with the element at index 'i'

    for i in range(0, n):
        if(arr[i] !=0):
            arr[count],arr[i] = arr[i], arr[count]
            count +=1
def printArray(arr, n):
 
    for i in range(0, n):
        print(arr[i],end=" ")

# arr = [ 0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9 ]
arr = [1, 2, 0, 0, 0, 3, 6]
n = len(arr)
 
print("\nOriginal array:", end=" ")
printArray(arr, n)
 
moveZerosToEnd(arr, n)
 
print("\nModified array: ", end=" ")
printArray(arr, n)


# arr = [1, 2, 0, 0, 0, 3, 6]   # not working with this example

def tryPush(arr):
    n =len(arr)
    for i in range(n-1):
        if(arr[i+1] ==0 and arr[i]>0):
            arr[i],arr[i+1] =arr[i+1], arr[i]
    if arr[n-1] > 0:
        for i in range(n-2):
            if arr[i] >0 and arr[i+1] ==0:
                arr[i+1],arr[n-1] =arr[n-1],arr[i+1]

    # for j in range(n-2,0,-1):
    #     val =arr[n-1]
    #     if(arr[j]>0 and arr[j+1] ==0):
    #         arr[j],arr[val] =arr[val],arr[j]

    return arr

print("\ntriallllllllllllll")
print(tryPush(arr))

def test(arr):
    i =0 
    j =len(arr)-1
    
    while i < len(arr) and j >=0 and i < j:
        if (arr[i] == 0):
            if(arr[j] != 0):
                arr[i], arr[j] = arr[j], arr[i]
                i = i+1
                j = j-1
            else:
                j =j -1
        else:
            i = i+1
    return arr
            

print("test")

print("expected: [1, 2, 3, 6, 0, 0, 0], actual:", test([1, 2, 0, 0, 0, 3, 6]))
print("expected: [1, 2, 4, 3, 5, 0, 0, 0], actual:", test([1, 2, 0, 4, 3, 0, 5, 0]))


'''

'''
def moveZerosToEndUpdated(arr):
    n = len(arr)
    count = 0 # 

    # traverse the array. If arr[i] is non-zero, then
    # update the value of arr at index count to arr[i]
    for i in range(0,n):
        if(arr[i] != 0):
            arr[count] =arr[i]
            count +=1

    # update all elements at index >= count with value 0
    for i in range(count,n):
        arr[i] =0
    return arr

print("##################### def moveZerosToEndUpdated #####################")
print("expected: [1, 2, 3, 6, 0, 0, 0], actual:", moveZerosToEndUpdated([1, 2, 0, 0, 0, 3, 6]))
print("expected: [1, 2, 4, 3, 5, 0, 0, 0], actual:", moveZerosToEndUpdated([1, 2, 0, 4, 3, 0, 5, 0]))