"""
Train Ride

Recently you've moved to the new city Umbristan working in the government sector. You haven't been 
able to get your driver's license since moving to the city. Therefore, you have to take the subway.
The subway can be denoted by n stations numbered from 1 to n. There are a series of lines in the 
city which consist of train tracks running between 2 different stations. The lines are denoted by a
number from 1 to k where 1 <= k <= n. The Umbristan subway system has a strange fare system. 
When you buy a ticket you can pay any price between 1 to k. Then after purchasing the ticket you can
only ride lines between 1 and the price you paid for the ticket(inclusive).

You having recently moved to the city lack funds and wanting to save as much money as possible, you 
are interested in the minimum price you have to spend in order to make it to your workplace.

You live at station 1 and your workplace is located at station n.

The first input is the number n denoting the number of stations.

The second input is the number k denoting the number of lines.

The third input is a list of triplets where the first 2 values denotes the 2 stations connected and 
the 3rd value is the line it belongs to.

If a path does not exist between your workplace and home, output -1, otherwise output the minimum 
ticket price needed for you to travel to your workplace.

Examples
Example 1:
Input:

n = 5, k = 2, connections = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [2, 4, 2], [1, 5, 2]]
Output:

1
Explanation:

You only need connections on line 1 in order to go from station 1 to station n. Therefore, you only
need to buy a ticket with price 1.
"""

from typing import List

def train_ride(n: int, k: int, connections: List[List[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return 0

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    connections = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = train_ride(n, k, connections)
    print(res)