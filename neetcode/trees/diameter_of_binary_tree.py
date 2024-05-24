"""
Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of
a binary tree is the length of the longest path between any two nodes in a tree. This path
may or may not pass through the root.

Example:
Given a binary tree,
                1
               / \
              2   3
             / \
            4   5
Returns 3, which is the length of the path [4,2,1,3] or [5,2,1,3]
Note: The length of path between two nodes is represented by the number of edges between them.

Brute force approach: O(n^2)

Solution: O(n) -visit every node at most one time

"""

# Definition for a binary tree node
class TreeNode:

    def __init__(self, val=0,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def diameter_of_binary_tree(self, root:TreeNode)->int:

        res =[0]
        
        def dfs(root):
            
            if not root:
                return -1
            
            left  = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], 2+left+right)

            return 1 + max(left, right)

        dfs(root)
        
        return res[0]


    def diameter_of_bt(self, root):
        if not root:
            return 0

        # Helper function to calculate the height of a tree
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        def diameter(node):
            """
            Recursively calculate the diameter of the tree

            Args:
                node(TreeNode): instance of a TreeNode
            Returns:
                int: diameter of the tree
            """
            if not node:
                return 0

            # Calculate the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)

            # Calculate the diameter passing through the current node
            current_diameter = left_height + right_height

            # Recursively find the diameters of the left and right subtrees
            left_diameter  = diameter(node.left)
            right_diameter = diameter(node.right)

            # Return the maximum diameter among the current node and its subtrees
            return max(current_diameter, left_diameter, right_diameter)

        return diameter(root)

    
import unittest
class TestDiameterOfBinaryTree(unittest.TestCase):
    """
    
    Sample Test Cases:

    Empty Tree: Tests the function with no nodes.
    Single Node: Tests the function with a tree having only one node.
    Two Nodes: Tests the function with a tree having two nodes.
    Linear Tree: Tests a tree where all nodes are in a single line (left-skewed).
    Balanced Tree: Tests a tree that is balanced.
    Full Binary Tree: Tests a full binary tree.
    Skewed Right Tree: Tests a tree that is skewed to the right.
    Complex Tree: Tests a tree with a more complex structure.
    """

    def setUp(self) -> None:
        super().setUp()
        self.sol= Solution()

        self.tree            = TreeNode(1)
        self.tree.left       = TreeNode(2)
        self.tree.right      = TreeNode(3)
        self.tree.left.left  = TreeNode(4)
        self.tree.left.right = TreeNode(5)

        self.r1                 = TreeNode(1)
        self.r1.left            = TreeNode(2)
        self.r1.left.left       = TreeNode(3)
        self.r1.left.right      = TreeNode(4)
        self.r1.left.left.left  = TreeNode(5)
        self.r1.left.right.right= TreeNode(6)

    def test_sample_tree(self):
        self.assertEqual(3, self.sol.diameter_of_binary_tree(self.tree), "Should return True")

    def test_sample_tree_2(self):
        self.assertEqual(3, self.sol.diameter_of_bt(self.tree), "Should return True")

    def test_2_sample_tree(self):
        self.assertEqual(4, self.sol.diameter_of_binary_tree(self.r1), "Should return True")

    def test_2_sample_tree_2(self):
        self.assertEqual(4, self.sol.diameter_of_bt(self.r1), "Should return True")

    print("~~~")

    def test_empty_tree(self):
        self.assertEqual(self.sol.diameter_of_binary_tree(None), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.sol.diameter_of_binary_tree(root), 0)

    def test_two_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(self.sol.diameter_of_binary_tree(root), 1)

    def test_linear_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertEqual(self.sol.diameter_of_binary_tree(root), 2)

    def test_balanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(self.sol.diameter_of_binary_tree(root), 3)

    def test_full_binary_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.sol.diameter_of_binary_tree(root), 4)

    def test_skewed_right_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        self.assertEqual(self.sol.diameter_of_binary_tree(root), 3)

    def test_complex_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.left.left.left = TreeNode(6)
        self.assertEqual(self.sol.diameter_of_binary_tree(root), 4)


        
if __name__ =="__main__":
    unittest.main()