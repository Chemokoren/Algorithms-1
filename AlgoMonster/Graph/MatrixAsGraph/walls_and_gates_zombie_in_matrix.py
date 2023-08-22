"""
Walls and Gates / Zombie in Matrix

You are given an m by n grid of integers representing a map of a dungeon. In this map:

-1 represents a wall or an obstacle of some kind.
0 represents a gate out of the dungeon.
INF represents empty space.

For this question, let INF be 2^31 -1 == 2147483647, which is the max value of the integer type
in many programming languages.

Venturing into the dungeon is very dangerous, so you would like to know how close you are at 
each point in the dungeon to the exit. Given the map of the dungeon, return the same map, 
but for each empty space, that space is replaced by the number of steps it takes to reach any
exit. If a space cannot reach the exit, that space remains INF.

Note that each step, you can move horizontally or vertically, but you cannot move pass a wall or
an obstacle.

Input

dungeon_map: a matrix of integer representing the dungeon map.

Output

A matrix of integer representing the dungeon map with the addition of distance to an exit for
each empty space.

Example 1:

dungeon_map =[
    [INF, -1,   0, INF],
    [INF, INF, INF, -1],
    [INF, -1,  INF, -1],
    [0,   -1, INF, INF]
]

Output: [ [3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4], ]

Explanation:

Constratins

1 <= n, m<=500


"""
from typing import List

def map_gate_distances(dungeon_map: List[List[int]]) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    return []

if __name__ == '__main__':
    dungeon_map = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = map_gate_distances(dungeon_map)
    for row in res:
        print(' '.join(map(str, row)))

