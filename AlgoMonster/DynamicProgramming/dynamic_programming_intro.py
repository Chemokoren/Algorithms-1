"""
What is Dynamic Programming?

Prerequisite: DFS, backtracking, memoization

Dynamic programming is an algorithmic optimization technique that breaks down a
complicated problem into smaller overlapping subproblems in a recursive manner and use 
solutions to the subproblems to construct solution to the original problem.

Name Origin

"Dynamic programming”, an awfully scary name. What does it even mean?? What’s so “dynamic”
about programming?

The name was invented by Richard Bellman in the 1950s when computers are still decades 
away. So by “programming” he really did NOT mean programming as in coding at a computer. 
Bellman was a mathematician, and what he really meant by programming was “planning” and 
“decision making”.

    Trivia time: according to Wikipedia, Bellman was working at RAND corporation, and it 
    was hard to get mathematical research funding at the time. To disguise the fact that
    he was conducting mathematical research, he phrased his research in a less mathematical
    term “dynamic programming”. “The word dynamic was chosen by Bellman to capture the 
    time-varying aspect of the problems, and because it sounded impressive. 
    The word programming referred to the use of the method to find an optimal program, in 
    the sense of a military schedule for training or logistics.”

So what he really meant was “multistage planning”, a simple concept of solving bigger 
problems using smaller problems while saving results to avoid repeated calculations. 
That sounds awfully familiar, isn’t that memoization? Yes it is. Keep on reading.

Characteristics of Dynamic Programming

A problem is a dynamic programming problem if it satisfy two conditions:

    - The problem can be divided into subproblems, and its optimal solution can be 
    constructed from optimal solutions of the subproblems. In academic terms, this is 
    called optimal substructure

   - The subproblems from 1) overlap.

1. Optimal substructure

Consider the problem of the shortest driving path from San Francisco (SF) to San Diego 
(SD). Since the highway goes through Los Angeles (LA), the problem can be divided into two
subproblems - driving from SF to LA and driving from LA to SD.

In addition, shortest_path(SF, SD) = shortest_path(SF, LA) + shortest_path(LA, SD).
Optimal solution to the problem = combination of optimal solutions of the subproblems.


Now let’s look at an example where the problem does NOT have optimal substructure. 
Consider buying an airline ticket from New York (NYC) to San Francisco (SF). Let’s assume 
there is no direct flight and we have to transit through Chicago (CHI). Even though our 
trip is divided into two parts NYC to CHI and CHI to SF, most often the cheapest ticket 
from NYC to SF != cheapest ticket from NYC to CHI + cheapest ticket from CHI to SF 
because airlines do not normally price multi-leg trips the sum of individual flights to 
maximize profit.

2. Overlapping subproblems

As we have seen in the memoization section, Fibonacci number calculation has a good amount
of repeated computation (overlapping subproblems) whose results can be cached and reused.


If the above two conditions are satisfied, then the problem can be solved with dynamic 
programming.

DP == DFS + memoization

You might have seen posts on coding forum titled “simple DFS solution” and “0.5 sec DP 
solution” for the same problem. The reason is the two methods are equivalent. They are two 
different approaches to DP: one is top-down, the other one is bottom-up.

How to Solve Dynamic Programming Problems?

Top-down: this is basically DFS + memoization as we have seen memoization. We split large
problems and recursively solving smaller subproblems.

Bottom-up: we try to solve subproblems first and then use their solutions to find solutions
to bigger subproblems. This is normally done in a tabular form.

Let’s look at a concrete example.

Fibonacci

Let's revisit the Fibonacci number problem from the memoization section.


Top-down with Memoization

Recall we have a system for backtracking and memoization

    Draw the tree: see the tree above

    Identify states

    What state do we need to know whether we have reached a solution? We need to know the 
    value of n we are computing
    What state do we need to decide which child nodes should be visited next and which 
    ones? There is no extra state we need. We always visit n-1 and n-2.

    DFS + memoization


"""

def fib(n, memo):
    if n in memo:
        return memo[n]

    if n == 0 or n ==1:
        return n
    res = fib(n-1, memo) + fib(n-2, memo)

    memo[n] = res # save in memo before returning
    return res
"""
Bottom up with Tabulation

For the bottom-up dynamic programming, we want to start with subproblems first and work 
our way up to the main problem. This is normally done by filling up a table.

For the Fibonacci problem, we want to fill a one-dimensional table dp where each entry at
index i represents value of the Fibonacci number at index i. The last element of the 
array is the result we want to return.

The order of filling matters because we cannot calculate dp[i] before we filled dp[i - 1]
and dp[i - 2].

dp[i]   0   1   1   2   3   5
i       0   1   2   3   4   5

"""

def fib(n):
    dp=[0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] +dp[i-2])

    return dp[-1]

