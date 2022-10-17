from typing import Optional
"""
Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in 
height by no more than 1.

 Example 1:
                    3
                   / \
                  9   20
                      / \
                    15   7
Input: root =[3,9,20,null,null,15,7]
Output: true
"""
class _Node:
    """Node class Structure"""
    def __init__(self,data) -> None:
        self.data =data
        self.next =None
        
class queue:
    """linked queue implementation"""
    def __init__(self) -> None:
        self.head   = None
        self.tail   = None
        self._size  = 0
        
    def is_empty(self):
        """check if queue is empty"""
        return self._size == 0
        
    def enqueue(self,e):
        """enqueue an item in array queue"""
        new_node =  _Node(e)
        if self.is_empty():
            self.head   = new_node
            self.tail   = new_node
        self.tail.next  = new_node
        self._size +=1
        
        
    def dequeue(self):
        """remove first item in queue"""
        if self.is_empty():
            print("queue is empty")
            return
        val = self.head.data
        self.head = self.head.next
        self._size -=1
        return val
    
    
    
# Definition for a binary tree node.
class TreeNode:
    """TreeNode class Structure"""
    def __init__(self, val=0, left =None, right=None):
        self.val    = val
        self.left   = left
        self.right  = right
        
    def levelorder(self,troot):
        """levelorder traversal"""
        tr = troot
        print(troot.val, end='-->')
        q = queue()
        q.enqueue(tr.val)
        
        while not q.is_empty():
            tr = q.dequeue()
            if tr.left:
                print(tr.left.val, end="-->")
                q.enqueue(tr.left)
            if tr.right:
                print(tr.right.val, end="-->")
                q.enqueue(tr.right)
                
        
        
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode])->bool:
        """
        Function to determine if Binary Tree is balanced.
        
            Parameters:
                root(TreeNode): optional TreeNode root
            Returns:
                bool: True if balanced else False
        
        """

        def dfs(root):
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced =(left[0] and right[0] and
                        abs(left[1] - right[1] <= 1)
                        )
            return [balanced, 1+max(left[1], right[1])]
        
        # returns the bool value
        return dfs(root)[0] 
    
tr = TreeNode(3)
tr.left =TreeNode(9)
tr.right =TreeNode(20)
tr.right.left =TreeNode(15)
tr.right.right =TreeNode(7)

cls = Solution()
print("is balanced::", cls.isBalanced(tr))
# tr.levelorder(tr.val)