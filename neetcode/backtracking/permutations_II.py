from typing import List
"""
Given a collection of numbers, nums, that might contain duplicates, return all possible 
unique permutations in any order.

Example 1:

Input: nums =[1,1,2]

Output:

[[1,1,2],
[1,2,1],
[2,1,1]
]

"""
class Solution:

    # O(n * 2^n)
    def permuteUnique(self, nums: List[int])->List[List[int]]:
        res =[]
        perm =[]
        count ={n:0 for n in nums}

        for n in nums:
            count[n] += 1

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] +=1
                    perm.pop()
        dfs()
        return res
nums =[1,1,2]

sol = Solution()
print(sol.permuteUnique(nums))