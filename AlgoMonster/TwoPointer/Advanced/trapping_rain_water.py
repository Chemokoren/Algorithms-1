"""
Trapping Rain Water

Given a list of non-negative integers representing elevations of columns, and assuming 
each column is of equal width of 1, find how much water is trapped in the columns after
a rain. Left and right boundaries outside of the columns have 0 elevations.

Input: [3, 2, 1, 2, 2, 3, 2] Output: 5

"""

from typing import List

def trapping_rain_water(elevations: List[int]) -> int: 
    possible_trapped = 0 
    total_trapped = 0 
    curr_highest = -float('inf')

    for e in elevations:
        if e >= curr_highest:
            curr_highest = e
            total_trapped += possible_trapped
        else:
            possible_trapped += curr_highest - e
    return total_trapped

input_vals= [3, 2, 1, 2, 2, 3, 2]

print(trapping_rain_water(input_vals))