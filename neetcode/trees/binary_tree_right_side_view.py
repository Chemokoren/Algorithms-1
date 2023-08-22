from typing import List
import collections
"""
Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values
of the nodes you can see ordered from top to bottom
Example:
Input: [1,2,3,null,5,null,4]
Output: [1,3,4]
Explanation:
        1               <---
       / \
      2   3             <---
      \    \
      5     4           <---
    /
   7
BFS (level order traversal)
"""
from collections import deque
# Definition for a binary tree node .
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val    = val
        self.left   = left
        self.right  = right

    def insert(self,data):
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            if data > self.val:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.val = TreeNode(data)
    
class Solution:
    def rightSideView(self, root:TreeNode)->List[int]:
        res =[]
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen =len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
    
    """Testing!!!"""
    def right_side_view(self, root):
        """
        Program to return all the nodes seen while standing on
        the right view
        Params:
            root(rootNode): the tree's root
        Returns:
            None
        """
        queue = deque()
        queue.append(root)
        res =[]
        if root:
            res.append(root.val)
        
        while queue:
            # pop first item in list
            node = queue.popleft()
            if node.left and node.right:
                res.append(node.right.val)
                queue.append(node.left)
                queue.append(node.right)
            elif node.left and not node.right:
                res.append(node.left.val)
                queue.append(node.left)
            elif not node.left and not node.right:
                    pass
        return res

input_val= [1,2,3,None,5,None,4]
tree = TreeNode(1) 
tree.left=TreeNode(2)
tree.right=TreeNode(3)
tree.left.right=TreeNode(5)
tree.right.right=TreeNode(4)
tree.left.right.left=TreeNode(7)


sol = Solution()
print(sol.rightSideView(tree))
# print("maneno::", sol.right_side_view(tree))

