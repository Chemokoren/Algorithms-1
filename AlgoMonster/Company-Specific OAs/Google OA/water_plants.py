"""
(OA) - Water Plants

You work in a restaurant and is tasked to fill some bowls with soup in a big stock pot. The bowls are 
positioned in a row, and you are going to fill the bowls with a large ladle.
To avoid mistakes, you have decided to:

    Fill the bowls from left to right;
    Fill each bowl if you have enough soup for it, otherwise refill the ladle with more soup;
    Fill each bowl in one go without taking a break to refill the ladle. This means that you may 
    sometimes have to refill your ladle before or after filling a bowl, even though the ladle isn't
    completely empty.

You start at the stock pot, which is positioned one step before the first bowl. How many steps will 
you take to finish filling all the bowls in the row? The bowls are positioned one step apart from 
each other.

Given an array of n integers representing the amount of soup required for each bowl and the ladle 
capacity, return the number of steps needed to fill all the bowls.

Constraints

    1 <= n <= 1000
    1 <= bowls[i] <= 10^6
    1 <= capacity <= 10^9
    The ladle is large enough to fully fill any bowl

Examples

Example 1:
Input:

bowls = [2, 4, 5, 1, 2]

capacity = 6
Output: 17

Explanation:

First, you fill bowl 0 and 1 - 2 steps. Then, you go back and refill - 2 steps - and fill bowl 
2 and 3 - 4 steps. You go back and refill - 4 steps - and fill bowl 4 - 5 steps. So you take a total 
of 2 + 2 + 4 + 4 + 5 = 17 steps.

"""

from typing import List

def min_steps(bowls: List[int], capacity: int) -> int:
    return 0

if __name__ == '__main__':
    bowls = [int(x) for x in input().split()]
    capacity = int(input())
    res = min_steps(bowls, capacity)
    print(res)
