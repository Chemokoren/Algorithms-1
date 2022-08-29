"""
Product of maximum in first array and minimum in second

Given two arrays, the task is to calculate the product of max element of first array and min
element of second array

Input : arr1[] = {5, 7, 9, 3, 6, 2},  
        arr2[] = {1, 2, 6, -1, 0, 9} 

Output : max element in first array 
is 9 and min element in second array 
is -1. The product of these two is -9.

Input : arr1[] = {1, 4, 2, 3, 10, 2},  
        arr2[] = {4, 2, 6, 5, 2, 9} 
Output : max element in first array 
is 10 and min element in second array 
is 2. The product of these two is 20.


"""
from audioop import reverse

# Time Complexity : O(n log n)  | Space Complexity : O(1)
def product_max_min(arr1, arr2):
    arr1.sort(reverse=True)
    arr2.sort()

    return arr1[0] * arr2[0]

print("Expected: -9, Actual: ", product_max_min([5, 7, 9, 3, 6, 2], [1, 2, 6, -1, 0, 9]))
print("Expected: 20, Actual: ", product_max_min([1, 4, 2, 3, 10, 2], [4, 2, 6, 5, 2, 9]))


print("\n my tests \n")
def my_tests(arr1, arr2):
    max_val =max(arr1)
    min_val=min(arr2)
    return max_val * min_val

print("Expected: -9, Actual: ", my_tests([5, 7, 9, 3, 6, 2], [1, 2, 6, -1, 0, 9]))
print("Expected: 20, Actual: ", my_tests([1, 4, 2, 3, 10, 2], [4, 2, 6, 5, 2, 9]))

# Time complexity: O(n) | Space complexity: O(1)
def my_tests_two(arr1, arr2):

    min_val = float("inf")
    max_val =-float("inf")

    for i in arr1:
        if i > max_val:
            max_val =i
        

    for i in arr2:
        if i < min_val:
            min_val =i
    return max_val * min_val

print("Expected: -9, Actual: ", my_tests_two([5, 7, 9, 3, 6, 2], [1, 2, 6, -1, 0, 9]))
print("Expected: 20, Actual: ", my_tests_two([1, 4, 2, 3, 10, 2], [4, 2, 6, 5, 2, 9]))
