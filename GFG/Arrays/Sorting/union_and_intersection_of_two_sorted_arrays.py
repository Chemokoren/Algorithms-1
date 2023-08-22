"""
Union and Intersection of two sorted arrays

Given two sorted arrays, find their union and intersection

Input: arr1[] = {1, 3, 4, 5, 7}
        arr2[] = {2, 3, 5, 6} 
Output: Union : {1, 2, 3, 4, 5, 6, 7} 
         Intersection : {3, 5}

Input: arr1[] = {2, 5, 6}
        arr2[] = {4, 6, 8, 10} 
Output: Union : {2, 4, 5, 6, 8, 10} 
         Intersection : {6}

Union of arrays arr1[] and arr2[]

To find union of two sorted arrays, follow the following merge procedure
1. Use two index variables i and j, initial values i =0, j =0
2) if arr1[i] is smaller than arr2[j] then print arr1[i] and increment i.
3) if arr1[i] is greater than arr2[j] then print arr2[j] and increment j.
4) If both are same then print any of them and increment both i and j.
5) Print remaining elements of the larger array.

Time Complexity : O(m + n)
Auxiliary Space: O(1)


"""
# m == len(arr1), n  == len(arr2)
def printUnion(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i], end=" ")
            i +=1
        elif arr2[j] < arr1[i]:
            print(arr2[j], end=" ")
            j += 1
        else:
            j +=1
            i +=1

    
    # print remaining elements of the larger array
    while i < m:
        print(arr1[i], end=" ")
        i += 1
    while j < n:
        print(arr2[j], end=" ")
        j += 1

printUnion([1, 2, 4, 5, 6], [2, 3, 5, 7])

print("\n #################################### \n")
printUnion([1, 2, 2, 2, 3], [2, 3, 4, 5])

"""

Method 3:

Time Complexity: O(l1 + l2) 
Auxiliary Space: O(n)

"""

# sorted arrays (Handling Duplicates)
def union_array(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    i = 0
    j = 0
     
    # keep track of last element to avoid duplicates
    prev = None
     
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            if arr1[i] != prev:
                print(arr1[i], end=' ')
                prev = arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            if arr2[j] != prev:
                print(arr2[j], end=' ')
                prev = arr2[j]
            j += 1
        else:
            if arr1[i] != prev:
                print(arr1[i], end=' ')
                prev = arr1[i]
            i += 1
            j += 1
             
    while i < m:
        if arr1[i] != prev:
            print(arr1[i], end=' ')
            prev = arr1[i]
        i += 1
 
    while j < n:
        if arr2[j] != prev:
            print(arr2[j], end=' ')
            prev = arr2[j]
        j += 1
     
  
union_array([1, 2, 2, 2, 3], [2, 3, 4, 5])


"""
Intersection of arrays arr1[] and arr2[]

To find intersection of 2 sorted arrays, follow the below approach : 

    1) Use two index variables i and j, initial values i = 0, j = 0 
    2) If arr1[i] is smaller than arr2[j] then increment i. 
    3) If arr1[i] is greater than arr2[j] then increment j. 
    4) If both are same then print any of them and increment both i and j.

Time Complexity : O(m + n)
Auxiliary Space: O(1)

"""
# Python program to find intersection of
# two sorted arrays
# Function prints Intersection of arr1[] and arr2[]
# m is the number of elements in arr1[]
# n is the number of elements in arr2[]
def printIntersection(arr1, arr2, m, n):
	i, j = 0, 0
	while i < m and j < n:
		if arr1[i] < arr2[j]:
			i += 1
		elif arr2[j] < arr1[i]:
			j+= 1
		else:
			print(arr2[j],end=" ")
			j += 1
			i += 1

# Driver program to test above function
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
m = len(arr1)
n = len(arr2)
printIntersection(arr1, arr2, m, n)



"""
Handling duplicate in Arrays : 
The above code does not handle duplicate elements in arrays. The intersection should not count duplicate elements. To handle duplicates just check whether the current element is already present in the intersection list. Below is the implementation of this approach.

Time Complexity : O(m + n) 
Auxiliary Space : O(min(m, n))

"""
# Python3 program to find Intersection of two
# Sorted Arrays (Handling Duplicates)
def IntersectionArray(a, b, n, m):
	'''
	:param a: given sorted array a
	:param n: size of sorted array a
	:param b: given sorted array b
	:param m: size of sorted array b
	:return: array of intersection of two array or -1
	'''

	Intersection = []
	i = j = 0
	
	while i < n and j < m:
		if a[i] == b[j]:

			# If duplicate already present in Intersection list
			if len(Intersection) > 0 and Intersection[-1] == a[i]:
				i+= 1
				j+= 1

			# If no duplicate is present in Intersection list
			else:
				Intersection.append(a[i])
				i+= 1
				j+= 1
		elif a[i] < b[j]:
			i+= 1
		else:
			j+= 1
			
	if not len(Intersection):
		return [-1]
	return Intersection

# Driver Code
if __name__ == "__main__":

	arr1 = [1, 2, 2, 3, 4]
	arr2 = [2, 2, 4, 6, 7, 8]
	
	l = IntersectionArray(arr1, arr2, len(arr1), len(arr2))
	print(*l)






'''
my tests
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





print("Exp Union:[1, 2, 3, 4, 5, 6, 7], Inter:[3, 5]", my_tests([1, 3, 4, 5, 7],[2, 3, 5, 6]))
print("Exp Union:[2, 4, 5, 6, 8, 10], Inter:[6]", my_tests([2, 5, 6],[4, 6, 8, 10]))