"""
Find a peak element

Given an array of integers. Find a peak element in it. An array element is a peak if it is NOT
smaller than its neighbours. For corner elements, we need to consider only one neighbour.



Input: array[]= {5, 10, 20, 15}
Output: 20
The element 20 has neighbours 10 and 15,
both of them are less than 20.

Input: array[] = {10, 20, 15, 2, 23, 90, 67}
Output: 20 or 90
The element 20 has neighbours 10 and 15, 
both of them are less than 20, similarly 90 has neighbours 23 and 67.

Following corner cases give better idea about the problem. 

    If input array is sorted in strictly increasing order, the last element is always a peak element. For example, 50 is peak element in {10, 20, 30, 40, 50}.
    If the input array is sorted in strictly decreasing order, the first element is always a peak element. 100 is the peak element in {100, 80, 60, 50, 20}.
    If all elements of input array are same, every element is a peak element.

It is clear from the above examples that there is always a peak element in the input array.

Naive Approach

- The array can be traversed and the element whose neighbours are less than that element can be 
returned.

Algorithm: 

    In the array, the first element is greater than the second or the last element is greater than
    the second last, print the respective element and terminate the program.
    And traverse the array from the second index to the second last index
    If for an element array[i], it is greater than both its neighbours, 
    i.e., array[i] > =array[i-1] and array[i] > =array[i+1], then print that element and 
    terminate.
"""

# Time complexity: O(n) |  Auxiliary Space: O(1)
def findPeak(arr) :
    n = len(arr)
    
    # first or last element is peak element
    if (n == 1) :
        return 0
    
    if (arr[0] >= arr[1]) :
        return 0    

    if (arr[n - 1] >= arr[n - 2]) :
        return n - 1
        
    # check for every other element
    for i in range(1, n - 1) :
        # check if the neighbors are smaller
        if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]) :
            return i
			
print("Index of a peak point is", findPeak([ 1, 3, 20, 4, 1, 0 ]))

"""
Efficient Approach

Divide and Conquer can be used to find a peak in O(Logn) time. The idea is based on the technique 
of Binary Search to check if the middle element is the peak element or not. If the middle element
is not the peak element, then check if the element on the right side is greater than the middle 
element then there is always a peak element on the right side. If the element on the left side is
greater than the middle element then there is always a peak element on the left side. Form a 
recursion and the peak element can be found in log n time. 

"""



print("\n my tests \n")
'''
my tests 
'''

def my_tests(arr):
    res =[]

    for i in range(len(arr)):
        if i == 0:
            if arr[i+1] < arr[i]:
                res.append(arr[i])

        elif i == len(arr)-1:
            if arr[i-1] <arr[i]:
                res.append(arr[i])
        else:
            if arr[i-1] < arr[i] and arr[i+1] < arr[i]:
                res.append(arr[i])
    return res



print("Expected: 20, Actual:", my_tests([5, 10, 20, 15]))
print("Expected: [20,90], Actual:", my_tests([10, 20, 15, 2, 23, 90, 67]))
print("Expected: [ ], Actual:", my_tests([10, 20, 30, 40, 50]))
print("Expected: [ ], Actual:", my_tests([100, 80, 60, 50, 20]))
