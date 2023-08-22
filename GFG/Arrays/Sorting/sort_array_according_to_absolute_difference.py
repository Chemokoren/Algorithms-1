"""

Sort an array according to absolute differece with given value

Given an array of n distinct elemenets and a number x, arrange array elements according
to the absolute difference with x, i.e., an element having minimum difference comes first,
and so on.
Note: If two or more elements are at equal distance arrange them in the same
sequence as in the given array.

Input : arr[] : x = 7, arr[] = {10, 5, 3, 9, 2}
Output : arr[] = {5, 9, 10, 3, 2}
Explanation:
7 - 10 = 3(abs)
7 - 5 = 2
7 - 3 = 4 
7 - 9 = 2(abs)
7 - 2 = 5
So according to the difference with X, 
elements are arranged as 5, 9, 10, 3, 2.

Input : x = 6, arr[] = {1, 2, 3, 4, 5}   
Output :  arr[] = {5, 4, 3, 2, 1}

Input : x = 5, arr[] = {2, 6, 8, 3}   
Output :  arr[] = {6, 3, 2, 8}

The idea is to use a self-balancing binary search tree. We traverse the input array and 
for every element, we find its difference with x and store the difference as key and 
element as the value in a self-balancing binary search tree. Finally, we traverse the 
tree and print its inorder traversal which is the required output.

C++ Implementation : 
In C++, self-balancing-binary-search-tree is implemented by set, map, and multimap. 
We can’t use set here as we have key-value pairs (not only keys). We also can’t directly 
use map also as a single key can belong to multiple values and map allows a single value 
for a key. So we use multimap which stores key-value pairs and can have multiple values 
for a key.

    Store the values in the multimap with the difference with X as key.
    In multimap, the values will be already in sorted order according to key i.e. 
    difference with X because it implements self-balancing-binary-search-tree internally.
    Update all the values of an array with the values of the map so that the array has 
    the required output.

Time Complexity: O(n Log n) 
Auxiliary Space: O(n)

"""

# Python3 program to sort an
# array according absolute
# difference with x.

# Function to sort an array
# according absolute difference
# with x.
def rearrange(arr, n, x):

	m = {}

	# Store values in a map
	# with the difference
	# with X as key
	for i in range(n):
		m[arr[i]] = abs(x - arr[i])

	m = {k : v for k, v in sorted(m.items(),
		key = lambda item : item[1])}

	# Update the values of array
	i = 0

	for it in m.keys():
		arr[i] = it
		i += 1

# Function to print the array
def printArray(arr, n):

	for i in range(n):
		print(arr[i], end = " ")
		
# Driver code
if __name__ == "__main__":

	arr = [10, 5, 3, 9, 2]
	n = len(arr)
	x = 7
	rearrange(arr, n, x)
	printArray(arr, n)


























'''
my tests

'''
def my_tests(arr, k):
    dic ={}
    for i in range(len(arr)):
        abs_val =abs(k-arr[i])
        dic[arr[i]] =abs_val
    new_val = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}

    return list(new_val.keys())



print("Expected:[5, 9, 10, 3, 2], Actual:", my_tests([10, 5, 3, 9, 2], 7))
print("Expected:[5, 4, 3, 2, 1], Actual:", my_tests([1, 2, 3, 4, 5] , 6))
print("Expected:[6, 3, 2, 8], Actual: ", my_tests([2, 6, 8, 3], 5))

