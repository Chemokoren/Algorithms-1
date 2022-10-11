"""
invert a binary tree

Example 

                    4                               4
                  /   \                            /  \
                  2    7                          7    2 
                 / \   /\                        / \  / \ 
                1   3 6  9                      9  6 3   1
use DFS
"""

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val =0, left =None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:
        """
        Invert and return the new binary tree.
        
            Parameters:
                root(TreeNode): binary tree to be inverted
            Returns
                root(TreeNode): resultant inverted binary tree
        """
        if not root:
            return None

        # swap the children
        tmp         = root.left
        root.left   = root.right
        root.right  = tmp

        self.invert_tree(root.left)
        self.invert_tree(root.right)
        return root
    
tr = TreeNode(4)
tr.left  = TreeNode(2)
tr.right = TreeNode(7)
tr.left.left   = TreeNode(1)
tr.left.right  = TreeNode(3)
tr.right.left  = TreeNode(6)
tr.right.right = TreeNode(9)

cls = Solution()
res_root=cls.invert_tree(tr)
print("inverted tree: ",res_root.val,res_root.left.val,res_root.right.val)