"""
The Kirkman Problem
--------------------

We Are Pruning Search Trees

If you had to systematically enumerate all possible candidate solutions to a “slots-and-values” 
problem, you might write them all out as paths in a tree. 
Each root-to-leaf-path is a candidate solution. Here are the candidates for the no-equal-substring 
problem, using the digits 0, 1, and 2, of length 4:

                                    0
                            /       |      \
                           0        1        2
                         / | \    / | \    / | \
                        0  1  2  0  1  2  0  1  2          

https://drive.google.com/file/d/1cyl-KCOTGn5FiyC7Z764l0JOJICvXIw5/view?usp=sharing

I only had room to show 4 levels (81 possible solutions, 121 nodes total); showing even 10 levels 
would require 59,049 leaf nodes (88,573 total nodes), and 50 levels would be, well, you get the idea.

To solve a constraint problem we search for a solution. A brute-force algorithm searchs the whole tree,
but with backtracking, we get to throw away massive parts of the tree when we discover a partial 
solution cannot be extended to a complete solution.

So after realizing the second value cannot be a zero, you can avoid considering (i.e., you prune) every
possible string stating with 00. We built up a search tree with only 21 nodes, as opposed to 88,753.

A Generic Backtracking Solver

Each of the problems above are in the some sense the same problem. They all work by calling some 
initialization function, then for each possible slot, you try each possible value in turn, stopping when a
solution is found, or backracking when we can’t fill the current slot.
So we can write a backtracking engine that is parameterized by the type of slots, the values for each slot,
and a function that determines whether the current partial solution is safe.

"""

# A Python Backtracking Engine
def solve(values, safe_up_to, size):
    """ Finds a solution to a backtracking problem 

    values -- a sequence of values to try, in order. For a map coloring problem, this may be a list of
    colors, such as ['red','green','yellow', 'purple']
    safe_up_to -- a function with two arguments, solution and position, that returns whether the value
    assigned to slots 0..pos in the solution list, satisfy the problem constraints.
    size -- the total number of "slots" you are trying to fill

    Return the solution as a list of values
    """
    solution =[None] * size

    def extend_solution(position):
        
        for value in values:
            solution[position] =value
            if safe_up_to(solution,position):
                if position >= size-1 or extend_solution(position+1):
                    return solution
        return None
    return extend_solution(0)

# solving the no-equal-adjacent substrings problem
import backtracker

def no_adjacencies(string, up_to_index):
    # see if the sequence filled from indices 0 up_to_index, inclusive, is free of any adjacent 
    # substrings. We'll have to try all subsequences of length 1,2,3, up to half the length of the
    #  string. Return False as soon as we find an equal adjacent pair.
    length = up_to_index + 1
    for j in range(1, length//2+1):
        if(string[length-2*j:length-j] == string[length-j:length]):
            return False
    return True
print(''.join(str(v) for v in backtracker.solve(range(3), no_adjacencies,50)))


'''
the 8-Queens Problem:
'''
import backtracker

def no_conflicts(board, up_to_column):
    # see if any queens in columns to the left of up_to_column intefere with the queen in up_to_column.
    # Return False as soon as you find one that does.
    for col in range(up_to_column):
        if(board[col] == board[up_to_column]                            # same row
            or board[col] == board[up_to_column] + up_to_column - col   # diagonal
            or board[col] == board[up_to_column] + col - up_to_column): # diagonal
            return False

    return True

print(backtracker.solve(range(8), no_conflicts, 8))


'''
Iterative Implementations

The solutions above used recursion to implement backtracking. This is great because if we ever have to
backtrack, we return right in the middle of a for-loop so we know the next value to try.
This is actually awesome.

Can we do things iteratively?

Well, yeah, but we have to some incrementing an decrementing manually, and some ugly loop controlling.

iterative engine in Python
'''

def solve(highest_value, safe_up_to, num_slots):
    """ Finds a solution to a backtracking problem

    highest_value -- the largest value to try. Values for the slots will be in the range 
    0..highest_value, inclusive.

    safe_up_to -- a function with two arguments, solution and position, that returns whether the values
    assigned to slots 0..position in the solution list, satisfy the problem constraints.

    num_slots --the total number of "slots" you are trying to fill

    Return the solution as a list of values.
    """
    solution = [None] * num_slots

    def solve_from(position):
        while True:
            if safe_up_to(solution, position):
                if position >= num_slots-1:
                    # we filled the last slot and everything is okay
                    return solution
                position += 1
                solution[position] =0
            else:
                # Backtrack. Weight have to undo several slots, so ...
                while(solution[position] == highest_value-1):
                    solution[position] =None
                    position -= 1
                if position < 0:
                    break
        # We backtracked beyond the starting point, meaning we could not find 
        # a valid value for the first slot, so no solution
        return None

    # With the iterative solution, I think you have to begin by priming the solution list with the first
    # value in the first slot
    solution[0] =0
    return solve_from(0)


'''
Brute-force search and backtracking (perhaps with branch and bound) are generally where we start learning
about search. But the fun stuff is yet to come. You’ll learn about heuristics, randomization, and performing
parallel searches with multiple agents. There is hill climbing and simulated annealing. And some of these 
problems can be solved with dynamic programming. There are entire programming languages built around
constraint solving. And there are tons of subfields of mathematical optimization.

This stuff is huge in artificial intelligence and machine learning.

'''