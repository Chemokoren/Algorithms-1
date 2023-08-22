"""
Train Ride II

    Prereq: Train Ride

You have carefully planned out the minimum ticket price you have to pay but you forgot one important
fact, are you going to make it to work on time? After considering this, you hurry to change your 
ticket plans as now you need to not only buy the cheapest ticket but also make sure you get to work
on time. You quickly whip out your map and now mark each connection in the subway with a time, the 
time it takes to ride between those 2 stations.

The new input format is as follows,

The first input still denotes n the number of stations.

The second input still denotes k the number of lines.

The third input now denotes 't' the time that you need to be at station n by starting at station 1 
in minutes.

The fourth linput now has the connections except now there are four values. First 2 values contains 
the connection, the 3rd value is the line number it belongs, the 4th value is the time needed to 
traverse this connection in minutes.

Output the lowest ticket cost such that you can make it to work on time.

Output -1 if no such ticket can be bought to get you to work on time.

Examples
Example 1:
Input:

n = 5, k = 2, t = 6, connections = [[1, 2, 1, 1], [2, 3, 1, 2], [3, 4, 1, 3], [4, 5, 1, 4], [1, 5, 2, 6]]
Output:

2
Explanation:

If you only use the connections on line 1 there exists a path to your workplace but you will be late
to work. The total time would be 1 + 2 + 3 + 4 = 10 minutes but you only have 6 minutes. 
By buying a ticket with price 2 you can take the connection [1, 5, 2, 6] which will take only 
6 minutes and therefore allow you to arrive at work on time.

"""
from typing import List

def train_ride_2(n: int, k: int, t: int, connections: List[List[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return 0

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    t = int(input())
    connections = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = train_ride_2(n, k, t, connections)
    print(res)
