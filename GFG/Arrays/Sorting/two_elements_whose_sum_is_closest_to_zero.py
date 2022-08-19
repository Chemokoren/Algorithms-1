"""
Two elements whose sum is closest to zero

An array of integers is given, both +ve and -ve. You need to find the two elements such that
their sum is closest to zero.

METHOD 1: Simple

For each element, find the sum of it with every other element in the array and compare sums.
Finally, return the minimum sum.

METHOD -2
- sort all the elements of the input array using their absolute values
- check absolute sum of arr[i-1] and arr[i] if their absolute sum is less than min update
min with their absolute value
- use two variables to store the index of the elements

Time Complexity: O(nlogn) 
Auxiliary Space : O(1)

"""
def findMinSum(arr):

    n =len(arr)

    for i in range(1,n):

        # Modified to sort by absolute values
        if(not abs(arr[i-1]) < abs(arr[i])):
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
        
    min_val =float('inf')
    x = 0
    y = 0

    for i in range(1, n):

        # Absolute value shows how close it is to zero
        if(abs(arr[i-1] +arr[i]) <= min_val):
            min_val =abs(arr[i-1] + arr[i])
            x = i -1
            y = i
    return arr[x], arr[y]

print("Expected:::::", findMinSum([ 1, 60, -10, 70, -80, 85 ]))







'''
my tests
'''
# Time Complexity: complexity to sort + complexity of finding the 
# optimum pair = O(nlogn) + O(n) = O(nlogn)
# Auxiliary Space: O(1)
def my_tests(arr):
    arr.sort()
    smallest =float('inf')

    start =0
    end =len(arr)-1
    i =0
    j= 0

    if len(arr) < 2:
        return "Invalid Input"

    while start <= end:

        sum_val =arr[end]+arr[start]
        if abs(sum_val) < smallest:
            smallest = abs(sum_val)
            i =start
            j =end

        if(sum_val < 0):
            start +=1
        else:
            end -=1
 
    return smallest

print("Expected:[-80,85], Actual:", my_tests([1, 60, -10, 70, -80, 85]))
print("Expected: Invalid Input, Actual:", my_tests([1]))

def my_tests_two(arr):
    
    smallest =float('inf')
    start =None
    end =None

    if(len(arr)) <2:
        return "Invalid Input"

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs((arr[i] + arr[j])) < smallest:
                smallest=abs(arr[i] + arr[j])
                start = arr[i]
                end   = arr[j]

    return smallest, start, end

print("Expected:[-80,85], Actual:", my_tests_two([1, 60, -10, 70, -80, 85]))
print("Expected: Invalid Input, Actual:", my_tests_two([1]))
