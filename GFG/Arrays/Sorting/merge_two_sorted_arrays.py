"""

Merge two sorted arrays with O(1) extra space

We are given two sorted arrays. We need to merge these two arrays such that the initial numbers(
    after complete sorting) are in the first array and the remaining numbers are in the second
    array. Extra space is allowed in O(1)

Example: 

Input: ar1[] = {10};
       ar2[] = {2, 3};
Output: ar1[] = {2}
        ar2[] = {3, 10}  

Input: ar1[] = {1, 5, 9, 10, 15, 20};
       ar2[] = {2, 3, 8, 13};
Output: ar1[] = {1, 2, 3, 5, 8, 9}
        ar2[] = {10, 13, 15, 20}

"""

from array import array


def my_tests(arr1, arr2):
    i =0
    j =0
     
    while i <len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            arr1[i] , arr2[j] =arr2[j], arr1[i]
            i +=1
        elif arr1[i] < arr2[j]:
            i +=1
            j +=1
    
    while j < len(arr2)-1:
        if arr2[j] > arr2[j+1]:
            arr2[j], arr2[j+1] =arr2[j+1], arr2[j]
            j +=1

    return arr1, arr2


print("Expected:, Actual", my_tests([10],[2,3]))
print("Expected:, Actual", my_tests([1, 5, 9, 10, 15, 20],[2, 3, 8, 13]))