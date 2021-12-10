"""
Reversal Algorithm Right Rotation Array

-reversal algorithm for right rotation of an array

Consider an arry, right rotate it by k elements

1,2,3,4,5,6,7,8,9,10
8,9,10,1,2,3,4,5,6,7

Input: arr[] = {121, 232, 33, 43 ,5}
           k = 2
Output: 43 5 121 232 33

Note : In the solution above, k is assumed to be smaller than or equal to n.
We can easily modify the solutions to handle larger k values by doing k = k % n
Algorithm: 
 

rotate(arr[], d, n)
  reverseArray(arr[], 0, n-1) ;
  reverse(arr[], 0, d-1);
  reverse(arr[], d, n-1);
"""

# program for right rotation of an array (Reversal algorithm)
# Function to reverse arr from index start to end

def reverseArray(arr,start,end):
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start =start +1
        end = end -1

# Function to right rotate arr of size n by d
def rightRotate(arr, d, n):
    reverseArray(arr,0, n-1)
    reverseArray(arr,0, d-1)
    reverseArray(arr,d, n-1)

# function to pr an array
def prArray(arr, size):
    for i in range(0, size):
        print(arr[i], end =' ')


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
k = 3
     
# Function call
rightRotate(arr, k, n)
prArray(arr, n)


