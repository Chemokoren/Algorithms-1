"""
Count Good Nodes in a Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from
root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

                3
               / \
              1   4
             /    / \
            3    1   5
Input: root =[3,1,4,3,null, 1, 5]
Output: 4
Explanation: Nodes in blue are good .
Root Node(3) is always a good node .
Node 4 -> (3,4) is the maximum value in the path starting from the root.

solution:
O(n) time and O(h) or(log(n)) space where h could be at most equal to n

Microsoft's faq -2021
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode)->int:

        def dfs(node, maxVal):
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0
            maxVal =max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)