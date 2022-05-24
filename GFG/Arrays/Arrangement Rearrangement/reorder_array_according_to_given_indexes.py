"""
Reorder an array according to given indexes

Given two integer arrays of same size, "arr[]" and "index[]", reorder elements in "arr[]" 
according to given index array. It is not allowed to given array arr's length.

Example: 

Input:  arr[]   = [10, 11, 12];
        index[] = [1, 0, 2];
Output: arr[]   = [11, 10, 12]
        index[] = [0,  1,  2] 

Input:  arr[]   = [50, 40, 70, 60, 90]
        index[] = [3,  0,  4,  1,  2]
Output: arr[]   = [40, 60, 90, 50, 70]
        index[] = [0,  1,  2,  3,   4]

Expected time complexity O(n) and auxiliary space O(1)

A simple solution is to use an auxiliary array temp[] of same size as given arrays.
Traverse the given array and put all elements at their correct place in temp[] using index[]
Finally copy temp[] to arr[] and sell all values of index[i] as i.

"""

# program to sort an array according to given indexes


# Function to reorder elements of arr[] according to index[]
def reorder(arr, index, n):
    temp =[0] * n

    # arr[i] should be present at index[i] index
    for i in range(0, n):
        temp[index[i]] = arr[i]
        
    # copy temp[] to arr[]
    for i in range(0, n):
        arr[i] =temp[i]
        index[i] =i

arr = [50, 40, 70, 60, 90]
index = [3, 0, 4, 1, 2]
n = len(arr)
 
reorder(arr, index, n)
 
print("Reordered array is:")
for i in range(0,n):
    print(arr[i],end = " ")
 
print("\nModified Index array is:")
for i in range(0,n):
    print(index[i],end = " ")

print("\nsolution without auxiliary array: \n")

"""
solution without auxiliary array

1) Do following for every element arr[i]
   a) While index[i] is not equal to i
       (i)  Store array and index values of the target (or 
            correct) position where arr[i] should be placed.
            The correct position for arr[i] is index[i]
       (ii) Place arr[i] at its correct position. Also
            update index value of correct position.
       (iii) Copy old values of correct position (Stored in
            step (i)) to arr[i] and index[i] as the while 
            loop continues for i.

"""

# A O(n) time and O(1) extra space program to sort an array according to given indexes

# Function to reorder elements of arr[] according to index[]

def reorder(arr, index, n):
    # fix all elements one by one
    for i in range(0,n):

        # while index[i] and arr[i] are not fixed
        while(index[i] != i):

            # store values of the target(or correct) position before placing arr[i] there
            oldTargetI = index[index[i]]
            oldTargetE =arr[index[i]]

            # place arr[i] at its target (or correct) position. Also copy corrected index for
            # new position
            arr[index[i]] = arr[i]
            index[index[i]] = index[i]

            # copy old target values to arr[i] and index[i]
            index[i] =oldTargetI
            arr[i] = oldTargetE

arr = [50, 40, 70, 60, 90]
index= [3, 0, 4, 1, 2]
n = len(arr)
 
reorder(arr, index, n)
 
print("Reordered array is:")
for  i in range(0, n):
    print(arr[i],end=" ")
 
print("\nModified Index array is:")
for i in range(0, n):
    print(index[i] ,end=" ")



"""
Another Method without using an auxiliary array is to sort the arrays. 
Sort the index array and customize the sort to swap the arr[] data whenever you swap 
the index[] data.

Time Complexity: O(nlogn)

"""

# code to reorder an array according to the given indices
def heapify(arr, index, i):
    largest = i

    # left child in 0 based indexing
    left = 2 * i + 1

    # right child in 1 based indexing
    right = 2 * i + 2

    global heapSize

    # Find largest index from root, left and right child
    if(left < heapSize and index[left] > index[largest]):
        largest = left

    if(right < heapSize and index[right] > index[largest]):
        largest = right

    if(largest != i):
        # swap arr whenever index is swapped
        arr[largest], arr[i] = arr[i], arr[largest]
        index[largest], index[i] =index[i], index[largest]

        heapify(arr, index, largest)

def heapSort(arr, index, n):
    
    # Build heap
    global heapSize

    for i in range(int((n-1) / 2), -1, -1):
        heapify(arr, index, i)


    # swap the largest element of index[first element] with the last element
    for i in range(n-1, 0, -1):
        index[0], index[i] =index[i], index[0]


        # swap arr whenever index is swapped
        arr[0], arr[i] =arr[i], arr[0]


        heapSize -=1
        heapify(arr, index, 0)

# Driver Code
arr = [ 50, 40, 70, 60, 90 ]
index = [ 3, 0, 4, 1, 2 ]
 
n = len(arr)
global heapSize
heapSize = n
heapSort(arr, index, n)
 
print("Reordered array is: ")
print(*arr, sep = ' ')
print("Modified Index array is: ")
print(*index, sep = ' ')



'''
Time Complexity: O(nlogn)
 

Another method to solve the problem is with space Complexity of O(1) is :-

Swap the elements present in the arr until the index_arr[i] is not equal to the i.

Let’s dry run the below code for the given input :- 

1st iteration :- (i=0)

arr = [ 50, 40, 70, 60, 90 ]

index_arr = [3, 0, 4, 1, 2 ]

since the index_arr[i] is not equal to i

swap the content present in the arr[i] with arr[index[i] and similarly swap for the index_arr also. 
After swapping we will have the following arr and index_arr values:- 

arr = [ 60, 40, 70, 50, 90 ]

index_arr = [1, 0, 4, 3, 2 ]

Since index_arr[0] is not equal to i.

we again swap the content present at i with index_arr[i] for both the arrays (arr , index_arr).

arr = [ 40, 60, 70, 50, 90 ]

index_arr = [0, 1, 4, 3, 2 ]

2nd Iteration:- (i=1)

Since the value of index_arr[i] == i ; condition under the while loop does not get executed as the condition 
under the braces get false and hence move to the next iteration:- 

3rd Iteration :- (i=2)

Since the value of index_arr[i] is not equal to i. Swap the content.

After Swapping we will get:- 

arr = [ 40, 60, 90, 50, 70 ]

index_arr = [0, 1, 2, 3, 4].

Now for the next iteration (4th and 5th iteration) since the Value of index_arr[i] is equal to i .
we just skip that loop ( because the condition under the while loop gets false and hence the while loop does
not get executed.) and move to the next iteration.

'''

def test_two(arr, index_arr):
	n = len(arr)
	
	for i in range(n):
		while(index_arr[i] != i):
			arr[i], arr[index_arr[i]] =arr[index_arr[i]], arr[i]
			index_arr[i],index_arr[index_arr[i]] =index_arr[index_arr[i]],index_arr[i]
	print(arr)
	
arr   = [10, 11, 12]
index = [1, 0, 2]

# print("expected:[11, 10, 12], actual:",test_two(arr, index))
# print("expected:[40, 60, 90, 50, 70], actual:",test_two([50, 40, 70, 60, 90], [3,  0,  4,  1,  2]))


'''
my test
time: O(n)
space=O(n)
'''
def test(arr, index):
	
	temp =[0]*len(arr)
	count =0
	for i in index:
		temp[i] =arr[count]
		count +=1
		
	return temp

arr   = [10, 11, 12];
index = [1, 0, 2];

print("expected:[11, 10, 12], actual:",test(arr, index))
print("expected:[40, 60, 90, 50, 70], actual:",test([50, 40, 70, 60, 90], [3,  0,  4,  1,  2]))
	

