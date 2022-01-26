"""
Given two binary trees and imagine that when you put one of them to cover the 
other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two
nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of the new tree.

Example 1:
Input:

    Tree 1                                  Tree 2
        1                                       2
        /\                                     /  \               
       3  2                                   1   3  
      /                                        \   \
     5                                          4   7

Merged tree:
                            3
                           / \
                          4   5
                         / \   \
                        5  4    7

time complexity: O(n+m) where n is nodes in the first tree and m in the second tree

"""
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val =0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) ->TreeNode:
        if not t1 and not t2:
            return None

        v1 = t1.val if t1 else 0
        v2 = t2.val if t2 else 0
        
        root = TreeNode(v1 + v2)

        root.left =self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        root.right =self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)

        return root
