from typing import List
"""
You are given an integer array matchsticks where matchsticks[i] is length of the ith 
matchstick. You want to use all the matchsticks to make one square. You should not break
 any stick, but you can link them up, and each matchstick must be used exactly one time.

 Return true if you can make this square and false otherwise.

 Example 1:

 Input: matchsticks =[1,1,2,2,2]
 Output: true
 Explanation: You can form a square with length 2, one side of the square has two sticks
 each of length 1.

 Time complexity O(4^n) because we are making 4 decisions every time and the height of the
 decision tree is n.

"""

class Solution:
    def makeSquare(self, matchsticks: List[int])-> bool:
        """
        Program to use matchsticks to form a square.
        Parameters:
            matchsticks(List[int]): 
        Returns:
            res(bool): Return True if possible else False
        """
        length = sum(matchsticks) // 4
        sides =[0] * 4

        if sum(matchsticks) / 4 != length:
            return False
        
        # sorting helps us to return earlier if the longest matchstick is not
        # equal to the sides
        matchsticks.sort(reverse=True)
        
        def backtrack(i): # index of match stick
            # return true if we go through all the matchsticks
            if i == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i +1):
                        return True
                    sides[j] -= matchsticks[i] # back track to previous position
            return False
        return backtrack(0)

sol = Solution()
print(sol.makeSquare([1,1,2,2,2]))

