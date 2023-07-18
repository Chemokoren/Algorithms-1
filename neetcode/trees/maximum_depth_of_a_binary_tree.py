from collections import deque
"""
Maximum Depth of Binary tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the
root node down to the farthest leaf node.

Example:

                    3
                   / \
                  9   20
                      / \
                    15   7
Input: root =[3,9,20,null,null,15,7]
Output: 3

"""
# Recursive DFS O(n) time | O(n) space in the worst case if its not a balanced binary 
# tree

# Definition for a binary tree node .
class TreeNode:

    def __init__(self, val =0, left=None, right=None):
        self.val  = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode)->int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    # BFS
    def maxDepthBFS(self, root: TreeNode)->int:
        if not root:
            return 0
        level = 0
        q =deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

    # Iterative DFS
    def maxDepthIterativeDFS(self, root: TreeNode)->int:
        stack =[[root, 1]]
        res = 0

        while stack:
            node, depth =stack.pop()

            if node:
                res =max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res
    
sol =Solution()
tree =TreeNode(3)
tree.left=TreeNode(9)
tree.right=TreeNode(20)
tree.right.left=TreeNode(15)
tree.right.right=TreeNode(7)

print("maxDepth::", sol.maxDepth(tree))
print("maxDepthBFS::", sol.maxDepthBFS(tree))
print("maxDepthIterativeDFS::", sol.maxDepthIterativeDFS(tree))