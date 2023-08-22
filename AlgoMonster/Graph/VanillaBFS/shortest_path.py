"""
Shortest Path Between A and B

Given an(unweighted) graph, return the length of the shortest path between two nodes A and B.

Input:

                        0
                       / \
                      1 _ 2
                     /
                    3 

graph: {
    0:[1,2],
    1:[0,2,3],
    2:[0,1]
    3:[1]
}
A:0
B:3

Output: 2
"""
def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    return 0

if __name__ == '__main__':
    graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    a = int(input())
    b = int(input())
    res = shortest_path(graph, a, b)
    print(res)