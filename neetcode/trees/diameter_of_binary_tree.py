"""
Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of
a binary tree is the length of the longest path between any two nodes in a tree. This path
may or may not pass through the root.

Example:
Given a binary tree,
                1
               / \
              2   3
             / \
            4   5
Returns 3, which is the length of the path [4,2,1,3] or [5,2,1,3]
Note: The length of path between two nodes is represented by the number of edges between them.

Brute force approach: O(n^2)

Solution: O(n) -visit every node at most one time

"""

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def diameterOfBinaryTree(self, root:TreeNode)->int:

        res =[0]
        
        def dfs(root):
            
            if not root:
                return -1
            
            left  = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], 2+left+right)

            return 1 + max(left, right)

        dfs(root)
        
        return res[0]
    

tree            = TreeNode(1)
tree.left       = TreeNode(2)
tree.right      = TreeNode(3)
tree.left.left  = TreeNode(4)
tree.left.right = TreeNode(5)

cls = Solution()
print("Expected::, Actual::", cls.diameterOfBinaryTree(tree))
