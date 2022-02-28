"""
Russian Doll Envelopes

You have a list of envelopes, who each have an integer width and height. An envelope can fit into another envelope if and only if the first envelope's width and height is smaller than the other envelope's width and height (you cannot rotate either envelopes).

Given a list of envelopes, find the maximum number of envelopes that you can fit inside one another like a Russian Doll.
Input

    envelopes: a list of integer pairings representing the envelopes. For each pair, the first integer represents the width, and the second integer represents the height.

Output

The number representing the max envelope layers.
Examples
Example 1:

Input:

envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]

Output: 3

Explanation:

[2, 3] goes inside [5, 4], which goes inside [6, 7]
Constraints

    1 <= len(envelopes) <= 5000
    1 <= width[i], height[i] <= 10^4


"""

from typing import List

def max_layers(envelopes: List[List[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return 0

if __name__ == '__main__':
    envelopes = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = max_layers(envelopes)
    print(res)