"""
Flip Equivalent Binary Trees

For a binary tree T, we can define a flip operation as follows: choose any node, and
swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X
equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if two trees are
flip equivalent or false otherwise.

    Example 1:
                    1                           1
                   / \                         / \
                  2   3                       3   2
                / \   /                       \   / \
               4  5  6                        6  4   5
                 / \                                / \
                7   8                              8   7
Input: root1 =[1,2,3,4,5,6,null,null,null,7,8], root2=[1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1,3,and 5 .

"""
from typing import Optional

class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flip_equiv(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        """
        Determine if two binary trees are flip equivalent.

        Flip equivalent trees are trees that are the same or can be made the same by swapping the left and right children
        of some nodes. This method uses a recursive approach to check if the trees are flip equivalent.

        :param r1: The root of the first binary tree.
        :param r2: The root of the second binary tree.
        :return: True if the trees are flip equivalent, otherwise False.
        """

        # Base case: If either r1 or r2 is None, they are equivalent only if both are None.
        if not r1 or not r2:
            return not r1 and not r2

        # If the values of the current nodes are different, the trees are not equivalent.
        if r1.val != r2.val:
            return False

        # Check if the trees are equivalent without any flips.
        a = self.flip_equiv(r1.left, r2.left) and self.flip_equiv(r1.right, r2.right)

        # Check if the trees are equivalent with flips (left and right children swapped).
        b = self.flip_equiv(r1.left, r2.right) and self.flip_equiv(r1.right, r2.left)

        # The trees are flip equivalent if either of the above conditions is true.
        return a or b

"""
Explanation of Test Cases:

    Empty Trees: Tests the case where both trees are None.
    One Empty Tree: Tests cases where one tree is None and the other is not.
    Identical Trees: Tests trees that are identical in structure and values.
    Flipped Trees: Tests trees that are structurally flipped but have equivalent values.
    Different Structures: Tests trees that have different structures but are flip equivalent.
    Different Values: Tests trees that have different values.
    Complex Flip Equivalent: Tests a more complex scenario where multiple flips are required to make the trees equivalent.
"""
import unittest
class TestFlipEquiv(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    def test_flip_equiv(self):
        tr1 = TreeNode(1)
        tr1.left = TreeNode(2)
        tr1.right = TreeNode(3)
        tr1.left.left = TreeNode(4)
        tr1.left.right = TreeNode(5)
        tr1.right.left = TreeNode(6)
        tr1.left.right.left = TreeNode(7)
        tr1.left.right.right = TreeNode(8)

        tr2 = TreeNode(1)
        tr2.left = TreeNode(3)
        tr2.right = TreeNode(2)
        tr2.left.right = TreeNode(6)
        tr2.right.left = TreeNode(4)
        tr2.right.right = TreeNode(5)
        tr2.right.right.left = TreeNode(8)
        tr2.right.right.right = TreeNode(7)

        self.assertEqual(True, self.solution.flip_equiv(tr1, tr2))

    def test_empty_trees(self):
        self.assertTrue(self.solution.flip_equiv(None, None))

    def test_one_empty_tree(self):
        root1 = TreeNode(1)
        self.assertFalse(self.solution.flip_equiv(root1, None))
        self.assertFalse(self.solution.flip_equiv(None, root1))

    def test_identical_trees(self):
        root1 = TreeNode(1, TreeNode(2), TreeNode(3))
        root2 = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertTrue(self.solution.flip_equiv(root1, root2))

    def test_flipped_trees(self):
        root1 = TreeNode(1, TreeNode(2), TreeNode(3))
        root2 = TreeNode(1, TreeNode(3), TreeNode(2))
        self.assertTrue(self.solution.flip_equiv(root1, root2))

    def test_different_structures(self):
        root1 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        root2 = TreeNode(1, TreeNode(3), TreeNode(2, None, TreeNode(4)))
        self.assertTrue(self.solution.flip_equiv(root1, root2))

    def test_different_values(self):
        root1 = TreeNode(1, TreeNode(2), TreeNode(3))
        root2 = TreeNode(1, TreeNode(2), TreeNode(4))
        self.assertFalse(self.solution.flip_equiv(root1, root2))

    def test_complex_flip_equiv(self):
        root1 = TreeNode(1,
                         TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)),
                         TreeNode(3, None, TreeNode(6, TreeNode(8))))
        root2 = TreeNode(1,
                         TreeNode(3, TreeNode(6, None, TreeNode(8))),
                         TreeNode(2, TreeNode(4, None, TreeNode(7)), TreeNode(5)))
        self.assertTrue(self.solution.flip_equiv(root1, root2))

if __name__ == '__main__':
    unittest.main()