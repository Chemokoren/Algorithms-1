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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    
    def findBottomLeftValue(self, root: Optional[TreeNode])->int:
        q= deque([root])

        while q:
            node =q.popleft()

            if node.right: q.append(node.right)
            if node.left: q.append(node.left)
        return node.val