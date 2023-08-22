from typing import Optional
"""
Trim a Binary Search Tree

Given the root of a binary search tree and the lowest and highest boundaries as low 
and high, trim the tree so that all its elements lies in [low, high]. Trimming the
tree should not change the relative structure of the elements that will remain in the tree
(i.e., any node's descendant should remain a descendant). It can be proven that there is
a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending 
on the given bounds.

Example 1
    1                      1
  /   \        ->           \
 0     2                     2

 Input: root =[1,0,2], low = 1, high = 2
 Output: [1, null, 2]
"""

class TreeNode:

    def __init__(self, root, left=None, right=None):
        self.val = root
        self.left = left
        self.right = right

    
class Solution:

    def TrimBST(self, root: Optional[TreeNode], low: int, high:int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > high:
            self.TrimBST(root.left, low, high)
        if root.val < low:
            self.TrimBST(root.right, low, high)
        root.left =self.TrimBST(root.left, low, high)
        root.right =self.TrimBST(root.right, low, high)
        return root
    
def traverse(root):
    print(root.val, end="-->")
    if root.left:
        traverse(root.left)
    if root.right:
        traverse(root.right)
    

# Construct the binary search tree
#     1
#    / \
#   0   2
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(2)

# Create an instance of the Solution class
solution = Solution()

# Trim the tree within the boundaries [1, 2]
trimmed_root = solution.TrimBST(root, 1, 2)

# Print the trimmed tree (inorder traversal)
def inorder_traversal(node):
    if not node:
        return []
    return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

print(inorder_traversal(trimmed_root))  # Output: [1, 2]


# sol = Solution()
# traverse(sol.TrimBST(tr, 1, 2))
# print("Expected::[1, null, 2], Actual::", traverse(sol.TrimBST(tr, 1, 2)))


# def serialize_tree(root):
#     if not root:
#         return "null"
#     left_str = serialize_tree(root.left)
#     right_str = serialize_tree(root.right)
#     return f"{root.val}, {left_str}, {right_str}"

# # Test the Solution class
# def test_solution():
#     # Construct the binary search tree
#     #     1
#     #    / \
#     #   0   2
#     root = TreeNode(1)
#     root.left = TreeNode(0)
#     root.right = TreeNode(2)

#     solution = Solution()
#     trimmed_root = solution.TrimBST(root, 1, 2)
    
#     # Expected result: "1, null, 2, null, null"
#     expected_result = "1, null, 2, null, null"
#     actual_result = serialize_tree(trimmed_root)
    
#     assert expected_result == actual_result, f"Expected: {expected_result}, Actual: {actual_result}"
#     print("Test passed!")

# # Run the test
# test_solution()
