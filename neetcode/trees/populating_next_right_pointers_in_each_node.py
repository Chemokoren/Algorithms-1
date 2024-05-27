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

# from typing import Optional
# # Definition for a node
# class Node:

#     def __init__(self, val: int =0, left: 'Node' =None, right: 'Node' =None, next: 'Node'=None):
#         self.val   = val
#         self.left  = left
#         self.right = right
#         self.next  = next

# class Solution:

#     def connect(self, node: 'Optional[Node]') -> 'Optional[Node]':
#         cur, nxt = node, node.left if node else None

#         while cur and nxt:
#             cur.left.next = cur.right
#             if cur.next:
#                 cur.right.next = cur.next.left
            
#             cur = cur.next
#             if not cur:
#                 cur = nxt
#                 nxt = cur.left
#         return node

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        # Start with the root node
        leftmost = root
        
        while leftmost.left:
            # Traverse the current level
            head = leftmost
            while head:
                # Connection 1: Connect left child to right child
                head.left.next = head.right
                # Connection 2: Connect right child to the next left child, if next is not None
                if head.next:
                    head.right.next = head.next.left
                # Move to the next node in the current level
                head = head.next
            # Move to the next level
            leftmost = leftmost.left
        
        return root

# Helper function to print the tree levels with next pointers for debugging
def print_levels(root):
    level = root
    while level:
        current = level
        while current:
            print(current.val, end=' -> ')
            current = current.next
        print('NULL')
        level = level.left

# # Example Usage
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

# solution = Solution()
# solution.connect(root)
# print_levels(root)


import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution =Solution()

    def test_single_node(self):
        root = Node(1)
        self.solution.connect(root)
        self.assertIsNone(root.next)

    def test_two_levels(self):
        root = Node(1, Node(2), Node(3))

        self.solution.connect(root)
        self.assertIsNone(root.next)
        self.assertEqual(root.left.next, root.right)
        self.assertIsNone(root.right.next)

    def test_three_levels(self):
        root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))

        self.solution.connect(root)
        self.assertIsNone(root.next)
        self.assertEqual(root.left.next, root.right)
        self.assertIsNone(root.right.next)
        self.assertEqual(root.left.left.next, root.left.right)
        self.assertEqual(root.left.right.next, root.right.left)
        self.assertEqual(root.right.left.next, root.right.right)
        self.assertIsNone(root.right.right.next)

    def test_empty_tree(self):
        root = None

        result = self.solution.connect(root)
        self.assertIsNone(result)

    def test_no_children(self):
        root = Node(1, left=Node(2), right=None)

        self.solution.connect(root)
        self.assertIsNone(root.next)
        self.assertIsNone(root.left.next)

    def test_partial_children(self):
        root = Node(1, Node(2, Node(4), None), Node(3, None, Node(7)))

        self.solution.connect(root)
        self.assertIsNone(root.next)
        self.assertEqual(root.left.next, root.right)
        self.assertIsNone(root.right.next)
        self.assertEqual(root.left.left.next, root.right.right)
        self.assertIsNone(root.right.right.next)

if __name__ == '__main__':
    unittest.main()
