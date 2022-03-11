"""
(OA) 2021 | Activate Fountain

There is a one-dimensional garden of length n - 1 meters. Every 1 meter there is a sprinkler, and each
sprinkler has a different covering range. The sprinklers are labelled 0 ~ n - 1, indicating that the 
sprinklers are 0 ~ n - 1 meters away from the start of the fountain. The ith sprinkler covers r[i] 
meters of land, meaning that everywhere from i - r[i] meters to i + r[i] meters (inclusive) will be
covered by the sprinkler.

In order to save water, you want to turn on the least amount of sprinklers while still having 
everywhere in the garden be covered by at least one sprinkler. In order to achieve this purpose, find
the minimum amount of sprinkler that you need to turn on.

Parameter

    r: A list of integers indicating the range of the fountains at each position.

Result

    The minimum amount of sprinklers needed to cover the entirety of the garden.

Examples
Example 1:

Input: r = [1, 2, 1]

Output: 1

Explanation: The sprinkler 1 meter away from the start has a range of 2, which means that it can
cover everywhere from -1 meter to 3 meter, which covers the entirety of the garden. It doesn't matter
if the sprinkler exceed the garden range, as long as the garden gets covered.

Constraints

    1 <= n <= 10^5
    0 <= r[i] <= 100
    There is always one way to cover everything in the garden

"""
from typing import List

def min_activations(r: List[int]) -> int:
    return 0

if __name__ == '__main__':
    r = [int(x) for x in input().split()]
    res = min_activations(r)
    print(res)