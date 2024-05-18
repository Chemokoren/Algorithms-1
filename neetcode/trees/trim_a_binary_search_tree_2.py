from typing import Optional
"""
Trim a Binary Search Tree

Given the root of a binary search tree and the lowest and highest boundaries as low 
and high, trim the tree so that all its elements lies in [low, high]. Trimming the
tree should not change the relative structure of the elements that will remain in the tree
(i.e., any node's descendant should remain a descendant). It can be proven that there is
a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending 
on the given bounds.

Example 1
    1                      1
  /   \        ->           \
 0     2                     2

 Input: root =[1,0,2], low = 1, high = 2
 Output: [1, null, 2]
"""

class TreeNode:

    def __init__(self, root, left=None, right=None):
        self.val = root
        self.left = left
        self.right = right

    
class Solution:

    def trim_BST(self, root: Optional[TreeNode], low: int, high:int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > high:
            self.trim_BST(root.left, low, high)
        if root.val < low:
            self.trim_BST(root.right, low, high)

        root.left =self.trim_BST(root.left, low, high)
        root.right =self.trim_BST(root.right, low, high)
        return root
    
def preorder_traversal(root):
    print(root.val, end="-->")
    if root.left:
        preorder_traversal(root.left)
    if root.right:
        preorder_traversal(root.right)
    

# Construct the binary search tree
#     1
#    / \
#   0   2
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(2)

# Create an instance of the Solution class
solution = Solution()

# Trim the tree within the boundaries [1, 2]
trimmed_root = solution.trim_BST(root, 1, 2)

# Print the trimmed tree (inorder traversal)
def inorder_traversal(node):
    if not node:
        return []
    return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

print(inorder_traversal(trimmed_root))  # Output: [1, 2]









import unittest

class TestTrimBST(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        """Tests trimming an empty tree, which remains empty."""
        root = None
        low = 1
        high = 10
        trimmed_root = self.solution.trim_BST(root, low, high)
        self.assertIsNone(trimmed_root)

    def test_single_node_within_range(self):
        """Tests trimming a single node within the range."""
        root = TreeNode(5)
        low = 3
        high = 7
        trimmed_root = self.solution.trim_BST(root, low, high)
        self.assertEqual(trimmed_root.val, 5)
        self.assertIsNone(trimmed_root.left)
        self.assertIsNone(trimmed_root.right)

    def test_single_node_outside_range(self):
        """Tests trimming a single node outside the range."""
        root = TreeNode(5)
        low = 7
        high = 10
        trimmed_root = self.solution.trim_BST(root, low, high)
        self.assertIsNone(trimmed_root)

    def test_balanced_tree(self):
        """Tests trimming a balanced tree."""
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(7)
        low = 3
        high = 5
        trimmed_root = self.solution.trim_BST(root, low, high)
        self.assertEqual(trimmed_root.val, 4)
        self.assertEqual(trimmed_root.left.val, 3)
        self.assertIsNone(trimmed_root.left.left)
        self.assertIsNone(trimmed_root.left.right)
        self.assertIsNone(trimmed_root.right)

    def test_left_subtree_trimming(self):
        """Tests trimming only the left subtree."""
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        low = 3
        high = 7
        trimmed_root = self.solution.trim_BST(root, low, high)
        self.assertEqual(trimmed_root.val, 4)
        self.assertEqual(trimmed_root.left.val, 3)
        self.assertIsNone(trimmed_root.left.left)
        self.assertIsNone(trimmed_root.left.right)
        self.assertEqual(trimmed_root.right.val, 6)
        self.assertEqual(trimmed_root.right.right.val, 7)

    def test_right_subtree_trimming(self):
        """Tests trimming only the right subtree."""
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.right.right = TreeNode(7)
        low = 1
        high = 5
        trimmed_root = self.solution.trim_BST(root, low, high)
        self.assertEqual(trimmed_root.val, 4)
        self.assertEqual(trimmed_root.left.val, 2)
        self.assertIsNone(trimmed_root.right)

if __name__ == '__main__':
    unittest.main()








# def serialize_tree(root):
#     if not root:
#         return "null"
#     left_str = serialize_tree(root.left)
#     right_str = serialize_tree(root.right)
#     return f"{root.val}, {left_str}, {right_str}"

# # Test the Solution class
# def test_solution():
#     # Construct the binary search tree
#     #     1
#     #    / \
#     #   0   2
#     root = TreeNode(1)
#     root.left = TreeNode(0)
#     root.right = TreeNode(2)

#     solution = Solution()
#     trimmed_root = solution.TrimBST(root, 1, 2)
    
#     # Expected result: "1, null, 2, null, null"
#     expected_result = "1, null, 2, null, null"
#     actual_result = serialize_tree(trimmed_root)
    
#     assert expected_result == actual_result, f"Expected: {expected_result}, Actual: {actual_result}"
#     print("Test passed!")

# # Run the test
# test_solution()
