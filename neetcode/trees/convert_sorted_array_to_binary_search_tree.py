from typing import List
"""
Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a
height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in 
which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: 

One possible answer is: [0, -3, 9, -10, null, 5], which represents the following
height balanced BST:

            0                   0
           / \                /   \
         -3   9             -10    5
         /   /                \     \
      -10   5                 -3     9
"""
from collections import deque
class TreeNode:
    """
    TreeNode class structure.
    
    """
    
    def __init__(self, val =0, left=None, right=None) -> None:
        self.val   = val
        self.left  = left
        self.right = right

def level_order_traversal(root):
    """
    Find level order traversal in a BST

    Parameters:
        root(TreeNode): the tree's root node

    Returns:
        None
    """
    queue = deque()
    # initialize the queue with the root node
    queue.append(root)

    while queue:

        # pop the first item in the queue
        node = queue.popleft()
        # print the node's value
        print(node.val, end="-->")

        if node.left:
            #  add left subtree to the queue
            queue.append(node.left)

        if node.right:
            # add right subtree to the queue
            queue.append(node.right)
    print("\n")


# O(n) time complexity | O(log(n)) memory because log(n) is going to be the
# height of the tree and it is balanced
class Solution:
    """
    Converting a sorted array to a BST
    """
    def sorted_array_to_bst(self, nums: List[int]) ->TreeNode:
        """
        Convert Sorted Array to Binary Search Tree.
        
        Args: 
            nums(List[int]): sorted array of integers
        Returns:
            root(TreeNode) : binary search tree
        
        """

        def helper(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left  = helper(l, m -1)
            root.right = helper(m + 1, r)
            return root
        return helper(0, len(nums)-1)

sol =Solution()
root =sol.sorted_array_to_bst([-10, -3, 0, 5, 9])
print("root node::", root.val)
level_order_traversal(root)

