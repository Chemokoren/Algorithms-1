"""
Merge Sort 

-It's a combination of three things splitting, sorting, & merging 
- Exploits the fact that arrays of 0 or 1 element are always sorted
- Works by decomposing an array into smaller arrays of 0 or 1 elements, then building up a newly sorted array.

Merging Arrays
- In order to implement merge sort, it's useful to first implement a function responsible for merging two 
sorted arrays
- Givn two arrays which are sorted, this helper function should create a new array which is also sorted,
and consists of all the elements in the two input arrays
- This function should run in O(n + m) time and O(n + m) space and should not modify the parameters 
passed to it.


Merging Arrays Pseudocode
-Create an empty array, take a look at the smallest values in each input array
- While there are still values we haven't looked at...
    - If the value in the first array is smaller than the value in the second array, push the value in the
    first array into our results and move on to the next value in the first array.
    - If the value in the first array is larger than the value in the second array, push the value in the 
    second array into our results and move on to the next value in the second array
    - Once we exhaust one array, push in all remaining values from the other array

mergeSort Pseudocode

- Break up the array into halves until you have arrays that are empty or have one element
- Once you have smaller sorted arrays, merge those arrays with other sorted arrays until you are back at
the full length of the array
- Once the array has been merged back together, return the merged(and sorted!) array

Big O of mergeSort

Time complexity: O(nlog(n)) for Best, average & worst case
Space Complexity: O(n)
"""
def merge(arr1, arr2):
    results =[]
    i = 0
    j = 0
    while i< len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            results.append(arr1[i])
            i +=1
        else:
            results.append(arr2[j])
            j +=1

    while i < len(arr1):
        results.append(arr1[i])
        i +=1
    while j < len(arr2):
        results.append(arr2[j])
        j +=1

    return results

# print(merge([1,10, 50], [2,14,99,100]))
# print(merge([], [1,3]))
print(merge([24], [10]))


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid=len(arr)//2
    left = mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

    # print(arr1, arr2)

print("merged results: ", mergeSort([99, 50, 2, 14, 10, 1, 100]))
# print("merged results: ", mergeSort([10,24,76,73,72,1, 9]))