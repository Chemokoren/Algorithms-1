"""

Merge two sorted arrays with O(1) extra space

We are given two sorted arrays. We need to merge these two arrays such that the initial numbers(
    after complete sorting) are in the first array and the remaining numbers are in the second
    array. Extra space is allowed in O(1)

Example: 

Input: ar1[] = {10};
       ar2[] = {2, 3};
Output: ar1[] = {2}
        ar2[] = {3, 10}  

Input: ar1[] = {1, 5, 9, 10, 15, 20};
       ar2[] = {2, 3, 8, 13};
Output: ar1[] = {1, 2, 3, 5, 8, 9}
        ar2[] = {10, 13, 15, 20}

This task is simple and O(m+n) if we are allowed to use extra space. But it becomes really 
complicated when extra space is not allowed and doesn't look possible in less than O(m*n) 
worst-case time. Though further optimizations are possible, the idea is to begin from the last
element of ar2[] and search it in ar1[]. If there is a greater element in ar1, then we move the 
last element of ar1[] to ar2[]. To keep ar1[] and ar2[] sorted, we need to place the last 
element of ar2[] at the correct place  in ar1[]. We can use Insertion Sort type of insertion 
for this.

Method 1
- Iterate through every element of ar2[] starting from last element. Do the following for every
element ar2[i]
    a) Store last element for ar1[i]: last = ar1[i]
    b) Loop from last element of ar1[] while element ar1[j] is greater than ar2[i].
        ar1[j+1] = ar1[j] // move element one position ahead
        j --
    c) If any element of ar1[] was moved
        ar1[j+1] =ar2[i]
        ar2[i] = last

Time Complexity: The worst-case time complexity of code/algorithm is O(m*n). The worst case 
occurs when all elements of ar1[] are greater than all elements of ar2[].

"""

def merge(arr1, arr2):

    m = len(arr1)
    n = len(arr2)

    # iterate through all elements of ar2[] starting from the last element
    for i in range(n-1, -1, -1):

        # Find the smallest element greater than ar2[i]. Move all elements one
        # position ahead till the smallest greater element is not found
        last = arr1[m-1]
        j = m-2
        while(j >= 0 and arr1[j] > arr2[i]):
            arr1[j+1] = arr1[j]
            j -=1

        
        # if there was a greater element
        if(last > arr2[i]):
            arr1[j+1] =arr2[i]
            arr2[i] = last

    return arr1, arr2


print("Expected:, Actual", merge([1, 5, 9, 10, 15, 20],[2, 3, 8, 13]))


"""
Method 2

-The solution can be further optimized by observing that while traversing the two sorted arrays
parallelly, if we encounter the jth second array element is smaller than ith first array element,
then jth element is to be included and replace some kth element in the first array.
This observation helps us with the following algorithm.

Algorithm
1) Initialize i, j, k as 0,0,n-1 where n is size of arr1
2) Iterate through every element of arr1 and arr2 using two pointers i and j respectively
    if arr1[i] is less than arr2[j]
        increment i
    else 
        swap the arr2[j] and arr1[k]
        increment j and decrement k

3) Sort both arr1 and arr2

Time Complexity: The time complexity while traversing the arrays in while loop is O(n+m) in worst case and 
sorting is O(nlog(n) + mlog(m)). So overall time complexity of the code becomes O((n+m)log(n+m)).
Space Complexity: As the function doesn’t use any extra array for any operations, the space 
complexity is O(1).
"""
def merge_two(arr1, arr2):
    n, m = len(arr1), len(arr2)
    i = 0
    j = 0
    k = n-1

    while (i <= k and j < m):
        if(arr1[i] < arr2[j]):
            i += 1
        else:
            arr2[j], arr1[k] =arr1[k],arr2[j]
            j += 1
            k -= 1
    arr1.sort()
    arr2.sort()
    return arr1, arr2

print("Two Expected:, Actual", merge_two([1, 5, 9, 10, 15, 20],[2, 3, 8, 13]))

"""
Method 3

- Algorithm
1) Initialize i with 0
2) Iterate while loop until last element of array 1 is greater than first element of array 2
        if arr1[i] greater than first element of arr2
            swap arr1[i] with arr2[0]
            sort arr2
        incrementing i

"""

def merge_three(arr1, arr2):
    n, m = len(arr1), len(arr2)

    i =0
    temp =0

    # while loop till last element of array 1(sorted) is greater than first element of
    # array 2(sorted)
    while (arr1[n-1] > arr2[0]):
        if(arr1[i] > arr2[0]):
            # Swap arr1[i] with first element of arr2 and sorting the updated arr2(arr1 is 
            # already sorted)
            # swap(arr1[i], arr2[0])
            arr1[i], arr2[0]= arr2[0], arr1[i]
            arr2.sort()
        i +=1

    return arr1, arr2

