from collections import deque
from typing import Optional
"""
Find Bottom Left Tree Value

Given the root of a binary tree, return the leftmost value in the last row of the 
tree

Example 1:
                2
               / \
              1   3
Input: root =[2,1,3]
Output: 1

"""

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def find_bottom_left_value(self, root: Optional[TreeNode]) -> int:
        """
        Find the bottom-left value in a binary tree.
        
        This function uses breadth-first search (BFS) to traverse the tree level by level from right to left.
        The last node processed will be the bottom-left node of the tree.
        
        :param root: The root node of the binary tree.
        :return: The value of the bottom-left node.
        """
        
        # Initialize a deque with the root node.
        q = deque([root])

        # Iterate while there are nodes in the deque.
        while q:
            # Pop the leftmost node from the deque.
            node = q.popleft()

            # Append the right child first, if it exists.
            if node.right:
                q.append(node.right)
            
            # Append the left child next, if it exists.
            if node.left:
                q.append(node.left)

        # The last node processed is the bottom-left node.
        return node.val
    
import unittest
class TestBottomLeftTreeValue(unittest.TestCase):

    """
    Sample Test Cases:

    Single Node: Tests the function with a tree having only one node.
    Two Nodes: Tests the function with a tree having two nodes (root with one left child).
    Balanced Tree: Tests a balanced tree where the bottom-left value is at the leftmost position.
    Right-Skewed Tree: Tests a tree that is skewed to the right to check if the last node is correctly identified.
    Left-Skewed Tree: Tests a tree that is skewed to the left, ensuring the leftmost bottom node is found.
    Complex Tree: Tests a more complex tree structure to ensure the algorithm works correctly in more intricate scenarios.
    """

    def setUp(self) -> None:
        super().setUp()
        self.sol = Solution()

        self.tree =TreeNode(2)
        self.tree.left =TreeNode(1)
        self.tree.right =TreeNode(3)


    def test_sample_tree(self):
        self.assertEqual(1, self.sol.find_bottom_left_value(self.tree))

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.sol.find_bottom_left_value(root), 1)

    def test_two_nodes(self):
        root = TreeNode(1, TreeNode(2))
        self.assertEqual(self.sol.find_bottom_left_value(root), 2)

    def test_balanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        self.assertEqual(self.sol.find_bottom_left_value(root), 4)

    def test_right_skewed_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        self.assertEqual(self.sol.find_bottom_left_value(root), 4)

    def test_left_skewed_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(self.sol.find_bottom_left_value(root), 4)

    def test_complex_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.right.left = TreeNode(8)
        root.right.right.left = TreeNode(9)
        self.assertEqual(self.sol.find_bottom_left_value(root), 8)

if __name__=="__main__":
    unittest.main()