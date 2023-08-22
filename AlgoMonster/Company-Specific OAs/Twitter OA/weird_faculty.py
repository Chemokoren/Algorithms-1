"""
(OA) 2021 | Weird Faculty

Alex and Sam are playing a weird game. The rule of this weird game is simple: there are a total of n
tasks total that Alex and Sam has to perform, labelled 0 to n-1. Alex has to perform task 0 to k-1,
while Sam has to perform task k to n-1, where k is a number decided by Alex. For each player, if they
succeed in that task, they gain 1 point, but if they fail, they lose 1 point.

Alex is a competitive person, and they are looking to beat Sam in this game by having more points.
Alex knows that they cannot beat Sam fair and square, since their skills are identical. In fact, they
know that for task i, the chance of succeeding that task for either of them is always p[i], where 
p[i] is an integer equal to either 0 or 1 (Not only is it extremely weird that the result of each 
game is definitive, but it's even weirder that Alex knows this information beforehand - that is not 
the point of this problem).

Since Alex is the one choosing the value of k, they can rig the game in their favor by choosing a k 
such that Alex's expected score is greater than Sam's expected score. Alex is also extremely lazy, 
so they would prefer that the k selected is as small as possible, while still satisfying the previous
criteria.

Given p, a list of the probability of success for each task, find the smallest k such that Alex's 
expected score beats Sam's expected score.

Parameter

    p: A list of integers representing the probability of success for each task.

Result

    The smallest k such that Alex's expected score beats Sam's expected score. If no such k exists, 
    return -1.

Examples

Example 1:

Input: p = [1, 0, 0, 1, 0]

Output: 0

Explanation: If Alex performs 0 tasks (k = 0), they will have 0 points and Sam will have -1 points 
(2 successful tasks and 3 failed tasks).

Example 2:

Input: p = [1, 1, 1, 0, 1]

Output: 2

"""

from typing import List

def game(p: List[int]) -> int:
    return 0

if __name__ == '__main__':
    p = [int(x) for x in input().split()]
    res = game(p)
    print(res)