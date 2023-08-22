"""
Smallest Difference Triplet from Three arrays

Three arrays of same size are given. Find a triplet such that maximum - minimum in that triplet is
minimum of all the triplets. A triplet should be selected in a way such that it should have one
number from each of the three given arrays.

If there are 2 or more smallest difference triplets, then the one with the smallest sum of its
elements should be displayed.

Examples : 

Input : arr1[] = [5, 2, 8]
    arr2[] = [10, 7, 12]
    arr3[] = [9, 14, 6]
Output : 7, 6, 5

Input : arr1[] = {15, 12, 18, 9}
    arr2[] = {10, 17, 13, 8}
    arr3[] = {14, 16, 11, 5}
Output : 11, 10, 9

Note:The elements of the triplet are displayed in non-decreasing order.


Simple Solution
- Consider each and every triplet and find the required smallest difference triplet out of them.
- Complexity of O(n^3)

Efficient Solution: 

    Sort the 3 arrays in non-decreasing order.
    Start three pointers from left most elements of three arrays.
    Now find min and max and calculate max-min from these three elements.
    Now increment pointer of minimum element’s array.
    Repeat steps 2, 3, 4, for the new set of pointers until any one pointer reaches to its end
"""
# # implementation of smallest difference triplet
# # function to find maximum number
def maximum(a, b, c):
    return max(max(a,b), c)

# function to find minimum number
def minimum(a, b, c):
    return min(min(a,b),c)


def smallest_difference_triplet(arr1, arr2, arr3):
    n = len(arr1)
    arr1.sort()
    arr2.sort()
    arr3.sort()
    
    # To store resultant three numbers
    res_min = 0; res_max = 0; res_mid = 0
    
    # pointers to arr1, arr2, arr3 respectively
    
    i = 0; j = 0; k = 0
    
    # Loop until one array reaches to its end # Find the smallest difference.
    
    diff = 2147483647
    while (i < n and j < n and k < n):
        
        sum = arr1[i] + arr2[j] + arr3[k]
        
        # maximum number
        max = maximum(arr1[i], arr2[j], arr3[k])
        
        # Find minimum and increment its index.
        # 
        min = minimum(arr1[i], arr2[j], arr3[k])
        if (min == arr1[i]):
            i += 1
            
        elif (min == arr2[j]):
            j += 1
        else:
            k += 1
            
        # Comparing new difference with the # previous one and updating accordingly
        
        if (diff > (max - min)):
            diff = max - min
            res_max = max
            res_mid = sum - (max + min)
            res_min = min
            
    return (res_max, res_mid, res_min)


print(smallest_difference_triplet([5, 2, 8], [10, 7, 12], [9, 14, 6]))
