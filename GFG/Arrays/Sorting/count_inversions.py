"""
Count Inversions in an array | Set 1 Using Merge Sort

Inversion Count for an array indicates - how far(or close) the array is from being sorted. If the
array is already sorted, then the inversion count is 0, but if the array is sorted in reverse
order, the inversion count is the maximum.

Formally speaking, two elements a[i] and a[j] form an inversion if a[i] >a[j] and i < j

Example:
Input: arr =[8, 4, 2, 1]

Output: 6

Explanation: Given array has six inversions:
(8,4), (4,2),(8,2), (8,1), (4,1), (2,1)

Input: arr =[3,1,2]
Output: 2
Explanation: Given array has two inversions:
(3,1),(3,2)

METHOD 1: Simple
Approach: Traverse through the array, and for every index, find the number of smaller elements on
its right side of the array. This can be done using a nested loop. Sum up the counts of all index
in the array and print the sum.
Algorithm:
- Traverse through the array from start to end
- For every element, find the count of elements smaller than the current number up to that 
index using another loop.
-Sum up the count of inversion for every index.
-Print the count of inversions



"""
# count inversions in an array
# Time Complexity: O(n^2), Two nested loops are needed to traverse the array from start to end
# Space Complexity:O(1), No extra space is required.
def getInvCount(arr):
    n = len(arr)
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count +=1
    return inv_count

print("Expected: 6,Actual:", getInvCount([8, 4, 2, 1]))
print("Expected: 2,Actual:", getInvCount([3, 1, 2]))
print("Expected: 5,Actual:", getInvCount([1, 20, 6, 4, 5]))


"""
METHOD 2: Enhanced Merge sort

Suppose the number of inversions in the left half and right half of the array(inv1, inv2), what 
kinds of inversions are not account for in inv1+inv2? The answers is - the inversions that need
to be counted during the merge step.
Therefore, to get the total number of inversions that needs to be added are the number of 
inversions in the left subarray, right subarray, and merge().

How to get the number of inversions in merge()?

In merge process, let i be used for indexing left sub-array and j for right sub-array.
At any step in merge(), if a[i] is greater than a[j], then there are (mid-1) inversions.
Because left and right subarrays are sorted, so all the remaining elements in left-subarray
(a[i+1], a[i+2] ... a[mid]) will be greater than a[j]

Algorithm:
1. The idea is similar to merge sort, divide the array into two equal or almost equal halves in
each step until until the base case is reached.
2. Create a function merge that counts the number of inversions when two halves of the array are
merged, create two indices i and j, i is the index for the first half, and j is an index of the
second half. If a[i] is greater than a[j], then there are (mid-1) inversions. Because left and 
right subarrays are sorted, so all the remaining elements in left-subarray(a[i+1], a[i+2] ...a[mid])
will be greater than a[j].
3. Create a recursive function to divide the array into halves and find the answer by summing
the number of inversions in the first half, the number of inversions in the second half and the 
number of inversions by merging the two.
4. The base case of recursion is when there is only one element in the given half.
5. Print the answer


    Time Complexity: O(n log n), The algorithm used is divide and conquer, So in each level,
    one full array traversal is needed, and there are log n levels,
    so the time complexity is O(n log n).
    Space Complexity: O(n), Temporary array.

Note that the code modifies (or sorts) the input array. If we want to count only inversions, 
we need to create a copy of the original array and call mergeSort() on the copy to preserve the 
original array’s order.

"""
# function to use Inversion Count

def mergeSort(arr):
    n = len(arr)

    # A temp_arr is created to store the sorted array in merge function
    temp_arr =[0]*n
    return _mergeSort(arr,temp_arr, 0, n-1)

# This function uses MergeSort to count inversions
def _mergeSort(arr, temp_arr, left, right):

    # inv_count stores inversion counts in @recursive call
    inv_count = 0
    # make recursive call iff there is > 1 element
    if left < right:
        mid =(left+right)//2

        # calculate inversion counts in the left subarray
        inv_count += _mergeSort(arr, temp_arr, left, mid)

        # calculate inversion counts in right subarray
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right)

        # merge two subarraysin a sorted subarray
        inv_count +=merge(arr, temp_arr, left, mid, right)
    return inv_count

# function merges two subarrays in a single sorted subarray
def merge(arr, temp_arr, left, mid, right):
    i = left # Starting index of left subarray
    j = mid + 1 # Starting index of right subarray
    k = left # Starting index of sorted subarray
    inv_count = 0

    # Conditions are checked to make sure that i and j don't exceed their subarray limits
    while i <= mid and j <= right:

        # There will be no inversion if arr[i] <= arr[j]
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # inversion will occur
            temp_arr[k] = arr[j]
            inv_count +=(mid-i + 1)
            k += 1
            j += 1

    # copy the remaining elements of left subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    # Copy the remaining elements of right subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    # copy the sorted subarray into the original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count

print("Expected:5, Actual:",mergeSort([1, 20, 6, 4, 5]))

"""
METHOD 3: Heapsort + Bisection

1. Create a heap with new pair elements, (element, index)
2. After sorting them, pop out each minimum sequence and create a new sorted list with 
the indexes
3. Calculate the difference between the original index and the index of bisection of the new
sorted list
4. sum up the difference

Complexity Analysis:  

    Time Complexity: O(n log n). Both heapsort and bisection can perform sorted insertion in 
    log n in each element, so the time complexity is O(n log n).
    Space Complexity: O(n). A heap and a new list are the same length as the original array.

"""

from heapq import heappush, heappop
from bisect import bisect, insort

def getNumOfInversions(A):
    N = len(A)

    if N <= 1:
        return 0
    sortList =[]
    result = 0

    # heapsort, O(N*log(N))
    for i, v in enumerate(A):
        heappush(sortList, (v,i))

    x =[] # create a sorted list of indexes
    while sortList:
        v, i = heappop(sortList) # O(log(N))
        # find the current minimum's index
        # the index y can represent how many minimums on the left 
        y = bisect(x, i) # O(log(N))
        # i can represent how many elements on the left
        # i - y can find how many bigger nums on the left
        result += i-y

        insort(x,i) # O(log(N))

    return result

print("The ", getNumOfInversions([-1, 6, 3, 4, 7, 4]))

print("\n my tests \n")
'''
my tests
'''
def my_tests(arr):
    count =0
    for i in range(len(arr)-1):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                count +=1
    return count

print("Expected: 6,Actual:", my_tests([8, 4, 2, 1]))
print("Expected: 2,Actual:", my_tests([3, 1, 2]))