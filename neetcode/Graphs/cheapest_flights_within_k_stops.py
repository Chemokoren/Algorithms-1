from typing import List
"""
Cheapest Flights within K Stops

There are n cities connected by some number of flights. You are given an array 
flights[i] =[fromi, toi, pricei] indicates that there is a flight from city fromi to city toi
with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst
with at most k stops. If there is no such route return -1.

Example 1:

                        0
                       / \
                      /   \
                100  /     \ 500
                    /       \  
                   /________> \
               V  1    100    2 V

Input: n =3, flights =[[0,1,100],[1,2,100],[0,2,500]], src =0, dst =2, k =1
Output: 200
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in 
the picture

Bellman -Ford algorithm
time: O(E.K)  because the loop is going to run k times and every time we loop we're going to
be iterating though every single edge in the graph
"""
class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int,k:int)->int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights: # s=source, d = destination, p = price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s]+p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]
