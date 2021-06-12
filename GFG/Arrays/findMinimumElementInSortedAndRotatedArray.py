"""
A sorted array is rotated at some unknown point, find the minimum element in it. 
The following solution assumes that all elements are distinct.

Examples: 

Input: {5, 6, 1, 2, 3, 4}
Output: 1

Input: {1, 2, 3, 4}
Output: 1

Input: {2, 1}
Output: 1

A simple solution is to traverse the complete array and find a minimum. 
This solution requires O(n) time. 
We can do it in O(Logn) using Binary Search.
If we take a closer look at the above examples, we can easily figure out the 
following pattern:

The minimum element is the only element whose previous is greater than it. 
If there is no previous element, then there is no rotation (the first element is minimum). 
We check this condition for the middle element by comparing it with 
(mid-1)’th and (mid+1)’th elements.
If the minimum element is not at the middle (neither mid nor mid + 1), 
then the minimum element lies in either the left half or right half. 
If the middle element is smaller than the last element, then the minimum element lies 
in the left half
Else minimum element lies in the right half.

This approach in the worst case(If all the elements are the same) takes O(N).
"""

# program to find the minimum element in a sorted and rotated array

def findMin(arr, low, high):
    # handle the case when the array is rotated at all
    if high < low:
        return arr[0]

    # if there is only one element left
    if high == low:
        return arr[0]

    # find mid
    mid = int((low + high)/2)

    # check if element(mid+1) is minimum element. Consider the case like [3,4,5,1,2]
    if mid < high and arr[mid +1] < arr[mid]:
        return arr[mid+1]

    # check if mid itself is the minimum element
    if mid > low and arr[mid] < arr[mid - 1]:
        return arr[mid]

    # Decide whether we need to go to left half or right half
    if arr[high] > arr[mid]:
        return findMin(arr,low, mid-1)
    return findMin(arr,mid+1, high)

arr1 = [5, 6, 1, 2, 3, 4]
n1 = len(arr1)
print("The minimum element is " + str(findMin(arr1, 0, n1-1)))
 
arr2 = [1, 2, 3, 4]
n2 = len(arr2)
print("The minimum element is " + str(findMin(arr2, 0, n2-1)))
 
arr3 = [1]
n3 = len(arr3)
print("The minimum element is " + str(findMin(arr3, 0, n3-1)))
 
arr4 = [1, 2]
n4 = len(arr4)
print("The minimum element is " + str(findMin(arr4, 0, n4-1)))
 
arr5 = [2, 1]
n5 = len(arr5)
print("The minimum element is " + str(findMin(arr5, 0, n5-1)))
 
arr6 = [5, 6, 7, 1, 2, 3, 4]
n6 = len(arr6)
print("The minimum element is " + str(findMin(arr6, 0, n6-1)))
 
arr7 = [1, 2, 3, 4, 5, 6, 7]
n7 = len(arr7)
print("The minimum element is " + str(findMin(arr7, 0, n7-1)))
 
arr8 = [2, 3, 4, 5, 6, 7, 8, 1]
n8 = len(arr8)
print("The minimum element is " + str(findMin(arr8, 0, n8-1)))
 
arr9 = [3, 4, 5, 1, 2]
n9 = len(arr9)
print("The minimum element is " + str(findMin(arr9, 0, n9-1)))

"""
Approach 2: handle duplicates in O(log n) time
"""

# program to find minimum element in a sorted and rotated array containing 
# duplicate elements

# Function to find minimum element
def findMin(arr,low,high):
    while(low < high):
        mid = low + (high - low) // 2

        if(arr[mid] == arr[high]):
            high -=1
        elif(arr[mid] > arr[high]):
            low = mid + 1
        else:
            high = mid

    return arr[high]

if __name__ == '__main__':
   
    arr1 = [5, 6, 1, 2, 3, 4];
    n1 = len(arr1);
    print("The minimum element is ",
          findMin(arr1, 0, n1 - 1));
 
    arr2 = [1, 2, 3, 4];
    n2 = len(arr2);
    print("The minimum element is ",
          findMin(arr2, 0, n2 - 1));
 
    arr3 = [1];
    n3 = len(arr3);
    print("The minimum element is ",
          findMin(arr3, 0, n3 - 1));
 
    arr4 = [1, 2];
    n4 = len(arr4);
    print("The minimum element is ",
          findMin(arr4, 0, n4 - 1));
 
    arr5 = [2, 1];
    n5 = len(arr5);
    print("The minimum element is ",
          findMin(arr5, 0, n5 - 1));
 
    arr6 = [5, 6, 7, 1, 2, 3, 4];
    n6 = len(arr6);
    print("The minimum element is ",
          findMin(arr6, 0, n6 - 1));
 
    arr7 = [1, 2, 3, 4, 5, 6, 7];
    n7 = len(arr7);
    print("The minimum element is ",
          findMin(arr7, 0, n7 - 1));
 
    arr8 = [2, 3, 4, 5, 6, 7, 8, 1];
    n8 = len(arr8);
    print("The minimum element is ",
          findMin(arr8, 0, n8 - 1));
 
    arr9 = [3, 4, 5, 1, 2];
    n9 = len(arr9);
    print("The minimum element is ",
          findMin(arr9, 0, n9 - 1));
 


