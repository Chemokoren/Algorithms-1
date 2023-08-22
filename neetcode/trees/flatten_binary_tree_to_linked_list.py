from typing import Optional
"""
Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same TreeNode class where the right child
pointer points to the next node in the list and the left child pointer is
always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree

            1                   1
           / \                   \
          2   5                   2  
         / \   \                    \
        3   4   6                    3
                                      \
                                       4
                                        \
                                         5
                                          \
                                           6

Input: root =[1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

O(n) time | O(h) memory & worst case is O(n) if it turns out to be a linked list
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val  = val
        self.left = left
        self.right = right

class Solution:

    def flatten(self, root: Optional[TreeNode])->None:
        """
        Do not return anything, modify root in-place instead.
        """

        # flatten the root tree and return list tail
        def dfs(root):
            if not root:
                return None

            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left =None
            last = rightTail or leftTail or root
            return last
        dfs(root)

# Test case
def test_flatten():
    s = Solution()
    
    # Create the tree: [1,2,5,3,4,null,6]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    # Call the flatten method
    s.flatten(root)

    # The tree should be flattened to: [1,null,2,null,3,null,4,null,5,null,6]
    # Check the flattened tree structure
    assert root.val == 1
    assert root.left is None
    assert root.right.val == 2
    assert root.right.left is None
    assert root.right.right.val == 3
    assert root.right.right.left is None
    assert root.right.right.right.val == 4
    assert root.right.right.right.left is None
    assert root.right.right.right.right.val == 5
    assert root.right.right.right.right.left is None
    assert root.right.right.right.right.right.val == 6
    assert root.right.right.right.right.right.left is None
    assert root.right.right.right.right.right.right is None
    print(root.right.right.right.right.right.right is None)

    print("Test passed successfully!")

test_flatten()