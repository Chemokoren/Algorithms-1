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
from collections import deque
class TreeNode:
    """
    Definition for a binary tree node
    
    """
    def __init__(self, val =0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    """
    Method performs level order traversal in a binary tree

    Parameters:
        root: is the root node of the given binary tree
    
    Returns:
        None
    """

    if not root:
        return
    
    queue =deque()
    queue.append(root)

    while queue:
        # pop the first item in the queue
        node = queue.popleft()
        print(node.val, end="-->")
        # check if node has a left child & append to the queue
        if node.left:
            queue.append(node.left)

        # check if node has a right child & append to the queue
        if node.right:
            queue.append(node.right)
    print("\n")

        
class Solution:

    """
    Solution for merging two binary trees

    """
    def merge_trees(self, t1: TreeNode, t2: TreeNode) ->TreeNode:
        """
        Merge two binary trees and return the new binary tree.
        
        Parameters:
            t1(TreeNode): first binary tree
            t2(TreeNode): second binary tree
                
        Returns:
            root(TreeNode): resultant binary tree
        """
        if not t1 and not t2:
            return None

        v1 = t1.val if t1 else 0
        v2 = t2.val if t2 else 0
        
        root = TreeNode(v1 + v2)

        root.left =self.merge_trees(t1.left if t1 else None, t2.left if t2 else None)
        root.right =self.merge_trees(t1.right if t1 else None, t2.right if t2 else None)

        return root
    
tr1 =TreeNode(1)
tr1.left  = TreeNode(3)
tr1.right = TreeNode(2)
tr1.left.left =TreeNode(5)

tr2 =TreeNode(2)
tr2.left  = TreeNode(1)
tr2.right = TreeNode(3)
tr2.left.right =TreeNode(4)
tr2.right.right =TreeNode(7)

cls = Solution()
# print("merged binary tree::", cls.merge_trees(tr1, tr2))
level_order_traversal(cls.merge_trees(tr1, tr2))
