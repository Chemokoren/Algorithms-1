"""
There are a total of n courses a student has to take, numbered from 0 to n-1. A course may have prerequisites. The "depends on" relationship is expressed as a pair of numbers. For example, [0, 1] means you need to take course 1 before taking course 0. Given n and the list of prerequisites, decide if it is possible to take all the courses.

Example 1:

Input: n = 2, prerequisites = [[0, 1]]

Output: true

Explanation: we can take 1 first and then 0.

Example 2:

Input: n = 2, prerequisites = [[0, 1], [1, 0]]

Output: false

Explanation: the two courses depend on each other, there is no way to take them
"""