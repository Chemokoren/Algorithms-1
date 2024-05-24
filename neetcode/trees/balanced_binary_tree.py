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
        if not troot:
            return
        print(troot.val, end='-->')
        tr = troot
        
        q = queue()
        q.enqueue(tr)
        
        while not q.is_empty():
            tr = q.dequeue()

            if tr.left:
                print(tr.left.val, end="-->")
                q.enqueue(tr.left)
            if tr.right:
                print(tr.right.val, end="-->")
                q.enqueue(tr.right)
                
tr = TreeNode(3)
tr.left =TreeNode(9)
tr.right =TreeNode(20)
tr.right.left =TreeNode(15)
tr.right.right =TreeNode(7)   
     
print(f" levelorder :: {TreeNode().levelorder(tr)}")
        
class Solution:

    def is_balanced(self, root: Optional[TreeNode])->bool:
        """
        Function to determine if Binary Tree is balanced.
        
        Args:
            root(TreeNode): optional TreeNode root
        
        Returns:
            bool: True if balanced else False
        
        Example:
            >>> root = TreeNode(1)
            >>> root.left = TreeNode(2)
            >>> root.right = TreeNode(3)
            >>> root.left.left = TreeNode(4)
            >>> root.left.right = TreeNode(5)
            >>> root.right.right = TreeNode(6)
            >>> is_balanced(root)
            True
        
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
            balanced =(left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            height = 1 + max(left[1], right[1])
            return [balanced, height]
    
        # returns the bool value
        return dfs(root)[0] 
    


class Solution2:
    
    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        """
        Function to determine if Binary Tree is balanced.

        Parameters:
            root (TreeNode): Optional TreeNode root of the binary tree.

        Returns:
            bool: True if the binary tree is balanced, otherwise False.
        
        Example:
            >>> tree = TreeNode(1)
            >>> tree.left = TreeNode(2)
            >>> tree.right = TreeNode(3)
            >>> tree.left.left = TreeNode(4)
            >>> tree.left.right = TreeNode(5)
            >>> tree.right.right = TreeNode(6)
            >>> Solution2().is_balanced(tree)
            True
        """
        
        # Helper function to calculate the height of a subtree rooted at 'node'
        def get_height(node):
            """
            Helper function to calculate the height of a subtree.

            Parameters:
                node (TreeNode): The root node of the subtree.

            Returns:
                int: The height of the subtree rooted at 'node'.
            """
            if not node:
                return 0

            left_height = get_height(node.left)
            right_height = get_height(node.right)

            return max(left_height, right_height) + 1

        # Helper function to recursively check if the binary tree is balanced
        def is_balanced_helper(node):
            """
            Helper function to recursively check if the binary tree is balanced.

            Parameters:
                node (TreeNode): The root node of the binary tree.

            Returns:
                bool: True if the binary tree rooted at 'node' is balanced, otherwise False.
            """
            if not node:
                return True

            left_height = get_height(node.left)
            right_height = get_height(node.right)

            # Check if the absolute difference in heights of left and right subtrees is greater than 1
            if abs(left_height - right_height) > 1:
                return False

            # Recursively check if both left and right subtrees are balanced
            return is_balanced_helper(node.left) and is_balanced_helper(node.right)

        # Call the helper function to check if the entire binary tree is balanced
        return is_balanced_helper(root)



import unittest
class TestBalancedBinaryTree(unittest.TestCase):

    class TreeNode:
        """TreeNode class Structure"""
        def __init__(self, val=0, left =None, right=None):
            self.val    = val
            self.left   = left
            self.right  = right

    def setUp(self) -> None:
        super().setUp()

        self.tr = TreeNode(3)
        self.tr.left =TreeNode(9)
        self.tr.right =TreeNode(20)
        self.tr.right.left =TreeNode(15)
        self.tr.right.right =TreeNode(7)
        self.cls = Solution()

        # Sample balanced tree
        #     1
        #    / \
        #   2   3
        #  / \
        # 4   5
        self.balanced_tree = TreeNode(1)
        self.balanced_tree.left = TreeNode(2)
        self.balanced_tree.right = TreeNode(3)
        self.balanced_tree.left.left = TreeNode(4)
        self.balanced_tree.left.right = TreeNode(5)

        # Sample unbalanced tree
        #     1
        #    / \
        #   2   3
        #      / \
        #     4   5
        #        /
        #       6
        self.unbalanced_tree = TreeNode(1)
        self.unbalanced_tree.left = TreeNode(2)
        self.unbalanced_tree.right = TreeNode(3)
        self.unbalanced_tree.right.left = TreeNode(4)
        self.unbalanced_tree.right.right = TreeNode(5)
        self.unbalanced_tree.right.right.left = TreeNode(6)

    
    def test_balanced_tree(self):
        expected =True
        self.assertEqual(expected, self.cls.is_balanced(self.tr))

    def test_second_balanced_tree(self):
        expected =True
        self.assertEqual(expected, self.cls.is_balanced(self.balanced_tree))

    def test_unbalanced_tree(self):
        expected =False
        self.assertFalse(expected, self.cls.is_balanced(self.unbalanced_tree))
    

if __name__=="__main__":
    unittest.main()