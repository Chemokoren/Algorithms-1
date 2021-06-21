"""
Double the first element and move zero to end

For a given array of n integers assume that '0' is an invalid number and all others as a 
valid number. Convert the array in such a way that if both current and next element is valid 
then double current value and replace the next number with 0. After the modification,
rearrange the array such that all 0's shifted to the end.

Examples: 

Input : arr[] = {2, 2, 0, 4, 0, 8}
Output : 4 4 8 0 0 0

Input : arr[] = {0, 2, 2, 2, 0, 6, 6, 0, 0, 8}
Output :  4 2 12 8 0 0 0 0 0 0

Approach: First modify the array as mentioned, i.e., if the next valid number is the same
as the current number, double its value and replace the next number with 0.

1. if n == 1
2.     return
3. for i = 0 to n-2
4.     if (arr[i] != 0) && (arr[i] == arr[i+1])
5.         arr[i] = 2 * arr[i]
6.       arr[i+1] = 0
7.       i++

Time Complexity: O(n).

"""

# Python implementation to rearrange the array elements after modification
# function which pushes all zeros to end of an array
def pushZerosToEnd(arr,n):
    # count of non-zero elements
    count =0
    # Traverse the array. If element encountered is non-zero, then replace the element
    # at index 'count' with this element
    for i in range(0, n):
        if arr[i] != 0:
            # here count is incremented
            arr[count] = arr[i]
            count += 1

    # Now all non-zero elements have been shifted to front and 'count' is set as index of
    # first 0. Make all elements 0 from count to end.

    while( count< n):
        arr[count] =0
        count +=1

# function to rearrange the array elements after modification
def modifyAndRearrangeArr(arr, n):
    # if 'arr[]' contains a single element only
    if n == 1:
        return

    # traverse the array
    for i in range(0, n-1):

        # if true, perform the required modification
        if(arr[i] !=0) and (arr[i] == arr[i+1]):

            # double current index value
            arr[i] = 2 * arr[i]

            # put 0 in the next index
            arr[i + 1] = 0

            # increment by 1 so as to move two indexes ahead during loop iteration
            i+=1

    # push all the zeros at the end of 'arr[]'
    pushZerosToEnd(arr,n)

# function to print the array elements
def printArray(arr, n):

    for i in range(0, n):
        print(arr[i], end=" ")
        

arr = [ 0, 2, 2, 2, 0, 6, 6, 0, 0, 8 ]
n = len(arr)
 
print("Original array:",end=" ")
printArray(arr, n)
 
modifyAndRearrangeArr(arr, n)
 
print("\nModified array:",end=" ")
printArray(arr, n)

"""
Approach with efficient zero shiftings:

Although the above solution is efficient, we can further optimise it in shifting 
zero algorithms by reducing the number of operations.

in the above shifting algorithms, we scan some elements twice when we set the count
 index to last index element to zero.

 Efficient zero shifting algorithms:

 int lastSeenPositiveIndex = 0;
for( index = 0; index < n; index++)
{
    if(array[index] != 0)
    {
        swap(array[index], array[lastSeenPositiveIndex]);
        lastSeenPositiveIndex++;
    }
}

"""
print("shiftAllZeroToLeft \n")
# maintain last index with positive value
def shiftAllZeroToLeft(arr, n):
    lastSeenNonZero = 0
    for index in range(0, n):

        # if element is non-zero
        if(arr[index] != 0):
            # swap current index, with lastSeen non-zero
            arr[index], arr[lastSeenNonZero] = arr[lastSeenNonZero], arr[index]

            # next element will be last seen non-zero
            lastSeenNonZero +=1


arr = [ 0, 2, 2, 2, 0, 6, 6, 0, 0, 8 ]
print(arr)
shiftAllZeroToLeft(arr,len(arr))

print(arr)

