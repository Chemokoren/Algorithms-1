"""
Burst Balloons

You are given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on
it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i -1] * nums[i] * nums[i + 1] coins. if
i-1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with
a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:

Input: nums =[3, 1, 5, 8]
Output: 167
Explanation:
nums =[3,1,5,8] --->[3,5,8]--->[3,8]--->[8]--->[]
coins =3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 167
"""

class Solution:

    """
    Time Complexity:

    The time complexity is more challenging to analyze because it involves the recursive exploration of different combinations. Let's denote nn as the length of the input list nums.

        In the worst case, the recursive function explores all possible combinations of bursting balloons.
        At each recursive call, we iterate over the indices of nums, and for each index, we make another recursive call.
        The number of recursive calls at each level of the recursion is proportional to the length of nums.

    Considering the worst case, where every balloon can be chosen or not chosen at each level, the total number of recursive calls is 2n2n.

    Therefore, the time complexity is exponential: O(2n)O(2n).
    Space Complexity:

    The space complexity is determined by the depth of the recursion and the size of the data structures used.

        The depth of the recursion is at most nn (the length of nums).
        At each level of recursion, a new list of balloons (new_nums) is created, which takes O(n)O(n) space.

    Therefore, the space complexity is O(n)O(n) due to the recursion depth and the size of the data structures.
    Important Note:

    The given solution has a high time complexity due to its recursive nature, and it may not be efficient for large inputs. Dynamic programming or memoization techniques can be employed to optimize the time complexity by avoiding redundant calculations and storing intermediate results. If efficiency is a concern, it's recommended to explore alternative approaches to solving the problem.

    """
    from typing import List

    def burst_balloons(self, nums):
        nums.insert(0, 1)
        nums.append(1)

        global_total = 0

        def dfs(nums, current_total):
            nonlocal global_total

            if len(nums) == 2:
                global_total = max(global_total, current_total)
                return

            for i in range(1, len(nums) - 1):
                new_total = current_total + nums[i - 1] * nums[i] * nums[i + 1]
                new_nums = nums[:i] + nums[i + 1:]
                dfs(new_nums, new_total)

        dfs(nums, 0)

        return global_total
    """
    This code is an implementation of a dynamic programming solution to the "Burst Balloons" problem. The goal is to find the maximum coins obtained by bursting balloons arranged in a row, where each balloon has an associated value. The function maxCoins takes a list of balloon values (nums) and returns the maximum coins that can be obtained.

    Padding:
    --------
    nums = [1] + nums + [1]

    Padding the nums list with 1s at the beginning and end. This is done to simplify
    boundary conditions during the calculation.

    Memoization Dictionary:
    ----------------------
    

    dp = {}

    A dictionary (dp) is used for memoization to store intermediate results of subproblems. It helps avoid redundant calculations and improves the efficiency of the algorithm.

    
    DFS Function:
    -------------

    def dfs(l, r):
        if l > r:
            return 0
        if (l, r) in dp:
            return dp[(l, r)]
        dp[(l, r)] = 0
        for i in range(l, r + 1):
            coins = nums[l - 1] * nums[i] * nums[r + 1]
            coins += dfs(l, i - 1) + dfs(i + 1, r)
            dp[(l, r)] = max(dp[(l, r)], coins)
        return dp[(l, r)]

    -This is a recursive function (dfs) that explores different combinations of bursting 
    balloons and calculates the maximum coins. 
    -The parameters l and r represent the range of indices for the current subproblem.
    - Base Case: If l > r, there are no balloons in the current subproblem, so the function
      returns 0.
    - Memoization: If the result for the current subproblem (l, r) is already in the dp 
    dictionary, it is returned.
    - Initialize dp[(l, r)] to 0.
    - Iterate over the possible positions to burst a balloon (i) within the current range.
    - Calculate the coins obtained by bursting the balloon at position i.
    - Recursively call dfs for the two subproblems on the left and right of the burst balloon.
    - Update dp[(l, r)] with the maximum coins obtained in the current subproblem.
    - Return the maximum coins for the current subproblem.
    
    Return Result:
    --------------
    return dfs(1, len(nums) - 2)

    The initial call to the dfs function with the range [1, len(nums) - 2] to consider all 
    balloons except the padding.

    The solution uses dynamic programming with memoization to avoid redundant calculations 
    and improve efficiency. The time complexity is improved to O(n^3), where n is the length 
    of the input list nums, compared to the pure recursive solution.

    Time Complexity:
    ----------------

    The time complexity of this solution is O(n^3), where n is the length of the input list
      nums.

        DFS Recursion:
            The dfs function is a recursive function that explores different combinations 
            of bursting balloons.
            The recursion depth is at most n, where n is the length of the nums list.
            At each level of recursion, a nested loop iterates over the range [l,r]
             with a maximum of O(n) iterations.

        Memoization:
            The use of memoization with the dp dictionary ensures that each subproblem is 
            solved only once, reducing redundant calculations.
            The size of the memoization dictionary is O(n^2) because there are n^2
            possible subproblems.

    Combining these factors, the overall time complexity is O(n^3).


    Space Complexity:
    ----------------

    The space complexity of this solution is also O(n^2) due to the memoization dictionary.

    Memoization Dictionary:

        The dp dictionary is used for memoization to store intermediate results of 
        subproblems.
        The size of the dictionary is O(n^2) because there are n^2 possible subproblems.
        Each entry in the dictionary requires constant space.

    Additional Space:
        The recursive call stack contributes to the space complexity, but its maximum depth 
        is at most nn.

    Therefore, the dominant factor in space complexity is the memoization dictionary, 
    resulting in a space complexity of O(n^2).

    Summary:

    Time Complexity: O(n^3)
    Space Complexity: O(n^2)

    The memoization technique significantly improves the time complexity compared to a naive 
    recursive solution without memoization, making the algorithm more efficient for larger 
    inputs.

    """
    
    def maxCoins(self, nums: List[int])-> int:
        nums =[1] + nums + [1]
        dp ={}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l -1] * nums[i] * nums[r+1]
                coins += dfs(l, i -1) + dfs(i +1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]
        return dfs(1, len(nums)-2)

sol = Solution()
print(sol.burst_balloons([3, 1, 5, 8]))
print(sol.maxCoins([3, 1, 5, 8]))

print('---')
print(sol.burst_balloons([3, 5, 8]))
print(sol.maxCoins([3, 5, 8]))