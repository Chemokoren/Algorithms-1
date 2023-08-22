def binarysearchIterative(A, key):
    low =0
    high = len(A) -1
    while(low <= high):
        mid =(low + high) //2
        if key == A[mid]:
            return True
        elif key < A[mid]:
            high =mid-1
        else:
            low =mid+1
    return False

A = [15, 21, 47,84,96]
found =binarysearchIterative(A, 46)
print("The element 46",found)


"""
binary search recursive
"""

def binarysearchRecursive(A, key, low, high):
    if low > high:
        return False
    else:
        mid = (low + high ) // 2
        if key == A[mid]:
            return True
        elif key < A[mid]:
            return binarysearchRecursive(A, key,low,mid-1)
        else:
            return binarysearchRecursive(A, key,mid+1,high)

A = [15, 21, 47,84,96]
low =0
high =len(A) -1
found =binarysearchRecursive(A ,84, low,high)
print("The element recursively 46: ",found)