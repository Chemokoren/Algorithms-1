'''
Binary Tree
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
def invertBinaryTreeIterative(tree): # takes in a binary tree or the root node of a binary tree
    my_queue =[tree] # holds the root node
    while len(my_queue):
        tree_element = my_queue.pop(0)
        if tree_element is None: # nothing to swap past a leaf node     
            continue
        swapLeftAndRightElement(tree_element)
        my_queue.append(tree_element.left)
        my_queue.append(tree_element.right)

def swapLeftAndRightElement(tree):
    tree.left, tree.right = tree.right, tree.left


# O(n) time | O(d) space
# O(n) time | O(d) or O(log(n))space  where d is the depth of the tree

def invertBinaryTreeRecursive(tree):
    if tree is None:
        return 
    swapLeftAndRightElement(tree)
    invertBinaryTreeRecursive(tree.left)
    invertBinaryTreeRecursive(tree.right)


# Driver code
print(invertBinaryTreeRecursive(tree))