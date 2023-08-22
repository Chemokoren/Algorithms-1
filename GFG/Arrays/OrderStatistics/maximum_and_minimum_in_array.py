"""
METHOD 1 (Simple Linear Search) 

Initialize values of min and max as minimum and maximum of the first two elements 
respectively. Starting from 3rd, compare each element with max and min, and 
change max and min accordingly (i.e., if the element is smaller than min then 
change min, else if the element is greater than max then change max, else ignore
the element) 

"""

def max_min(arr):
    max_val =-float('inf') 
    min_val = float('inf')

    if len(arr) ==1:
        min_val =arr[0]
        max_val =arr[0]
        return min_val, max_val

    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val =arr[i]
        
        if arr[i] < min_val:
            min_val =arr[i]
    return min_val, max_val

print("expected: (1, 3000), actual: ",max_min([1000, 11, 445, 1, 330, 3000]))
print("expected: (1, 1), actual: ",max_min([1]))

"""

Time Complexity: O(n)

Auxiliary Space: O(1) as no extra space was needed.

In this method, the total number of comparisons is 1 + 2(n-2) in the worst case 
and 1 + n – 2 in the best case. 
In the above implementation, the worst case occurs when elements are sorted in 
descending order and the best case occurs when elements are sorted in ascending 
order.

METHOD 2 (Tournament Method) 

Divide the array into two parts and compare the maximums and minimums of the two
parts to get the maximum and the minimum of the whole array.


Pair MaxMin(array, array_size)
   if array_size = 1
      return element as both max and min
   else if arry_size = 2
      one comparison to determine max and min
      return that pair
   else    /* array_size  > 2 */
      recur for max and min of left half
      recur for max and min of right half
      one comparison determines true max of the two candidates
      one comparison determines true min of the two candidates
      return the pair of max and min

"""

def get_min_max(low, high, arr):
    arr_max =arr[low]
    arr_min =arr[low]

    # if there is only one element
    if low == high:
        arr_max =arr[low]
        arr_min = arr[low]
        