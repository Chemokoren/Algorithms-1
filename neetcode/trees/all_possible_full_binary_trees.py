from typing import List, Optional
"""
All possible Full Binary Trees - Memoization

Given an integer n, return a list of all possible full binary trees with n nodes. Each node
of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final 
list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Example : n=7

        0               0               0               0                       0
       / \             / \             / \             / \                     / \
      0   0           0   0           0   0           0   0                   0   0
         / \             / \         / \  /\         / \                     / \   
        0   0           0   0       0  0 0  0       0   0                   0   0
           / \         / \                              /\                 / \ 
          0   0       0   0                            0  0               0   0   


O(2^n) time complexity
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def all_possible_FBT(self, n:int)-> List[Optional[TreeNode]]:
        """
        Function to generate all possible Full Binary Trees (FBTs) with a given number of nodes.

        Parameters:
            n (int): The number of nodes in the desired Full Binary Trees.

        Returns:
            List[Optional[TreeNode]]: A list containing all possible FBTs with 'n' nodes.
                                       Each TreeNode represents the root of a Full Binary Tree.
                                       Returns an empty list if 'n' is even or negative.

        Example:
            >>> sol = Solution()
            >>> result = sol.all_possible_FBT(3)
            >>> for tree in result:
            >>>     print(tree)
            TreeNode object representing a Full Binary Tree with 3 nodes.
            ...
            TreeNode object representing a Full Binary Tree with 3 nodes.
        """

        # Dictionary to store results of subproblems: maps 'n' to list of FBTs with 'n' nodes
        dp ={0: [], 1: [TreeNode()]} 

        # Helper function to recursively generate all possible FBTs with 'n' nodes
        def backtrack(n):
            # If result for 'n' has already been computed, return it from dp
            if n in dp:
                return dp[n]
            
            res =[]

            # Explore all possible combinations of left and right subtrees for 'n' nodes
            for left in range(n): # 0 - (n-1)
                right = n - 1 - left
                leftTrees, rightTrees = backtrack(left), backtrack(right)

                # Combine left and right subtrees to form FBTs with 'n' nodes
                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
            
            # Store the list of FBTs for 'n' nodes in dp
            dp[n] = res
            return dp[n]
        
        # Call the helper function to generate all possible FBTs with 'n' nodes
        return backtrack(n)

# Example usage:
sol = Solution()
result = sol.all_possible_FBT(3)
for tree in result:
    print(tree)

    
# print(len(sol.all_possible_FBT(7)))
    
import unittest

class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()

    def test_all_possible_FBT_with_negative_n(self):
        # Test case with negative value of n
        result = self.sol.all_possible_FBT(-1)
        self.assertEqual(result, [])

    def test_all_possible_FBT_with_even_n(self):
        # Test case with even value of n
        result = self.sol.all_possible_FBT(4)
        self.assertEqual(result, [])

    def test_all_possible_FBT_with_zero_n(self):
        # Test case with n = 0
        result = self.sol.all_possible_FBT(0)
        self.assertEqual(result, [])

    def test_all_possible_FBT_with_small_n(self):
        # Test case with small value of n
        result = self.sol.all_possible_FBT(3)
        # Expected number of FBTs for n = 3 is 5
        print("aaa::", len(result))  # Add this line to print the length of the result list
        self.assertEqual(len(result), 5)
        # Check if all FBTs have 3 nodes
        for tree in result:
            self.assertEqual(self.get_tree_size(tree), 3)

    def get_tree_size(self, root):
        # Helper function to get the size of the binary tree
        if root is None:
            return 0
        return 1 + self.get_tree_size(root.left) + self.get_tree_size(root.right)

if __name__ == '__main__':
    print(f"testing")
    unittest.main()
