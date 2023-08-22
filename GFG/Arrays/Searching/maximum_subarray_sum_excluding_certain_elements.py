"""
Maximum Subarray Sum Excluding Certain Elements

Given an array of A of n integers and an array B of m integers find the Maximum Contiguous 
Subarray Sum of array A such that any element of array B is not present in that subarray.

Examples : 

    Input : A = {1, 7, -10, 6, 2}, B = {5, 6, 7, 1} 
    Output : 2 

    Explanation
    
    Since the Maximum Sum Subarray of A is not allowed to have any element that is 
    present in array B. The Maximum Sum Subarray satisfying this is {2} as the only allowed 
    subarrays are:{-10} and {2}. The Maximum Sum Subarray being {2} which sums to 2

    Input : A = {3, 4, 5, -4, 6}, B = {1, 8, 5} 
    Output : 7

    Explanation 

    The Maximum Sum Subarray satisfying this is {3, 4} as the only allowed subarrays are 
    {3}, {4}, {3, 4}, {-4}, {6}, {-4, 6}. The Maximum Sum subarray being {3, 4} which sums to 7

Method 1: O(n*m)
We can solve this problem using the Kadane's algorithm. Since we don't want any of the elements
of array B to be part of any subarray of A, we need to modify the classical Kadane's Algorithm
alittle.

Whenever we consider an element in the Kadane's algorithm we either extend current subarray or we
start a new subarray.

curr_max = max(a[i], curr_max+a[i])
if (curr_max < 0)
    curr_max = 0

Now, in this problem when we consider any element, we check by linearly searching in the array B,
if that element is present in B then we set curr_max to zero which means that at that index all
subarrays we considered upto that point would end and not be extended further as no further 
contiguous arrays can be formed, i.e.

If Ai is present in B, all subarrays in A from 0 to (i – 1) cannot be extended further as, 
the ith element can never be included in any subarray

If the current element of array A is not part of array B, we proceed with the Kadane’s Algorithm 
and keep track of the max_so_far.

"""
# program to find max subarray sum excluding some elements

# function to check the element present in array B
INT_MIN =-float("inf")

def is_present(B, x):
    m = len(B)
    for i in range(0,m):
        if B[i] == x:
            return True
    return False

# Time Complexity:  O(n*m) | Auxiliary Space: O(1)
def find_max_subarray_sum(A,B):
    n = len(A)
    m = len(B)

    # set max_so_far to INT_MIN
    max_so_far = INT_MIN
    curr_max = 0
    for i in range(0, n):
        if is_present(B, A[i]) == True:
            curr_max = 0
            continue
            
        # proceed as in Kadane's Algorithm
        curr_max =max(A[i], curr_max + A[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far


print("Expected:7, Actual:", find_max_subarray_sum([3, 4, 5, -4, 6], [1, 8, 5]))
print("Expected:2, Actual:", find_max_subarray_sum([1, 7, -10, 6, 2], [5, 6, 7, 1]))


"""
Method 2: O((n+m) *log(m))

- This approach makes searching of an element of array A, in array B, faster by using 
Binary search

Note that we need to sort Array B to apply Binary search on it

Time Complexity: O(nlog(m) + mlog(m)) or O((n + m)log(m)). 
Note: The mlog(m) factor is due to sorting the array B.
Auxiliary Space: O(1)

"""

def binary_search(arr, key):
    arr.sort()
    i = 0
    j = len(arr)

    while (i <=j):
        mid = (i +j)//2
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            j = mid-1
        else:
            i = mid +1
    return False
        
def find_max_subarray_sum_two(arr1, arr2):

    max_so_far =-float("inf")
    current_max =0

    for i in range(len(arr1)):
        if binary_search(arr2,arr1[i]) == True:
            current_max =0
            continue
        
        current_max = max(arr1[i], current_max+arr1[i])
        max_so_far = max(max_so_far, current_max)
    return max_so_far

print("BS Expected:7, Actual:", find_max_subarray_sum_two([3, 4, 5, -4, 6], [1, 8, 5]))
print("BS Expected:2, Actual:", find_max_subarray_sum_two([1, 7, -10, 6, 2], [5, 6, 7, 1]))

"""
Method 3: O(max(n,m)) approach
- The main idea behind this approach is save B array in a map which will help you to check if A[i]
is present in B or not.

Time Complexity: O(max(n,m))
Auxiliary Space: O(n)

"""
# function calculates the max sum of contiguous subarray of B whose elements are not present in A
def find_max_sub_array_sum_three(A,B):

    m = dict()
    # Mark all the elements present in B
    for i in range(len(B)):
        if B[i] not in m:
            m[B[i]] = 0

        m[B[i]] = 1

    # Initialize max_so_far with INT_MIN
    max_so_far = -float("inf")-1
    currmax = 0

    # Traverse the array A
    for i in range(len(A)):
        if(currmax < 0 or (A[i] in m and m[A[i]] == 1)):
            currmax = 0
            continue

        currmax =max(A[i], A[i]+currmax)
        max_so_far=max(max_so_far, currmax)

    return max_so_far

print("map Expected:7, Actual:", find_max_sub_array_sum_three([3, 4, 5, -4, 6], [1, 8, 5]))
print("map Expected:2, Actual:", find_max_sub_array_sum_three([1, 7, -10, 6, 2], [5, 6, 7, 1]))




'''

my tests

'''

def my_tests(arr1, arr2):
    for i in range(len(arr2)):
        if arr2[i] in arr1:
            arr1.remove(arr2[i])
    print("aa", arr1)
    current_max = -float("inf")
    running_max = -float("inf")

    for i in range(len(arr1)):
        current_max =max(arr1[i], current_max+arr1[i])
        running_max =max(running_max, current_max)
    
    return running_max

print("Expected:7, Actual:", my_tests([3, 4, 5, -4, 6], [1, 8, 5]))
print("Expected:2, Actual:", my_tests([1, 7, -10, 6, 2], [5, 6, 7, 1]))