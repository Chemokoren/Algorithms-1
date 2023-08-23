"""
Convert BST to Greater Tree

Given the root of a Binary Search Tree(BST), convert it to a Greater Tree such that every
key of the original BST is changed to the original key plus  the sum of all keys greater
than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
                            4 (30)
                         /      \
                       1 (36)     6 (21)     
                     /   \      /    \
                   0(36) 2(35) 5(26)  7(15)
                          \             \
                          3(33)          8(8)        
"""
from typing import Optional
# Definition for a binary tree node
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def convertBST(self, root: Optional[TreeNode])-> Optional[TreeNode]:
        curSum = 0

        def dfs(node):

            if not node:
                return
            nonlocal curSum
            dfs(node.right)
            tmp = node.val
            node.val +=curSum
            curSum += tmp
            dfs(node.left)
        dfs(root)
        return root