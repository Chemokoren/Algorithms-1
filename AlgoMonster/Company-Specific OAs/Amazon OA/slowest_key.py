"""

Amazon Online Assessment (OA) - Slowest Key

Practice here: https://leetcode.com/problems/slowest-key/

Solution and Explanation

This question asks for the key with largest duration releaseTimes[i] - releaseTimes[i - 1]. We can 
simple loop through each release time and calculate its difference to the previous time. If multiple
characters have the same duration, we want to use the lexicographically largest.


"""
from typing import List
class Solution:

    def slowestKey(self,releaseTimes: List[int], keysPressed: str)->str:
        slowest_key ='a'
        longest_duration = 0
        n = len(keysPressed)

        for i in range(n):
            pressedTime = releaseTimes[i - 1] if i >  0 else 0
            duration = releaseTimes[i] - pressedTime
            if duration == longest_duration:
                slowest_key = max(slowest_key, keysPressed[i])
            elif duration > longest_duration:
                slowest_key = keysPressed[i]
                longest_duration = duration
                
        return slowest_key

