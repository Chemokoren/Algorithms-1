"""
This problem is similar to Task Scheduling. The primary difference is now we assign times to tasks and we ask for the minimum amount of time to complete all tasks. There will be an extra times array such that times[i] indicates the time required to complete task[i]. You have also invited all your friends to help complete your tasks so you can work on any amount of tasks at a given time. Be sure to remember that task a must be completed before task b so despite your unlimited manpower your friends must still wait for task a to complete before starting task b.

There is guaranteed to be a solution.
Examples
Example 1
Input:

tasks = ["a", "b", "c", "d"]

times = [1, 1, 2, 1]

requirements = [["a", "b"], ["c", "b"], ["b", "d"]]

Output: 4


Solution

Since this problem is similar to Task Scheduling, we still use the template for Kahn's Algorithm
. The basic idea is to perform a topological sort except we also keep track of the largest 
amount of time expended for a particular path through the graph. 

The time it takes to complete a task is inhibited by the most time-consuming task in its 
dependencies. We make sure that we update every node such that it contains the maximum time 
needed to complete every prerequisite task. 

We then make sure to update every children such that it contains the distance as the final 
answer is essentially the maximal path through the graph.

Time Complexity: O(n+m)

The time complexity is equal to n the number of nodes in the graph plus m the number of edges in the graph. This is because we have to go through every connection and node once when we sort the graph.
"""