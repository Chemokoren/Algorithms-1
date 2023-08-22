"""
Find relative complement of two sorted arrays

Given two sorted arrays arr1 and arr2 of size m and n respectively. We need to find relative complement
of two array i.e, arr1-arr2 which means that we need to find all those elements which are present in
arr1 but not in arr2.

Input : arr1[] = {3, 6, 10, 12, 15}
        arr2[] = {1, 3, 5, 10, 16}
Output : 6 12 15
The elements 6, 12 and 15 are present
in arr[], but not present in arr2[]
         
Input : arr1[] = {10, 20, 36, 59}
        arr2[] = {5, 10, 15, 59}
Output : 20 36

Take two pointers i and j which traverse through arr1 and arr2 respectively. 
If arr1[i] element is smaller than arr2[j] element print this element and increment i. 
If arr1 element is greater than arr2[j] element then increment j. 
otherwise increment i and j. 

Time Complexity : O(m + n)
Auxiliary Space: O(1)

"""
# program to find all those elements of arr1[] that are not present in arr2[]
def relative_complement(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i = 0
    j = 0
    while(i < n  and j < m):
        # if current element in arr2[]is greater, then arr1[i] can't be present in arr2[j..m-1]
        if(arr1[i] < arr2[j]):
            print(arr1[i], " ", end="")
            i +=1

            # skipping smaller elements of arr2[]
        elif(arr1[i] > arr2[j]):
            j += 1

            # Equal elements found(skipping in both arrays)
        elif(arr1[i] == arr2[j]):
            i += 1
            j += 1
    # Printing remaining elements of arr1[]
    while(i < n):
        print(arr1[i], " ", end="")

relative_complement([3, 6, 10, 12, 15], [1, 3, 5, 10, 16])







def my_tests(arr1, arr2):
    res =[]
    for i in range(len(arr1)):
        if arr1[i] not in arr2:
            res.append(arr1[i])
    return res

print("Expected:[20 36], Actual: ",my_tests([10, 20, 36, 59], [5, 10, 15, 59]))
print("Expected:[6 12 15], Actual: ",my_tests([3, 6, 10, 12, 15], [1, 3, 5, 10, 16]))

