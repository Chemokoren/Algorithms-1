"""
Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees )that store values 1...n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:
1               3       3        2     1
  \            /       /       /   \     \
    3         2       1       1     3     2
   /         /         \                    \
  2         1           2                    3
"""

import unittest

class Solution:


    # time complexity: O(n^2) | space complexity: O(n)
    def num_trees(self, n: int) -> int:
        # num_tree[4]  = num_tree[0] * num_tree[3] +
        #                num_tree[1] * num_tree[2] +
        #                num_tree[2] * num_tree[1] +
        #                num_tree[3] * num_tree[1]
        num_tree =[1] * (n + 1)

        # base cases
        # 0 nodes = 1 tree
        # 1 nodes = 1 tree

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root -1
                right = nodes - root
                total += num_tree[left] * num_tree[right]
            num_tree[nodes] = total
        return num_tree[n]
    
class TestUniqueBinarySearchTree(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_unique_binary_search_trees(self):
        self.assertEqual(5, self.sol.num_trees(3))

if __name__=="__main__":
    unittest.main()