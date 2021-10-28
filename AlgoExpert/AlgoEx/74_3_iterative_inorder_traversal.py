"""
Iterative Inorder Traversal

            1
           / \
          2    3
        /     / \
       4     6   7
       \
        9

        cb(4), cb(9), cb(2), cb(1), cb(6), cb(3), cb(7)
        

"""

# O(time) time | O(1) spaced
def iterativeInOrderTraversal(tree, callback):
    previousNode = None
    currentNode =tree

    while currentNode is not None:
        if previousNode is None or previousNode == currentNode.parent:
            if currentNode.left is not None:
                nextNode = currentNode.left
            else:
                callback(currentNode)
                nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        elif previousNode == currentNode.left:
            callback(currentNode)
            nextNode = currentNode.right if currentNode.right is not None else currentNode.parent

        else: # elif previousNode = currentNode.right
            nextNode = currentNode.parent
        
        previousNode = currentNode
        currentNode = nextNode
