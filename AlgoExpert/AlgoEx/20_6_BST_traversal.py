# O(n) time | O(n) space
def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
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