print("Three Expected:, Actual", merge_three([1, 5, 9, 10, 15, 20],[2, 3, 8, 13]))


"""
Method 4

- Let the length of the shorter array be 'm' and the larger array be 'n'

Step 1: Select the shorter array and find the index at which partition should be done.
    1) Partition the shorter array at its median(l1)
    2) Select the first n-l1 elements from the second array.
    3) Compare the border elements i.e.
        if l1 < r2 and l2 < r2 we have found the index
        else if l1 > r2 we have to search in the left subarray
        else we have to search in the right subarray

NOTE: This step will store all the smallest elements in the shorter array.
Step 2: Swap all the elements right to the index(i) of the shorter array with the first n-i 
elements of the larger aray.
Step 3: Sort both the arrays
 if len(arr1) > len(arr2) all the smallest elements are stored in arr2 so we have to move all
 the elements in arr1 since we have to print arr1 first.
Step 4: Rotate the larger array(arr1) m times counter-clockwise.
Step 5: Swap the first m elements of both arrays

"""
import sys

def rotate(a, n, idx):
    for i in range((int)(idx/2)):
        a[i], a[idx-1-i] = a[idx-1-i], a[i]
    for i in range(idx, (int)((n + idx)/2)):
        a[i], a[n-1-(i-idx)] = a[n-1-(i-idx)], a[i]

    for i in range((int)(n/2)):
        a[i], a[n-1-i] = a[n-1-i], a[i]

def sol(a1, a2):
    n, m =len(a1), len(a2)

    l = 0
    h =n-1
    idx = 0
    while(l <= h):
        c1 =(int)((l+h)/2)
        c2 = n-c1-1
        l1 =a1[c1]
        l2 =a2[c2-1]
        r1 =sys.maxint if c1 == n-1 else a1[c1+1]
        r2 =sys.maxint if c2 == m else a2[c2]
        if l1 >r2:
            h = c1-1
            if h == -1:
                idx = 0
        elif l2 > r1:
            l = c1 + 1
            if l == n-1:
                idx = n
        else:
            idx =c1 + 1
            break
    for i in range(idx, n):
        a1[i], a2[i-idx] =a2[i-idx], a1[i]

    a1.sort()
    a2.sort()
# Time Complexity: O(min(nlogn, mlogm))
def merge_four(a1, a2):
    n, m = len(a1), len(a2)
    if n > m:
        sol(a2,a1)
        rotate(a1,n,n-m)
        for i in range(m):
            a1[i], a2[i] = a2[i], a1[i]
    else:
        sol(a1, a2)

    return a1, a2


print("Four Expected:, Actual", merge_four([1, 5, 9, 10, 15, 20],[2, 3, 8, 13]))


"""
Method 5: Insertion sort with Simultaneous Merge

Approach
1. Sort list 1 by always comparing with head/first of list 2 and swapping if required
2. after each head/first swap, perform insertion of the swapped element into correct position in 
list 2 which will eventually sort list 2 at the end

For every swapped item from list 1, perform insertion sort in list 2 to find its correct position
so that when list 1 is sorted, list 2 is also sorted

Time Complexity: O(m*n) list 1 traversal and list 2 insertions
Auxiliary Space: O(1)
If m == n: Time = O(n^2) insertion sort complexity

"""
# "Insertion sort of list 2 with swaps from list 1"
# swap elements to get list 1 correctly, meanwhile place the swapped item in correct position
# of list 2 eventually list 2 is also sorted
# Time =O(m*n) or O(n*m)
# AUX = O(1)
def merge_five(arr1, arr2):
    x, y = arr1, arr2
    end =len(arr1)
    i = 0
    while(i < end):                 # O(m) or O(n)
        if(x[i] > y[0]):
            swap(x,y, i,0)
            insert(y, 0)            # O(n) or O(m) number of shifts
        i += 1

# O(n)
def insert(y,i):
    orig = y[i]
    i += 1
    while(i<len(y) and y[i]<orig):
        y[i-1] =y[i]
        i+= 1
    y[i-1] =orig

def swap(x, y, i, j):
    temp =x[i]
    x[i] =y[j]
    y[j] =temp

def test():
    c1 =[2,3,8,13]
    c2 =[1,5,9,10,15,20]
    for _ in range(2):
        merge(c1,c2)
        print(c1,c2)
        c1,c2 =c2,c1

test()

"""
Method: Using Euclidean Division Lemma

Approach
- Just merge the two arrays as we do in merge sort, while simulatenously using Euclidean Division 
Lemma, i.e.(((Operation on array) % x) * x). And at least after merging divide both the arrays
with x. Where x needs to be a number greater than all elements of array. Here in this case x,
(according to the constraints) can be 10e7+1.

Time Complexity: O(m + n)
Auxiliary Space: O(1), since no extra space has been taken.

"""
# Python program to merge two sorted arrays without using extra space


