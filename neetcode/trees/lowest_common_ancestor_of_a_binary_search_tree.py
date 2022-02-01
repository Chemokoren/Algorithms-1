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

# Definition for a binary tree node .
class TreeNode:
    def __init__(self,x) -> None:
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',q: 'TreeNode')->'TreeNode':
        cur = root

        while cur:
            if p.val >cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else: return cur