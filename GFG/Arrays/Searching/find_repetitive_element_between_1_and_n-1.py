"""
Find the only repetitive element between 1 to n-1

We are given an array  arr[] of size n. Numbers are from 1 to (n-1) in random order. The array has
only one repetitive element. We need to find the repetitive element.

Examples:

    Input: a[] = {1, 3, 2, 3, 4}
    Output: 3

    Input : a[] = {1, 5, 1, 2, 3, 4}
    Output: 1

Method 1: Simple
- We use two nested loops
- The outer loop traverses through all elements and the inner loop checks if the element picked
by the outer loop appears anywhere else.

Time Complexity: O(n2)
Auxiliary Space: O(1)

"""
def find_repeating(arr):
    n = len(arr)
    for i in range(n):
      for j in range(i + 1, n):
        if (arr[i] == arr[j]):
          return arr[i];
         
print(find_repeating([9, 8, 2, 6, 1, 8, 5, 3, 4, 7]))

"""
Method 2: Using Sum Formula
- We know sum of first n-1 natural numbers is (n-1)*n/2. We compute sum of array elements and 
subtract natural number sum from it to find the only missing element.

Time Complexity: O(n)
Auxiliary Space: O(1)
Causes overflow for large arrays.

"""
def find_repeating_two(arr):
    n = len(arr)
    # find array sum and subtract sum, first n-1 natural numbers from it to find the result
    return sum(arr) -(((n-1) * n) // 2)


print("Two Expected:8, Actual:",find_repeating_two([9, 8, 2, 6, 1, 8, 5, 3, 4, 7]))

# does not work on the following case
print("Two Expected:97, Actual:",find_repeating_two([97, 18, 42, 86, 91, 38, 56, 39, 14, 97]))

"""

Method 4: Use Hashing

- use a hash table to store elements visitied. If a seen element appears again, we return it.

Time Complexity: O(n)
Auxiliary Space: O(n)

"""
# program to find the only repeating element in an array where elements are from 1 to n-1
def find_reapeating_three(arr):
    n = len(arr)
    s = set()

    for i in range(n):
        if arr[i] in s:
            return arr[i]
        s.add(arr[i])
    return -1

print("Three Expected:8, Actual:",find_reapeating_three([9, 8, 2, 6, 1, 8, 5, 3, 4, 7]))
print("Three Expected:8, Actual:",find_reapeating_three([9, 8, 2, 6, 1, 8, 5, 3]))
print("Three Expected:97, Actual:",find_reapeating_three([97, 18, 42, 86, 91, 38, 56, 39, 14, 97]))


"""
Method 5(Use XOR)
- The idea is based on the fact that x ^ x = 0 and x ^ y = y ^ x.
1) Compute XOR of elements from 1 to n-1.
2) Compute XOR of array elements.
3) XOR of above two would be our result.

Time Complexity: O(n)
Auxiliary Space: O(1)

"""
def find_repeating_four(arr):
    n = len(arr)

    # res is going to store value of 1^2^3..^(n-1)^arr[0] ^
    # arr[1] ^ .... arr[n-1]
    res = 0
    for i in range(0, n-1):
        res = res ^(i +1) ^ arr[i]
    res = res ^ arr[n-1]
    return res



print("Four Expected:8, Actual:",find_repeating_four([9, 8, 2, 6, 1, 8, 5, 3, 4, 7]))

# does not work for the following
print("Four Expected:8, Actual:",find_repeating_four([9, 8, 2, 6, 1, 8, 5, 3]))
print("Four Expected:97, Actual:",find_repeating_four([97, 18, 42, 86, 91, 38, 56, 39, 14, 97]))


"""

Method 6: Using indexing

1. Iterate through the array.
2. For every index visit a[index], it it is positive change the sign of element at a[index] index,
else print the element.

Time Complexity: O(n)
Auxiliary Space: O(1)

"""
def find_repeating_five(arr):
    n = len(arr)
    missingElement = 0

    # indexing based
    for i in range(0, n):

        element = arr[abs(arr[i])]
        if(element < 0):
            missingElement = arr[i]
            break
        arr[abs(arr[i])] = -arr[abs(arr[i])]
    return abs(missingElement)


print("Five Expected:8, Actual:",find_repeating_five([9, 8, 2, 6, 1, 8, 5, 3, 4, 7]))

# does not work on these two
# print("Five Expected:8, Actual:",find_repeating_five([9, 8, 2, 6, 1, 8, 5, 3]))
# print("Five Expected:97, Actual:",find_repeating_five([97, 18, 42, 86, 91, 38, 56, 39, 14, 97]))


"""
Method 7 : ( Linked-list cycle Method )

Use two pointers the fast and the slow. The fast one goes forward two steps each time, while the slow one goes only step each time. They must meet the same item when slow==fast. In fact, they meet in a circle, the duplicate number must be the entry point of the circle when visiting the array from array[0]. Next we just need to find the entry point. We use a point(we can use the fast one before) to visit form beginning with one step each time, do the same job to slow. When fast==slow, they meet at the entry point of the circle. The easy understood code is as follows.



"""


'''
my tests

'''

# Time complexity: O(n) | Space complexity: O(n)
def my_tests(arr):
    dic ={}
    for i in range(len(arr)):
        if arr[i] in dic:
            return arr[i]
        dic[arr[i]] =arr[i]

print("Expected:3, Actual:",my_tests([1, 3, 2, 3, 4]))
print("Expected:1, Actual:",my_tests([1, 5, 1, 2, 3, 4]))
print("Expected:8, Actual:",my_tests([9, 8, 2, 6, 1, 8, 5, 3, 4, 7]))
print("Expected:97, Actual:",my_tests([97, 18, 42, 86, 91, 38, 56, 39, 14, 97]))