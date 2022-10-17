"""
Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees ) that store values 1 ... n ?

Example :

Input: 3
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

    def numTrees(self, n:int)->int:
        # numTree[4] = numTree[0] * numTree[3] +
        #            = numTree[1] * numTree[2] +
        #            = numTree[2] * numTree[1] +
        #            = numTree[3] * numTree[1]

        numTree =[1] * (n + 1)

        # 0 nodes = 1 tree
        # 1 nodes = 1 tree
        
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left    =   root -1
                right   =   nodes - root
                total   +=  numTree[left] * numTree[right]
            numTree[nodes] = total
        return numTree[n]
        
sol = Solution()
print("Unique BST:", sol.numTrees(2))