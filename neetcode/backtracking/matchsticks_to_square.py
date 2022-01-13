from typing import List
"""
You are given an integer array matchsticks where matchsticks[i] is length of the ith 
matchstick. You want to use all the matchsticks to make one square. You should not break
 any stick, but you can link them up, and each matchstick must be exactly one time.

 Return true if you can make this square and false otherwise.

 Example 1:

 Input: matchsticks =[1,1,2,2,2]
 Output: true
 Explanation: You can form a square with length 2, one side of the square came two sticks with
 length 1.

 Time complexity O(4^n) because we are making 4 decisions every time and the height of the
 decision tree is n.

"""

class Solution:
    def makeSquare(self, matchsticks: List[int])-> bool:
        length = sum(matchsticks) // 4
        sides =[0] * 4

        if sum(matchsticks) / 4 != length:
            return False
        matchsticks.sort(reverse=True)
        
        def backtrack(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i +1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        return backtrack(0)

matchsticks =[1,1,2,2,2]
sol = Solution()
print(sol.makeSquare(matchsticks))

