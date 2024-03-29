from typing import List
"""
Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height 
balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the
depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

one possible answer is [0, -3, 9 -10, null, 5], which represents the following height 
balanced BST:

         0
       /  \
     -3    9
     /    /
 -10    5

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val =val
        self.left = left
        self.right =right

def print_tree(root):
    if(root.val):
        print(root.val, end=',')
    if root.left:
        print_tree(root.left)
    if root.right:
        print_tree(root.right)


class Solution:
    def sortedArrayToBST(self,nums: List[int])->TreeNode:
        # O(n) time, O(log(n)) space because it is going to be the height of our tree
        def helper(l, r):
            if l > r:
                return None
            m = (l + r) //2

            root =TreeNode(nums[m])
            root.left=helper(l, m-1)
            root.right =helper(m+1, r)
            return root
        return helper(0, len(nums)-1)

arr= [-10,-3,0,5,9]
sol =Solution()
print(sol.sortedArrayToBST(arr))
print_tree(sol.sortedArrayToBST(arr))
