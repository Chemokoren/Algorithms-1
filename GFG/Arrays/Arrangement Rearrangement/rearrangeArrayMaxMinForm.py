"""
Given a sorted array of positive integers, rearrange the array alternately i.e first element should be maximum value, second minimum value, third second max, fourth second min and so on. 

Examples: 

Input: arr[] = {1, 2, 3, 4, 5, 6, 7} 
Output: arr[] = {7, 1, 6, 2, 5, 3, 4}

Input: arr[] = {1, 2, 3, 4, 5, 6} 
Output: arr[] = {6, 1, 5, 2, 4, 3} 

Expected time complexity: O(n).

The idea is to use an auxiiliary array. We maintain two pointers one to the leftmost or
smallest element and other to rightmost or largest element. We move both pointers 
toward each other and altervatively copy elements at these pointers to an auxiliary array. 
Finally, we copy the auxiliary array back to the original array.

Time Complexity: O(n) 
Auxiliary Space: O(n) 

"""

# program to rearrange an array in minimum-max form

# prints max at first positio, min at second position, second max at third position, second
# min at fourth position  etc.

def rearrange(arr, n):
    # Auxiliary array to hold modified array
    temp = n * [None]

    # Indexes of smallest and largest elements from remaining array.
    small, large =0, n-1

    # To indicate whether we need to copy remaining largest or remaining smallest at next
    # position
    flag = True

    # store result in temp[]
    for i in range(n):
        if flag is True:
            temp[i] = arr[large]
            large -= 1
        else:
            temp[i] = arr[small]
            small += 1

        flag =bool(1-flag)

    # copy temp[] to arr[]
    print("aaaaa: ", temp)
    for i in range(n):
        arr[i] = temp[i]
    return arr

arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
print("Original Array")
print(arr)
print("Modified Array")
print(rearrange(arr, n))

print("\n Rearrange an array in maximum minimum form | Set 2 (O(1) extra space)\n ")
"""
Rearrange an array in maximum minimum form | Set 2 (O(1) extra space)

The idea is to use multiplication and modular trick to store two elements at an index
Solution:
O(n) time 
O(1) space

even index: remaining maximum element.

odd index: remaining minimum element.

max_index: Index of remaining maximum element
            (moves from right to left)

min_index: Index of remaining minimum element
            (moves from left to right)

Initialize: max_index ='n-1'
            min_index = 0
            max_element =arr[max_index] + 1  // can be any element which is more than the max value in array

For i = o to n-1
    if 'i' is even
    arr[i] += arr[max_index] % max_element * max_element
    max_index--
Else // if 'i' is odd
    arr[i] += arr[min_index] % max_element * max_element
    min_index++

How does expression "arr[i] += arr[max_index] % max_element * max_element " work?

The purpose of this expression is to store two elements at index arr[i].
arr[max_index] is stored as multiplier and "arr[i]" is stored as remainder. For example
in {1 2 3 4 5 6 7 8 9}, max_element is 10 and we store 91 at index 0. With 91, 
we can get original as 91%10  and new element as 91/10
"""

def rearrange(arr, n):
    # initialize index of first minimum and first maximum element
    max_idx = n-1
    min_idx = 0

    # store maximum element of array
    max_elem = arr[n-1]+ 1

    # Traverse array elements
    for i in range(0, n):

        if i % 2 == 0:
            arr[i] += (arr[max_idx] % max_elem) * max_elem
            max_idx -= 1

        # At odd index : we have to put minimum element
        else:
            arr[i] += (arr[min_idx] % max_elem) * max_elem
            min_idx += 1

    # array elements back to it's original form
    for i in range(0, n):
        arr[i] = arr[i] / max_elem


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
 
print ("Original Array")
 
for i in range(0, n):
    print (arr[i], end = " ")
     
rearrange(arr, n)
 
print ("\nModified Array")
for i in range(0, n):
    print (int(arr[i]), end = " ")


print("\n A simpler approach \n")
"""

A simpler approach will bet to observe indexing positioning of maximum elements and 
minimum elements. The even index stores maximum elements and the odd index stores 
the minimum elements. With every increasing index, the maximum element decreases by one
and the minimum  element increases by one. A simple traversal can be done and arr[] can
be filled in again.
Note: This approach is only valid when elements of given sorted array are consecutive i.e.
vary by one unit.
"""

def rearrange(arr, n):
    # initialize index of first minimum & first maximum element
    max_ele =arr[n-1]
    min_ele =arr[0]

    # traverse array elements
    for i in range(n):
        # at even index: we have to put maximum element
        if i % 2 == 0:
            arr[i] = max_ele
            max_ele -= 1

        # at odd index: we have to put minimum element
        else:
            arr[i] = min_ele
            min_ele += 1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = len(arr)
print("Origianl Array")
for i in range(n):
    print(arr[i], end = " ")
 
rearrange(arr, n)
print("\nModified Array")
for i in range(n):
    print(arr[i], end = " ")


