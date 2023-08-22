"""
Find Union and Intersection of two unsorted arrays

Given two unsorted arrays that represent two sets(elements in every array are distinct), find the
union and intersection of two arrays.

For example, if the input arrays are:

arr1[] = {7, 1, 5, 2, 3, 6} 
arr2[] = {3, 8, 6, 20, 7} 

Then your program should print Union as {1, 2, 3, 5, 6, 7, 8, 20}  and intersection as [3,6,7].
Note that the elements of union and intersection can be printed in any order.

METHOD 1: Using Set

We can get the Union of two arrays using the set data structure.
when we put the elements of both the array into the set we will get only the distinct elements 
that are equal to the union operation over the arrays.


"""

# union of two arrays using Set
# Time Complexity: O( max(m,n) )
def get_union(a, b):
    n = len(a)
    m = len(b)

    # defining set container
    hs = set()

    if(n<m):
        min_val =n
    else:
        min_val =m

    # add elements from both the arrays for index from 0 to min(n,m)-1
    for i in range(0, min_val):
        hs.add(a[i])
        hs.add(b[i])

    if(n>m):
        for i in range(m, n):
            hs.add(a[i])
    else:
        if(n < m):
            for i in range(m, n):
                hs.add(b[i])

    return hs


print("Expectation:, Actual:", get_union([1, 2, 5, 6, 2, 3, 5, 7, 3], [2, 4, 5, 6, 8, 9, 4, 6, 5, 4]))

"""
Method 2: (Using map data structure)

From the knowledge of data structures, we know that map stores distinct keys only. So if we insert
any key appearing more than one time it gets stored only once. The idea is to insert both the 
arrays in one common map which would then store the distinct elements of both arrays 
(union of both the array).

 time complexity O(m+n)

"""

def print_union(a, b):
    n = len(a)
    m = len(b)

    mp ={}
    # Inserting array elements in mp
    for i in range(n):
        mp[a[i]] =i
    
    for i in range(m):
        mp[b[i]] =i

    return mp.keys()

print("Union Expectation:, Actual:", print_union([ 1, 2, 5, 6, 2, 3, 5 ], [ 2, 4, 5, 6, 8, 9, 4, 6, 5 ]))
print("Union Expectation:[1, 2, 3, 5, 6, 7, 8, 20]", print_union([7, 1, 5, 2, 3, 6],[3, 8, 6, 20, 7]))


"""
Method 5: Use Sorting and Searching

Union
- Initialize Union U as empty
- Find smaller m and n and sort the smaller array
- Copy the smaller array to U.
- For every element x of a larger array, do the following
    - Binary search x in the smaller array. If x is not present, then copy it to U
- Return U

Intersection
- Initialize intersection I as empty
- find smaller of m and n and sort the smaller array.
- For every element x of a larger array, do the following
    - binary search x in the smaller array. If x is present, then copy it to I.
- Return I

Time complexity of this method is min(mLogm + nLogm, mLogn + nLogn) which can also be written as 
O((m+n)Logm, (m+n)Logn). 


"""

