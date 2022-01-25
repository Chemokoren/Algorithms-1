class Node:
    def __init__(self,element) -> None:
        self.element = element
        self.left = None
        self.right = None

    def insert(self,value):
        if self.element:
            if value < self.element:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            if value > self.element:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)

        else:
            self.element = value
            
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.element),
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
    if abs(target - closest) > abs(target -tree.element):
        closest = tree.element
    if target < tree.element:
        return findClosestValueInBSTHelper(tree.left,target,closest)
    elif target > tree.element:
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
        if abs(target -closest) > abs(target-currentNode.element):
            closest = currentNode.element
        if (target < currentNode.element):
            currentNode = currentNode.left
        elif (target > currentNode.element):
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
print("findClosestValueInBSTHelper: approach 1", findClosestValueInBSTHelper(my_tree,my_target,my_closest))
print("my closest value is: ", findClosestValueInBSTIterative(my_tree,my_target))