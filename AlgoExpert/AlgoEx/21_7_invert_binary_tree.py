"""
            1                                   1
          /   \                                /  \
         2     3                              3    2
        / \   / \                            / \  / \
       4   5 6   7                          7  6 5   4
      / \                                           / \
     8   9                                         9   8

     initial tree                           inverted tree    



"""
# O(n) time | O(n) space
def invertBinaryTreeIterative(tree):
    my_queue =[tree]
    while len(my_queue):
        tree_element = my_queue.pop(0)
        if tree_element is None:
            continue
        swapLeftAndRightElement(tree_element)
        my_queue.append(tree_element.left)
        my_queue.append(tree_element.right)

def swapLeftAndRightElement(tree):
    tree.left, tree.right = tree.right, tree.left


# O(n) time | O(d) space
def invertBinaryTreeRecursive(tree):
    if tree is None:
        return 
    swapLeftAndRightElement(tree)
    invertBinaryTreeRecursive(tree.left)
    invertBinaryTreeRecursive(tree.right)
