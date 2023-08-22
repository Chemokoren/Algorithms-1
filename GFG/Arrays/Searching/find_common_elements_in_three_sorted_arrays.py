"""
Find common elements in three sorted arrays

Given three arrays sorted in non-decreasing order, print all common elements in these arrays

    Input: 
    ar1[] = {1, 5, 10, 20, 40, 80} 
    ar2[] = {6, 7, 20, 80, 100} 
    ar3[] = {3, 4, 15, 20, 30, 70, 80, 120} 
    Output: 20, 80

    Input: 
    ar1[] = {1, 5, 5} 
    ar2[] = {3, 4, 5, 5, 10} 
    ar3[] = {5, 5, 10, 20} 
    Output: 5, 5

A simple solution is to first find intersection of two arrays and store the intersection in a 
temporary array, then find the intersection of third array and temporary array. Time complexity of 
this solution is O(n1+n2+n3) where n1, n2 and n3 are sizes of ar1[], ar2 and ar3[] respectively.

The above solution requires extra space and two loops, we can find the common elements using
a single loop without extra space. The idea is similar to intersection of two arrays. Like two 
arrays loop, we run a loop and traverse three arrays.

Let the current element traversed in ar1[] be x, in ar2[] be y and in ar3[] be z. We can have the
following cases inside the loop.
- if x, y and z are same, we can simply print any of them as common element and move ahead in all
three arrays.
- Else if x <y, we can move ahead in ar1[] as x cannot be a common element.
- Else if x > z and y > z, we can simply move ahead in ar3[] as z cannot be a common element.


Time complexity of the above solution is O(n1 + n2 + n3). In the worst case, the largest sized 
array may have all small elements and middle-sized array has all middle elements.

Auxiliary Space:   O(1)

"""
def find_common(ar1, ar2,ar3):
    i,j,k =0,0,0

    # iterate through three arrays while all arrays have elements
    while i < len(ar1) and j <len(ar2) and k < len(ar3):

        # if x ==y and y==z, print any of them and move ahead in all arrays
        if(ar1[i] == ar2[j] and ar2[j] ==ar3[k]):
            print(ar1[i])
            i +=1
            j +=1
            k +=1
        # x < y
        elif ar1[i] < ar2[j]:
            i += 1
        
        # y < z 
        elif ar2[j] < ar3[k]:
            j += 1

        # We reach here when x > y and z < y, i.e., z is smallest
        else:
            k +=1


print("CC Expected:[20,80]", find_common([1, 5, 10, 20, 40, 80],[6, 7, 20, 80, 100],[3, 4, 15, 20, 30, 70, 80, 120]))

"""

Method 2:

 

The approach used above works well if the arrays does not contain duplicate values however it can fail in cases where the array elements are repeated. This can lead to a single common element to get printed multiple times.

 

These duplicate entries can be handled without using any additional data structure by keeping the track of the previous element. Since the elements inside the array are arranged in sorted manner there is no possibility for the repeated elements to occur at random positions. 

 

Let’s consider the current element traversed in ar1[] be x, in ar2[] be y and in ar3[] be z and let the variables prev1, prev2, prev3 for keeping the track of last encountered element in each array and initialize them with INT_MIN. Hence for every element we visit across each array, we check for the following.

 

    If x = prev1, move ahead in ar1[] and repeat the procedure until x != prev1. Similarly, apply the same for the ar2[] and ar3[].
    If x, y, and z are same, we can simply print any of them as common element, update prev1, prev2, and prev3 and move ahead in all three arrays.
    Else If (x < y), we update prev1 and move ahead in ar1[] as x cannot be a common element.
    Else If (y < z), we update prev2 and move ahead in ar2[] as y cannot be a common element.
    Else If (x > z and y > z), we update prev3 and we move ahead in ar3[] as z cannot be a common element.

Time Complexity for the above approach still remains O(n1 + n2 + n3) and space complexity also
remains O(1) and no extra space and data structure is required to handle the duplicate array
 entries.

"""

