"""
Given a sorted array, and a target number e.g. 45, find the range of indices in the input array in 
between which you can find the target value.

In this case the range is [4,9] because 4 is the first index where you can find the first target value 45 and 
9 is the last index you can find the value 45.
"""
# recursive approach
# O(log(n)) time | O(log(n)) space
def searchForRange(array, target):
    finalRange =[-1, -1]
    alteredBinarySearch(array, target, 0, len(array)-1, finalRange, True)
    alteredBinarySearch(array, target, 0, len(array)-1, finalRange, False)
    return finalRange

def alteredBinarySearch(array, target, left,right, finalRange, goLeft):
    if left > right:
        return
    mid =(left + right)
    if array[mid] < target:
        alteredBinarySearch(array, target, mid + 1, right, finalRange, goLeft)
    elif array[mid] > target:
        alteredBinarySearch(array, target, left, mid -1, finalRange, goLeft)
    else:
        if goLeft:
            if mid ==0 or array[mid -1] != target:
                finalRange[0] =mid
            else:
                alteredBinarySearch(array, target, left, mid -1, finalRange, goLeft)
        else:
            if mid == len(array) -1 or array[mid + 1] != target:
                finalRange[1] =mid
            else:
                alteredBinarySearch(array, target, mid+1, right, finalRange, goLeft)

# iterative approach
# O(log(n)) time | O(1) space
def searchForRange1(array, target):
    finalRange =[-1, -1]
    alteredBinarySearch(array, target, 0, len(array), -1, finalRange, True)
    alteredBinarySearch(array, target, 0, len(array), -1, finalRange, False)

def alteredBinarySearch1(array, target, left,right, finalRange, goLeft):
    if left > right:
        return
    mid =(left + right)
    if array[mid] < target:
        left =mid + 1
    elif array[mid] > target:
        right =mid -1
    else:
        if goLeft:
            if mid ==0 or array[mid -1] != target:
                finalRange[0] =mid
                return
            else:
                right = mid -1
        else:
            if mid == len(array) -1 or array[mid + 1] != target:
                finalRange[1] =mid
                return
            else:
                left =mid+1

print("Recursive approach", searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45))
print("Iterative approach", searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45))