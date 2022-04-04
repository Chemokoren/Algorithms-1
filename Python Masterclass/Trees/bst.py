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

Finding a Node in a BST

Steps - Iteratively or Recursively

Starting at the root
-Check if there is a root, if not -we're done searching!
-If there is a root, check if  the value of the new node is the value we are looking for.
If we found it, we're done!
-If not, check to see if the value is greater than or less than the value of the root
-If it is greater
    -check to see if there is a node to the right
        - if there is, move to that node and repeat these steps
        - If there is not, we're done searching!
- If it is less
    -check to see if there is a node to the left
        - if there is, move to that node and repeat these steps
        - If there is not, we're done searching!

"""


from jinja2 import Undefined


class Node:

    def __init__(self, value) -> None:
        self.value  = value
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self) -> None:
        self.root = None

    def insert_node_recursive(self, val):
        n = Node(val)
        if self.root == None:
            self.root=n
            return
        else:
            if n.value > self.root.value:
                if self.root.right:
                    self.insert_node(val)
                    return
                self.root.right=n
            else:
                if self.root.left:
                    self.insert_node(val)
                    return
                self.root.left=n
      
    def insert_node_iterative(self, val):
        n = Node(val)
        if self.root == None:
            self.root=n
            # return
        current = self.root
        while(True):
            if(val == current.value): 
                return Undefined
            
            if n.value > current.value:
                if current.right:
                    current = current.right
                current.right=n
            else:
                if current.left:
                    current = current.left
                current.left=n

    def search_iterative(self, val):
        n = Node(val)
        if self.root == None:
            return Undefined
        if self.root == val:
            return True
        current = self.root
        while(True):
            if val > current.value:
                if current.right:
                    if current.right == val:
                        return True
                    current = current.right
            else:
                if current.left:
                    if current.left == val:
                        return True
                    current = current.left

#       10
#   5       13
# 2   7  11    16

tree = BinarySearchTree()
tree.insert_node_iterative(10)
tree.insert_node_iterative(5)
tree.insert_node_iterative(13)
tree.insert_node_iterative(2)
tree.insert_node_iterative(7)
tree.insert_node_iterative(11)
tree.insert_node_iterative(16)
tree.insert_node_iterative(10)
# tree.root =Node(10)
# tree.root.right =Node(15)
# tree.root.left =Node(7)
# tree.root.left.right=Node(9)

print("10 root: ",tree.root.value)
print("5 left:",tree.root.left.value)
print("2 left left:",tree.root.left.right.value)
print("7 left right:",tree.root.left.right.value)
print("13 right:",tree.root.right.value)
print("11 right left:",tree.root.right.left.value)
print("16 right right",tree.root.right.right.value)

print(" search for 5", tree.search_iterative(5))