"""
Subproblems and Recurrence Relation

The formula dp[i] = dp[i - 1] + dp[i - 2] is called the recurrence relation. It is the 
key to solving any dynamic programing problem.

For the Fibonacci number problem, the relation is already given dp[i] = dp[i - 1] + 
dp[i - 2]. We will discuss the patterns of recurrence relation in the next section.

Should I do top-down or bottom-up?

Top-down pros:

    The order of computing subproblems doesn't matter. For bottom-up, we have to fill the
    table in an order such that all the subproblems are solved first. For example, to fill
    dp[8], we have to have filled dp[6] and dp[7] first. For top-down, we can let recursion
    and memoization take care of the subproblems and therefore not worry about the order.
    Easier to reason for partition type of problems (how many ways are there to.., 
    splitting a string into...), just do DFS and add memoization.

Bottom-up pros:

    Easier to reason the time complexity (since it's just the time to fill the table)
    No recursion, and thus no system stack overflow although not a huge concern for normal 
    coding interviews.

From our experiences, deciding on top-down or bottom-up depends on the problem. Some types
of problems are easier to reason and solve with top-down than bottom-up and vice versa. 
We will see a breakdown in the next section.

Greedy Algorithm vs Dynamic Programming

What is a greedy algorithm? As the name would suggest its an algorithm where we essentially
always want to choose the best answer. The main difference between the two is that the 
answer to a dynamic programming problem is not always necessarily the best answer for 
every state. This can be due to other restrictions in the problem statement such that we 
don't always want to pick the best answer. A good way to distinguish between the two is to
figure out a dynamic programming solution and see if you can optimize by always picking 
the best answer for the dynamic programming substates.

For example, consider if you were given a series of interval and you were asked to pick 
the minimum number of intervals required to cover a given length. Let dp[i] denote the 
minimum number of intervals to make an interval of length i. 
Then dp[i] = min(dp[i], dp[i - length[j]] + 1) where length is the array containing the 
interval lengths. We then realize that for our dp state that we should greedily pick the 
longest interval each time if permitted which leads us to our greedy solution. This was a
rather simple example but it may be helpful for more obscure greedy solutions that disguise
as dynamic programming problems.

Divide and Conquer vs Dynamic Programming

Both Divide and Conquer and dynamic programming break the original problem into multiple 
subproblems. The difference is in dynamic programming the subproblems overlap whereas in 
divide and conquer they don't.

Consider Merge Sort, the sub-arrays are sorted and merged but the sub-arrays do not have 
any overlap. Now consider Fibonacci, the green and red nodes in the "overlapping 
subproblems" clearly overlap.

When to use dynamic programming

Mathematically, dynamic programming is an optimization method on one or more sequences 
(e.g. arrays, matrices). So questions asking about optimal way to do something on one or 
more sequences is often a good candidate for dynamic programming.

Signs of dynamic programming:

    -The problem asks for the maximum/longest, minimal/shortest value/cost/profit you can 
   get from doing operations on a sequence.
    -You've tried greedy but it sometimes it gives the wrong solution. This often means 
    you have to consider subproblems for an optimal solution.
    - The problem asks for how many ways there are to do something. This can often be 
    solved by DFS + memoization, i.e. top-down dynamic programming.
    - Partition a string/array into sub-sequences so that certain condition is met. This 
    is often well-suited for top-down dynamic programming.
    - The problems is about optimal way to play a game.

How to Develop Intuition for Dynamic Programming Problems

As you may have noticed, the concept of DP is quite simple - find the overlapping 
subproblems, solve them and use the subproblem solutions to find the solution to the 
original problem. The hard part is to know how to find the recurrence relation. 
The best way to develop an intuition is to get familiar with common patterns. Some classic
examples include longest common subsequence (LCS), 0-1 knapsack, longest increasing 
subsequence (LIS).

Sequence

This is the most common type of DP problem and a good place to get a feel of dynamic
programming. In the recurrence relation,dp[i] normally means max/min/best value for the 
sequence ending at index i.

    House robber - find maximum amount of loot
    Coin change - find minimum amount of coins needed to make up an amount

Grid

This is the 2D version of the sequence DP. dp[i][j] means max/min/best value for matrix 
cell ending at index i, j.

    Robot unique paths - number of ways for robot to move from top left to bottom right
    Min path sum - find path in a grid with minimum cost
    Maximal square - find maximal square of 1s in a grid of 0s and 1s

Dynamic number of subproblems

This is similar to "Sequence DP" except dp[i] depends on a dynamic number of subproblems, 
e.g. dp[i] = max(d[j]..) for j from 0 to i.

    Longest Increasing Subsequence - find the longest increasing subsequence of an array 
    of numbers
    Buy/sell stock with at most K transactions - maximize profit by buying and selling 
    stocks using at most K transaction

Partition

This is a continuation of DFS + memoization problems. These problems are easier to reason 
and solve with a top-down approach. The key to solve these problems is to draw the 
state-space tree and then traverse it.

    Decode ways - how many ways to decode a string
    Word break - partition a word into words in a dictionary
    Triangle - find the smallest sum path to traverse a triangle of numbers from top to
    bottom
    Partition to Equal Sum Subsets - partition a set of numbers into two equal-sum subsets

Interval

The key to solve this type of problem involves finding subproblem defined on an interval
dp[i][j].

    Number of ways to partition a string into palindromes.

Two Sequences

This type of problem has two sequences in their problem statement. dp[i][j] represents the
max/min/best value for the first sequence ending in index i and second sequence ending in
index j.

    Edit distance - find the minimum distance to edit one string to another
    Longest common subsequence - find the longest common subsequence that is common in 
    two sequences

Game theory

This type of problem asks for whether a player can win a decision game. The key to solving
game theory problems is to identify winning state, and formulating a winning state as a 
state that returns a losing state to the opponent

    Coins in a line
    Divisor game
    Stone game

0-1 Knapsack Problem

This problem type has a series of objects and usually asks for the maximum value that can 
be achieved from the objects without achieving a certain weight

    0-1 Knapsack - find the maximum object value we can put in our knapsack without 
    exceeeding the weight
    Perfect Squares - find the smallest amount of perfect squares needed to sum to a 
    particular number

Bitmask

This types of DP problems use bitmasks to reduce factorial complexity (n!) to 2^n by 
encoding the dp state in bitmasks.

    Longest Path in a DAG - find the longest path in a directed acyclic graph.
    Minimum Cost to Visit Every Node in a Graph - find the minimum cost to traverse every
    node in a directed weighted graph


"""