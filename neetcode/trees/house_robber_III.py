"""
House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to
this area, called the "root." Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this place forms a binary tree." It
will automatically contact the police if two directly-linked houses were broken into on the 
same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
    input: [3, 2, 3, null, 3, null, 1]
                            3
                           / \
                          2   3
                          \    \ 
                           3    1
Output: 7
Explanation: Maximum amount of money the thief can rob = 3+ 3+1 =7

Solution: DFS -O(n)

"""
from typing import Optional
import unittest




class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        Solve the House Robber III problem where you need to maximize the amount of money
        you can rob from a binary tree structure without robbing two directly connected houses.

        This method uses a depth-first search approach and returns the maximum money that can be robbed.

        :param root: The root node of the binary tree.
        :return: The maximum amount of money that can be robbed.
        """

        def dfs(node: Optional[TreeNode]) -> list[int]:
            """
            Perform a depth-first search to calculate the maximum money that can be robbed.

            This helper function returns a pair of values:
            - The first value represents the maximum money when robbing the current node.
            - The second value represents the maximum money when not robbing the current node.

            :param node: The current node in the binary tree.
            :return: A list containing two integers [withRoot, withoutRoot].
            """
            if not node:
                # If the current node is None, return [0, 0] indicating no money can be robbed.
                return [0, 0]

            # Recursively calculate the values for the left and right subtrees.
            leftPair = dfs(node.left)
            rightPair = dfs(node.right)

            # Calculate the maximum money when robbing the current node.
            withRoot = node.val + leftPair[1] + rightPair[1]
            # Calculate the maximum money when not robbing the current node.
            withoutRoot = max(leftPair) + max(rightPair)

            # print(f"Node value: {node.val}, withRoot: {withRoot}, withoutRoot: {withoutRoot}")

            # Return the pair [withRoot, withoutRoot].
            return [withRoot, withoutRoot]

        # Start the DFS from the root and return the maximum of the two values in the result.
        return max(dfs(root))

class TestRob(unittest.TestCase):
    """
    Empty Tree: Tests the case where the tree is None.
    Single Node: Tests the case where the tree has only one node.
    Two Levels: Tests a simple tree with two levels.
    Three Levels: Tests a more complex tree with three levels.
    Complex Tree: Tests a tree with an irregular structure and multiple levels.
    Left Heavy Tree: Tests a tree that is heavy on the left side.
    Right Heavy Tree: Tests a tree that is heavy on the right side.
    """

    def setUp(self):
        self.solution = Solution()

    def test_sample(self):
        tr = TreeNode(3)
        tr.left = TreeNode(2)
        tr.right = TreeNode(3)
        tr.left.right = TreeNode(3)
        tr.right.right = TreeNode(1)

        tr2 = TreeNode(3)
        tr2.left = TreeNode(20)
        tr2.right = TreeNode(4)
        tr2.left.left = TreeNode(100)
        tr2.right.right = TreeNode(1)

        self.assertEqual(7, self.solution.rob(tr))
        self.assertEqual(104, self.solution.rob(tr2))

    def test_empty_tree(self):
        self.assertEqual(self.solution.rob(None), 0)

    def test_single_node(self):
        root = TreeNode(3)
        self.assertEqual(self.solution.rob(root), 3)

    def test_two_levels(self):
        root = TreeNode(3, TreeNode(2), TreeNode(3, None, TreeNode(3)))
        self.assertEqual(self.solution.rob(root), 6)

    def test_three_levels(self):
        root = TreeNode(3,
                        TreeNode(4, TreeNode(1), TreeNode(3)),
                        TreeNode(5, None, TreeNode(1)))
        self.assertEqual(self.solution.rob(root), 9)

    def test_complex_tree(self):
        root = TreeNode(3,
                        TreeNode(2, TreeNode(3, TreeNode(3)), TreeNode(1)),
                        TreeNode(3, None, TreeNode(3, TreeNode(1), TreeNode(5))))
        self.assertEqual(self.solution.rob(root), 14)

    def test_left_heavy_tree(self):
        root = TreeNode(3, TreeNode(4, TreeNode(1, TreeNode(3))), None)
        self.assertEqual(self.solution.rob(root), 7)

    def test_right_heavy_tree(self):
        root = TreeNode(3, None, TreeNode(4, None, TreeNode(1, None, TreeNode(3))))
        self.assertEqual(self.solution.rob(root), 7)

if __name__ == '__main__':
    unittest.main()