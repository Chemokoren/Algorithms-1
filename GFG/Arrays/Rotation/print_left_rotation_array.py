"""
Print left rotation of array in O(n) time and O(1) space

Given an array of size n and multiple values around which we need to left rotate
the array. How to quickly print multiple left rotations?

Input : 
arr[] = {1, 3, 5, 7, 9}
k1 = 1
k2 = 3
k3 = 4
k4 = 6

Output : 

3 5 7 9 1
7 9 1 3 5
9 1 3 5 7
3 5 7 9 1


Input : 

arr[] = {1, 3, 5, 7, 9}
k1 = 14 

Output : 
9 1 3 5 7

"""

# program to implement left rotation of an array K number of times

# Function to leftRotate array multiple times
def leftRotate(arr, n, k):
    # To get the starting point of rotated array
    mod = k % n

    # prints the rotated array from start position
    for i in range(n):
        print(str(arr[(mod + i) % n]),end=" ")
    print()
    return

arr = [1, 3, 5, 7, 9]
n = len(arr)
k = 2
 
# Function Call
leftRotate(arr, n, k)
 
k = 3
 
# # Function Call
leftRotate(arr, n, k)
 
# k = 4
 
# # Function Call
leftRotate(arr, n, k)

print("Method II: \n")

"""
Method II:  

The implementation we will use Standard Template Library (STL) which will be making
the solution more optimize and easy to Implement.

"""

# implementation to print left rotation of any array K times
from collections import deque

# Function For the K Times Left Rotation
def leftRotateUpdated(arr,k,n):
    # The collections module has a deque class which provides the rotate(), which is
    # inbuilt function to allow rotation
    arr =deque(arr)

    # using rotate() to left rotate by k
    arr.rotate(-k)
    arr = list(arr)


    # print the roated array from the start position

    for i in range(n):
        print(arr[i], end=" ")

if __name__ == '__main__':
       
    arr = [ 1, 3, 5, 7, 9 ]
    n = len(arr)
    k = 2
   
    print("approach 1:\n")

    leftRotateUpdated(arr, k, n)

    print("approach 2:\n")
    k = 14 
    leftRotateUpdated(arr, k, n)
    #Output : 9 1 3 5 7

