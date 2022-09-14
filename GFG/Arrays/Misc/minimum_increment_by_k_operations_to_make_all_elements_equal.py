"""
Minimum increment by k operations to make all elements equal

You are given an array of n-elements, you have to find the number of operations needed to make all 
elements of array equal. Where a single operation can increment an element by k. If it is not possible
to make all elements equal print-1.

Example:

Input : arr[] = {4, 7, 19, 16},  k = 3
Output : 10

Input : arr[] = {4, 4, 4, 4}, k = 3
Output : 0

Input : arr[] = {4, 2, 6, 8}, k = 3
Output : -1

To solve this question we require to check whether all elements can become equal or not and that too
only by incrementing k from elements value. For this we have to check that the difference of any two
elements should always be divisible by k. If it is so, then all elements can become equal otherwise
they cannot become equal in any case by incrementing k from them. Also, the number of operations
required can be calculated by finding value of(max -Ai)/k for all elements. Where max is maximum element
of array.

// iterate for all elements
for (int i=0; i<n; i++)
{
    // check if element can make equal to max
    //  or not if not then return -1
    if ((max - arr[i]) % k != 0 )
        return -1;

    // else update res for required operations
    else
        res += (max - arr[i]) / k ;
}

return res;


Time Complexity: O(n)
Auxiliary Space: O(1)

"""
# function for calculating min operations
def minOps(arr, k):

    n = len(arr)
    # max elements of array
    max1 = max(arr)
    res = 0

    # iterate for all elements
    for i in range(0, n):
        # check if element can make equal to max or not if not then return -1
        if((max1 - arr[i]) % k !=0):
            return -1

        # else update res for required operations
        else:
            res += (max1 - arr[i]) / k

    # return result
    return int(res)


print("Expected: 24 , Actual:", minOps([21, 33, 9, 45, 63], 6))
print("Expected: 10 , Actual:", minOps([4, 7, 19, 16], 3))
print("Expected: 0 , Actual:", minOps([4, 4, 4, 4], 3))
print("Expected: -1 , Actual:", minOps([4, 2, 6, 8], 3))