# print union and intersection of two unsorted arrays
def print_union_two(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    # before finding union, make sure arr[0..m-1] is smaller
    if (m > n):
        tempp = arr1
        arr1 = arr2
        arr2 = tempp

        temp = n
        m = n
        n = temp

        # Now arr1[] is smaller

        # sort the first array and print its elements (these two steps 
        # can be swapped as order in output is not important)
        arr1.sort()
        for i in range(0, m):
            print(arr1[i], end=" ")

        # search every element of bigger array in smaller array and print the 
        # element if not found
        for i in range(0,n):
            if(binary_search(arr1,0,m-1, arr2[i]) == -1):
                print(arr2[i], end=" ")

# prints intersection of arr1[0..m-1] and arr2[0..n-1]
def print_intersection(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    # Before finding intersection, make sure arr1[0..m-1] is smaller
    if(m > n):
        tempp = arr1
        arr1 = arr2
        arr2 = tempp

        temp = m
        m = n
        n = temp

        # Now arr1[] is smaller
        # sort smaller array arr1[0..m-1]
        arr1.sort()

        # Search every element of bigger array in smaller array and print the element if found
        for i in range(0, n):
            if (binary_search(arr1, 0, m -1, arr2[i]) !=-1):
                print(arr2[i], end=" ")

# A recursive binary search function - It returns location of x in the given array arr[l..r] is
# present, otherwise -1
def binary_search(arr, l, r, x):
    if(r >= l):
        mid = int(l +(r-l)/2)

        # if the element is present at the middle itself
        if(arr[mid] == x):
            return mid

        # if element is smaller than mid, then it can only be present in left subarray
        if(arr[mid] > x):
            return binary_search(arr, l, mid -1, x)
        # else the element can only be present in right subarray
        return binary_search(arr, mid+1, r, x)
    # we reach here when element is not present in array
    return -1

print_union_two([7, 1, 5, 2, 3, 6], [3, 8, 6, 20, 7])
print("\n\n")
print_intersection([7, 1, 5, 2, 3, 6], [3, 8, 6, 20, 7])



"""
Another Approach (When elements in the array may not be distinct) :

"""
# function to find intersection when elements may not be distinct
def intersection(a, b):
    n = len(a)
    m = len(b)
     
    # sort
    a.sort()
    b.sort()

    i = 0
    j = 0

    while( i< n and j < m):
        if(a[i] > b[j]):
            j +=1
        else:
            if(b[j] > a[i]):
                i += 1
            else:
                # when both are equal
                print(a[i], end=" ")
                i += 1
                j += 1
    
print(" intersection::::")
intersection([1, 3, 2, 3, 4, 5, 5, 6], [3, 3, 5])


"""
Method 6: Works for repeated and distant elements

Sort both arrays and proceed as below

Union 
1. Iterate in while loop until any one array is finished
2. In each iteration we look for smaller in both arrays and we print it and increment its
pointer only if it is not same as the last element printed in union
3. After we finish while we iterate the remaining of two array in the similar way as above 
and print the union

Intersection
1. Iterate in while loop till any of the one array is finished.
2. In each iteration, we look for smaller of the two elements from both the array and increase 
its pointer because it will not e in other list, hence not part of intersection.
3. For intersection, if both the elements are equal we print it and increment both pointer only
if it is not same as the last element printed in intersection.



"""

# function to find union
def union(a, b):
    n, m = len(a), len(b)
 
    # sort
    a.sort()
    b.sort()

    result =[0 for _ in range(n+m)]

    index, left, right =0,0,0
    while left < n and right < m:
        if(a[left] < b[right]):
            if(index != 0 and a[left] == result[index-1]):
                left +=1
            else:
                result[index] = a[left]
                left += 1
                index +=1

        else:
            if(index != 0 and b[right] == result[index-1]):
                right += 1
            else:
                result[index] = b[right]
                right += 1
                index += 1
    while(left < n):
        if(index != 0 and a[left] == result[index]):
            left += 1
        else:
            result[index] =a[left]
            left += 1
            index +=1

    print("Union: ", *result[:index])

# function to find intersection
def intersection(a, b):
    n, m = len(a), len(b)
 
    # sort
    a.sort()
    b.sort()
    i, j, k = 0,0,0
    result =[0 for _ in range(n + m)]
    while i < n and j < m:
        if a[i] < b[j]:
            i +=1
        elif a[i] > b[j]:
            j += 1
        else:
            if k != 0 and a[i] == result[k-1]:
                i +=1
                j +=1
            else:
                result[k] = a[i]
                i +=1
                j +=1
                k += 1
    print("intersection:", *result[:k])


print("union & intersection \n")

union([ 1, 3, 2, 3, 3, 4, 5, 5, 6 ],[ 3, 3, 5 ])
intersection([ 1, 3, 2, 3, 3, 4, 5, 5, 6 ], [ 3, 3, 5 ])

"""

Method: Using Hashing

Union 

    Initialize an empty hash set hs.
    Iterate through the first array and put every element of the first array in the set S.
    Repeat the process for the second array.
    Print the set hs.

Intersection 

    Initialize an empty set hs.
    Iterate through the first array and put every element of the first array in the set S.
    For every element x of the second array, do the following :

Search x in the set hs. If x is present, then print it. Time complexity of this method is ?(m+n) 
under the assumption that hash table search and insert operations take ?(1) time.

The time complexity of this method is O(m+n) under the assumption that hash table search and insert
operations take O(1) time.
"""

# Python program to find union and intersection
# using sets


def printUnion(arr1, arr2, n1, n2):
	hs = set()

	# Insert the elements of arr1[] to set hs
	for i in range(0, n1):
		hs.add(arr1[i])

	# Insert the elements of arr1[] to set hs
	for i in range(0, n2):
		hs.add(arr2[i])
	print("Union:")
	for i in hs:
		print(i, end=" ")
	print("\n")

	# Prints intersection of arr1[0..n1-1] and
	# arr2[0..n2-1]


def printIntersection(arr1, arr2, n1, n2):
	hs = set()

	# Insert the elements of arr1[] to set S
	for i in range(0, n1):
		hs.add(arr1[i])
	print("Intersection:")
	for i in range(0, n2):

		# If element is present in set then
		# push it to vector V
		if arr2[i] in hs:
			print(arr2[i], end=" ")


# Driver Program
arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]
n1 = len(arr1)
n2 = len(arr2)

# Function call
printUnion(arr1, arr2, n1, n2)
printIntersection(arr1, arr2, n1, n2)



"""

Method 8 (Kind of hashing technique without using any predefined Java Collections) 

    Initialize the array with a size of m+n
    Fill first array value in a resultant array by doing hashing(to find appropriate position)
    Repeat for the second array
    While doing hashing if a collision happens increment the position in a recursive way

"""

# Python3 program to find union and intersection
# using similar Hashing Technique
# without using any predefined Java Collections
# Time Complexity best case & avg case = O(m+n)
# Worst case = O(nlogn)


# Prints intersection of arr1[0..n1-1] and
# arr2[0..n2-1]
def findPosition(a, b):
	v = len(a) + len(b);
	ans = [0]*v;
	zero1 = zero2 = 0;
	print("Intersection :",end=" ");
	
	# Iterate first array
	for i in range(len(a)):
		zero1 = iterateArray(a, v, ans, i);
	
	# Iterate second array
	for j in range(len(b)):
		zero2 = iterateArray(b, v, ans, j);
	
	zero = zero1 + zero2;
	placeZeros(v, ans, zero);
	printUnion(v, ans, zero);
	
# Prints union of arr1[0..n1-1] and arr2[0..n2-1]
def printUnion(v, ans,zero):
	zero1 = 0;
	print("\nUnion :",end=" ");
	for i in range(v):
		if ((zero == 0 and ans[i] == 0) or
			(ans[i] == 0 and zero1 > 0)):
			continue;
		if (ans[i] == 0):
			zero1+=1;
		print(ans[i],end=",");

def placeZeros(v, ans, zero):
	if (zero == 2):
		print("0");
		d = [0];
		placeValue(d, ans, 0, 0, v);
	if (zero == 1):
		d=[0];
		placeValue(d, ans, 0, 0, v);

# Function to iterate array
def iterateArray(a,v,ans,i):
	if (a[i] != 0):
		p = a[i] % v;
		placeValue(a, ans, i, p, v);
	else:
		return 1;
	
	return 0;

def placeValue(a,ans,i,p,v):
	p = p % v;
	if (ans[p] == 0):
		ans[p] = a[i];
	else:
		if (ans[p] == a[i]):
			print(a[i],end=",");
		else:
			# Hashing collision happened increment
			# position and do recursive call
			p = p + 1;
			placeValue(a, ans, i, p, v);

# Driver code
a = [ 7, 1, 5, 2, 3, 6 ];
b = [ 3, 8, 6, 20, 7 ];
findPosition(a, b);


"""


"""
# Python program to find union and intersection
# using sets


def printUnion(arr1, arr2, n1, n2):
	hs = set()
	# Insert the elements of arr1[] to set hs
	for i in range(0, n1):
		hs.add(arr1[i])
	# Insert the elements of arr1[] to set hs
	for i in range(0, n2):
		hs.add(arr2[i])
	print("Union:")
	for i in hs:
		print(i, end=" ")
	print("\n")
	# Prints intersection of arr1[0..n1-1] and
	# arr2[0..n2-1]


def printIntersection(arr1, arr2, n1, n2):
	hs = set()
	# Insert the elements of arr1[] to set S
	for i in range(0, n1):
		hs.add(arr1[i])
	print("Intersection:")
	for i in range(0, n2):
		# If element is present in set then
		# push it to vector V
		if arr2[i] in hs:
			print(arr2[i], end=" ")


# Driver Program
arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]
n1 = len(arr1)
n2 = len(arr2)

# Function call
printUnion(arr1, arr2, n1, n2)
printIntersection(arr1, arr2, n1, n2)





print("\n my tests \n")

'''
my tests

Time Complexity: O(n+m) n=arr1, m=arr2, Space Complexity: O(n+m)
'''
def my_tests(arr1,arr2):
    se = set()
    for x in arr1:
        se.add(x)

    for x in arr2:
        se.add(x)

    union =list(se)


    intersection =[]

    map ={}
    for i in range(len(arr1)):
        map[arr1[i]] =arr1[i]

    

    for i in range(len(arr2)):
        if arr2[i] in map:
            intersection.append(arr2[i])

    return union, intersection





print("Exp Union:[1, 2, 3, 5, 6, 7, 8, 20], Inter:[3,6,7]", my_tests([7, 1, 5, 2, 3, 6],[3, 8, 6, 20, 7]))