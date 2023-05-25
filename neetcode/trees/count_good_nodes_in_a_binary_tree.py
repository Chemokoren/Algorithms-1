"""
Count Good Nodes in a Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from
root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

                3
               / \
              1   4
             /    / \
            3    1   5
            
Input: root =[3,1,4,3,null, 1, 5]
Output: 4

Root Node(3) is always a good node .
Node 4 -> (3,4) is the maximum value in the path starting from the root.

solution:
O(n) time and O(h)i.e. height of the tree or(log(n)) space where h could be at most equal
to n

Microsoft's faq -2021
"""

class TreeNode:
    """
    Represents a node in a binary tree.
    """

    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a TreeNode object with a value and references to left and right child nodes.

        Args:
            val (int): The value of the node. Defaults to 0.
            left (TreeNode): The left child node. Defaults to None.
            right (TreeNode): The right child node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Provides a solution to count the number of "good" nodes in a binary tree.
    """

    def good_nodes(self, root: TreeNode) -> int:
        """
        Counts the number of "good" nodes in a binary tree.

        A "good" node is defined as a node whose value is greater than or equal to
        the maximum value encountered from the root to that node.

        Args:
            root (TreeNode): The root node of the binary tree.

        Returns:
            int: The count of "good" nodes in the binary tree.
        """

        def dfs(node, max_val):
            """
            Helper function for depth-first search (DFS) traversal of the binary tree.

            Args:
                node (TreeNode): The current node being visited.
                max_val (int): The maximum value encountered so far.

            Returns:
                int: The count of "good" nodes in the subtree rooted at the current node.
            """

            if not node:
                # Base case: if the node is None, return 0 (no nodes to process).
                return 0

            # Check if the value of the current node is greater than or equal to max_val.
            # If it is, it is a "good" node, so increment the count (res) by 1.
            res = 1 if node.val >= max_val else 0

            # Update max_val to the maximum value between max_val and the value of the current node.
            max_val = max(max_val, node.val)

            # Recursive calls to traverse the left and right child nodes,
            # accumulating the results in res.
            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)

            # Return the total count of "good" nodes encountered during the traversal.
            return res

        # Call the dfs function with the root node and the initial maximum value set to the value of the root node.
        return dfs(root, root.val)


# Create a binary tree
tr = TreeNode(3)
tr.left = TreeNode(1)
tr.right = TreeNode(4)
tr.left.left = TreeNode(3)
tr.right.left = TreeNode(1)
tr.right.right = TreeNode(5)

# Create an instance of the Solution class and count the number of good nodes
cls = Solution()
print("Number of good nodes in the binary tree is:", cls.good_nodes(tr))
