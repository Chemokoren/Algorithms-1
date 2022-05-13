"""
reverse array/string

Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}

Iterative way :
 
1) Initialize start and end indexes as start = 0, end = n-1 
2) In a loop, swap arr[start] with arr[end] and change start and end as follows : 
start = start +1, end = end – 1

Time Complexity : O(n)
"""

def reverseList(A, start, end):
    while start < end:
        A[start],A[end] = A[end], A[start]
        start += 1
        end -= 1

A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)

"""
Recursive Way:

1) Initialize start and end indexes as start = 0, end = n-1 
2) Swap arr[start] with arr[end] 
3) Recursively call reverse for rest of the array.

Time Complexity : O(n)
"""

print(" ########### Recursive Way: ############ \n")
def reverseListRec(A,start, end):
    if start >= end:
        return
    A[start],A[end] =A[end],A[start]
    reverseList(A,start+1, end-1)


A = [1, 2, 3, 4, 5, 6]
print(A)
reverseListRec(A, 0, 5)
print("Reversed list is")
print(A)

"""
Using Python List slicing
"""
print("Python List slicing: \n")
def reverseListSlicing(A):
    print(A[::-1])

A = [1, 2, 3, 4, 5, 6]
print(A)
print("Reversed list is")
reverseListSlicing(A) 