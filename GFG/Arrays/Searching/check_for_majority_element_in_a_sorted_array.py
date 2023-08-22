"""
Check for Majority Element in a sorted array

write a function to find if a given integer x appears more than n/2 times in  a sorted array of
n integers.

Basically, we need to write a function say isMajority() that takes an array (arr[] ), array’s size (n) and a number to be searched (x) as parameters and returns true if x is a majority element (present more than n/2 times).

Examples: 

Input: arr[] = {1, 2, 3, 3, 3, 3, 10}, x = 3
Output: True (x appears more than n/2 times in the given array)

Input: arr[] = {1, 1, 2, 4, 4, 4, 6, 6}, x = 4
Output: False (x doesn't appear more than n/2 times in the given array)

Input: arr[] = {1, 1, 1, 2, 2}, x = 1
Output: True (x appears more than n/2 times in the given array)


Using Binary Search

- Use binary search methodology to find the first occurrence of the given number. 
The criteria for binary search is important here.

Time Complexity: O(Logn) 

Auxiliary Space: O(1)
"""

# This function returns true if the x is present more than n / 2
# times in arr[] of size n */
def isMajority(arr, x):
    n =len(arr)
    
    # Find the index of first occurrence of x in arr[] */
    i = _binarySearch(arr, 0, n-1, x)
    
    # If element is not present at all, return false*/
    if i == -1:
        return False
        
    # check if the element is present more than n / 2 times */
    if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
        return True
    else:
        return False

# If x is present in arr[low...high] then returns the index of
# first occurrence of x, otherwise returns -1 */
def _binarySearch(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 # low + (high - low)//2;

		''' Check if arr[mid] is the first occurrence of x.
			arr[mid] is first occurrence if x is one of the following
			is true:
			(i) mid == 0 and arr[mid] == x
			(ii) arr[mid-1] < x and arr[mid] == x'''
		
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return _binarySearch(arr, (mid + 1), high, x)
		else:
			return _binarySearch(arr, low, (mid -1), x)
	return -1



print("Expected: True, Actual:", isMajority([1, 2, 3, 3, 3, 3, 10], 3))



"""
Algorithmic Paradigm: Divide and Conquer

METHOD 3: 
it is already given that the array is sorted and there exists a majority element,
checking if a particular element is as easy as checking if the middle element of the array is 
the number we are checking against.

Since a majority element occurs more than n/2 times in an array, it will always be the middle 
element. We can use this logic to check if the given number is the majority element.

"""
# Time complexity: O(1) | Auxiliary Space: O(1)
def is_majority_element(arr,key):
    n = len(arr)
    if(arr[n//2]) == key:
        return True
    return False

print("Expected:, Actual:", is_majority_element([1, 2, 3, 3, 3, 3, 10], 3))

