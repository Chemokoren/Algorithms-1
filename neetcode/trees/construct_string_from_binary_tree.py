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
1 -> 2 -> 4 -> 3

Input: root =[1,2,3,4]
Output: "1(2(4))   (3)"
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
    """
    Serializes a binary tree into a parenthesized string representation.
    """

    def tree_str(self, root: Optional[TreeNode]) -> str:
        """
        Performs a preorder depth-first search (DFS) on the binary tree
        and constructs a parenthesized string representation.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            str: The parenthesized string representation of the binary tree.

        Raises:
            TypeError: If the input `root` is not a TreeNode object.
        """

        if not isinstance(root, TreeNode):
            raise TypeError("Input must be a TreeNode object")

        res = []

        def preorder(root):
            """
            Performs a preorder DFS traversal on the binary tree,
            appending node values and parentheses to the `res` list.

            Args:
                root (Optional[TreeNode]): The current node in the traversal.
            """

            if not root:
                return

            res.append("(")
            res.append(str(root.val))

            # Handle case of a node with only a right child
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

print(sol.tree_str(tree))