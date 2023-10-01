"""
All Possible Full Binary Trees

Given an integer n, return a list of all possible full binary trees with n nodes. Each 
node of each tree in the answer must have Node.val == 0

Each element of the answer is the root node of one possible tree. You may return the final
list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

    x                       x                     x                   x              x 
  /   \                   /  \                  /   \               /   \           /  \
x       x               x      x               x     x             x     x         x    x
      /   \                   /  \           /  \   /  \          /  \            /  \ 
     x      x               x      x        x    x  x    x       x    x          x    x
          /   \           /   \                                      /  \       /  \
         x      x        x     x                                    x    x     x    x    

"""
from typing import List, Optional

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left =left
        self.right = right

class Solution:

    def allPossibleFBT(self, n: int) -> List(Optional[TreeNode]):

        # ret the list of fbt with n nodes
        def backtrack(n):

            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            res =[]

            for l in range(n): # 0 - (n - 1)
                r = n -1 -l
                leftTrees, rightTrees =backtrack(l), backtrack(r)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
            return res
        return backtrack(n)
