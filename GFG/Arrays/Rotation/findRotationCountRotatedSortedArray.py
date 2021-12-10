"""
Consider an array of distinct numbers sorted in increasing order. The array has been rotated (clockwise) k number of times. Given such an array, find the value of k.
Examples: 
 

Input : arr[] = {15, 18, 2, 3, 6, 12}
Output: 2

Explanation : Initial array must be {2, 3,
6, 12, 15, 18}. We get the given array after 
rotating the initial array twice.

Input : arr[] = {7, 9, 11, 12, 5}
Output: 4

Input: arr[] = {7, 9, 11, 12, 15};
Output: 0

Method 1 (Using linear search)

If we take closer look at examples, we can notice that the number of rotations 
is equal to index of minimum element. A simple linear solution is to find 
minimum element and returns its index.

Time Complexity : O(n) 
Auxiliary Space : O(1) 

"""

# program to find number of rotations in a sorted and rotated array.
# returns counts of rotations for an array which is first sorted in ascending order, 
# then rotated
def countRotations(arr, n):
    # find index of minimum element
    min =arr[0]
    for i in range(0, n):
        if(min > arr[i]):
            min = arr[i]
            min_index =i
    return min_index

arr = [15, 18, 2, 3, 6, 12]
n = len(arr)
print(countRotations(arr, n))


"""
Method 2 (Efficient Using Binary Search) 
Here also we find the index of minimum element, but using Binary Search. 
 

The minimum element is the only element whose previous is greater than it. 
If there is no previous element, then there is no rotation (first element is minimum). 
We check this condition for middle element by comparing it with (mid-1)’th and
(mid+1)’th elements.
If the minimum element is not at the middle (neither mid nor mid + 1),
then minimum element lies in either left half or right half. 
If middle element is smaller than last element, then the minimum element lies 
in left half
Else minimum element lies in right half.

Time Complexity : O(Log n) 
Auxiliary Space : O(1) 

"""

# returns count of rotations for an array which is first sorted in ascending order,
# then rotated
def countRotations(arr, low, high):

    # condition needed to handle the case when arry is not rotated at all
    if( high < low):
        return 0

    # if there is only one element left
    if(high == low):
        return low

    # find mid (low + high) /2
    mid =low + (high - low) /2
    mid =int(mid)

    # check if element (mid+1) is minimum element. Consider the cases like {3,4,5,1,2}
    if(mid < high and arr[mid+1] < arr[mid]):
        return mid+1

    # check if mid itself is minimum element
    if(mid > low and arr[mid] < arr[mid - 1]):
        return mid

    # decide whether to go to left half or right half
    if(arr[high] > arr[mid]):
        return countRotations(arr, low, mid-1)
    return countRotations(arr, mid+1, high)

arr = [15, 18, 2, 3, 6, 12]
n = len(arr)
print(countRotations(arr, 0, n-1))  