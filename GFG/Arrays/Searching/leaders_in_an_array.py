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


"""

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

def my_tests_two(arr):
    res =[]
    start =0
    end =len(arr)-1
    res.append(arr[end])
    end -=1
    while start <=end:
        if (check_if_greater(arr[end:], arr[end]) ==True):
            res.append(arr[end])
            end -=1
        end -=1
    res.reverse()
    return res


def check_if_greater(arr, key):
    return max(arr) ==key


print("Expected:", my_tests_two([16,17,4,3,5,2]))

def leader_array(arr):
    res =[]
    for i in range(len(arr)-1):
        new_arr =arr[i+1:]
        max_val =max(new_arr)
        if arr[i] >max_val:
            res.append(arr[i])
    res.append(arr[-1])
    return res

print("Expected:[17,5,2], Actual:", leader_array([16,17,4,3,5,2]))