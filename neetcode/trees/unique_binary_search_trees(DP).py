"""
Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees ) that store values 1 ... n ?

Example :

Input:  3
Output: 5

Explanation:

Given n = 3, there are a total of 5 uniue BST's:

1           3       3           2           1
 \         /       /           / \           \
  3       2       1           1   3           2  
 /       /         \                            \
2       1           2                            3

"""

class Solution:

    def num_trees(self, n:int)->int:
        # num_trees[4]      = num_trees[0] * num_trees[3] +
        #                   = num_trees[1] * num_trees[2] +
        #                   = num_trees[2] * num_trees[1] +
        #                   = num_trees[3] * num_trees[0]

        vals =[1] * (n + 1)

        # 0 nodes = 1 tree
        # 1 nodes = 1 tree
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left    =   root -1
                right   =   nodes - root
                total   +=  vals[left] * vals[right]
            vals[nodes] = total
        return vals[n]
        

import unittest

class TestUniqueBinarySearchTrees(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_four_trees(self):
        self.assertEqual(14, self.sol.num_trees(4))

    def test_three_trees(self):
        self.assertEqual(5, self.sol.num_trees(3))

    def test_two_trees(self):
        self.assertEqual(2, self.sol.num_trees(2))

    def test_one_trees(self):
        self.assertEqual(1, self.sol.num_trees(1))

    def test_zero_trees(self):
        self.assertEqual(1, self.sol.num_trees(0))


if __name__== "__main__":
    unittest.main()
