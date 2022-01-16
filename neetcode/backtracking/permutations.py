from typing import List
"""
Permutations

Given an array nums of distinct integers, return all possible permutations. You can return
the answer in any order.

Example 1:

Input: nums =[1,2,3]
Output:[[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]

Example 2:

Input: nums =[0,1]
Output: [[0,1], [1,0]]

Example 3:

Input: nums =[1]
Output: [[1]]

Working_________
given 3 vals the no of permutations is 3 * 2* 1 = 6 (3 options in 1st choice, two and 1)

              0
           /  |  \ 
          1   2    3
         /\  / \  / \
        2  3 1  3 1  2  
       /  /  |  | |  |
      3  2   3  1 2  1

Actual algorithm used in the solution
(2,3,1) (3,2,1)             [1,2,3]
                        /      |       \
(2,3) (3,2)         [2,3]     [1,3]    [1,2]   
                    / \       /  \      / \
                   [3] [2]   [3]  [1]  [2] [1] 

"""

class Solution:

    def permute(self, nums: List[int]) ->List[List[int]]:
        result =[]

        # base case
        if(len(nums) == 1):
            return [nums[:]] # the latter is faster than nums.copy()

        for i in range(len(nums)):
            n = nums.pop(0)
            perms =self.permute(nums)
            for perm in perms: #(case 1: append 1 to [3,2], [2,3] leading to [3,2,1],[2,3,1])
                perm.append(n)

            result.extend(perms)
            nums.append(n)

        return result

nums =[1,2,3]
sol = Solution()
print(sol.permute(nums))

    