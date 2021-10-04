class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def insert(self,value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            if value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)

        else:
            self.value = value
            
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value),
        if self.right:
            self.right.printTree()


# Approach 1
# Average: O(log(n)) time | O(log(n)) space
# Worst: O(log(n)) time | O(log(n)) space
def findClosestValueInBST(tree,target):
    return findClosestValueInBSTHelper(tree, target, float("inf"))

def findClosestValueInBSTHelper(tree,target, closest):
    if tree is None:
        return closest
    if abs(target -closest) > abs(target -tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBSTHelper(tree.left,target,closest)
    elif target > tree.value:
        return findClosestValueInBSTHelper(tree.right, target, closest)
    else:
        return closest


# Approach 2
# Average: O(log(n)) time | O(log(n)) space
# Worst: O(log(n)) time | O(log(n)) space

def findClosestValueInBSTIterative(tree, target):
    currentNode =tree
    closest = float("inf")

    while currentNode is not None:
        if abs(target -closest) > abs(target-currentNode.value):
            closest = currentNode.value
        if (target < currentNode.value):
            currentNode = currentNode.left
        elif (target > currentNode.value):
            currentNode = currentNode.right
        else:
            break
    return closest



root = Node(10)
root.insert(5)
root.insert(15)
root.insert(2)
root.insert(5)
root.insert(13)
root.insert(22)
root.insert(14)
root.printTree()



my_target =10
my_tree =root
my_closest =float("inf")
print("my closest value is: ", findClosestValueInBSTIterative(my_tree,my_target))