"""

Train Ride III

    Prereq: Train Ride II

It's been a month since you started working in Umbristan and all is going well. Like any developed 
nation Umbristan has been dabbling in new technologies and recently unveiled its newest invention 
the teleporter! The company heading the technology has also announced the locations where the 
teleporters will be placed. Some places will be at existing train stations, some at entirely new 
locations perhaps not serviceable by train. The company is charging a flat fare for use of any 
teleporter within one day so after the fee is paid you are free to use the teleporters as much as 
you want. The only disadvantage is that the teleporters only allow you to move to other teleporters.
The teleporter company has also worked with the train company to place the teleporters such that it
takes no time to move between trains and teleporters for the teleporters located at train stations.
Another problem is that teleporters also have their own train station "lines". That is teleporters 
are given a numerical ID such that they can only teleport to other teleporters with the same ID. 
The teleporter company is still a start-up and trying to save money so each location has a maximum 
of 1 teleporter. The benefit is that this new technology may be able to improve your daily commute. 
You go back to the trusty map you drew up for Train Ride II and get to work planning your new 
transit route. Can you once again figure out the minimum price needed to get to your workplace on 
time?

The new input format is as follows,

The first line still denotes n the total number of teleporter locations and train stations. A 
teleporter can be located at a train station and is treated as 1 location.

The second line still denotes k the number of lines.

The third line still denotes 't' the time that you need to be at station n by starting at station 1 
in minutes.

The fourth line now contains p the fare needed to use the teleporter for the day

The fifth line now has the connections except now there are four values. First 2 values contains the
connection, the 3rd value if the line number it belongs, the 4th value is the time needed to 
traverse this connection in minutes.

The sixth line now has a list of pairs that contains the teleporters. Each teleporter is denoted by 
the first value which is the location it is location at, and the second value which is its numerical
ID indicating which teleporters it is connected to.

Output the minimum amount of money you need to spend such that you can make it to work on time.

Output -1 if no amount of money spend can get you to work on time.

Author's note: This question is likely too complicated to be asked in an actual interview but serves
as an interesting thought exercise. In some ways, this can overprepare you for interviews which is 
a lot better than being underprepared so there is some value in attempting this question.

Feel free however to skip this question if your primary goal is to get questions similar to those in
an interview or online assessment.

Examples
Example 1:
Input:

n = 5, k = 2, t = 6, p = 2, connections = [[1, 2, 1, 1], [2, 3, 1, 2], [3, 4, 1, 3], [4, 5, 1, 4], [1, 5, 2, 7]], teleporters = [[1, 1], [5, 1], [2, 2]]
Output:

2
Explanation:

Now there doesn't exist a way to use the trains to get to work on time but if we pay a fare of 2 we 
gain access to the teleporters and can get to work instantly.

"""

from typing import List

def train_ride_3(n: int, k: int, t: int, p: int, connections: List[List[int]], teleporter: List[List[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return 0

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    t = int(input())
    p = int(input())
    connections = [[int(x) for x in input().split()] for _ in range(int(input()))]
    teleporter = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = train_ride_3(n, k, t, p, connections, teleporter)
    print(res)
