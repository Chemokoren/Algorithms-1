"""
Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search 
tree(BST)
A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's
key
-The right subtree of a node contains only nodes with keys greater than the 
node's key.
- Both the left and right subtrees must also be binary search trees.

Example:

            2
           / \  
          1   3
Input: root =[2,1,3]
Output = True

sol: Recursive DFS O(2.n) =
O(n)

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode)->bool:

        def valid(node, left, right):
            if not node:
                return True # an empty node is a BST
            if not (node.val < right and node.val > left):
                return False
            return (valid(node.left, left, node.val) and 
                    valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))