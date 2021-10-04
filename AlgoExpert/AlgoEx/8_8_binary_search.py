# O(log(n)) time | O(log(n)) space
def binarySearchRecursive(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array,target, left, right):
    if left > right:
        return -1
    middlePoint = (left+right)//2
    potentialMatch =array[middlePoint]

    if target == potentialMatch:
        return True
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middlePoint-1)
    elif target > potentialMatch:
        return binarySearchHelper(array, target, middlePoint+1, right)

# O(log(n)) time | O(1) space
def binarySearchIterative(array, target):
    return binarySearchHelperIterative(array, target,0,len(array)-1)

def binarySearchHelperIterative(array, target, left, right):
    while left <= right:
        middle = (left+right)//2
        potentialMatch =array[middle]

        if potentialMatch == target:
            return middle
        elif  target < potentialMatch:
            right = middle -1
        elif target > potentialMatch:
            left = middle + 1
    return -1



my_array =[0,1,21,33,45,45,61,71,72,73]
my_target =74

print(binarySearchIterative(my_array,my_target))