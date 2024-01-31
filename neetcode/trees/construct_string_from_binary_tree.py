"""
Construct String from Binary Tree

Given the root of a binary tree, construct a string consisting of parenthesis and integers
from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis and pairs that do not affect the one-to-one mapping 
relationship between the string and the original binary tree.

Example 1:
                1
              /    \
            2        3
           /
          4

preorder
1 -> 2 -> 4->3

Input: root =[1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4())(3()())", but you 
need to  omit all the unnecessary empty parenthesis pairs. And it will be 
"1(2(4))(3)"
"""
from typing import Optional

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val =val
        self.left = left
        self.right = right


class Solution:

    def tree2str(self, root: Optional[TreeNode])-> str:

        res =[]

        def preorder(root):

            if not root:
                return
            res.append("(")
            res.append(str(root.val))

            if not root.left and root.right:
                res.append("()")

            preorder(root.left)
            preorder(root.right)
            res.append(")")
        
        preorder(root)
        return "".join(res)[1:-1]
    
        
tree       = TreeNode(1)
tree.left  = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left  = TreeNode(4)

sol = Solution()

print(sol.tree2str(tree))