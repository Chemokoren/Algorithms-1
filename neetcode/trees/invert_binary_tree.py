"""
invert a binary tree

Example 

                    4                               4
                  /   \                            /  \
                  2    7                          7    2 
                 / \   /\                        / \  / \ 
                1   3 6  9                      9  6 3   1
use DFS
"""
from collections import deque

class TreeNode:
    """
    Definition or representation for a binary tree node.
    
    """
    def __init__(self, val =0, left =None, right = None):
        self.val = val
        self.left = left
        self.right = right

def pre_order_traversal(root):
    """
    Performs pre-order traversal on a given binary tree

    Parameters:
        root(TreeNode): refers to the tree's root node
    
    Returns:
        None
    """
    if root:
        # Print the value of the current node
        print(root.val, end="-->")
        if root.left:
            # Traverse the left subtree recursively
            pre_order_traversal(root.left)
        if root.right:
            # Traverse the right subtree recursively
            pre_order_traversal(root.right)

def in_order_traversal(root):
    """
    Performs an in-order traversal of a binary tree and prints the values of each node.

    Parameters:
        root (TreeNode): The root node of the binary tree.

    Returns:
        None
    """
    if root:
        if root.left:
             # Traverse the left subtree recursively
            in_order_traversal(root.left) 
        
        # Print the value of the current node
        print(root.val, end="-->")  
        
        if root.right:
            # Traverse the right subtree recursively
            in_order_traversal(root.right)  


def level_order_traversal(root):
    """
    Performs a level-order traversal of a binary tree and prints the values of each node.

    Parameters:
        root (TreeNode): The root node of the binary tree.

    Returns:
        None
    """
    if not root:
        return
    
    # Create a queue using deque
    queue = deque()  

    # Enqueue the root node
    queue.append(root)

    while queue:
        # Dequeue the node from the front of the queue
        node = queue.popleft()  
        # Print the value of the current node
        print(node.val, end="-->")  

        if node.left:
            # Enqueue the left child if it exists
            queue.append(node.left)  

        if node.right:
            # Enqueue the right child if it exists
            queue.append(node.right)  
    print("\n")

        
class Solution:

    """
    Provides solution to invert a given binary tree
    """
    def invert_tree(self, root: TreeNode) -> TreeNode:
        """
        Inverts and return the new binary tree.
        
        Parameters:
            root(TreeNode): binary tree to be inverted
        Returns
            root(TreeNode): resultant inverted binary tree
        """
        if not root:
            return None

        # swap the children
        tmp         = root.left
        root.left   = root.right
        root.right  = tmp

        # recursively call invert_tree on the left and right child
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        
        # return the root of resultant binary tree
        return root
    
tr = TreeNode(4)
tr.left  = TreeNode(2)
tr.right = TreeNode(7)
tr.left.left   = TreeNode(1)
tr.left.right  = TreeNode(3)
tr.right.left  = TreeNode(6)
tr.right.right = TreeNode(9)

cls = Solution()
res_root=cls.invert_tree(tr)
level_order_traversal(res_root)
# print("inverted tree: ",res_root.val,res_root.left.val,res_root.right.val)