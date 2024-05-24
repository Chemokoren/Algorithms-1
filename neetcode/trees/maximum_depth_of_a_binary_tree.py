from collections import deque
"""
Maximum Depth of Binary tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the
root node down to the farthest leaf node.

Example:

                    3
                   / \
                  9   20
                      / \
                    15   7
Input: root =[3,9,20,null,null,15,7]
Output: 3

"""
# Recursive DFS O(n) time | O(n) space in the worst case if it's not a balanced binary tree

class TreeNode:
    """Definition for a binary tree node"""

    def __init__(self, val =0, left=None, right=None):
        self.val  = val
        self.left = left
        self.right = right

class Solution:

    # O(n) time && O(n) space if it is not a balance binary tree
    def max_depth(self, root: TreeNode)->int:
        if not root:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
    
    # BFS
    def max_depth_BFS(self, root: TreeNode)->int:
        if not root:
            return 0
        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

    def max_depth_iterative_DFS(self, root: TreeNode)->int:
        """Iterative DFS"""
        stack =[[root, 1]]
        res = 0

        while stack:
            node, depth =stack.pop()
            if node:
                res =max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res


import unittest
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sample(self):
        tree = TreeNode(3)
        tree.left = TreeNode(9)
        tree.right = TreeNode(20)
        tree.right.left = TreeNode(15)
        tree.right.right = TreeNode(7)

        self.assertEqual(self.solution.max_depth(tree), 3)
        self.assertEqual(self.solution.max_depth_BFS(tree), 3)
        self.assertEqual(self.solution.max_depth_iterative_DFS(tree), 3)

    def test_max_depth(self):
        # Test case 1: Empty tree
        self.assertEqual(self.solution.max_depth(None), 0)

        # Test case 2: Single node tree
        root = TreeNode(1)
        self.assertEqual(self.solution.max_depth(root), 1)

        # Test case 3: Balanced tree with depth 3
        #      1
        #     / \
        #    2   3
        #   / \
        #  4   5
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        root.right = TreeNode(3)
        self.assertEqual(self.solution.max_depth(root), 3)

        # Test case 4: Unbalanced tree with depth 4
        #      1
        #     /
        #    2
        #   /
        #  3
        # /
        #4
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3, TreeNode(4)))
        self.assertEqual(self.solution.max_depth(root), 4)

        # Test case 5: Tree with multiple branches
        #      1
        #     / \
        #    2   3
        #   /     \
        #  4       5
        #           \
        #            6
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4))
        root.right = TreeNode(3, None, TreeNode(5, None, TreeNode(6)))
        self.assertEqual(self.solution.max_depth(root), 4)

if __name__ == '__main__':
    unittest.main()
