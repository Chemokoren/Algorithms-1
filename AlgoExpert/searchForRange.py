# recursive approach
# O(log(n)) time | O(log(n)) space
def searchForRange(array, target):
    finalRange =[-1, -1]
    alteredBinarySearch(array, target, 0, len(array), -1, finalRange, True)
    alteredBinarySearch(array, target, 0, len(array), -1, finalRange, False)

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
