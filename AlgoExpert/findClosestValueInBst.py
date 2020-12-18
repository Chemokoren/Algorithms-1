# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space

def findClosestValuesInBst(tree, target):
    return findClosestValuesInBstHelper(tree,target,float("inf"))

def findClosesValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest =tree.value
    if target < tree.value:
        return findClosesValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosesValueInBstHelper(tree.right,target,closest)
    else:
        return closest


# iterative approach
# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space

def findClosestValuesInBstIter(tree, target):
    return findClosesValueInBstHelperIterative(tree,target,float("inf"))

def findClosesValueInBstHelperIterative(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest =currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
        return closest

