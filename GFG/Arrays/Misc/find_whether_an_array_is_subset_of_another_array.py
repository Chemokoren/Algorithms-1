"""
Find whether an array is a subset of another array

Given two arrays: arr1[0..m-1] and arr2[0..n-1]. Find whether arr2[] is a subset of arr1[] or not.
Both the arrays are not in sorted order. It may be assumed that elements in both arrays are 
distinct.
    Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1} 
    Output: arr2[] is a subset of arr1[]

    Input: arr1[] = {1, 2, 3, 4, 5, 6}, arr2[] = {1, 2, 4} 
    Output: arr2[] is a subset of arr1[]

    Input: arr1[] = {10, 5, 2, 23, 19}, arr2[] = {19, 5, 3} 
    Output: arr2[] is not a subset of arr1[] 

Naive Approach to Find whether an array is subset of another array

Use two loops: The outer loop picks all the elements of arr2[] one by one. The inner loop linearly
searches for the element picked by the outer loop. If all elements are found then return 1, 
else return 0.

"""

# Time Complexity: O(m*n) | Auxiliary Space: O(1)
def naive_sol(arr1, arr2):
    for i in range(len(arr2)):
        flag = False
        for j in range(len(arr1)):
            if(arr1[j] ==arr2[i]):
                flag =True
        if flag == False:
            return False

    return True

print("Naive Expected:True, Actual:", naive_sol([11, 1, 13, 21, 3, 7], [11, 3, 7, 1]))
print("Naive Expected:True, Actual:", naive_sol([1, 2, 3, 4, 5, 6], [1, 2, 4]))
print("Naive Expected: False, Actual:", naive_sol([10, 5, 2, 23, 19], [19, 5, 3]))


"""
Find whether an array is subset of another array using Sorting and Binary Search

The idea is to sort the given array arr1[], and then for each element in arr2[] do a binary 
search for it in sorted arr1[]. If the element is not found then return 0. If all elements are 
present then return 1.

Illustration:

    Given array arr1[] = { 11, 1, 13, 21, 3, 7 } and arr2[] = { 11, 3, 7, 1 }.

    Step 1: We will sort the array arr1[], and have arr1[] = { 1, 3, 7, 11, 13, 21}.

    Step 2: We will look for each element in arr2[] in arr1[] using binary search.

        arr2[] = { 11, 3, 7, 1 }, 11 is present in arr1[] = { 1, 3, 7, 11, 13, 21}
        arr2[] = { 11, 3, 7, 1 }, 11 is present in arr1[] = { 1, 3, 7, 11, 13, 21}
        arr2[] = { 11, 3, 7, 1 }, 11 is present in arr1[] = { 1, 3, 7, 11, 13, 21}
        arr2[] = { 11, 3, 7, 1 }, 11 is present in arr1[] = { 1, 3, 7, 11, 13, 21}

    As all the elements are found we can conclude arr2[] is the subset of arr1[].

Algorithm:

The algorithm is pretty straightforward. 

    Sort the first array arr1[].
    Look for the elements of arr2[] in sorted arr1[].
    If we encounter a particular value that is present in arr2[] but not in arr1[], the code 
    will terminate, arr2[] can never be the subset of arr1[].
    Else arr2[] is the subset of arr1[].


Time Complexity: O(mLog(m) + nlog(m)). O(mLog(m)) for sorting and O(nlog(m)) for binary searching 
each element of one array in another. In the above code, Quick Sort is used and the worst-case 
time complexity of Quick Sort is O(m2).

Auxiliary Space: O(n)

"""

# program to find whether an array is a subset of another array
# Return 1 if arr2[] is a subset of arr1[]

def is_subset(arr1, arr2, m, n):
    m = len(arr1)
    n = len(arr2)

    i =0
    quick_sort(arr1, 0, m-1)
    for i in range(n):
        if(binarySearch(arr1, 0, m-1, arr2[i]) ==-1):
            return 0
    return 1

def binarySearch(arr, low, high, x):
    if(high >= low):
        mid = (low + high)//2
 
        # Check if arr[mid] is the first
        # occurrence of x.
        # arr[mid] is first occurrence if x is
        # one of the following
        # is true:
        # (i) mid == 0 and arr[mid] == x
        # (ii) arr[mid-1] < x and arr[mid] == x
        if((mid == 0 or x > arr[mid-1]) and (arr[mid] == x)):
            return mid
        elif(x > arr[mid]):
            return binarySearch(arr, (mid + 1), high, x)
        else:
            return binarySearch(arr, low, (mid - 1), x)
 
    return -1
 
