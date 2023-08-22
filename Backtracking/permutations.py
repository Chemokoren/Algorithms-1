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

The concept of returning all possible solutions points to backtracking

3 Keys of backtracking
-1) Choices - set of decisions we need to take (choose one number)
-2) Constraints - decisions are limited by a set of constraints (We can only use one number & we can't reuse this number latter)
-3) Goal - We make these decisions in order to reach a goal(build permutation)


Backtracking recipe
-------------------

void Backtrack(res, args):
    if(GOAL REACHED):
            add solution to res
            return

    for i in range(0,NB_CHOICES):
        if(CHOICES[i] is valid):
            make choices[i]

            Backtrack(res, args)

            undo choices[i]


"""
from itertools import permutations
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

# solution II
def backtrack(res, nums, permutation, used): # res: int, nums:int, permutation:int, used: bool,
    if(len(permutation) == len(nums)): # goal is reach
        res.append(permutation) # res.push_back(permutation)
        return

    for i in range(0, len(nums)): #in nb_choices
        if(not used[i]): # valid choice
            # make choice
            used[i] =True
            permutation.append(nums[i]) # permutation.push_back(nums[i])
            backtrack(res,nums,permutation, used)
            # undo the choice
            used[i]= False
            permutation.pop() # permutation.pop_back()

def permute(nums):
    res =[]
    used =[False] * len(nums)
    permutation =[]
    backtrack(res, nums, permutation, used)
       
    return res

print("strange ")
print(permute([1,2,3]))




def permuteApp(list, s):
    if list == 1:
        return s
    else:
        return [
            y + x
            for y in permuteApp(1,s)
            for x in permuteApp(list -1,s)
        ]

print(permuteApp(1, ["a","b","c"]))
print(permuteApp(2, ["a","b","c"]))

"""
There are three types of problems in backtracking:

    Decision Problem – Search for a feasible solution
    Optimization Problem – Search for the best solution
    Enumeration Problem – Find all feasible soutions

State Space Tree – A state-space tree is a tree representing all the possible states (solution or nonsolution) 
of the problem from the root as an initial state to the leaf as a terminal state. Problems can be represented 
using the state-space tree.

The state-space tree comprises the states of the given problem. Then, we can check if these states are the 
solutions or not. A backtracking algorithm traverses the tree recursively in the depth-first search manner.

Backtracking follows the below mentioned approach:

    It checks whether the given node is a valid solution or not.
    Discard several inavlid solutions with one iteration.
    Enumerate all subtree of the node to find the valid solution.

Algorithms that use backtracking

Some algorithms that use backtracking include:

    N-queens problem
    Graph coloring
    Crosswords
    Rat in the maze

Recursion vs. backtracking
--------------------------

Recursion involves a function calling itself until it reaches the base case.

Backtracking uses recursion to discover all of the possibilities until we get the best end result for the 
problem.

##### Backtracking is an approach to solving constraint-satisfaction problems without trying all possibilities.

These problems are interesting because there are so many candidate solutions, the vast majority of which do not
satisfy the given constraints. Can’t we just try them all, one-by-one, until one does? Not really, because:

In the N-Queens Problem, there are (n^2n) ways to place n queens on an n×n board. For an 8×8
board there are 4,426,165,368 possible arrangements.

For Sudoku, there are 9^n ways to fill the n blank squares. Suppose we were given 20 cells filled in. 
There are 16,​173,​092,​699,​229,​880,​893,​718,​618,​465,​586,​445,​357,​583,​280,​647,​840,​659,​957,​609 possible ways to fill
 in the remaining 61 cells.

For the No Equal Adjacent Substrings Problem, there are nk possible strings. That’s a huge number. For a
100-character long string of trinary digits, we have
 515,​377,​520,​732,​011,​331,​036,​461,​129,​765,​621,​272,​702,​107,​522,​001 possibilities.

When k-coloring maps of n regions, there are kn possible colorings. For example, there are 
1,​267,​650,​600,​228,​229,​401,​496,​703,​205,​376 ways to color a 50-region map with 4 colors.

There are (15!)7 ways to arrange the walkers in a 7-day Kirkman Schoolgirls Problem. That is an 85-digit
number.

In the Traveling Salesperson Problem, there are n! possible paths. 200! is a 375-digit number.
500! has 1,135 digits. 

A brute-force algorithm tries all possibilities. Not going to happen.

Smart Approach
--------------

Think about how you would solve the no-equal-adjacent-substring problem.

Would you try to build up a solution, digit-by-digit? Click the STEP button to take a step at a time and 
see if it matches your intuition:

Visualize the problem as “filling in slots.” For each slot, try each value in turn. When a value doesn’t work
in a slot, you’ve effectively eliminated zillions of candidates. When nothing works in a slot, you have to 
backtrack.

Let’s see more examples. For each example,

    Notice the formulation of the problem into slots and values.
    Watch carefully for the occurences of backtracking. 

Eight-Queens

For each column (1..8), try to place a queen in each row (1..8) in turn, so that no two queens attack
each other.

Map Coloring

For each country, try the colors red, green, orange, yellow in turn, so that no two adjacent countries have 
the same color.

No Equal Adjacent Substrings

For each slot 1..50, try the digits 0, 1, and 2 in order, such that no two adjacent substrings are equal.
answ: 01020120210120102012021020102101201020120210120102

Sudoku

For each non-fixed square, try each of the values 1..9 in turn. 

Maze Solving

At each square, try going up, then left, then right, then down. Whenever the new square has not been visited, 
move there. When you have to backtrack, mark the square as fully explored.


    
"""