"""
invert a binary tree

Example 

                    4                               4
                  /   \                            /  \
                  2    7                          7    2 
                 / \   /\                        / \  / \ 
                1   3 6  9                      9  6 3   1
use DFS
"""

# Definition for a binary tree node .
class TreeNode:
    def __init__(self, val =0, left =None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # swap the children
        tmp = root.left
        root.left = root.right
        root.right =tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root