def find_common_three(ar1, ar2, ar3):

    n1 = len(ar1)
    n2 = len(ar2)
    n3 = len(ar3)

    # Initialize starting indexes for ar1[], ar2 and ar3[]
    i = 0
    j = 0
    k = 0
    
    # prev1, prev2, prev3 tracks previous elements
    prev1 = prev2 =prev3 =-float("inf")-1

    while i < len(ar1) and j <len(ar2) and k < len(ar3):

        # if ar1[i] = prev1 and i < n1, keep incrementing i
        while(ar1[i] == prev1 and i < n1-1):
            i +=1

        # if ar2[j] == prev2 and j < n2, keep incrementing j
        while(ar2[j] == prev2 and j < n2):
            j +=1

        # if ar3[k] = prev3 and k < n3, keep incrementing k
        while(ar3[k] == prev3) and k < n3:
            k += 1
        
        # if x = y and y = , or any of them, update prev1, prev2, prev3 and move ahead in each 
        # array
        if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
            print(ar1[i], end=" ")
            prev1 = ar1[i]
            prev2 = ar2[j]
            prev3 = ar3[k]
            i += 1
            j += 1
            k += 1
        # if x < y, update prev1 and increment i
        elif(ar1[i] < ar2[j]):
            prev1 = ar1[i]
            i +=1

        # If y < z, update prev2 and increment j
        elif(ar2[j] < ar3[k]):
            prev2 = ar2[j]
            j += 1
        # We reach here when x > y and z < y, i.e., z is smallest update prev3 and increment k
        else:
            prev3 =ar3[k]
            k += 1

print("Three Expected:[20,80]", find_common_three([1, 5, 10, 20, 40, 80],[6, 7, 20, 80, 100],[3, 4, 15, 20, 30, 70, 80, 120]))


"""

Method 4:

In this approach, we will first delete the duplicate from each array, and after this, we will 
find the frequency of each element and the element whose frequency equals 3 will be printed. 
For finding the frequency we can use a map but in this, we will use an array instead of a map. 
But the problem with using an array is, we cannot find the frequency of negative numbers so in the
code given below we will consider each and every element of array to be positive.

Time Complexity: O(n1 + n2) 
Auxiliary Space: O(maximum element in array))

"""

def common_elements_four(arr1,arr2, arr3):
    n1 = len(arr1)
    n2 = len(arr2)
    n3 = len(arr3)

    # creating a max variable for storing the maximum value present in all the three arrays
    # this will be the size of array for calculating the frequency of each element present in all
    # the array
    Max = -float("inf") -1

    # deleting duplicates in linear time for arr1
    res1 = 1
    for i in range(1, n1):
        Max = max(arr1[i], Max)
        if arr1[i] != arr1[res1 - 1]:
            arr1[res1] = arr1[i]
            res1 +=1

    # deleting duplicates in linear time for arr2
    res2 = 1

    for i in range(1, n2):
        Max = max(arr2[i], Max)
        if(arr2[i] != arr2[res2 -1]):
            arr2[res2] = arr2[i]
            res2 +=1

    # deleting duplicates in linear time for arr3
    res3 = 1
    for i in range(1, n3):
        Max = max(arr3[i], Max)
        if(arr3[i] != arr3[res3 -1]):
            arr3[res3] = arr3[i]
            res3 += 1

    # creating an array for finding frequency
    freq =[0 for i in range(Max + 1)]

    # calculating the frequency of all the elements present in all the array
    for i in range(res1):
        freq[arr1[i]] +=1
    for i in range(res2):
        freq[arr2[i]] +=1
    for i in range(res3):
        freq[arr3[i]] +=1

    # iterating till max and whenever the frequency of element will be three we print that 
    # element
    for i in range(Max + 1):
        if freq[i] == 3:
            print(i, end=" ")


    
print("Four Expected:[20,80]", common_elements_four([1, 5, 10, 20, 40, 80],[6, 7, 20, 80, 100],[3, 4, 15, 20, 30, 70, 80, 120]))


