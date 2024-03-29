"""
Flip Equivalent Binary Trees

For a binary tree T, we can define a flip operation as follows: choose any node, and
swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X
equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if two trees are
flip equivalent or false otherwise.

    Example 1:
                    1                           1
                   / \                         / \
                  2   3                       3   2
                / \   /                       \   / \
               4  5  6                        6  4   5
                 / \                                / \
                7   8                              8   7
Input: root1 =[1,2,3,4,5,6,null,null,null,7,8], root2=[1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1,3,and 5 .

"""
from typing import Optional

# Definition for a binary tree node.

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, r1: Optional[TreeNode], r2: Optional[TreeNode])->bool:
        if not r1 or not r2:
            return not r1 and not r2
        if r1.val != r2.val:
            return False

        a = self.flipEquiv(r1.left, r2.left) and self.flipEquiv(r1.right, r2.right)
        b = self.flipEquiv(r1.left, r2.right) and self.flipEquiv(r1.right, r2.left)
        return a or b
    

tr1 = TreeNode(1)
tr1.left=TreeNode(2)
tr1.right = TreeNode(3)
tr1.left.left=TreeNode(4)
tr1.left.right=TreeNode(5)
tr1.right.left = TreeNode(6)
tr1.left.right.left=TreeNode(7)
tr1.left.right.right=TreeNode(8)


tr2 = TreeNode(1)
tr2.left=TreeNode(3)
tr2.right = TreeNode(2)
tr2.left.right=TreeNode(6)
tr2.right.left=TreeNode(4)
tr2.right.right=TreeNode(5)
tr2.right.right.left=TreeNode(8)
tr2.right.right.right=TreeNode(7)


sol =Solution()
print("Expected:: True, Actual::", sol.flipEquiv(tr1, tr2))
