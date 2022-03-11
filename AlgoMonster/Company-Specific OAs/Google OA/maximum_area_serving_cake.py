"""
(OA) - Maximum Area Serving Cake

Given an array of positive integers representing the radii of circular pizzas and the number of guests
at a movie party, return the size of the largest piece of pizza (rounded to 4 decimal places) that can
be cut so that every guest gets a slice of pizza with the same size.
It is not possible that a single slice has some part of one pizza and some part of another pizza, 
and each guest gets only once slice of pizza.

Constraints:

    1 <= number of pizzas <= 1000
    1 <= radii[i] <= 1000
    1 <= number of guests <= 1000

Examples
Example 1:
Input:

radii = [1, 1, 1, 2, 2, 3]

guests = 6
Output: 7.0686
Explanation:

You can divide the pizza with a radius of 3 by 4: area 28.743 / 4 = 7.0686 to get 4 slices. Get the 
remaining 2 slices from the pizzas wth radius 2 because they have an area larger than 7.0686.

Example 2:
Input:

radii = [4, 3, 3]

guests = 3
Output: 28.2743
Example 3:
Input:

radii = [6, 7]

guests = 12
Output: 21.9911

"""

from typing import List

def get_max_pizza_slice_size(radii: List[int], guests: int) -> float:
    return 0.0

if __name__ == '__main__':
    radii = [int(x) for x in input().split()]
    guests = int(input())
    res = get_max_pizza_slice_size(radii, guests)
    print(f'{res:.4f}')