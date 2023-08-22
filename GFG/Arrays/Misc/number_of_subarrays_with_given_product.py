"""
Number of subarrays with given product

Given an array of positive numbers and a number k, find the number of subarrays having product
exactly equal to k. We may assume that there is no overflow.

Input : arr = [2, 1, 1, 1, 4, 5]
        k = 4
Output : 4
1st subarray : arr[1..4]
2nd subarray : arr[2..4]
3rd subarray : arr[3..4]
4th subarray : arr[4]

Input : arr = [1, 2, 3, 4, 1]
        k = 24
Output : 4
1st subarray : arr[0..4]
2nd subarray : arr[1..4]
3rd subarray : arr[1..3]
4th subarray : arr[0..3]

A simple solution is to consider all subarrays and find their products. For every product, check 
if it is equal to k. If yes, then increment result.

An efficient solution is  to use sliding window technique can be used to solve the problem. We 
use two pointers start and end to represent starting and ending point of sliding window.

Initially both start and 
"""

def arr_prod(arr):
    prod =1
    for i in range(len(arr)):
        prod *=arr[i]
    return prod

def my_tests(arr, key):
    i =0
    j=0
    count =0
    res =[]

    while j <= len(arr)-1:
        arr_val =arr_prod(arr[i:j+1])
        if arr_val == key:
            res.append(arr[i:j+1])
            count +=1
            i += 1
        elif arr_val > key:
             i+=1
        else:
            j+=1
    return res,count
            

print("Expected:, Actual:", my_tests([2, 1, 1, 1, 4, 5], 4))



