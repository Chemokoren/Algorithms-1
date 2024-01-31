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

from typing import Optional
# Definition for a node
class Node:

    def __init__(self, val: int =0, left: 'Node' =None, right: 'Node' =None, next: 'Node'=None):
        self.val   = val
        self.left  = left
        self.right = right
        self.next  = next

    class Solution:

        def connect(self, node: 'Optional[Node]') -> 'Optional[Node]':
            cur, nxt = node, node.left if node else None

            while cur and nxt:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                
                cur = cur.next
                if not cur:
                    cur = nxt
                    nxt = cur.left
            return node