"""
0-1 Knapsack Problem | Dynamic Programming

For this article we discuss a classic dynamic programming problem which is 0-1 knapsack.
The problem we are interested in is given a series of objects with a weight and value and
a knapsack that can carry a set amount of weight, what is the maximum object value we 
can put in our knapsack without exceeeding the weight.

Input

    weights: an array of integers that denote the weights of objects
    values: an array of integers that denote the values of objects
    max_weight: the maximum weight in the knapsack

Output

the maximum value in the knapsack
Examples
Example 1:

Input:

weights = [3, 4, 7]

values = [4, 5, 8]

max_weight = 7

Output: 5

Explanation:

We have a knapsack of max limit 7 with 3 objects of weight-value pairs of 
[3,4],[4,5],[7,8] then the maximal value we can achieve is using the first 2 objects to 
obtain value 4 + 5 = 9.

The other possibilities would all be only 1 object in our knapsack which would only yield
values 4, 5, and 9.


Solution
Brute force

A brute force method would enumerate all the possibilities such that for every object we 
try including it into our knapsack which would result in time complexity O(2^n) where n
is the total number of objects. This is due to the fact that one would have to use some
sort of recursive function and try every object combination and checking which one 
contains the maximum value.

2D Dynamic Programming

For this problem, we introduce a classic dynamic programming solution which has time 
complexity O(n * w) where w is the target weight. The intuition for this DP is to maintain 
a 2-D array where 1 dimension maintains the current object we are considering and another
dimension considers the weight that we use up.

In other words, dp[i][j] denotes the maximal value obtainable using the first i objects 
and only taking up j weight. We then have 
dp[i][j] = max(dp[i][j], dp[i - 1][j - weight[i]] + value[i]). Evidently in most cases a 
time complexity of O(n * w) would be better then O(2^n) except for cases where n is 
sufficiently small and/or w is sufficiently large.

2D to 1D Optimization

We have discussed how to do knapsack using 2-D DP but now we discuss how we can optimize
this into 1-D DP. We realize that for the first dimension keeping track of the objects 
that we only ever use the previous row so therefore, we can simply remove that dimension 
from out DP without consequence.

The basic idea is to maintain a 1-D array that keeps track of the maximal value we can 
get for a certain amount of weight. We can loop from the largest value to the smallest 
value to ensure we do not use a given object twice. Looping backwards ensures we only 
ever use DP values from the previous row which is equivalent to the 2-D DP except we can
save some memory.

The dp state can then be calculated using
dp[j] = max(dp[j], dp[j - weight[i]] + value[i]). We first set each array element to be
-1 which means we have not reached that weight. If we have not reached that weight we 
should skip it and make sure to not compute the value for that index.

Here is a graphic to demonstrate this idea. Note that when a weight is smaller than the 
array index we stop considering the index as it means our weight is greater than the 
current capacity of the knapsack.

"""

from typing import List

def knapsack(weights: List[int], values: List[int], max_weight: int) -> int:
    # initialize the array and set values to -1 except for index 0
    dp =[-1] * (max_weight +1)
    dp[0] = 0

    # loop through the objects
    for i in range(len(weights)):
        # loop through the dp indexes from largest value to smallest one
        for j in range(max_weight,weights[i]-1, -1):
            # check if we have  reached the weight value before
            if dp[j -weights[i]] != -1:
                dp[j] =max(dp[j], dp[j -weights[i]] + values[i])
    return max(dp)

if __name__ == '__main__':
    # weights = [int(x) for x in input().split()]
    # values  = [int(x) for x in input().split()]

    weights = [3, 4, 7]
    values  = [4, 5, 8]
    max_weight = 7

    # max_weight = int(input())
    res = knapsack(weights, values, max_weight)
    print(res)

"""
0-1 Knapsack variants

Hopefully, this should give you a good idea of how the algorithm works. A trick that may 
be useful to know is that there are more than one method to use dynamic programming for 
this problem. We discussed here achieving the maximum value for a given weight but we 
similarly could have done the minimum weight achievable for a particular value instead 
to achieve similar results.

0-1 Knapsack and Coin Change, what's the connection?

Some of you may have realized the similarities bore to the coin change problem(Coin Change)
. In fact the coin change can be thought of as a variant of the 0-1 Knapsack Problem. 
If we have dp[i] instead of representing the maximum value achievable for a certain weight
we change it to represent the minimum weight required to achieve a certain value and 
change all the weights to 1 we now have the solution to the coin change problem. 
Our new dp transition is then simply dp[i] = min(dp[i], dp[i - values[j]] + 1). 
The implementation specifics is left as an exercise to the reader and should be reasonably
similar to the 0-1 Knapsack Problem implementation. 
Remember that you can use a coin multiple times which is another difference betweeen coin
change and the 0-1 knapsack problem. Now onto the implementation,

"""

def knapsack(weights, values, target):

    # initialize the array and set values to -1 except for index 0
    dp = [-1] * (target + 1)
    dp[0] = 0

    # loop through the objects
    for i in range(len(weights)):

        # loop through the dp indexes from largest value to smaller one
        for j in range(target, weights[i]-1, -1):
            
            # check if we have reached the weight value before
            if dp[j -weights[i]] != -1:
                dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[target]