def merge_six(arr1, arr2, n, m):
	# three pointers to iterate
	i = 0
	j = 0
	k = 0
	# for euclid's division lemma
	x = 10e7 + 1
	# in this loop we are rearranging the elements of arr1
	while i < n and (j < n and k < m):
		# if both arr1 and arr2 elements are modified
		if arr1[j] >= x and arr2[k] >= x:
			if arr1[j] % x <= arr2[k] % x:
				arr1[i] += (arr1[j] % x) * x
				j += 1
			else:
				arr1[i] += (arr2[k] % x) * x
				k += 1
		# if only arr1 elements are modified
		elif arr1[j] >= x:
			if arr1[j] % x <= arr2[k]:
				arr1[i] += (arr1[j] % x) * x
				j += 1
			else:
				arr1[i] += (arr2[k] % x) * x
				k += 1
		# if only arr2 elements are modified
		elif arr2[k] >= x:
			if arr1[j] <= arr2[k] % x:
				arr1[i] += (arr1[j] % x) * x
				j += 1
			else:
				arr1[i] += (arr2[k] % x) * x
				k += 1
		# if none elements are modified
		else:
			if arr1[j] <= arr2[k]:
				arr1[i] += (arr1[j] % x) * x
				j += 1
			else:
				arr1[i] += (arr2[k] % x) * x
				k += 1
		i += 1

	# we can copy the elements directly as the other array
	# is exchausted
	while j < n and i < n:
		arr1[i] += (arr1[j] % x) * x
		i += 1
		j += 1
	while k < m and i < n:
		arr1[i] += (arr2[k] % x) * x
		i += 1
		k += 1
	# we need to reset i
	i = 0

	# in this loop we are rearranging the elements of arr2
	while i < m and (j < n and k < m):
		# if both arr1 and arr2 elements are modified
		if arr1[j] >= x and arr2[k] >= x:
			if arr1[j] % x <= arr2[k] % x:
				arr2[i] += (arr1[j] % x) * x
				j += 1

			else:
				arr2[i] += (arr2[k] % x) * x
				k += 1

		# if only arr1 elements are modified
		elif arr1[j] >= x:
			if arr1[j] % x <= arr2[k]:
				arr2[i] += (arr1[j] % x) * x
				j += 1

			else:
				arr2[i] += (arr2[k] % x) * x
				k += 1

		# if only arr2 elements are modified
		elif arr2[k] >= x:
			if arr1[j] <= arr2[k] % x:
				arr2[i] += (arr1[j] % x) * x
				j += 1

			else:
				arr2[i] += (arr2[k] % x) * x
				k += 1

		else:
			# if none elements are modified
			if arr1[j] <= arr2[k]:
				arr2[i] += (arr1[j] % x) * x
				j += 1

			else:
				arr2[i] += (arr2[k] % x) * x
				k += 1

		i += 1
	# we can copy the elements directly as the other array
	# is exhausted
	while j < n and i < m:
		arr2[i] += (arr1[j] % x) * x
		i += 1
		j += 1

	while k < m and i < m:
		arr2[i] += (arr2[k] % x) * x
		i += 1
		k += 1

	# we need to reset i
	i = 0
	# we need to divide the whole arr1 by x
	while i < n:
		arr1[i] /= x
		i += 1

	# we need to reset i
	i = 0
	# we need to divide the whole arr2 by x
	while i < m:
		arr2[i] /= x
		i += 1

# Driver program


ar1 = [1, 5, 9, 10, 15, 20]
ar2 = [2, 3, 8, 13]
m = len(ar1)
n = len(ar2)

merge_six(ar1, ar2, m, n)

print("After Merging \nFirst Array:", end=" ")
for i in range(m):
	print(int(ar1[i]), end=" ")
print("\nSecond Array:", end=" ")
for i in range(n):
	print(int(ar2[i]), end=" ")



 
# print("Six Expected:, Actual: ", merge_six([1, 5, 9, 10, 15, 20],[2, 3, 8, 13]))




print("\n my tests \n")

'''
my tests
'''
def my_tests(arr1, arr2):
    i =0
    j =0
     
    while i <len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i +=1
        else:
            arr2[j], arr1[i] =arr1[i], arr2[j]
            j +=1
    
    # while j < len(arr2)-1:
    #     if arr2[j] > arr2[j+1]:
    #         arr2[j], arr2[j+1] =arr2[j+1], arr2[j]
    #         j +=1

    return arr1, arr2


# print("Expected:, Actual", my_tests([10],[2,3]))
# print("Expected:, Actual", my_tests([1, 5, 9, 10, 15, 20],[2, 3, 8, 13]))