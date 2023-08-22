"""
(OA) 2021 | Parking Dilemma

You are in charge of a linear parking lot. There are n cars parked permanently in this parking lot. 
The ith car occupies the pos[i]th parking slot. You feel bad for the car owners of these cars, so you
decided to build a roof to cover k cars from the rain. Why build just a singular roof and why only 
cover k cars instead of every car? You didn't get paid enough for this.

To save costs, you decide to minimize the size of the roof while still making sure you cover at least 
k cars. Given the positions of these n cars and k, find the minimum number of parking slots this roof
should cover.

Parameters

    pos: A list of integers representing the positions of the cars.
    k: The minimum amount of cars your roof should cover.

Result

    The minimum number of parking slots the roof needs to cover.

Examples
Example 1:

Input: pos = [2, 10, 8, 17], k = 3

Output: 9

Explanation: You need a roof spanning from 2 to 10 to cover the first three cars.
Constraints

    1 <= n <= 10^5
    1 <= k <= n
    1 <= pos[i] <= 10^9

"""

from typing import List

def min_roof_size(pos: List[int], k: int) -> int:
    return 0

if __name__ == '__main__':
    pos = [int(x) for x in input().split()]
    k = int(input())
    res = min_roof_size(pos, k)
    print(res)