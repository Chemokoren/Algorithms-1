"""
Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent 
has two children. The binary tree has the following definition:

struct Node {int val; Node *left; Node *right; Node *next;}

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


Populate each next pointer to point to its next right node. If there is no next right node,
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL .

Example 1:

             1                              1 ->NULL
           /   \                           /   \ 
         2       3                       2 --->  3 -> NULL
       /  \     /  \                   /   \    /   \
      4   5    6    7                4 ---> 5-->6 --->7 -> NULL


"""
import unittest
from typing import Optional

class Node:
    """Definition for a node"""

    def __init__(self, val: int =0, left: 'Node' =None, right: 'Node' =None, next: 'Node'=None):
        self.val   = val
        self.left  = left
        self.right = right
        self.next  = next

class Solution:
    def connect_optimized(self, node: Optional[Node]) -> Optional[Node]:
        # `cur` points to the current node we're processing
        # `nxt` points to the leftmost node of the next level
        cur, nxt = node, node.left if node else None

        # While there are more levels to process (`cur` and `nxt` are not None)
        while cur and nxt:
            # Connect the left child to the right child
            cur.left.next = cur.right

            # If there is a next node at the current level, connect the current node's right child
            # to the next node's left child
            if cur.next:
                cur.right.next = cur.next.left

            # Move to the next node at the current level
            cur = cur.next

            # If we've reached the end of the current level
            if not cur:
                # Move to the next level
                cur = nxt
                # Update `nxt` to point to the leftmost node of the next level
                nxt = cur.left

        # Return the root node after all connections have been made
        return node

    def connect(self, root: Node) -> Node:# BFS solution
        """
        Populates each node's `next` pointer to point to its next right node.

        If there is no next right node, the `next` pointer is set to `None`.

        Args:
            root (Node): The root of the perfect binary tree.

        Returns:
            Node: The modified root node with updated `next` pointers.
        """
        if not root:
            return None

        queue = [root]

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.pop(0)

                # Link the current node's `next` pointer to the next node in the same level.
                if i < level_size - 1:
                    node.next = queue[0]

                # Add left and right children to the queue for the next level.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root



class TestSolution(unittest.TestCase):
    """
    Test Cases:

    test_connect_empty_tree: Tests the function with an empty tree (root is None). It should return None.
    test_connect_single_node: Tests the function with a single-node tree. The node should have its next pointer set to None.
    test_connect_two_levels: Tests the function with a tree of two levels. Checks the connections between the first level's left and right children.
    test_connect_three_levels: Tests the function with a tree of three levels. Checks the connections between all nodes at each level.
    test_connect_various_structures: Tests the function with another perfect binary tree to ensure it handles various structures correctly. The expected result is checked using the tree_to_next_pointers helper method.
    """
    def setUp(self):
        self.solution = Solution()

    def tree_to_next_pointers(self, root):
        """
        Helper function to collect the next pointers in a tree level by level.
        Returns a list of lists where each sublist contains the node values for that level.
        """
        if not root:
            return []

        levels = []
        level = [root]

        while level:
            current_values = []
            next_level = []
            for node in level:
                if node:
                    current_values.append(node.val)
                    if node.next:
                        current_values.append("->")
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
            levels.append(current_values)
            level = next_level

        return levels

    def test_sample_data(self):
        # Create the tree
        tr = Node(1)
        tr.left = Node(2)
        tr.right = Node(3)

        # Apply the connect method
        self.solution.connect(tr)

        # Check the results
        self.assertIsNone(tr.next)
        self.assertEqual(tr.left.next, tr.right)
        self.assertIsNone(tr.right.next)

    # def test_sample_data_2(self):
    #     # Create the tree
    #     tr = Node(1)
    #     tr.left = Node(2)
    #     tr.right = Node(3)
    #     tr.left.left = Node(4)
    #     tr.left.right = Node(5)
    #     tr.right.left = Node(6)
    #     tr.right.right = Node(7)
    #
    #     # Apply the connect method
    #     self.solution.connect(tr)
    #
    #     # Check the results
    #     self.assertIsNone(tr.next)
    #     self.assertEqual(tr.left.next, tr.right)
    #     self.assertIsNone(tr.right.next)
    #     self.assertEqual(tr.left.left.next, tr.left.right)
    #     self.assertEqual(tr.left.right.next, tr.right.left)
    #     self.assertEqual(tr.right.left.next, tr.right.right)
    #     self.assertIsNone(tr.right.right.next)
    #
    # def test_connect_empty_tree(self):
    #     self.assertIsNone(self.solution.connect(None))
    #
    # def test_connect_single_node(self):
    #     root = Node(1)
    #     self.solution.connect(root)
    #     self.assertIsNone(root.next)
    #
    # def test_connect_two_levels(self):
    #     root = Node(1, Node(2), Node(3))
    #     self.solution.connect(root)
    #     self.assertIsNone(root.next)
    #     self.assertEqual(root.left.next, root.right)
    #     self.assertIsNone(root.right.next)
    #
    # def test_connect_three_levels(self):
    #     root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    #     self.solution.connect(root)
    #     self.assertIsNone(root.next)
    #     self.assertEqual(root.left.next, root.right)
    #     self.assertIsNone(root.right.next)
    #     self.assertEqual(root.left.left.next, root.left.right)
    #     self.assertEqual(root.left.right.next, root.right.left)
    #     self.assertEqual(root.right.left.next, root.right.right)
    #     self.assertIsNone(root.right.right.next)
    #
    # def test_connect_various_structures(self):
    #     # Test with another perfect binary tree of three levels
    #     root = Node(10, Node(20, Node(30), Node(40)), Node(50, Node(60), Node(70)))
    #     self.solution.connect(root)
    #     self.assertEqual(self.tree_to_next_pointers(root), [
    #         [10],
    #         [20, "->", 50],
    #         [30, "->", 40, "->", 60, "->", 70]
    #     ])

if __name__ == '__main__':
    unittest.main()
