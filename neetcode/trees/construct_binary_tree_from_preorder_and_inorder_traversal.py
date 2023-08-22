from typing import List
"""
Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a 
binary tree and inorder is the inorder traversal of the same tree, construct and return the
binary tree.

Example 1:

                3
               / \
              9   20
                  / \
                15   7


Input: preorder =[3,9,20,15,7], inorder=[9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
"""
# Definition for a binary tree node .
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int])->TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid +1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

def level_order_traversal(root):
    if root:
        print(root.val,end="-->")
        level_order_traversal(root.left)
        level_order_traversal(root.right)


"""
To construct a binary tree from the given preorder and inorder traversals, you can follow a recursive 
approach. The idea is to use the preorder array to determine the root of the current subtree, 
and then use the inorder array to determine the left and right subtrees of the root.

The buildTree function takes in the preorder and inorder arrays as input and returns the root of the
 constructed binary tree.

The code uses a recursive helper function, buildTreeHelper, which takes the indices of the current
subtree in the preorder and inorder arrays.

It constructs the root of the subtree,determines the sizes of the left and right subtrees, 
and recursively builds them.

By running this code with the given example input, you will obtain the desired binary 
tree representation: [3,9,20,null,null,15,7].


    
"""
def buildTree(preorder, inorder):
    # Create a dictionary to store the indices of inorder values
    inorder_map = {val: idx for idx, val in enumerate(inorder)}

    def buildTreeHelper(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_start > preorder_end:
            return None

        # The first element in the preorder traversal is the root of the current subtree
        root_val = preorder[preorder_start]
        root = TreeNode(root_val)

        # Find the index of the root in the inorder traversal
        root_idx_inorder = inorder_map[root_val]

        # Determine the sizes of the left and right subtrees
        left_subtree_size = root_idx_inorder - inorder_start
        right_subtree_size = inorder_end - root_idx_inorder

        # Recursively build the left and right subtrees
        root.left = buildTreeHelper(preorder_start + 1, preorder_start + left_subtree_size,
                                    inorder_start, root_idx_inorder - 1)
        root.right = buildTreeHelper(preorder_end - right_subtree_size + 1, preorder_end,
                                     root_idx_inorder + 1, inorder_end)

        return root
    # Call the helper function with the initial indices
    return buildTreeHelper(0, len(preorder) - 1, 0, len(inorder) - 1)

# Example usage:
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = buildTree(preorder, inorder)



preorder =[3,9,20,15,7]
inorder=[9,3,15,20,7]

sol = Solution()
print(sol.buildTree(preorder,inorder))
level_order_traversal(sol.buildTree(preorder,inorder))

print("##################### second approach ###########################")

level_order_traversal(buildTree(preorder, inorder))
