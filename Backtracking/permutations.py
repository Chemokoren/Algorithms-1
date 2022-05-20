"""
The big picture of backtracking

-Backtracking solves problems by trying a series of actions. If a series failes, we back up and try a
a different series.(Maze is an example of the broader graph search)

- Any problem that can be described as a choice of discreet choices can be worked using backtracking

The recursive solution may be elegant, but remember not to dwell on the backtracking concept or what the
recursion is doing.

When the perfomance difference between solutions is small, the best choice to solve a problem may just
be whichever one makes the most sense to you.

Permutations
------------

- Given an aray nums of distinct integers, return all possible permutations. You can return the 
answer in any order.

Example 1:

Input: nums =[1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

                                        [1,2,3]
                                      /     |     \
                                [2,3]      [1,3]  [1,2]
                              /   \       /   \   /   \
                            [3]   [2]    [3]  [1] [2] [1]

Example 2:

Input: nums =[0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums =[1]
Output: [[1]]



"""
from typing import List

class Solution:

    # def permute(self, nums:List[int])->List[List[int]]:
    def permute(self, nums):

        result =[]

        # base case
        if(len(nums) == 1):
            return [nums.copy()] #[:]

        for i in range(len(nums)):
            n = nums.pop(0)

            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result

sol = Solution()
print("expected: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], actual: ", sol.permute([1,2,3]))
print("expected: [[0,1],[1,0]], actual: ", sol.permute([0,1]))
print("expected: [[1]], actual: ", sol.permute([1]))
