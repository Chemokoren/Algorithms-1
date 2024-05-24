import unittest
"""
Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree
of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree is a tree that consits of a node in tree and all of this node's
descendants. The tree could also be considered as a subtree of itself.


Example 1:

                root                        subRoot
                3                               4
               / \                             / \
              4   5                           1   2  
             / \
            1   2

Input: root =[3,4,5,1,2], subRoot =[4,1,2]
Output = True

O(S*T) time where S is nodes in the main tree and T the nodes in the subtree
"""

# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val =0, left =None, right=None):
        self.val    = val
        self.left   = left
        self.right  = right

    # only applicable to binary search tree
    def insert_main(self,data):
        
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert_main(data)
            if data > self.val:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert_main(data)
        else:
            self.val = TreeNode(data)

    # preorder traversal
    def traverse(self):
        if self.val:
            print(self.val,end="--")
            self.traverse(self.left)
            self.traverse(self.right)

    # Print the tree : inorder traversal
    def print_tree(self):
      if self.left:
         self.left.print_tree()
      print(self.val,end='--'),
      if self.right:
         self.right.print_tree()

class Solution:

    def is_subtree(self, s:TreeNode, t:TreeNode)-> bool:
        if not t: return True
        if not s: return False

        if self.same_tree(s, t):
            return True

        return (self.is_subtree(s.left, t) or 
                self.is_subtree(s.right, t))

    def same_tree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.same_tree(s.left, t.left) and
                    self.same_tree(s.right, t.right))
        return False








class TestSubtree(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

        self.t1 =TreeNode(3)
        self.t1.left =TreeNode(4)
        self.t1.right =TreeNode(5)
        self.t1.left.left =TreeNode(1)
        self.t1.left.right =TreeNode(2)

        self.t2 = TreeNode(4)
        self.t2.left = TreeNode(1)
        self.t2.right = TreeNode(2)


    def test_sub_tree(self):
        self.assertEqual(True, self.sol.is_subtree(self.t1, self.t2), "Should be True")

if __name__ == '__main__':
    unittest.main()
