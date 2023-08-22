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

    def is_balanced(self, root: Optional[TreeNode])->bool:
        """
        Function to determine if Binary Tree is balanced.
        
        Args:
            root(TreeNode): optional TreeNode root
        
        Returns:
            bool: True if balanced else False
        
        """

        def dfs(root):
            
            """
            Helper function for DFS in a binary tree

            Args:
                root: this is the root node of the binary tree

            Returns:
                [bool, int]: list containing a boolean value & an integer of the difference
            """
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced =(
                left[0] and 
                right[0] and
                abs(left[1] - right[1] <= 1)
                )
            height = 1 + max(left[1], right[1])
            return [balanced, height]
    
        # returns the bool value
        return dfs(root)[0] 
    
tr = TreeNode(3)
tr.left =TreeNode(9)
tr.right =TreeNode(20)
tr.right.left =TreeNode(15)
tr.right.right =TreeNode(7)

cls = Solution()
print("is balanced::", cls.is_balanced(tr))
# tr.levelorder(tr.val)

# Sample balanced tree
#     1
#    / \
#   2   3
#  / \
# 4   5
balanced_tree = TreeNode(1)
balanced_tree.left = TreeNode(2)
balanced_tree.right = TreeNode(3)
balanced_tree.left.left = TreeNode(4)
balanced_tree.left.right = TreeNode(5)

# Sample unbalanced tree
#     1
#    / \
#   2   3
#      / \
#     4   5
#        /
#       6
unbalanced_tree = TreeNode(1)
unbalanced_tree.left = TreeNode(2)
unbalanced_tree.right = TreeNode(3)
unbalanced_tree.right.left = TreeNode(4)
unbalanced_tree.right.right = TreeNode(5)
unbalanced_tree.right.right.left = TreeNode(6)

solution = Solution()
print("balanced::",solution.isBalanced(balanced_tree))     # Expected output: True
print("unbalanced::", solution.isBalanced(unbalanced_tree))   # Expected output: False



class Solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Function to determine if Binary Tree is balanced.

        Parameters:
            root (TreeNode): Optional TreeNode root
        Returns:
            bool: True if balanced else False
        """

        def get_height(node):
            if not node:
                return 0

            left_height = get_height(node.left)
            right_height = get_height(node.right)

            return max(left_height, right_height) + 1

        def is_balanced_helper(node):
            if not node:
                return True

            left_height = get_height(node.left)
            right_height = get_height(node.right)

            if abs(left_height - right_height) > 1:
                return False

            return (
                is_balanced_helper(node.left)
                and is_balanced_helper(node.right)
            )

        return is_balanced_helper(root)

print("############### sol ###############")
sol = Solution2()
print(sol.isBalanced(balanced_tree))     # Expected output: True
print(sol.isBalanced(unbalanced_tree))   # Expected output: False

# import collections
# class SolutionOne:
    
    
#     def BinarySideView(self,root):
#         q = collections.deque([root])
#         res =[]
        
#         while q:
#             for _ in range(len(q)):
#                 rightSide = None
#                 node 	  = q.popleft()
                
#                 if (node):
#                     rightSide = node
#                     q.append(node.left)
#                     q.append(node.right)
#             if rightSide:
#                 res.append(rightSide.val)
#         return res
	
	
	
# si =SolutionOne()
# print("Expected::, Actual::", si.BinarySideView(tr))