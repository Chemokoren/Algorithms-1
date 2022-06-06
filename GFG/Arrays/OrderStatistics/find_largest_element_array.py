"""
Program to find largest element in an array

Given an array, find the largest element in it.

Input : arr[] = {10, 20, 4}
Output : 20

Input : arr[] = {20, 10, 20, 4, 100}
Output : 100

The solution is to initialize  max as first element, then traverse the given array from second 
element till end. For every traversed element, compare it with max, if it is greater than max,
then update max.


"""
# program to find maximum in arr[] of size n
def largest(arr):
    # return max using max inbuilt max() function
    return max(arr)


arr = [10, 324, 45, 90, 9808]
n = len(arr)
 
#calculating length of an array
 
Ans = largest(arr)
 
#display max
print ("Largest in given array is",Ans)
