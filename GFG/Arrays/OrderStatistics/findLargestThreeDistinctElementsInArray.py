"""
Find the largest three distinct elements in an array

- Given an array with all distinct elements, find largest three elements.
Expected time complexity is O(n) and extra space is O(1)

Input: arr[] = {10, 4, 3, 50, 23, 90}
Output: 90, 50, 23

Method 1: Algorithm

1) Initialize the largest three elements as minus infinite. 
first = second =third = - infinity

2) Iterate through all elements of array.
a) Let current array element be x.
b) If (x > first){
    # This order of assignment is important
    third = second
    second = first
    first = x
c) Else if (x > second){
    third = second
    second = x
}
d) Else if (x > third){
    third = x
}

3) print first, second, and third


"""

import sys

# Function to print three largest elements
def print3largest(arr, arr_size):
    # There should be atleast three elements
    if(arr_size < 3):
        print(" Invalid Input ")
        return

    third = first =second =-sys.maxsize

    for i in range(0, arr_size):
        # If current element is greater than first
        if(arr[i] > first):
            third =second
            second = first
            first = arr[i]

        # If arr[i] is in between first and second then update second
        elif(arr[i] > second):
            third = second
            second = arr[i]

        elif(arr[i] > third):
            third = arr[i]

    print("Three largest elements are", first, second, third, "\n")

arr = [12, 13, 1, 10, 34, 1]
n = len(arr)
print3largest(arr, n)


print("\n An efficient way to solve this problem: \n")
"""
An efficient way to solve this problem is to use any O(nLogn) sorting algorithm
& simply returning the last 3 largest elements

"""

# code to find largest three elements in an array
def find3largest(arr, n):
    arr = sorted(arr) # It uses tuned Quicksort with avg. case time complexity = O(nLogn)

    check = 0
    count = 1

    for i in range(1, n + 1):
        if(count < 4):
            if(check != arr[n - i]):

                # to handle duplicate values 
                print(arr[n-i], end=" ")
                check = arr[n - i]
                count += 1

        else:
            break

arr = [12, 45, 1, -1, 45, 54, 23, 5, 0, -10]
n = len(arr)
find3largest(arr, n)


print("\n my exploration: \n")
def printThreeLargest(arr, n):
    arr.sort(reverse=True)

    for  i in range(n):
        print(arr[i], end=" ")

arr =[10, 4, 3, 50, 23, 90]
n = len(arr)
printThreeLargest(arr, 3)
