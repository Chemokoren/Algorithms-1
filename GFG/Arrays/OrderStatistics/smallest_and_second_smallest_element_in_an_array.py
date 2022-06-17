"""
Find the smallest and second smallest elements in an array

Simple solution
-sort the array in increasing order. The first two elements in sorted array would be two smallest
elements.
-time complexity: O(n Log n)

Better Solution
- scan the array twice. In first traversal find the minimum element. Let this element be x. In
second traversal, find the smallest element greater than x. 
Time complexity: O(n)

Efficient soluion
- find the minimum two elements in one traversal

Algorithm:
1) initialize both first and second smallest as INT_MAX
first = second = INT_MAX
2) Loop through all the elements.
a) if the current element is smaller than first, then update first and second
b) Else if the current element is smaller than second then update the second

The same approach can be used to find the largest and second largest elements in an array.

Time Complexity: O(n)
"""

# program to find smallest and second smallest elements
import sys
def print2Smallest(arr):
    # There should be atleast two elements
    arr_size =len(arr)
    if arr_size < 2:
        print(" Invalid Input ")
        return

    first = second =sys.maxsize
    for i in range(0, arr_size):
        # If current element is smaller than first then update both first & second
        if arr[i] < first:
            second = first
            first = arr[i]

        # if arr[i] is in between first and second then update second
        if (arr[i] < second and arr[i] != first):
            second =arr[i]

    if(second == sys.maxsize):
        print("No second smallest element")
    else:
        print("The smallest element is", first, " and second smallest element is ", second)

arr = [12, 13, 1, 10, 34, 1]
print2Smallest(arr)


'''
my tests

'''

def find_smallest_2nd_smallest(arr):
	new_list=list(set((arr)))
	new_list.sort()
	return new_list[:2]
	
print("expected:[1, 10], actual:",find_smallest_2nd_smallest([12, 13, 1, 10, 34, 1]))


def smallest_2nd_smallest(arr):
	smallest = float('inf')
	second_smallest = float('inf')
	for i in range(len(arr)):
		if arr[i] < smallest:
			smallest =arr[i]
			
	for i in range(len(arr)):
		if(arr[i] < second_smallest and arr[i] > smallest):
			second_smallest =arr[i]
			
	return smallest, second_smallest
	

print("expected:[1, 10], actual:",smallest_2nd_smallest([12, 13, 1, 10, 34, 1]))	

def smallest_2nd_smallest_two(arr):
	smallest =second_smallest= float('inf')
	 
	for i in range(len(arr)):
		if arr[i] < smallest:
			second_smallest =smallest
			smallest =arr[i]
		elif arr[i] < second_smallest and arr[i] !=smallest:
			second_smallest =arr[i]
			
	return smallest, second_smallest
	

print("expected:[1, 10], actual:",smallest_2nd_smallest_two([12, 13, 1, 10, 34, 1]))		
