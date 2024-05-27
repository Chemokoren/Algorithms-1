"""
Given two binary trees, imagine that when you put one of them to cover the
other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two
nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of the new tree.

Example 1:

Input:

    Tree 1                                  Tree 2
        1                                       2
        /\                                     /  \
       3  2                                   1    3
      /                                        \    \
     5                                          4    7

Merged tree:
                            3
                           / \
                          4   5
                         / \   \
                        5  4    7
time complexity: O(n+m) where n is nodes in the first tree and m in the second tree

"""
import unittest
from collections import deque


class TreeNode:
    """
    Definition for a binary tree node
    
    """

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root):
    """
    Method performs level order traversal in a binary tree

    Args:
        root: is the root node of the given binary tree
    
    Returns:
        None
    """

    if not root:
        return

    queue = deque()
    queue.append(root)

    while queue:
        # pop the first item in the queue
        node = queue.popleft()
        print(node.val, end="-->")
        # check if node has a left child & append to the queue
        if node.left:
            queue.append(node.left)

        # check if node has a right child & append to the queue
        if node.right:
            queue.append(node.right)
    print("\n")


class Solution:
    """
    Solution for merging two binary trees
    """

    def merge_trees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        Merge two binary trees and return the new binary tree.
        
        Args:
            t1(TreeNode): first binary tree
            t2(TreeNode): second binary tree
                
        Returns:
            root(TreeNode): resultant binary tree
        """
        if not t1 and not t2:
            return None

        v1 = t1.val if t1 else 0
        v2 = t2.val if t2 else 0

        root = TreeNode(v1 + v2)

        root.left  = self.merge_trees(t1.left if t1 else None, t2.left if t2 else None)
        root.right = self.merge_trees(t1.right if t1 else None, t2.right if t2 else None)

        return root

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def tree_to_list(self, root: TreeNode) -> list:
        """Helper function to convert binary tree to list (level-order) for easier comparison in tests."""
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
        return result
    def test_sample(self):
        tr1 = TreeNode(1)
        tr1.left = TreeNode(3)
        tr1.right = TreeNode(2)
        tr1.left.left = TreeNode(5)

        tr2 = TreeNode(2)
        tr2.left = TreeNode(1)
        tr2.right = TreeNode(3)
        tr2.left.right = TreeNode(4)
        tr2.right.right = TreeNode(7)

        self.assertEqual(self.tree_to_list(self.solution.merge_trees(tr1, tr2)), [3, 4, 5, 5, 4, None, 7])
    def test_empty_trees(self):
        # Test case 1: Both trees are empty
        t1 = None
        t2 = None
        self.assertEqual(self.tree_to_list(self.solution.merge_trees(t1, t2)), [])

    def test_one_empty_tree(self):
        # Test case 2: One tree is empty
        t1 = TreeNode(1)
        t2 = None
        self.assertEqual(self.tree_to_list(self.solution.merge_trees(t1, t2)), [1])

    def test_trees_root_node(self):
        # Test case 3: Both trees have only root node
        t1 = TreeNode(1)
        t2 = TreeNode(2)
        self.assertEqual(self.tree_to_list(self.solution.merge_trees(t1, t2)), [3])

    def test_trees_with_multiple_levels(self):
        # Test case 4: Trees with multiple levels
        t1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
        t2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
        self.assertEqual(self.tree_to_list(self.solution.merge_trees(t1, t2)), [3, 4, 5, 5, 4, None, 7])

    def test_trees_with_uneven_strucutre(self):
        # Test case 5: Trees with uneven structures
        t1 = TreeNode(1, TreeNode(2))
        t2 = TreeNode(1, None, TreeNode(2))
        self.assertEqual(self.tree_to_list(self.solution.merge_trees(t1, t2)), [2, 2, 2])

    def test_larger_trees(self):
        # Test case 6: Larger trees
        t1 = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(9)))
        t2 = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(7, None, TreeNode(8)))
        self.assertEqual(self.tree_to_list(self.solution.merge_trees(t1, t2)), [8, 5, 15, 2, 7, 7, 17])

if __name__ == '__main__':
    unittest.main()

