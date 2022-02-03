from typing import Optional
"""
Trim a Binary Search Tree
Given the root of a binary tree and an integer targetSum return true if the tree has
a root-to-leaf path such that adding up all the values along the path equals 
targetSum.

A leaf is a node with no children

                        5
                       / \
                      4   8 
                    /     /\
                   11    13 4
                  / \        \
                 7   2        1

input: root =[5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum =22
Output: True
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right =right

# O(n) time where n is the number of nodes in the tree | O(h) space -> O(n) for worst case
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int)->bool:

        def dfs(node, curSum):
            if not node:
                return False
            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum
            return (dfs(node.left,curSum) or dfs(node.right,curSum))
        dfs(root,0)
