"""

Umbristan | Reverse Disjoint Union Set | Reverse Union Find

You have recently been promoted as the director of infrastructure of Umbristan. 
Congratulations! Our Duke Stack Umbristan has recently ordered the destruction of all the
roads of Umbristan so that new ones can be rebuilt. Our Duke has assigned you, the 
director of infrastructure, an important task. After each road in Umbristan is demolished
he wants to know how many clusters of cities will still be connected after the road is 
destroyed. Two cities are considered connected if there exists a series of roads one can 
take to travel to reach one city from another. A cluster of cities being connected means
that for any 2 cities in the cluster there exists a path between the 2 cities. The input 
will first consist of the number n which is the number of cities numbered from 1 to n. 
Then there will exist a list of roads that represent the road connecting 2 cities is now 
broken. Each road in this list is guaranteed to be a valid existing road. The final result
will be guaranteed to have no roads(since all roads must be destroyed).

Examples
Example 1:
Input: n = 4, breaks = [[1, 2], [2, 3], [3, 4], [1, 4], [2, 4]]
Output: [1, 1, 2, 3, 4]
Explanation:

"""
from typing import List

def umbristan(n: int, breaks: List[List[int]]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    return []

if __name__ == '__main__':
    n = int(input())
    breaks = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = umbristan(n, breaks)
    print(' '.join(map(str, res)))