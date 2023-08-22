'''
Creating a BST
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
    '''
    display the tree - inorder traversal
    '''
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value,end="-")
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
Traversal approaches
'''
# O(n) time | O(n) space
def InOrderTraverse(tree, array):
    if tree is not None:
        InOrderTraverse(tree.left, array)
        array.append(tree.value)
        InOrderTraverse(tree.right, array)
    return array

# O(n) time | O(n) space
def PreOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        PreOrderTraverse(tree.left, array)
        PreOrderTraverse(tree.right, array)
    return array

# O(n) time | O(n) space
def PostOrderTraverse(tree, array):
    if tree is not None:
        PreOrderTraverse(tree.left, array)
        PreOrderTraverse(tree.right,array)
        array.append(tree.value)
    return array

array_inorder =  []
array_preorder = []
array_postorder = []

print( tree.printTree())
print("Inorder traversal :", InOrderTraverse(tree, array_inorder))
print("Preorder traversal:", PreOrderTraverse(tree, array_preorder))
print("Postorder traversal:", PostOrderTraverse(tree, array_postorder))