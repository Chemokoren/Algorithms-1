"""
replace every array element by multiplication of previous and next

Given an array of integers, update every element with multiplication of previous and next elements with 
following exceptions. 

a) First element is replaced by multiplication of first and second. 
b) Last element is replaced by multiplication of last and second last.
Example: 
 

Input: arr[] = {2, 3, 4, 5, 6}
Output: arr[] = {6, 8, 15, 24, 30}

// We get the above output using following
// arr[] = {2*3, 2*4, 3*5, 4*6, 5*6} 

A Simple Solution is to create an auxiliary array, copy contents of given array
to auxiliary array. Finally traverse the auxiliary array and update given array 
using copied values. Time complexity of this solution is O(n), but it requires O(n)
extra space.
An efficient solution can solve the problem in O(n) time and O(1) space. 
The idea is to keep track of previous element in loop. 
Below is the implementation of this idea.

"""
# program to update every array element with multiplication of previous and 
# next numbers in array

def modify(arr, n):
    # Nothing to do when array size is 1
    if n <= 1:
        return
    
    # store current value of arr[0] and update it
    prev =arr[0]
    arr[0] = arr[0] * arr[1]

    # update the rest of the array elements
    for i in range(1, n-1):
        # store current value of next interaction
        curr =  arr[i]

        # update current value using previous value
        arr[i] = prev * arr[i+1]

        # update previous value
        prev = curr

    # update last array element
    arr[n-1] = prev * arr[n-1]

arr = [2, 3, 4, 5, 6]
n = len(arr)
modify(arr, n)
for i in range (0, n):
    print(arr[i],end=" ")


print("#################### replace_current #################### ")
# Time complexity: O(n) | Space complexity : O(n)
def replace_current(arr):
	n =len(arr)
	new_arr =[0] *n
	
	for i in range(n):
		if i==0:
			new_val =arr[i] *arr[i+1]
		elif i ==n-1:
			new_val=arr[-1] * arr[-2]
		else:
			new_val =arr[i-1] *arr[i+1]
		new_arr[i] =new_val
	arr=new_arr[::]
	return arr


	

print("expected:[6, 8, 15, 24, 30], actual:", replace_current([2, 3, 4, 5, 6]))

print("#################### modify #################### ")

def replace_current(arr):
	n =len(arr)
	
	if n <=1:
		return
	prev =None
	for i in range(n):
		if i ==0:
			new_val =arr[i] *arr[i+1]
		elif i == n-1:
			new_val =prev *arr[-1]
		else:
			new_val = prev * arr[i+1]
		prev =arr[i]
		arr[i] =new_val
		
			
	return arr


	

print("expected:[6, 8, 15, 24, 30], actual:", replace_current([2, 3, 4, 5, 6]))