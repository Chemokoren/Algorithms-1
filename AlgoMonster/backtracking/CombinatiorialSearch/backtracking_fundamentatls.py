"""
Backtracking Template

Combinatorial search problems

Combinatorial search problems involve finding grouping and assignments of objects that satisfy
certain conditions. Finding all permutations/subsets, solving sudoku, and 8-queens are classic
combinatorial problems.

Permutations

It's important to review basic high school combinatorics to get an intuition for combinatorial 
problems.
Permutation means arranging things with an order. For example, permulations of [1,2] are [1,2]
and [2,1]. Permutations are best visualized with trees.

                                0
                     /          |        \
                    [a]        [b]       [c]
                  b/ \c      a / \c     a/  \b
            [a,b]   [a,c] [b,a]  [b,c] [c,a] [c,b]
             |      |       |       |      |      |
            [a,b,c][a,c,b] [b,a,c] [b,c,a][c,a,b] [c,b,a]


The number of permutations is given by n! The way to think about permutation is to imagine you
have a bag of 3 letters. Initially, you have 3 letter to choose from, you pick one out of the 
bag, now you are left with 2 letters, you pick again and now there's only 1 letter. The number
of choices is 3*2*1 = 6(hence we have 6 leaf nodes in the above tree).

Complexity
The complexity of combinatorial problems often grows rapidly with the size of the problem. For
example, as we have seen the number of permutations of 3 objects is only 6. However, the number of 
permutations of 10 objects is about 3million. The number of permutations of 11 objects is about
40 million. The rapid growth of solution space with even a small increase in problem size is
called combinatorial explosion.

Combinatorial search == DFS on tree
In combinatorial search problems, search space is in the shape of a tree. The tree that represents
all the possible states is called State-space Tree.

Each node of the state-space tree represents a state we can reach in a combinatorial search(by
 doing a particular combination). Leaf nodes are the solutions to the problem (permutations in
 the above example).

 Combinatorial search problems boil down to DFS/backtracking on the state-space tree.
 Since the search space can be quite large, we often have to "prune" the tree, i.e. discard branches.

 Three steps to conquer combinatorial search problems
 We summarized a three-step system to solve combinatorial search problems:

 1. Identify the state(s)
 2. Draw the state-space tree.
 3. DFS/backtrack on the state-space tree.

 In step 1, we want to answer the following questions to identify the states:
 1. What state do we need to know whether we have reached a solution(and using it to construct 
 a solution if the problem asks for it). In the above permutation example, we need to keep track
  of the letters we have already selected when we do DFS.
2. What state do we need to decide which child nodes should be visitied next and which ones should 
be pruned. In the above permutation example, we have to know what are the letters left that we
can still use(since each letter can only be used once).

Draw the tree, draw the tree, draw the tree!!!
For step 2, you want to draw the tree (on a piece of paper if you have one). A small test case 
that's big enough to reach one solution(leaf node).

We can't strees how important this is. Once you draw the tree, the rest of the work becomes
easier -simply traverse the tree depth-first.

For step 3, apply the following backtracking template.

function dfs(node, state):

    if state is a solution:

        report(state) # e.g. add state to final result list

        return


    for child in children:

        if child is a part of a potential solution:

            state.add(child) # make move

            dfs(child, state)

            state.remove(child) # backtrack

"""
