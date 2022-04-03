"""
INSERTING A NODE
steps - iteratively or recursively
-create a new node
-starting at the root
    - check if there is a root, if not - the root now becomes the new node!
    - If there is a root, check if the value of the new node is greater than or less
    than the value of the root
    - If it is greater
        - Check to see if there is a node to the right
            - if there is, move to that node and repeat these steps
            - if there is not, add that node as the right property
    - if it is less
        - Check to see if there is a node to the left
            - if there is, move to that node and repeat these steps
            - if there is not, add that node as the left property
"""


class Node:
    def __init__(self, value) -> None:
        self.value  = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert_node(self, val):
        n = Node(val)

    

tree = BinarySearchTree()
tree.root =Node(10)
tree.root.right =Node(15)
tree.root.left =Node(7)
tree.root.left.right=Node(9)

print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)