"""
Leaders in an array

Write a program to print all the LEADERS in the array. An element is a leader if it is greater
than all the elements to its right side. And the rightmost element is always as a leader. For 
example in the array [16,17,4,3,5,2], leaders are 17,5,2
Let the input array be arr[] and the size of the array be size

Method 1: Simple

Use two loops. The outer loop runs from 0 to size -1 and one by one picks all elements from left
to right. The inner loop compares the picked element to all the elements to its right side. If 
the picked element is greater than all the elements to its right side, then the picked element 
is the leader.

Time Complexity: O(n*n)

Auxiliary Space: O(1)

"""
def print_leaders_two(arr):
    res =[]
    size =len(arr)
    for i in range(0, size):
        for j in range(i+1, size):
            if arr[i] <= arr[j]:
                break
        if j == size-1: # if loop didn't break
            res.append(arr[i])
            # print(arr[i], end=' ')
    return res


print("Expected:", print_leaders_two([16,17,4,3,5,2]))


"""
Method 2: Scan from right

Scan all the elements from right to left in an array and keep track of maximum till now. When 
maximum changes its value, print it.
Below image is a dry run of the above approach.

Time Complexity: O(n)
Auxiliary Space: O(1)

"""
def leaders_in_arr(arr):
    max_val =-float("inf")
    res =[]

    for i in range(len(arr)-1,0,-1):
        if arr[i] > max_val:
            max_val =arr[i]
            res.append(max_val)
    res.reverse()
    return res

print(" KK Expected:", leaders_in_arr([16,17,4,3,5,2]))

"""
Method 3: 

In the above implementation we get time complexity O(n), but the output we get is not in the same 
order as the elements appear in our input array, so to get out output in the same order as in 
the input array, we can use stack data structure.

"""
# Time complexity: O(n) | Auxiliary space: O(n)
def leaders_in_arr_lifo(arr):
    max_val =-float("inf")
    res =[]

    for i in range(len(arr)-1,0,-1):
        if arr[i] > max_val:
            max_val =arr[i]
            res.append(max_val)
    for i in range(len(res)):
        print(res.pop(), end=' ')

print(" LIFO Expected:", leaders_in_arr_lifo([16,17,4,3,5,2]))




print("\n my tests \n")

'''
my tests
'''

def my_tests(arr):
    res =[]
    for i in range(len(arr), 0,-1):
        if i == len(arr)-1:
            res.append(arr[i])
        else:
            if arr[i-1] < arr[i] and i >2:
                    res.append(arr[i])
    return res

# print("Expected:", my_tests([16,17,4,3,5,2]))

# Time complexity O(n)
def my_tests_two(arr):
    res =[]
    start =0
    end =len(arr)-1
    res.append(arr[end])
    end -=1
    while start <=end:
        if (check_if_greater(arr[end:], arr[end]) == True):
            res.append(arr[end])
            end -=1
        end -=1
    res.reverse()
    return res


def check_if_greater(arr, key):
    return max(arr) ==key


print("Expected:", my_tests_two([16,17,4,3,5,2]))

# Time complexity: O(n) if max ==1 else O(n^2) if max =O(n)
def leader_array(arr):
    res =[]
    for i in range(len(arr)-1):
        new_arr =arr[i+1:]
        max_val =max(new_arr)
        if arr[i] >max_val:
            res.append(arr[i])
    res.append(arr[-1])
    return res

print("LL Expected:[17,5,2], Actual:", leader_array([16,17,4,3,5,2]))