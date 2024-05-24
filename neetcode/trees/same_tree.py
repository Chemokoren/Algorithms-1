"""
Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the 
same or not.
Two binary trees are considered the same if they are structurally identical and the nodes
have the same value.

Example 1:
                            1                   1
                           / \                 / \
                          2   3               2   3
Input: p =[1,2,3], q=[1,2,3]
Output: true

O(p+q) time

"""

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val =val
        self.left = left
        self.right = right

class Solution:

    def is_same_tree(self, p: TreeNode, q: TreeNode)->bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.is_same_tree(p.left, q.left) and 
                self.is_same_tree(p.right, q.right))
                
import unittest                
class TestSameTree(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_sample_trees(self):
        tr_p =TreeNode(1)
        tr_p.left =TreeNode(2)
        tr_p.right =TreeNode(3)

        tr_q =TreeNode(1)
        tr_q.left =TreeNode(2)
        tr_q.right =TreeNode(3)

        self.assertEqual(True, self.sol.is_same_tree(tr_p, tr_q))


if __name__=="__main__":
    unittest.main()