"""
Method 4: Using STL 

The idea is to use hash set. Here we use 2 of the sets to store elements of the 1st and 2nd 
arrays. The elements of the 3rd array are then checked if they are present in the first 2 sets. 
Then, we use a 3rd set to prevent any duplicates from getting added to the required array.


Time Complexity: O(n1 + n2 + n3) 
Space complexity: O(n1 + n2 + n3) 
"""
def find_common_five(a,b,c):

    n1 = len(a)
    n2 = len(b)
    n3 = len(c)

    # three sets to maintain frequency of elements
    uset  = set()
    uset2 = set()
    uset3 = set()
    for i in range(n1):
        uset.add(a[i])

    for i in range(n2):
        uset2.add(b[i])

    # checking if elements of 3rd array are present in first 2 sets
    for i in range(n3):
        if(c[i] in uset and c[i] in uset2):

            # using a 3rd set to prevent duplicates
            if c[i] not in uset3:
                print(c[i], end=" ")
            uset3.add(c[i])

    
print("Five Expected:[20,80]", find_common_five([1, 5, 10, 20, 40, 80],[6, 7, 20, 80, 100],[3, 4, 15, 20, 30, 70, 80, 120]))


"""

Method 5: Using Binary Search
-----------------------------

This approach is a modification of previous approach. Here Instead of using map, we use binary 
search to find elements of 1st array that are present in 2nd and 3rd arrays.

Time complexity: O(n1(log(n2*n3))

Space complexity: O(1)

"""
# find all range having set bit sum X in array

def binary_search(arr, element):

    n = len(arr)
    l, h = 0, n-1
    while(l <= h):
        mid =(l + h) // 2
        if (arr[mid] == element):
            return True
        elif (arr[mid] > element):
            h = mid -1
        else:
            l = mid + 1
    return False

def find_common_six(a, b, c):
    n1 = len(a)
    res =[]

    # Iterate on first array
    for j in range(n1):
        if(j != 0 and a[j] ==a[j -1]):
            continue
        # check if the element is present in 2nd and 3rd
        if(binary_search(b, a[j]) and binary_search(c, a[j])):
            # print(a[j], end=" ")
            res.append(a[j])
        
    return res

print("Six Expected:[20,80]", find_common_six([1, 5, 10, 20, 40, 80],[6, 7, 20, 80, 100],[3, 4, 15, 20, 30, 70, 80, 120]))
print("Six Expected:[5,5]", find_common_six([1, 5, 5],[3, 4, 5, 5, 10],[5, 5, 10, 20]))








'''

my tests

'''
def my_tests(arr1,arr2,arr3):
    res =[]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            for k in range(len(arr3)):
                if arr1[i] == arr2[j] == arr3[k]:
                    # return arr1[i]
                    res.append(arr1[i])

    return res

# print("Expected:[5,5]", my_tests([1, 5, 5],[3, 4, 5, 5, 10],[5, 5, 10, 20]))
print("Expected:[20,80]", my_tests([1, 5, 10, 20, 40, 80],[6, 7, 20, 80, 100],[3, 4, 15, 20, 30, 70, 80, 120]))

# Time complexity: O(n) | Space complexity: O(1)
def my_tests_two(arr1,arr2,arr3):
    res =[]
    i =0
    j =0
    k =0

    while i < len(arr1) and j <len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            res.append(arr1[i])
            i +=1
            j +=1
            k +=1
        elif min(arr1[i], arr2[j], arr3[k]) ==arr1[i]:
            i +=1
        elif min(arr1[i], arr2[j], arr3[k]) ==arr2[j]:
            j +=1
        elif min(arr1[i], arr2[j], arr3[k]) ==arr3[k]:
            k +=1
    return res

print("Two Expected:[20,80]", my_tests_two([1, 5, 10, 20, 40, 80],[6, 7, 20, 80, 100],[3, 4, 15, 20, 30, 70, 80, 120]))
print("Expected:[5,5]", my_tests_two([1, 5, 5],[3, 4, 5, 5, 10],[5, 5, 10, 20]))