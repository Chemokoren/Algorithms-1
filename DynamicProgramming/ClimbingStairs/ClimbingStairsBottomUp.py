"""
Given a number of stairs, you need to find the number of distinct ways to climb them. 
You can only climb 1 or 2 steps at a time.
"""
def ClimbingStairsBottomUp(n):
    sub_solution = [-1]*(n + 1)
    sub_solution[1] = 1
    sub_solution[2] = 2

    for i in range(3,n+1):
        sub_solution[i] = sub_solution[i-1] + sub_solution[i-2]
        
    return sub_solution[n]

print(ClimbingStairsBottomUp(4))

"""
Walk through

In this code, we first initialize a list sub_solution with -1 values, where each element i in the list represents the number of ways to climb i stairs. We also initialize sub_solution[0] and sub_solution[1] to 1 since there is only one way to climb 0 or 1 stairs.

Then, we iterate through the remaining steps and calculate the number of ways to climb i stairs using the formula sub_solution[i] = sub_solution[i-1] + sub_solution[i-2]. This is the core of the dynamic programming solution where we build up the solution from the smaller sub-problems.

Finally, we return the number of ways to climb n stairs, which is sub_solution[n].

For example, ClimbingStairsDP(3) returns 3 which means there are 3 distinct ways to climb 3 stairs.
"""