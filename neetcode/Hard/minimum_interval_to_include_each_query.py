"""
Minimum interval to include Each Query

You are given a 2D integer array intervals, where intervals[i] =[lefti, righti] describes the
ith interval starting at lefti and ending at righti (inclusive). The size of an interval is
defined as the number of integers it contains, or more formally righti - lefti + 1

You are also given an integer array queries. The answer to the jth query is the size of
the smallest interval i such that lefti  <= queries[j] <= righti. If no such interval exists,
the answer is -1

Return an array containing the answers to the queries.

Example 1:
Input: intervals =[[1,4], [2,4],[3,6],[4,4]], queries =[2,3,4,5]
Output: [3,3,1,4]

Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2.
The answer is 4 -2 + 1 =3
- Query = 3: The interval [2,4] is the smallest interval containing 3.
The answer is 4 - 2 + 1 = 3.
- Query = 4 : The interval [4,4] is the smallest interval containing 4.
O(nlogn+qlogq)
"""
from typing import List
import heapq

# O(nlogn + qlogq) where  n is the length of the intervals and q is the length of the queries
# because the main time complexity is coming from the fact that we are sorting the inputs
class Solution:

    def minInterval(self, intervals: List[List[int]], queries: List[int])->List[int]:
        intervals.sort()

        minHeap =[]
        res, i ={}, 0

        for q in sorted(queries): # creating a copy of the queries and not modifying it
            while i < len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]
                heapq.heappush(minHeap, (r-1 +1, r))
                i +=1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] =minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]

intervals, queries =[[1,4], [2,4],[3,6],[4,4]], [2,3,4,5]
sol = Solution()
print(sol.minInterval(intervals,queries))