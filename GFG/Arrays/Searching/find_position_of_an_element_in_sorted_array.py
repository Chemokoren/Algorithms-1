"""
Find position of an element in a sorted array of infinite numbers

Suppose you have a sorted array of infinite numbers, how would you search an element in the array?

Since array is sorted, the first thing clicks into mind is binary search, but the problem here is 
that we don’t know size of array. 
If the array is infinite, that means we don’t have proper bounds to apply binary search. 
So in order to find position of key, first we find bounds and then apply binary search algorithm.
Let low be pointing to 1st element and high pointing to 2nd element of array, Now compare key with 
high index element, 
->if it is greater than high index element then copy high index in low index 
and double the high index. 
->if it is smaller, then apply binary search on high and low indices found. 

Let p be the position of element to be searched. Number of steps for finding high index ‘h’ is 
O(Log p). The value of ‘h’ must be less than 2*p. The number of elements between h/2 and h must be 
O(p). Therefore, time complexity of Binary Search step is also O(Log p) and overall time 
complexity is 2*O(Log p) which is O(Log p).

"""

# program to demonstrate working of an algorithm that finds an element in an array of infinite 
# size
def binary_search(arr,l,r,x):
 
    if r >= l:
        mid = l+(r-l)//2
 
        if arr[mid] == x:
            return mid
 
        if arr[mid] > x:
            return binary_search(arr,l,mid-1,x)
 
        return binary_search(arr,mid+1,r,x)
 
    return -1


# function takes an infinite size array and a key to be searched and returns its position if found 
# else -1
# we don't know size of a[] and we can assume size to be infinite in this function
# Note that this function assumes a[] to be of infinite size therefore, there is no index out of
# bound checking
def find_pos(a, key):
    l, h, val = 0, 1, a[0]

    # Find h to do binary search
    while val < key:
        l = h # store previous high
        h = 2 * h # double high index
        val = a[h] # update new val
    # at this point we have updated low and high indices, thus use binary search between them
    return binary_search(a,l,h,key)


arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
ans = find_pos(arr,10)
if ans == -1:
    print ("Element not found")
else:
    print("Element found at index",ans)