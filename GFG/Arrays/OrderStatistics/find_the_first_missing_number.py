"""
Find the smallest missing number

Given a sorted array of n distinct integers where each integer is in range from 0 to m-1 and m>n
Find the smallest number that is missing from the array.

Examples 

Input: {0, 1, 2, 6, 9}, n = 5, m = 10 
Output: 3

Input: {4, 5, 10, 11}, n = 4, m = 12 
Output: 0

Input: {0, 1, 2, 3}, n = 4, m = 5 
Output: 4

Input: {0, 1, 2, 3, 4, 5, 6, 7, 10}, n = 9, m = 11 
Output: 8

Method 1: Binary Search

For i = 0 to m-1, do binary search for i in the array. If i is not present in the array then
return i.
Time Complexity: O(m log n)

Method 2: Linear Search

If arr[0] is not 0, return 0. Otherwise traverse the input array starting from index 0, and for
each pair of elements a[i] and a[i+1], find the difference between them. If the difference is
greater than 1 then a[i]+1 is the missing number.

Time Complexity: O(n)

Method 3: Use modified binary search
In the standard Binary Search Process, the element to be searched is compared with the middle
element and on the basis of comparison result, we decide whether the search is over or to go 
to left half or right half.
In this method, we modify the standard Binary Search algorithm to compare the middle element 
with its index and make a decision on the basis of this comparison.
- If the first element is not same as its index then return first index
- Else get the middle index say mid
    - If arr[mid] greater than mid then the required element lies in left half
    - Else the required element lies in right half.

Note: This method doesn’t work if there are duplicate elements in the array.
Time Complexity: O(Logn)

"""
# program to find the smallest elements missing in a sorted array.
def findFirstMissing(array, start, end):
    if(start > end):
        return end + 1

    if(start != array[start]):
        return start

    mid = int((start +  end) / 2)

    # Left half has all elements from 0 to mid
    if(array[mid] == mid):
        return findFirstMissing(array, mid+1, end)
    return findFirstMissing(array, start, mid)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 10]
n = len(arr)
print("Smallest missing element is",
      findFirstMissing(arr, 0, n-1))


print("\n Another method: \n")
"""
Another method:

The idea is to use Recursive Binary to find the smallest missing number
- if the first element of the array is not 0, then the smallest missing number is 0.
- if the last element of the array is N-1,  then the smallest missing number is N.
- otherwise, find the middle element from the first and last index and check if  the middle 
element is equal to the desired element. i.e. first + middle_index.
    -if the middle element is the desired element, then the smallest missing element 
    is in the right search space of the middle.
    - otherwise, the smallest missing number is in the left search space of the middle
"""
# function to find smallest missing in Sorted Array
def findSmallestMissingSortedArray(arr):

    # check if 0 is missing in the array
    if(arr[0] !=0 ):
        return 0

    # check if all numbers 0 to n - 1 are present in array
    if(arr[-1] == len(arr) -1):
        return len(arr)

    first = arr[0]

    return newFindFirstMissing(arr, 0, len(arr) -1, first)

# Function to find missing element
def newFindFirstMissing(arr, start, end, first):
    if(start < end ):
        mid = int((start + end ) /2)

        # Index matches with value at that index, means missing element cannot be upto that point
        if(arr[mid] != mid + first):
            return newFindFirstMissing(arr, start, mid, first)
        else:
            return newFindFirstMissing(arr, mid+1, end , first)

    return start + first


arr = [ 0, 1, 2, 3, 4, 5, 7 ]
n = len(arr)
 
# Function Call
print("First Missing element is :", findSmallestMissingSortedArray(arr))