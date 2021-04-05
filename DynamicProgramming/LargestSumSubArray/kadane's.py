# Algorithm doesn't work for all negative numbers.
# It returns 0 if all numbers are negative.

"""
Complexity Analysis
Notice that each element has been visited only once.

Time Complexity = O(n)

Space Complexity = O(1)
"""

def kadene(array):
    max_so_far =0
    max_ending_here =0

    for i in range(len(array)):
        max_ending_here =max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here =0
        if max_so_far < max_ending_here:
            max_so_far =max_ending_here
    return max_so_far

# a = [-2, -3, 4, -1, -2, 1, 5, -3]
# a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
# a = [1, 2, 3, 4, 5]
# a = [1,2,3,4,-5,6]
a =[-2,1,-3,4,-1,2,1,-5,4]

print(kadene(a))