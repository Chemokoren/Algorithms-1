"""
(OA) 2021 | Social Network

In a social media website (which is probably Twitter, if you are wondering), there are a total of n 
users. Each user can follow any number of other users. Let f be a matrix of relationship between 
these users, where f[i][j] is either 0 or 1. A 1 indicates that person i (starting from 0) is 
following person j, while 0 means otherwise.

In this question, we assume that each person is following themselves, and following is symmetrical. 
That is, if i follows j, then j follows i. We can then define a "group" of people. A "group" of 
people are people that follow each other, either directly or indirectly. For example, if user 0 
follows user 1, and user 1 follows user 2, user 0 follows 2 indirectly.

Question: How many groups are among these n people?
Parameter

    f: An integer matrix representing the relationship matrix between the users.

Result

    An integer representing the number of groups among these people.

Examples
Example 1:

Input:

f = [

    [1, 1, 0],

    [1, 1, 0],

    [0, 0, 1],

]

Output: 2

Explanation: There are 2 groups: User 0, 1 and user 2. User 0 and 1 are in a group because they 
follow each other.

Constraints

    1 <= n <= 300

"""
from typing import List

def get_network(f: List[List[int]]) -> int:
    return 0

if __name__ == '__main__':
    f = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = get_network(f)
    print(res)
