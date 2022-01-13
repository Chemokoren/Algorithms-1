from typing import List
"""
Combinations

Given two integers n and k, return all possible combinations of k numbers out of the range 
[1, n]
You may return the answer in any order.

Example 1:

Input: n =4, k =2
Output:
[
    [2,4],
    [3,4],
    [2,3],
    [1,2],
    [1,3],
    [1,4],

]

k *n ^ k

but, the possible combinations are:

k * (n!) / (n-k)! * k!

"""
class Solution:

    def combine(self, n:int, k:int) -> List[List[int]]:
        res =[]

        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return 

            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i +1, comb)
                comb.pop()
        backtrack(1,[])
        return res

n, k =4, 2

sol =Solution()
print(sol.combine(n, k))