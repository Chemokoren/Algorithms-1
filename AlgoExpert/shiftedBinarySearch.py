# Iterative approach
# O(log(n)) time | O(1) space
def shiftedBinarySearch1(array, target):
    return shiftedBinarySearch1(array, target, 0, len(array) -1)
def shiftedBinarySearchHelper1(array, target, left, right):
    while left <=right:
        middle =(left + right) //2
        potentialMatch =array[middle]
        leftNum =array[left]
        rightNum =array[right]
        if target == potentialMatch:
            return middle
        elif leftNum <= potentialMatch:
            if target < potentialMatch and target >= leftNum:
                right =middle -1
            else:
                left =middle +1

        else:
            if target > potentialMatch and target <= rightNum:
                left = middle + 1
            else:
                right =middle - 1
    return -1

# Recursive approach
# O(log(n)) time | O(log(n)) space -because of frames in the callstack

def shiftedBinarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle =(left + right) //2
    potentialMatch =array[middle]
    leftNum =array[left]
    rightNum =array[right]

    if target == potentialMatch:
        return middle
    elif leftNum <= potentialMatch:
        if target < potentialMatch and target >=leftNum:
            return shiftedBinarySearchHelper(array, target , left, middle -1)
        else:
            return shiftedBinarySearchHelper(array, target, middle + 1, right)
    else:
        if target > potentialMatch and target <=rightNum:
            return shiftedBinarySearchHelper(array, target, middle +1, right)
        else:
             return shiftedBinarySearchHelper(array, target, left, middle-1)

