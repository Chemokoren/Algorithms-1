"""
Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Exanoke 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

        3
       / \
      9   20
          / \
        15   7

Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

"""
from collections import deque

# Definition for a binary tree node
class TreeNode:
        def __init__(self,x) -> None:
            self.val = x
            self.left =None
            self.right = None

class Solution:
        def __init__(self,q) -> None:
            self.q =q
            
        def levelOrder(self, root: TreeNode)->int: #root: TreeNode
                ans =[]

                if(root is None):
                        return ans
                
                q = deque([root])

                while(q):
                        n = len(q)
                        temp =[]
                        for i in range(0, n):
                                f = q.popleft()
                                temp.append(f.val)
                                if(f.left is not None):
                                         q.append(f.left)

                                if(f.right is not None):
                                        q.append(f.right)

                        if(len(temp) > 0):
                                ans.append(temp[:])
                                temp.clear()
                return ans

tree_vals = [3,9,20,None,None,15,7]
sol = Solution(tree_vals)
print(sol.levelOrder(3))

