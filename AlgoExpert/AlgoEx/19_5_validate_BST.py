"""

"""
'''
creating a Tree
'''
class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left  = None
        self.right = None
    
    def insert(self,data):
        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.value:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.value = Node(data)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value)
        if self.right:
            self.right.printTree()
tree = Node(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)
tree.insert(9)
tree.insert(10)

'''
Validating BST
'''

# O(n) time | O(d) space
def validateBST(tree):
    return validateBSTHelper(tree,float("-inf"),float("inf"))

def validateBSTHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >=maxValue:
        return False
    leftIsValid = validateBSTHelper(tree.left, minValue, tree.value)
    rightIsValid = validateBSTHelper(tree.right, tree.value, maxValue)
    return leftIsValid and rightIsValid


valBST  = validateBST(tree)
print("validate BST: ",valBST)
