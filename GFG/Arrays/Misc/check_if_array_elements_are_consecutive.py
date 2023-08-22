"""
Check if array elements are consecutive

Given an unsorted array of numbers, write a function that returns true if the array consists of
consecutive numbers

Examples: 
a) If the array is {5, 2, 3, 1, 4}, then the function should return true because the array has consecutive numbers from 1 to 5.
b) If the array is {83, 78, 80, 81, 79, 82}, then the function should return true because the array has consecutive numbers from 78 to 83.
c) If the array is {34, 23, 52, 12, 3}, then the function should return false because the elements are not consecutive.
d) If the array is {7, 6, 5, 5, 3, 4}, then the function should return false because 5 and 5 are not consecutive.

Method 1 (Use Sorting)

1) Sort all the elements. 
2) Do a linear scan of the sorted array. If the difference between the current element and the 
next element is anything other than 1, then return false. If all differences are 1, then return 
true.

Method 2: Use visited array

if the following two conditions are true, then return true.
1) max - min +1 =n  where max is the maximum element in the array, min is the minimum element in
the array and n is the number of elements in the array.
2) All elements are distinct
- To check if all elements are distinct, we can create a visited[] array of size n. Then,we can
map the ith element of input array arr[] to the visited array by using arr[i] - min as the index
in visited[].


"""
# Time Complexity: O(n) | Auxiliary Space: O(n) 
def are_consecutive(arr):
    n =len(arr)

    if(n < 1):
        return False

    # 1) Get the Minimum element in array
    min_val =min(arr)

    # 2) Get the Maximum element in array
    max_val =max(arr)

    # 3) max_val -min_val +1 is equal to n
    if(max_val - min_val)+1 == n:

        # create a temp array to hold visited flag of all elements. Note that, calloc is used here
        # so that all values are initialized as false
        visited =[False for i in range(n)]

        for i in range(n):

            # if we see an element again, then return false
            if visited[arr[i] -min_val] != False:
                return False

            # if visited first time, then mark the element as visited
            visited[arr[i] - min_val] = True


        # if all elements occur once, then return True
        return True
    return False # (if max_val -min_val+1 !=n )


if(are_consecutive([5, 4, 2, 3, 1, 6]) == True):
    print("Array elements are consecutive ")
else:
    print("Array elements are not consecutive ")

"""
Method 3: Mark visited array elements as negative
- This method is O(n) time complexity and O(1) extra space, but it changes the original array, 
and it works only if all numbers are positive. We can get the original array by adding an extra 
step though. It is an extension of method 2, and it has the same two steps.

1) max – min + 1 = n where max is the maximum element in the array, min is the minimum element in 
the array and n is the number of elements in the array. 
2) All elements are distinct.
In this method, the implementation of step 2 differs from method 2. Instead of creating a new 
array, we modify the input array arr[] to keep track of visited elements. The idea is to traverse 
the array and for each index i (where 0 ≤ i < n), make arr[arr[i] – min]] as a negative value. 
If we see a negative value again then there is repetition. 


Note that this method might not work for negative numbers. For example, it returns false for {2, 1, 0, -3, -1, -2}.
Time Complexity: O(n) 
Auxiliary Space: O(1) 

"""
def are_consecutive_two(arr):
    n = len(arr)

    if(n < 1):
        return False
    
    # 1) Get the minimum element in array
    min_val =getMin(arr)

    # 2) Get the maximum element in array
    max_val =getMax(arr)

    # max_val - min_val +1 is equal to n then only check all elements
    if(max_val - min_val +1 == n):

        for i in range(n):
            if(arr[i] < 0):
                j =-arr[i] - min_val
            else:
                j =arr[i] - min_val

            # if the value at index j is negative then there is repetition
            if(arr[j] > 0):
                arr[j] =-arr[j]
            else:
                return False

        # if we do not see a negative value then all elements are distinct
        return True

    return False


def getMin(arr):
    n = len(arr)
     
    min = arr[0]
    for i in range(1, n):
        if (arr[i] < min):
            min = arr[i]
    return min
 
def getMax(arr):
    n = len(arr)
    max = arr[0]
    for i in range(1, n):
        if (arr[i] > max):
            max = arr[i]
    return max
 
if(are_consecutive_two([1, 4, 5, 3, 2, 6]) == True):
        print(" Array elements are consecutive ")
else:
        print(" Array elements are not consecutive ")


"""
This method is O(n) time complexity and O(1) extra space, does not changes the original array, 
and it works every time.

    As elements should be consecutive, let’s find minimum element or maximum element in array.
    Now if we take xor of two same elements it will result in zero (a^a = 0).
    Suppose array is {-2, 0, 1, -3, 4, 3, 2, -1}, now if we xor all array elements with minimum
    element and keep increasing minimum element, the resulting xor will become 0 only if elements 
    are consecutive
     
Time Complexity: O(n) 
Auxiliary Space: O(1) 

"""
def are_consecutive_three(arr):
    n = len(arr)
    min_val = arr.index(min(arr))
    num = 0
    for i in range(0, n):
        num ^= arr[min_val] ^ arr[i]
        arr[min_val] +=1
    if num == 0:
        return True
    return False

if are_consecutive_three([1, 4, 5, 3, 2, 6]) == True:
        print(" Array elements are consecutive three", end=' ')
else:
    print(" Array elements are not consecutive three ", end=' ')


print("\n my tests\n")
'''
my tests
'''
# Time Complexity: O(n)  | Auxiliary Space: O(n) 
def my_tests_two(arr):
    max_val, min_val =max(arr), min(arr)
    if (max_val-min_val) + 1== len(arr) and are_there_duplicates(arr) == False:
        return True
    else:
        return False

def are_there_duplicates(arr):
    dic =dict()
    for i in range(len(arr)):
        if arr[i] in dic:
            return True
        else:
            arr[i] =1
    return False

print("Expected: True, Actual:", my_tests_two([5, 2, 3, 1, 4]))
print("Expected: True, Actual:", my_tests_two([83, 78, 80, 81, 79, 82]))
print("Expected: False, Actual:", my_tests_two([34, 23, 52, 12, 3]))
print("Expected: False, Actual:", my_tests_two([7, 6, 5, 5, 3, 4]))


# Time Complexity: O(n log n) | Space Complexity: O(1) 
def my_tests(arr):
    arr.sort()
    i =0
    while i <len(arr)-1:
        if arr[i]+1 != arr[i+1]:
            return False
        i +=1
    return True

print("Expected: True, Actual:", my_tests([5, 2, 3, 1, 4]))
print("Expected: True, Actual:", my_tests([83, 78, 80, 81, 79, 82]))
print("Expected: False, Actual:", my_tests([34, 23, 52, 12, 3]))
print("Expected: False, Actual:", my_tests([7, 6, 5, 5, 3, 4]))

