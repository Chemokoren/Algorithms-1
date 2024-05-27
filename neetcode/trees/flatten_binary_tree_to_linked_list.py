from typing import Optional
"""
Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same TreeNode class where the right child
pointer points to the next node in the list and the left child pointer is
always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree

            1                   1
           / \                   \
          2   5                   2  
         / \   \                    \
        3   4   6                    3
                                      \
                                       4
                                        \
                                         5
                                          \
                                           6

Input: root =[1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

O(n) time | O(h) memory & worst case is O(n) if it turns out to be a linked list
"""

class TreeNode:
    """ Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val  = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Flatten the binary tree to a linked list in-place.
        
        The tree is modified such that the left child of each node is set to None and the right child
        points to the next node in a pre-order traversal of the tree.
        
        :args root: The root node of the binary tree.
        :return: None
        """
        
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            """
            Perform depth-first search to flatten the tree.
            
            This helper function flattens the subtree rooted at the given node and returns the tail of the
            flattened subtree.
            
            :args node: The root node of the current subtree.
            :return: The tail node of the flattened subtree.
            """
            if not node:
                return None

            # Recursively flatten the left and right subtrees.
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)

            # If there is a left subtree, we need to rewire connections.
            if node.left:
                # The left subtree's tail's right child should point to the original right child.
                left_tail.right = node.right
                # The node's right child should now be the left child.
                node.right = node.left
                # Set the node's left child to None.
                node.left = None

            # The last node in the flattened subtree is the right_tail, if it exists,
            # else left_tail, if it exists, else the current node.
            return right_tail or left_tail or node

        # Start the flattening process from the root.
        dfs(root)


# Test case
def test_flatten():
    s = Solution()
    
    # Create the tree: [1,2,5,3,4,null,6]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    # Call the flatten method
    s.flatten(root)

    # The tree should be flattened to: [1,null,2,null,3,null,4,null,5,null,6]
    # Check the flattened tree structure
    assert root.val == 1
    assert root.left is None
    assert root.right.val == 2
    assert root.right.left is None
    assert root.right.right.val == 3
    assert root.right.right.left is None
    assert root.right.right.right.val == 4
    assert root.right.right.right.left is None
    assert root.right.right.right.right.val == 5
    assert root.right.right.right.right.left is None
    assert root.right.right.right.right.right.val == 6
    assert root.right.right.right.right.right.left is None
    assert root.right.right.right.right.right.right is None
    print(root.right.right.right.right.right.right is None)

    print("Test passed successfully!")

test_flatten()

import unittest
class TestFlatten(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tree_to_list(self, root: Optional[TreeNode]) -> list:
        """
        Helper function to convert the flattened tree to a list.
        :param root: The root node of the flattened tree.
        :return: A list representing the flattened tree.
        """
        result = []
        while root:
            result.append(root.val)
            root = root.right
        return result

    def test_single_node(self):
        root = TreeNode(1)
        self.solution.flatten(root)
        self.assertEqual(self.tree_to_list(root), [1])

    def test_two_nodes(self):
        root = TreeNode(1, TreeNode(2))
        self.solution.flatten(root)
        self.assertEqual(self.tree_to_list(root), [1, 2])

    def test_left_skewed_tree(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.solution.flatten(root)
        self.assertEqual(self.tree_to_list(root), [1, 2, 3])

    def test_right_skewed_tree(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.solution.flatten(root)
        self.assertEqual(self.tree_to_list(root), [1, 2, 3])

    def test_balanced_tree(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
        self.solution.flatten(root)
        self.assertEqual(self.tree_to_list(root), [1, 2, 3, 4, 5, 6])

    def test_complex_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(6)
        self.solution.flatten(root)
        self.assertEqual(self.tree_to_list(root), [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()
