"""
Find minimum difference between any two elements

Given an unsorted array, find the minimum difference between any pair in given array.


Input  : {1, 5, 3, 19, 18, 25};
Output : 1
Minimum difference is between 18 and 19

Input  : {30, 5, 20, 9};
Output : 4
Minimum difference is between 5 and 9

Input  : {1, 19, -4, 31, 38, 25, 100};
Output : 5
Minimum difference is between 1 and -4

Method 2: Efficient(O(nLogn))
The idea is to use sorting. Below are the steps.
- Sort array in ascending order. This step takes O(nLogn) time.
- Initialize the difference as infinte. This step takes O(1) time.
- Compare all adjacent pairs in sorted array and keep track of minimum difference. This 
step takes O(n) time.

Time Complexity: O(n log n).
Auxiliary Space: O(1).

"""
# function returns minimum difference between any pair
def findMinDiff(arr):

    n = len(arr)
    # sort array in non-decreasing order
    arr = sorted(arr)

    # Initialize differnce as Infinite
    diff =float('inf')

    # find the min diff by comparing adjacent pairs in sorted array
    for i in range(n-1):
        if(arr[i+1] - arr[i] < diff):
            diff = arr[i+1] - arr[i]

    return diff

print("Minimum difference is " + str(findMinDiff([1, 5, 3, 19, 18, 25])))
print("Extected: 1, Actual:", findMinDiff([1, 5, 3, 19, 18, 25]))
print("Extected: 4, Actual:", findMinDiff([30, 5, 20, 9]))
print("Extected: 5, Actual:", findMinDiff([1, 19, -4, 31, 38, 25, 100]))

print("\n my tests \n")

'''
my tests

'''
def my_tests(arr):
    min_diff =float('inf')
    nums =None
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if abs(arr[j] -arr[i]) < min_diff:
                min_diff = abs(arr[j] -arr[i])
                nums=[arr[j],arr[i]]
    return min_diff,nums

print("Extected: 1, Actual:", my_tests([1, 5, 3, 19, 18, 25]))
print("Extected: 4, Actual:", my_tests([30, 5, 20, 9]))
print("Extected: 5, Actual:", my_tests([1, 19, -4, 31, 38, 25, 100]))
