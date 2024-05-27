"""
Convert BST to Greater Tree

Given the root of a Binary Search Tree(BST), convert it to a Greater Tree such that every
key of the original BST is changed to the original key plus  the sum of all keys greater
than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
                            4 (30)
                         /      \
                       1 (36)     6 (21)     
                     /   \      /    \
                   0(36) 2(35) 5(26)  7(15)
                          \             \
                          3(33)          8(8)        
"""
from typing import Optional
from collections import deque

# Definition for a binary tree node
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

def bfs(root):
    queue =deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        print(node.val, end="-->")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()

def dfs(root):
    if not root:
        return
    print(root.val, end="-->")
    dfs(root.left)
    dfs(root.right)



class Solution:
    """
    Time Complexity: O(N), where N is the number of nodes in the BST.
    Space Complexity: O(N) due to the recursive nature of the `dfs` function.
    """

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Converts a Binary Search Tree (BST) into a new BST where each node's value
        
        is equal to the sum of all nodes greater than it in the original BST.

        Args:
            root (Optional[TreeNode]): The root node of the BST to be converted.

        Returns:
            Optional[TreeNode]: The root node of the converted BST.

        Raises:
            TypeError: If the input `root` is not a TreeNode object.

        """
        if not isinstance(root, TreeNode):
            raise TypeError("Input must be a TreeNode object")

        cur_sum = 0

        def dfs(node):
            """
            Performs an in-order depth-first search (DFS) on the BST,
            updating node values based on the sum of greater nodes.

            Args:
                node (TreeNode): The current node in the DFS traversal.
            """
            nonlocal cur_sum
            if not node:
                return

            dfs(node.right)  # Process right subtree first (in-order)
            tmp = node.val
            node.val += cur_sum
            cur_sum += tmp
            dfs(node.left)   # Process left subtree next (in-order)

        dfs(root)
        return root

    
tr = TreeNode(4)
tr.left =TreeNode(1)
tr.right =TreeNode(6)
tr.left.left =TreeNode(0)
tr.left.right =TreeNode(2)
tr.right.left =TreeNode(5)
tr.right.right =TreeNode(7)
tr.left.right.right =TreeNode(3)
tr.right.right.right =TreeNode(8)

sol = Solution()

# print("Expected::", sol.convertBST(tr).val)
print(" ########## BFS ########## ")
bfs(sol.convertBST(tr))
print(" ########## DFS ########## ")
# dfs(sol.convertBST(tr))