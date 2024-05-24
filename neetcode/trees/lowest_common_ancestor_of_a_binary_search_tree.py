"""
Given a binary search tree(BST), find the lowest common ancestor(LCA) of two given
nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is 
defined between two nodes p and q as the lowest node in T that has both p and q 
as descendants (where we allow a node to be a descendant of itself)."

Example 1:
                    6
                  /  \
                 2     8
               /  \   /  \
              0    4 7    9
                  / \
                 3   5
Input: root =[6,2,8,0,4,7,9,null,null,3,5], p=2, q =8
Output: 6
Explanation : The LCS of nodes 2 and 8 is 6.
O(log(n)) time | O(1) space 
"""
import unittest

# Definition for a binary tree node .
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Find the lowest common ancestor of two nodes in a binary search tree.

        Args:
            root (TreeNode): The root of the binary search tree.
            p (TreeNode): The first node.
            q (TreeNode): The second node.

        Returns:
            TreeNode: The lowest common ancestor of nodes p and q.
        """

        # Start from the root of the tree
        cur = root

        # Traverse the tree until a common ancestor is found
        while cur:
            # If both nodes are greater than the current node, move to the right subtree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # If both nodes are less than the current node, move to the left subtree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                # If one node is less and the other is greater than the current node, or if the current node
                # is equal to one of the nodes (it's the lowest common ancestor), return the current node.
                return cur


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_sample(self):
        tr = TreeNode(6)
        tr.left = TreeNode(2)
        tr.right = TreeNode(8)
        tr.left.left = TreeNode(0)
        tr.left.right = TreeNode(4)
        tr.right.left = TreeNode(7)
        tr.right.right = TreeNode(9)
        tr.left.right.left = TreeNode(3)
        tr.left.right.right = TreeNode(5)

        p,q = TreeNode(2), TreeNode(8)
        p1,q1 = TreeNode(7),TreeNode(6)
        p2,q2 = TreeNode(7),TreeNode(9)

        self.assertEqual(6,self.solution.lowestCommonAncestor(tr, p, q).val)
        self.assertEqual(6,self.solution.lowestCommonAncestor(tr, p1, q1).val)
        self.assertEqual(8,self.solution.lowestCommonAncestor(tr, p2, q2).val)

    def test_lowest_common_ancestor(self):
        # Create a binary search tree
        #        6
        #      /   \
        #     2     8
        #    / \   / \
        #   0  4  7  9
        #     / \
        #    3   5
        root = TreeNode(6)
        root.left = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
        root.right = TreeNode(8, TreeNode(7), TreeNode(9))

        # Test cases for nodes that exist in the tree
        self.assertEqual(self.solution.lowestCommonAncestor(root, root.left, root.right), root)  # LCA of 2 and 8 is 6
        self.assertEqual(self.solution.lowestCommonAncestor(root, root.left, root.left.right), root.left)  # LCA of 2 and 4 is 2
        self.assertEqual(self.solution.lowestCommonAncestor(root, root.left.left, root.left.right.right), root.left)  # LCA of 0 and 5 is 2

    def test_node_not_in_tree(self):
        # Create a binary search tree
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(7)

        # Test cases for a node not in the tree
        self.assertIsNone(self.solution.lowestCommonAncestor(root, TreeNode(2), TreeNode(4)))  # LCA of 2 and 4 is None (None of them exists in the tree)
        self.assertIsNone(self.solution.lowestCommonAncestor(root, TreeNode(6), TreeNode(8)))  # LCA of 6 and 8 is None (None of them exists in the tree)

if __name__ == '__main__':
    unittest.main()

