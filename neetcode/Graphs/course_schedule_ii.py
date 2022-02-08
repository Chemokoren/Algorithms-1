from typing import List
"""
Course Schedule II

There are a total of n courses you have to take labelled from 0 to n-1.

Some courses may have prerequisites, for example if prerequisites[i] =[ai, bi] this means
you must take the course bi before the course ai.

Given the toal number of courses numCourses and a list of the prerequisite pairs, return 
the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. If it is impossible to finish all 
courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites =[[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have
finished course 0. So the correct course order is [0,1]

This algorithm teaches you topological sort
Time: O(E+V) or O(P+n) where p is the prerequisites and n the number of courses
"""

class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]])->List[int]:

        # build adjacency list of prereqs
        prereq ={c:[] for c in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        # a course has 3 possible states:
        # visited -> crs has been added to output
        # visiting -> crs not added to ouput, but added to cycle
        # unvisited -> crs not added to output or cycle
        output = []
        visit, cycle =set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
