"""
Find Second largest element in an array
Difficulty Level : Easy
Last Updated : 08 Jul, 2021
Given an array of integers, our task is to write a program that efficiently finds the second largest element present in the array. 
Example:

Input: arr[] = {12, 35, 1, 10, 34, 1}
Output: The second largest element is 34.
Explanation: The largest element of the 
array is 35 and the second 
largest element is 34

Input: arr[] = {10, 5, 10}
Output: The second largest element is 5.
Explanation: The largest element of 
the array is 10 and the second 
largest element is 5

Input: arr[] = {10, 10, 10}
Output: The second largest does not exist.
Explanation: Largest element of the array 
is 10 there is no second largest element

Simple solution: 

sort the array in descending order and then return the second element which is not equal to 
the largest element from the sorted array.

Complexity Analysis:

Time Complexity: O(n log n). 
Time required to sort the array is O(n log n).
Auxiliary space: O(1). 
As no extra space is required.

"""
def print2largest(arr, arr_size):
    # There should be atleast two elements
    if(arr_size < 2):
        print("Invalid Input ")
        return 

    arr.sort

    #start from second last element as the largest element is at last
    for i in range(arr_size-2, -1, -1):
        # if the element is not equal to largest element
        if(arr[i] != arr[arr_size -1]):
            print("The second largest element is", arr[i])

        return

    print("There is no second largest element")


arr = [12, 35, 1, 10, 34, 1]
n = len(arr)
print2largest(arr, n)

print("\n Better solution: \n")

"""
Better solution:

The approach is to traverse the array twice. In the first traversal, find the maximum element.
In the second traversal find the greatest element less than the element obtained in the first
traversal.

Complexity Analysis:

Time Complexity: O(n). 
Two traversals of the array is needed.
Auxiliary space: O(1). 
As no extra space is required.


"""

# program to find second largest element in an array 
def print2largest(arr, arr_size):
    # There should be atleast two elements
    if(arr_size < 2):
        print(" Invalid Input ")
        return

    largest = second = -2454635434

    # find the largest element
    for i in range(0, arr_size):
        largest = max(largest, arr[i])

    print("largest:::::", largest)

    # find the second largest element
    for i in range(0, arr_size):
        if(arr[i] != largest):
            second = max(second, arr[i])

    if(second == -2454635434):
        print("There is no second largest element")

    else:
        print("The second largest element is: ",second)


if __name__ == '__main__':
   
    arr = [12, 35, 1,10, 34, 1]
    n = len(arr)
    print2largest(arr, n)


print("\n Efficient solution: \n")
"""
Efficient solution

Find the second largest element in a single traversal

1) Initialize two variables first and second to INT_MIN as
   first = second = INT_MIN
2) Start traversing the array,
   a) If the current element in array say arr[i] is greater
      than first. Then update first and second as,
      second = first
      first = arr[i]
   b) If the current element is in between first and second,
      then update second to store the value of current variable as
      second = arr[i]
3) Return the value stored in second.

Complexity Analysis:

Time Complexity: O(n). 
Only one traversal of the array is needed.
Auxiliary space: O(1). 
As no extra space is required.

"""
def print2largest(arr, arr_size):
    # There should be atleast two elements
    if(arr_size < 2):
        print(" Invalid Input ")
        return

    first = second =-2147483648

    for i in range(arr_size):
        # if current element is smaller than first then update both first & second
        if(arr[i] > first):
            second = first
            first = arr[i]

        # if arr[i] is in between first and second then update second
        elif (arr[i] > second and arr[i] != first):
            second =arr[i]


    if(second == -2147483648):
        print("There is no second largest element")

    else:
        print("The second largest element is", second)


arr = [12, 35, 1, 10, 34, 1]
n = len(arr)
 
print2largest(arr, n)


'''

my tests

'''


def find_second_largest(arr):
	dic =set((arr))
	new_arr=list(dic)
	new_arr.sort(reverse=True)
	
	return new_arr[1] if len(new_arr) >=2 else None
 
print()	
print("expected: 34, actual: ", find_second_largest([12, 35, 1, 10, 34, 1]))
print("expected: 5, actual: ", find_second_largest([10, 5, 10]))
print("expected: [], actual: ", find_second_largest([10, 10, 10]))


def find_second_largest_two(arr):
	largest =-float('inf')
	
	for i in range(len(arr)):
		if arr[i] > largest :
			largest =arr[i]

	arr.remove(largest)
	
	for i in range(len(arr)):
		if arr[i] > largest :
			largest =arr[i]
		
	return largest
	
print("\n second trial \n")	
print("expected: 34, actual: ", find_second_largest_two([12, 35, 1, 10, 34, 1]))
print("expected: 5, actual: ", find_second_largest_two([10, 5, 10]))
print("expected: [], actual: ", find_second_largest_two([10, 10, 10]))


def find_second_largest_three(arr):
	dic =set((arr))
	largest = -float('inf')
	for i in dic:
		if i > largest :
			largest =i
	dic.remove(largest)
	
	largest = -float('inf')
	for i in dic:
		if i > largest :
			largest =i
	return largest
	
	
print("\n third trial \n")	
print("expected: 34, actual: ", find_second_largest_three([12, 35, 1, 10, 34, 1]))
print("expected: 5, actual: ", find_second_largest_three([10, 5, 10]))
print("expected: [], actual: ", find_second_largest_three([10, 10, 10]))