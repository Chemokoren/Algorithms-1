from typing import List
import collections
"""
Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values(i.e, from
left to right, level by level)
                        3
                       / \
                      9   20
                          / \  
                         15  7
Input: root =[3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

solution uses BFS : O(n) time | O(n) space coz the tree can have at most O(n/2) nodes
"""

#Definition for Binary Tree

class TreeNode:

    class _Node:
        __slots__='_element','_left','_right'

        def __init__(self, element, left=None, right=None):
            self._element = element
            self._left = left
            self._right = right

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, e):
        troot = self._root
        ttroot = None
        while troot:
            ttroot = troot
            if e < troot._element:
                troot = troot._left
            elif e > troot._element:
                troot = troot._right
        node = self._Node(e)
        if self._root:
            if e < ttroot._element:
                ttroot._left  = node
            else:
                ttroot._right = node
        else:
            self._root = node

class Solution:

    def levelOrder(self, root:TreeNode)->List[List[int]]:
        res =[]
        
        q = collections.deque()
        q.append(root)

        while q:
            qLen =len(q)
            level =[]
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level: # ensure that level is non-empty
                res.append(level)

        return res
