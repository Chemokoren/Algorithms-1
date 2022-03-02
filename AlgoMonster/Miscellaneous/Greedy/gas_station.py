"""
Gas Station

There are a total of n gas stations along a clockwise, circular route, and for the ith gas station 
(starting from 0), there are gas[i] litre of gas stored.

The distance between the ith gas station and the i + 1th gas station is dist[i].

You have a car, and you would like to travel clockwise starting from any gas station and return to the
same gas station. The car has a sufficiently large gas tank, and for each unit of gas, your car can 
travel a unit distance. Initially, the fuel tank of your car is empty, but you can add fuel from any 
fuel station for as long as that fuel station has fuel left.

You wonder whether you can successfully travel this way. If so, output the index representing the 
starting gas station. Otherwise, output -1. The solution is guaranteed to be unique, if one exists.

Input

    gas: a list of integers representing the gas available for each gas station.
    dist: a list of integers representing the distance between each two adjacent gas stations.

Output

The unique starting gas station to be able to travel once, or -1 if no such station exists.
Examples
Example 1:

Input:

gas = [1, 2, 3, 4, 5]

dist = [3, 4, 5, 1, 2]

Output: 3

Explanation:

Starting from station 3, the car has 4 gas. It travels to the next station spending 1 gas, leaving 
3 gas. Pick up 5 gas, travel to the next station, and leaving 6 gas. For the next three station, 
there is enough fuel to travel to each one and return to the starting point.

Constraints

    1 <= len(gas) == len(dist) <= 10^4
    1 <= gas[i], dist[i] <= 10^4


"""
from typing import List

def starting_station(gas: List[int], dist: List[int]) -> int:
    return 0

if __name__ == '__main__':
    gas = [int(x) for x in input().split()]
    dist = [int(x) for x in input().split()]
    res = starting_station(gas, dist)
    print(res)