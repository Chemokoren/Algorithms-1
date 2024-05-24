"""
Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree(BST)

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example:

            2
           / \  
          1   3
          
Input: root =[2,1,3]
Output = True

sol: Recursive DFS O(2.n) =O(n)

"""
class TreeNode:
    """TreeNode class Structure """

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val    = val
        self.left   = left
        self.right  = right

        
class Solution:

    def is_valid_bst(self, root: TreeNode)->bool:
        """
        Validate Binary Search Tree.
        
            Args: 
                root(TreeNode): binary search tree to validate
            Returns:
                bool: True if it is a valid binary search tree and False otherwise
        """

        def valid(node, left, right):
            if not node:
                # an empty node is a BST
                return True 
            if not (node.val < right and node.val > left):
                return False
            return (valid(node.left, left, node.val) and 
                    valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))
    
    


import unittest

class TestValidBST(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        """Tests an empty tree, which is considered a valid BST."""
        root = None
        self.assertTrue(self.solution.is_valid_bst(root))

    def test_single_node_tree(self):
        """Tests a tree with a single node, which is also a valid BST."""
        root = TreeNode(5)
        self.assertTrue(self.solution.is_valid_bst(root))

    def test_valid_bst(self):
        """Tests a valid binary search tree."""
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertTrue(self.solution.is_valid_bst(root))

    def test_invalid_bst_left_violation(self):
        """Tests a tree with a violation in the left subtree."""
        root = TreeNode(5)
        root.left = TreeNode(7)  # Violation: left child's value is greater than root
        root.right = TreeNode(6)
        self.assertFalse(self.solution.is_valid_bst(root))

    def test_invalid_bst_right_violation(self):
        """Tests a tree with a violation in the right subtree."""
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        root.right.right = TreeNode(2)  # Violation: right child's value is less than root
        self.assertFalse(self.solution.is_valid_bst(root))

if __name__ == '__main__':
    unittest.main()
