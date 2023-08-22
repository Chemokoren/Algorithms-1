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
    def insertMain(self,data):
        
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insertMain(data)
            if data > self.val:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insertMain(data)
        else:
            self.val = data

    # preorder traversal
    def traverse(self):
        if self.val:
            print(self.val,end="--")
            self.traverse(self.left)
            self.traverse(self.right)

    # Print the tree : inorder traversal
    def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print(self.val,end='--'),
      if self.right:
         self.right.PrintTree()

class Solution:

    def isSubtree(self, s:TreeNode, t:TreeNode)-> bool:
        if not t: return True
        if not s: return False

        if self.sameTree(s, t):
            return True

        return (self.isSubtree(s.left, t) or 
                self.isSubtree(s.right, t))

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
                    self.sameTree(s.right, t.right))
        return False



t1 =TreeNode(3)
t1.left =TreeNode(4)
t1.right =TreeNode(5)
t1.left.left =TreeNode(1)
t1.left.right =TreeNode(2)

t2 = TreeNode(4)
t2.left = TreeNode(1)
t2.right = TreeNode(2)

sol = Solution()
print("Expected:: True, Actual::", sol.isSubtree(t1, t2))

class TestSubtree(unittest.TestCase):

    def test_sub_tree(self):
        self.assertEqual(True, sol.isSubtree(t1, t2), "Should be True")

if __name__ == '__main__':
    unittest.main()
