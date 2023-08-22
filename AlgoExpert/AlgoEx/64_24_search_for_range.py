"""
Search For Range - use altered binary search
"""

# O(log(n)) time | O(log(n)) space
def searchForRange(array, target):
    finalRange =[-1,-1]
    alteredBinarySearch(array, target, 0, len(array)-1, finalRange, True)
    alteredBinarySearch(array, target, 0, len(array)-1, finalRange, False)
    return finalRange

def alteredBinarySearch(array, target, left, right, finalRange, goLeft):
    if left > right:
        return
    mid = (left + right) // 2

    if array[mid] < target:
        alteredBinarySearch(array, target, mid+1, right, finalRange, goLeft)
    elif array[mid] > target:
        alteredBinarySearch(array, target, left, mid-1, finalRange, goLeft)
    else:
        if goLeft:
            if mid == 0 or array[mid-1] != target:
                finalRange[0] =mid
            else:
                alteredBinarySearch(array, target, left, mid-1, finalRange, goLeft)
        else:
            if mid == len(array) -1 or array[mid + 1] != target:
                finalRange[1] = mid
            else:
                alteredBinarySearch(array, target, mid +1, right, finalRange, goLeft)

# approach 2 - iterative
# O(log(n)) time | O(log(n)) space
def searchForRangeIterative(array, target):
    finalRange =[-1,-1]
    alteredBinarySearchIterative(array, target, 0, len(array)-1, finalRange, True)
    alteredBinarySearchIterative(array, target, 0, len(array)-1, finalRange, False)
    return finalRange

def alteredBinarySearchIterative(array, target, left, right, finalRange, goLeft):
    while left <= right:
        mid = (left + right) // 2

        if array[mid] < target:
            left = mid +1
        elif array[mid] > target:
            right = mid -1
        else:
            if goLeft:
                if mid == 0 or array[mid-1] != target:
                    finalRange[0] =mid
                    return 
                else:
                    right = mid-1
            else:
                if mid == len(array) -1 or array[mid + 1] != target:
                    finalRange[1] = mid
                    return 
                else:
                    left = mid +1


my_array =[0,1,21,33,45,45,45,45,45,45,61,71,73]
my_target=45

print("recursive approach: ",searchForRange(my_array, my_target))
print("iterative approach: ",searchForRangeIterative(my_array, my_target))