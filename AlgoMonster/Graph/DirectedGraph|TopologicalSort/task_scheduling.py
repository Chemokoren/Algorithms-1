"""
Task Scheduling

For this problem given a list of tasks and a list of requirements, compute a sequence of tasks 
that can be perfomd, such that we complete every task once we satisfy all the requirements.

Each requirement will be in the form of a list[a,b], where tasks a needs to be completed first
before task b can be completed, There is a guaranteed solution.

Example 1

Input:

tasks = ["a", "b", "c", "d"]

requirements = [["a", "b"], ["c", "b"], ["b", "d"]]


Output: ["a", "c", "b", "d"]

Solution:

This is the same problem as Course Schedule. This time let's solve it with Kahn's algorithm.

Time complexity: O(n+m)

The time complexity is equal to n the number of nodes in the graph plus m the number of edges
in the graph. This is because we have to go through every connection and node once when we
sort the graph.


"""

from typing import List

def task_scheduling(tasks: List[str], requirements: List[List[str]]) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    return []

if __name__ == '__main__':
    tasks = input().split()
    requirements = [input().split() for _ in range(int(input()))]
    res = task_scheduling(tasks, requirements)
    if len(res) != len(tasks):
        print(f'output size {len(res)} does not match input size {len(tasks)}')
        exit()
    indices = {task: i for i, task in enumerate(res)}
    for req in requirements:
        for task in req:
            if task not in indices:
                print(f"'{task}' is not in output")
                exit()
        a, b = req
        if indices[a] >= indices[b]:
            print(f"'{a}' is not before '{b}'")
            exit()
    print('ok')