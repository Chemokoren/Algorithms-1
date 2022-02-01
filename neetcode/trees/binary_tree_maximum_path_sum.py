"""
Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of
adjacent nodes in the sequence has an edge connecting them. A node can
only appear in the sequence at most once. Note that the path does not
need to pass through the root.

The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any path.

Example: 
                    1
                   / \
                  2   3

Input: root =[1,2,3]
Output: 6
Explanation: The optimal path is 2->1->3 with a path sum of 2+1+3 = 6

DFS -> O(n) time | O(h) space ->O(log(n)) if it is a balanced binary tree

"""
# Definition for a binary tree node.
class TreeNode:

    def __init__(self,val =0, left=None, right=None) -> None:
        self.val    = val
        self.left   = left
        self.right  = right

class Solution:

    def maxPathSum(self, root: TreeNode)->int:
        res =[root.val]

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0
            leftMax  = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax  = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum WITH split
            res[0] =max(res[0], root.val+leftMax+rightMax)

            return root.val+max(leftMax, rightMax)

        dfs(root)
        return res[0]
    