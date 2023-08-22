"""
Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth(1-indexed) smallest
element in the tree.

                    3
                   /  \
                  1    4
                   \
                    2
Input: root =[3,1,4,null,2], k=1 
Output: 1
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
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
            self.val = TreeNode(data)

    def traverse(self,troot):
        if troot:
            self.traverse(troot.left)
            print(troot.val,end="--")
            self.traverse(troot.right)


class IterativeSolution:
    
    def kthSmallest(self, root, k):
        n = 0
        stack =[]
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


tr = TreeNode(3)
tr.left =TreeNode(1)
tr.right =TreeNode(4)
tr.left.right =TreeNode(2)


isv = IterativeSolution()
	
print("AAAA::, Actual::", isv.kthSmallest(tr,1))


k=1
tree = TreeNode(20) 
tree.insert(8)
tree.insert(22)
tree.insert(4)
tree.insert(12)
tree.insert(10)
tree.insert(14)
#keys = [ 20, 8, 22, 4, 12, 10, 14 ]
# keys = [ 8, 22, 4, 12, 10, 14 ][1,2,3,4]
 
# for x in keys:
#     tree.insert(x)

# tree.traverse(tree.val)
print("Expected:, Actual::", isv.kthSmallest(tree, 7))
print("Traverse::",tree.traverse(tree))
class Solution1:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    if root is None: return None
    kth_smallest = None
    gen = self.in_order(root)
    for _ in range(k):
      kth_smallest = next(gen)
    return kth_smallest.val
  
  def in_order(self, root: TreeNode) -> TreeNode:
    if root.left:  
        yield from self.in_order(root.left)
    yield root
    if root.right: 
        yield from self.in_order(root.right)

sol =Solution1()
print("ndio ii::, Actual::", sol.kthSmallest(tr,1))