def partition(A, si, ei):
    """
    
    # Implementation of Quick Sort
    # A[] --> Array to be sorted
    # si --> Starting index
    # ei --> Ending index
 
    """
    x =A[ei]
    i =(si -1)

    for j in range(si, ei):
        if(A[j] <= x):
            i += 1
            A[i], A[j] = A[j],A[i]
    A[i+1], A[ei] =A[ei], A[i+1]
    return (i +1)


def quick_sort(A, si, ei):
    # partitioning index
    if(si < ei):
        pi = partition(A, si, ei)
        quick_sort(A, si, pi-1)
        quick_sort(A, pi + 1, ei)

arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]
 
m = len(arr1)
n = len(arr2)
 
if(is_subset(arr1, arr2, m, n)):
    print("arr2[] is subset of arr1[] ")
else:
    print("arr2[] is not a subset of arr1[] ")


"""
Find whether an array is subset of another array using Sorting and Merging

The idea is to sort the two arrays and then iterate on the second array looking for the same
values on the first array using two pointers. Whenever we encounter the same values we will
increment both the pointer and if we encounter any values less than that of the second array,
we will increment the value of the pointer pointing to the first array. If the value is greater
than that of the second array, we know the second array is not the subset of the first array.

Algorithm:

The initial step will be to sort the two arrays.

    Set two pointers j and i or arr1[] and arr2[] respectively.
    If arr1[j] < arr2[i], we will increase j by 1.
    If arr1[j] = arr2[i], we will increase j and i by 1.
    If arr1[j] > arr2[i], we will terminate as arr2[] is not the subset of arr1[].

Time Complexity: O(mLog(m) + nLog(n)) which is better than approach 2.
Auxiliary Space: O(1)

"""
def is_subset_two(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    i = 0
    j = 0
    if m < n:
        return 0

    arr1.sort()
    arr2.sort()

    while i < n and j < m:
        if arr1[j] < arr2[i]:
            j +=1
        elif arr1[j] == arr2[i]:
            j +=1
            i +=1
        elif arr1[j] > arr2[i]:
            return 0
    return False if i < n else True

if is_subset_two([11, 1, 13, 21, 3, 7], [11, 3, 7, 1]) == True:
    print("arr2 is subset of arr1 ")
else:
    print("arr2 is not a subset of arr1 ")


"""

Find whether an array is a subset of another array using Set

The idea is to insert all the elements of the first array and second array in the set, if the size of the set is equal to the size of arr1[] then the arr2[] is the subset of arr1[]. As no new elements are found in arr2[] hence is the subset.

Illustration:

    Given array arr1[] = { 11, 1, 13, 21, 3, 7 } and arr2[] = { 11, 3, 7, 1 }.

    Step 1: We will store the array arr1[] and arr2[] elements in Set

        The final Set = { 1, 3, 7, 11, 13, 21}

    Step 2: Size of arr1[] = 6 and size of the Set = 6

        Hence no new elements are found in arr2[]

    As all the elements are found we can conclude arr2[] is the subset of arr1[].

Algorithm:

The algorithm is pretty straightforward. 

    Store the first array arr1[] in a Set.
    Store the first array arr1[] in the same Set.
    If the size of arr1[] = size of the Set, arr2[] is the subset of arr1[].
    Else arr2[] is not the subset of arr1[].

Time Complexity: O(m+n) because we are using unordered_set and inserting in it, If we would be using an ordered set inserting would have taken log n increasing the TC to O(mlogm+nlogn), but order does not matter in this approach.
Auxiliary Space: O(n+m)

"""

def arr_is_subset_using_set(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    s = set()
    for i in range(m):
        s.add(arr1[i])

    p = len(s)
    for i in range(n):
        s.add(arr2[i])
    return len(s) ==p

# if (len(s) == p):
#     print("arr2[] is subset of arr1[] ")

# else:
#     print("arr2[] is not subset of arr1[] ")

print("Sets Expected:, Actual: ", arr_is_subset_using_set([11, 1, 13, 21, 3, 7],[11, 3, 7, 1]))


"""
Find whether an array is a subset of another array using the Frequency Table

The idea is to store the frequency of the elements present in the first array, then look for the elements present in arr2[] in the frequency array. As no new elements are found in arr2[] hence is the subset.

Illustration:

    Given array arr1[] = { 11, 1, 13, 21, 3, 7 } and arr2[] = { 11, 3, 7, 1 }.

    Step 1: We will store the array arr1[] elements frequency in the frequency array

        The frequency array will look like this

    Step 2: We will look for arr2[] elements in the frequnecy array.

        arr2[] = { 11, 3, 7, 1 }, 11 is present in the Frequnecy array
        arr2[] = { 11, 3, 7, 1 }, 3 is present in the Frequnecy array
        arr2[] = { 11, 3, 7, 1 }, 7 is present in the Frequnecy array
        arr2[] = { 11, 3, 7, 1 }, 1 is present in the Frequnecy array

    As all the elements are found we can conclude arr2[] is the subset of arr1[].

Algorithm:

The algorithm is pretty straightforward. 

    Store the frequency of the first array elements of arr1[] in the frequency array.
    Iterate on the arr2[] and look for its elements in the frequency array.
    If the value is found in the frequency array reduce the frequency value by one.
    If for any elements in arr2[] frequency is less than 1, we will conclude arr2[] is not the subset of arr1[],

Time Complexity: O(m+n) which is better than methods 1,2,3
Auxiliary Space: O(n)

"""

# Python3 program to find whether an array
# is subset of another array

# Return true if arr2[] is a subset of arr1[]


def isSubset(arr1, m, arr2, n):

	# Create a Frequency Table using STL
	frequency = {}

	# Increase the frequency of each element
	# in the frequency table.
	for i in range(0, m):
		if arr1[i] in frequency:
			frequency[arr1[i]] = frequency[arr1[i]] + 1
		else:
			frequency[arr1[i]] = 1

	# Decrease the frequency if the
	# element was found in the frequency
	# table with the frequency more than 0.
	# else return 0 and if loop is
	# completed return 1.
	for i in range(0, n):
		if (frequency[arr2[i]] > 0):
			frequency[arr2[i]] -= 1
		else:
			return False

	return True


# Driver Code
if __name__ == '__main__':

	arr1 = [11, 1, 13, 21, 3, 7]
	arr2 = [11, 3, 7, 1]

	m = len(arr1)
	n = len(arr2)

	if (isSubset(arr1, m, arr2, n)):
		print("arr2[] is subset of arr1[] ")
	else:
		print("arr2[] is not a subset of arr1[] ")





# Time complexity: O(n) | Space complexity: O(n)
def my_tests(arr1, arr2):
    dic =dict()
   
    for i in range(len(arr1)):
        dic[arr1[i]] =1
    
    for i in range(len(arr2)):
        if arr2[i] not in dic:
            return False
    return True


print("Expected:True, Actual:", my_tests([11, 1, 13, 21, 3, 7], [11, 3, 7, 1]))
print("Expected:True, Actual:", my_tests([1, 2, 3, 4, 5, 6], [1, 2, 4]))
print("Expected: False, Actual:", my_tests([10, 5, 2, 23, 19], [19, 5, 3]))


def my_tests_two(arr1, arr2):
    for i in range(len(arr2)):
        if arr2[i] not in arr1:
            return False
    return True

print("Expected:True, Actual:", my_tests_two([11, 1, 13, 21, 3, 7], [11, 3, 7, 1]))
print("Expected:True, Actual:", my_tests_two([1, 2, 3, 4, 5, 6], [1, 2, 4]))
print("Expected: False, Actual:", my_tests_two([10, 5, 2, 23, 19], [19, 5, 3]))

def sort_binary_search(arr1, arr2):
    arr1.sort()

    for i in range(len(arr2)):
        if(binary_search(arr1, arr2[i]) ==False):
            return False
    return True

def binary_search(arr, key):
    arr.sort()
    i =0
    end = len(arr)-1

    while i <= end:
        mid = (i + end)//2
        if arr[mid] ==key:
            return mid
        elif arr[mid] < key:
            i = mid + 1
        else:
            end = mid -1
    else:
        return False

print("Test", binary_search([11, 1, 13, 21, 3, 7], 8))

print("Binary Expected:True, Actual:", sort_binary_search([11, 1, 13, 21, 3, 7], [11, 3, 7, 1]))
print("Binary Expected:True, Actual:", sort_binary_search([1, 2, 3, 4, 5, 6], [1, 2, 4]))
print("Binary Expected: False, Actual:", sort_binary_search([10, 5, 2, 23, 19], [19, 5, 3]))

