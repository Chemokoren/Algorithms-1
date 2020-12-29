class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

# O(n) time | O(n) space
def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right,array)
    return array

# O(n) time | O(n) space
def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array

# O(n) time | O(n) space
def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right,array)
        array.append(tree.value)
    return array

#               10
#             /    \
#           5       15
#         /   \       \
#       2       5      22
#      /
#     1
#

# final result
# In-Order  [1,2,5,5,10,15,22]
# pre-Order [10,5,2,1,5,15,22]
# post-Order [1,2,5,5,22,15,10]

root =Node(10)
root.left =Node(5)
root.right =Node(15)
root.left.left =Node(2)
root.left.right =Node(5)
root.right.right =Node(22)
root.left.left.left =Node(1)

print("################ In Order Traversal ##################")
print(inOrderTraverse(root,[]))

print("################ Pre Order Traversal ##################")
print(preOrderTraverse(root,[]))

print("################ Post Order Traversal ##################")
print(postOrderTraverse(root,[]))
