from typing import List
"""
Course Schedule - Graph Adjacency List 

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1

Some Courses may have prerequisites, for example to take course 0 you have to first take
course 1 which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you
to finish all courses?

Example 1:

Input: numCourses =2, prerequisites =[[1,0]]
Output: True

Explanation: There are a total of 2 courses to take. To take course 1 you shoud have 
finished course 0. So it is possible.

Example 2: n=5
prereq =[[0,1],[0,2],[1,3],[1,4],[3,4]]
Output: = True

crs         pre
0           [1,2]
1           [3,4]
2           []
3           [4]
4           []

O(n+p) where n is the number of nodes and p the number of prerequisites

Example 3

        0 ---> 1---> 2--->0

Premap

crs     pre
0       [1]
1       [2]
2       [0]

VisitSet
0
1
2
Output: False


"""
class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]])->bool:
        preMap ={i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet = all courses along the curr DFS path
        visitSet =set()

        def dfs(crs):

            if crs in visitSet:
                return False

            if preMap[crs] ==[]:
                return True

            visitSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False

            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True