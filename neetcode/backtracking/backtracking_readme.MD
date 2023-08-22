
Question:

Write a program which returns all distinct non-attacking placements of n queens on an nxn chessboard, where n is an input to the program.

A non-attacking placement of queens is one in which no two queens are in the same row, column, or diagonal.

We will use backtracking to solve this problem.

This can be one of the most confusing topics that you have to learn, expecially if you have shaky foundations in thinking recursively and calculating harder complexities.

Other Well Know Backtracking Problems:
-) Generate The Powerset of An Array (Subsets)
-) Generate All Permutations of A String

Backtracking/Recursion is about following a path to a base case...our target...our answer. If a certain path ends up not meeting our constraints we will backtrack to an earlier state and try something else from there.

The 3 Keys To Backtracking Problems:

Our Choice
----------


-) What choice are we making at each call of the function
-) RECURSION REPRESENTS A DECISION.
-) RECURSION REPRESENTS A CHOICE & its associated state
-) Each function call represents a state. From that state decisions can be made.

Our Constraints
---------------


-) What tells us to stop following a certain path that we are searching on?
-) Have we exhausted all possibilities?

Our Goal
--------

-) What is our target?
-) What are we trying to find?
-) These will craft our base cases.

Example: You lost your keys. Where do you go? The most recent place you were. Then the most recent place from there. And so on. Then you go to somewhere else...eventually you find your keys or give up the search.

So for this problem:
--------------------

1) Our Choice - Where to place a queen
2) Our Constraints - The placement must be non-attacking
3) Our Goal - Place n-queens on the chess board

Time and Space Complexities:

Complexity for this problem is tricky.

The time complexity is lower bounded by the number of non-attacking placements because we will be making at least the amount of function calls that it takes to find those placements (meaning we don't even include work done in each call).

No exact form is known for this lower bound as a function of n, but it is conjectured to tend towards n! / (c ^ n) (where c ≈ 2.54) which is super-exponential.

Super exponential growth forms a "J-curve" that grows much faster than exponential functions.

RECURSION REPRESENTS A DECISION
-------------------------------

Whether this is a tree or a linked list, etc. When thinking recursively, our function sets forth rules that allows the function to make decisions based on state passed into it

All backtracking is about returning to previous decision points and explore another path that hasn't been taken yet to see if it yields an answer.


meanings:
---------

conjecture: form an opinion or supposition about (something) on the basis of incomplete information.