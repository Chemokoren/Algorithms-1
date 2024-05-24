import unittest
from typing import Optional
"""
Given the root of a binary tree and an integer targetSum return true if the tree has a 
root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:

                    5
                   / \
                  4   8
                 /   / \
                11  13  4   
               / \       \
              7   2       1
Input: root =[5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum =22
Output: True
"""

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val  =val
        self.left =left
        self.right = right

    def insert(self,data):
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            if data > self.val:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data

    def createTree(self,array):
        if (array == None or len(array)==0):
            return None

        treeNodeQueue = []
        integerQueue  = []

        for i in range(1,len(array)):
            integerQueue.append(array[i])
        

        treeNode = TreeNode(array[0])
        treeNodeQueue.append(treeNode)

        while (len(integerQueue)> 0):

            leftVal  = None if len(integerQueue)== 0 else integerQueue.pop(0)
            rightVal = None if len(integerQueue)== 0 else integerQueue.pop(0)

            current = treeNodeQueue.pop(0)

            if (leftVal !=None):
                    left = TreeNode(leftVal)
                    current.left = left
                    treeNodeQueue.append(left)
            
            if (rightVal !=None):
                    right = TreeNode(rightVal)
                    current.right = right
                    treeNodeQueue.append(right)
            
        
        return treeNode

class Solution:

    def has_path_sum(self, root: Optional[TreeNode], targetSum: int)->bool:

        # O(n) time where n is number of nodes 
        # O(h) memory complexity | O(n) time in the worst case & O(log(n)) if
        # it is a balanced binary tree
        def dfs(node, curSum):
            if not node:
                return False
            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum
            
            # We only need one path, so we return left or right path
            return (dfs(node.left, curSum) or 
                    dfs(node.right, curSum))
        return dfs(root, 0)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sample_1(self):
        tree_vals =[5,4,8,11,None,13,4,7,2,None,None,None,1]
        t =TreeNode()
        tree_root =t.createTree(tree_vals)
        self.assertTrue(self.solution.has_path_sum(tree_root, 22))

    def test_sample_2(self):
        tr = TreeNode(5)
        tr.left =TreeNode(4)
        tr.right=TreeNode(8)
        tr.left.left=TreeNode(11)
        tr.left.left.left =TreeNode(7)
        tr.left.left.right = TreeNode(2)
        tr.right.left=TreeNode(13)
        tr.right.right=TreeNode(4)
        tr.right.right.right=TreeNode(1)
        self.assertTrue(self.solution.has_path_sum(tr, 22))
    def test_empty_tree(self):
        self.assertFalse(self.solution.has_path_sum(None, 0))

    def test_single_node_tree(self):
        root = TreeNode(1)
        self.assertTrue(self.solution.has_path_sum(root, 1))
        self.assertFalse(self.solution.has_path_sum(root, 2))

    def test_tree_with_multiple_levels(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)

        self.assertTrue(self.solution.has_path_sum(root, 22))
        self.assertTrue(self.solution.has_path_sum(root, 26))
        self.assertTrue(self.solution.has_path_sum(root, 18))
        self.assertTrue(self.solution.has_path_sum(root, 27))

    def test_tree_with_negative_values(self):
        root = TreeNode(-2)
        root.right = TreeNode(-3)

        self.assertTrue(self.solution.has_path_sum(root, -5))
        self.assertFalse(self.solution.has_path_sum(root, -2))

    def test_complex_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        self.assertTrue(self.solution.has_path_sum(root, 7))
        self.assertTrue(self.solution.has_path_sum(root, 10))
        self.assertFalse(self.solution.has_path_sum(root, 1))
        self.assertFalse(self.solution.has_path_sum(root, 18))


if __name__ == '__main__':
    unittest.main()