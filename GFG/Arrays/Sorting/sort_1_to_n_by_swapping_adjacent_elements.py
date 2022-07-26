"""
Sort 1 to N by swapping adjacent elements

Given an array, A of size N consisting of elements 1 to N. A boolean array B consisting
of N-1 elements indicates that if B[i] is 1, then A[i] can be swapped with A[i+1].
Find out if A can be sorted by swapping elements.

Examples: 
 

Input : A[] = {1, 2, 5, 3, 4, 6}
        B[] = {0, 1, 1, 1, 0}
Output : A can be sorted
We can swap A[2] with A[3] and then A[3] with A[4].

Input : A[] = {2, 3, 1, 4, 5, 6}
        B[] = {0, 1, 1, 1, 1}
Output : A can not be sorted
We can not sort A by swapping elements as 1 can never be swapped with A[0]=2.

Here we can swap only A[i] with A[i+1]. So to find whether array can be sorted or not, 
Using boolean array B we can sort array for a continuous sequence of 1 for B. At last, 
we can check, if A is sorted or not.


Time Complexity: O(n*n*logn), where n time is used for iterating and n*logn for sorting 
inside the array
Auxiliary Space: O(1), as no extra space is required


"""
# program to test whether an array can be sorted by swapping adjacent elements using
# a bookean array


# return true if array can be sorted otherwise false
def sorted_after_swap(A,B):

    n = len(A)

    # check bool array B and sort elements for continuous sequence of 1
    for i in range(0, n-1):
        if(B[i] == 1):
            j = i
            while(B[j] == 1):
                j = j+1

            # Sort array A from i to j
            A = A[0:i] + sorted(A[i:j+1]) + A[j+1:]
            i = j

    # check if array is sorted or not
    for i in range(0, n):
        if(A[i] != i+1):
            return False

    return True


print("Expected:True, Actual:",sorted_after_swap([ 1, 2, 5, 3, 4, 6 ], [ 0, 1, 1, 1, 0 ]))

"""
Alternative Approach
--------------------
- It gives O(n) time for all cases.
- The idea here is that whenever the binary array has 1, we check if that index in array
A has i+1 or not. If it does not contain i+1, we simply swap a[i] with a[i+1]. The reason
for this is that the array should have i+1 stored at index i. And if at all the array is
sortable, then the only operation allowec is swapping. Hence, if the required condition is
not satisfied, we simply swap. If the array is sortable, swapping will take us one step
closer to the correct answer. And as expected, if the array is not sortable, then swapping
would lead to just another unsorted version of the same array.

Time Complexity: O(n)
Auxiliary Space: O(1)

"""
# return true if array can be sorted otherwise false
def sorted_after_swap_alternative(A, B):
    n = len(A)

    for i in range(0, n-1):
        if B[i]:
            if A[i] != i+1:
                A[i], A[i+1] = A[i+1], A[i]

    # check if array is sorted or not
    for i in range(n):
        if A[i] !=i+1:
            return False
    return True

print("Expected: True, Actual: ", sorted_after_swap_alternative([1, 2, 5, 3, 4, 6], [0, 1, 1, 1, 0]))






print("\n my tests \n ")

'''
my tests

'''
def my_tests(arr):
    start = 0
    end = len(arr)-1

    while start < end:
        if arr[start] > arr[start+1]:
            arr[start], arr[start+1] =arr[start+1],arr[start]
        start +=1
    return arr

print("Expected:[1, 2, 3, 4, 5, 6], Actual:", my_tests([1, 2, 5, 3, 4, 6]))
print("Expected:[1, 2, 3, 4, 5, 6], Actual:", my_tests([2, 3, 1, 4, 5, 6]))
