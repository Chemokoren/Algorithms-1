"""

"""
def ClimbingStairsTopDown(n):
    sub_solution = [-1]*(n + 1)
    return ClimbingStairsTopDownHelper(n, sub_solution)

def ClimbingStairsTopDownHelper(n, sub_solution):
    if n == 0 or n == 1:
        return 1
    
    if sub_solution[n] != -1:
        return sub_solution[n]
    
    sub_solution[n] = ClimbingStairsTopDownHelper(n-1, sub_solution) + ClimbingStairsTopDownHelper(n-2, sub_solution)
    
    return sub_solution[n]

print(ClimbingStairsTopDown(3))

"""
Code Break-Down
---------------

In this code, we first initialize a list sub_solution with -1 values, where each element i in the list represents the number of ways to climb i stairs. We then call a helper function ClimbingStairsTopDownHelper which recursively computes the number of ways to climb n stairs, using the top-down dynamic programming approach.

The helper function takes two parameters: n which is the number of stairs to climb, and sub_solution which is the list containing the precomputed solutions. The first two base cases are handled when n is 0 or 1, which return 1 since there is only one way to climb 0 or 1 stairs.

If the solution for n is already precomputed in sub_solution, we simply return it. Otherwise, we compute it by recursively calling the ClimbingStairsTopDownHelper function for n-1 and n-2, and add them together. We then store this result in sub_solution[n] for future use and return it.

Finally, we call ClimbingStairsTopDown function with n as the input parameter and it returns the number of ways to climb n stairs.

For example, ClimbingStairsTopDown(3) returns 3 which means there are 3 distinct ways to climb 3 stairs.
ChatGPT Mar 23 Version. Free Research Preview. ChatGPT may produce inaccurate information about people, places, or facts
"""
