"""
search an element in a sorted and rotated array

An element in a sorted array can be found in O(log n) time
via binary search. But suppose we rotate an ascending order 
sorted array at some pivot unknown to you beforehand. 
For instance, 1 2 3 4 5 might become 3 4 5 1 2. 
Devise a way to find an element in the rotated array 
in O(log n) time.

Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
         key = 3
Output : Found at index 8

Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
         key = 30
Output : Not found

Input : arr[] = {30, 40, 50, 10, 20}
        key = 10   
Output : Found at index 3

All solutions provided here assume that all elements
in the array are distinct.

Approach: 
 
The idea is to find the pivot point, divide the array in two sub-arrays
and perform binary search.
The main idea for finding pivot is – for a sorted (in increasing order)
and pivoted array, pivot element is the only element for which next 
element to it is smaller than it.
Using the above statement and binary search pivot can be found.
After the pivot is found out divide the array in two sub-arrays.
Now the individual sub – arrays are sorted so the element can be
searched using Binary Search.

Implementation:

Input arr[] = {3, 4, 5, 1, 2}
Element to Search = 1
  1) Find out pivot point and divide the array in two
      sub-arrays. (pivot = 2) /*Index of 5*/
  2) Now call binary search for one of the two sub-arrays.
      (a) If element is greater than 0th element then
             search in left array
      (b) Else Search in right array
          (1 will go in else as 1 < 0th element(3))
  3) If element is found in selected sub-array then return index
     Else return -1.

Time Complexity: O(log n). 
Binary Search requires log n comparisons to find the element. So time complexity is O(log n).
Space Complexity:O(1), No extra space is required.

"""

# program to search an element in a sorted & pivoted array
# searches an element key in a pivoted, sorted array arrp[] of size n
def pivotedBinarySearch(arr, n, key):
    pivot =findPivot(arr, 0, n-1)

    # if we didn't find a pivot,
    # then arry is not rotated at all
    if pivot == -1:
        return binarySearch(arr,0,n-1,key)

    # If we found a pivot, then first compare with pivot & then
    # search in two subarrays around pivot
    if(arr[pivot] == key):
        return pivot
    if(arr[0] <= key):
        return binarySearch(arr, 0, pivot -1, key)
    return binarySearch(arr, pivot+1, n-1, key)

# function to get pivot. For array
# 3,4,5,6,1,2, it returns 3 (index of 6)
def findPivot(arr, low, high):

    # base case
    if high < low:
        return -1
    if high == low:
        return low
    
    # low + (high-low)/2
    mid =int((low+high)/2)

    if mid < high and arr[mid] > arr[mid +1]:
        return mid
    if mid > low and arr[mid] < arr[mid -1]:
        return mid-1
    if arr[low] >=arr[mid]:
        return findPivot(arr, low, mid-1)
    return findPivot(arr,mid+1, high)

def binarySearch(arr, low, high, key):
    if high < low:
        return -1
    # low + (high -low) /2
    mid =int((low + high)/2)

    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarySearch(arr,(mid + 1), high, key)
    return binarySearch(arr, low, (mid-1), key)

arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
n = len(arr1)
key = 3
print("Index of the element is : ", pivotedBinarySearch(arr1, n, key))

