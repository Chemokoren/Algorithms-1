# algorithm to count leaf nodes in a binary tree
# a node is a leaf if both left and right child nodes are NULL

# getLeafCount(node)
# if node is NULL then return 0
# Else If left and right child nodes are NULL return 1
# Else recursively calculate leaf count of the tree using formula:
# Leaf count of a tree = Leaf count of left subtree + Leaf count of right subtree

class Node:
    def __init__(self, data):
        self.data =data
        self.left =None
        self.right =None

# Function to get the count of leaf nodes in a binary tree
def getLeafCount(node):
    if node is None:
        return 0
    if(node.left is None and node.right is None):
        return 1
    else:
        return getLeafCount(node.left) + getLeafCount(node.right)

# program to test getLeafCount

root =Node(1)
root.left =Node(2)
root.right =Node(3)
root.left.left =Node(4)
root.left.right =Node(5)
root.right.left =Node(20)
root.right.right =Node(22)

print("Leaf count of the tree is %d" % (getLeafCount(root)))

