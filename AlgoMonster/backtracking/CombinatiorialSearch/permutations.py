"""
Permutations

-Given a string of unique letters, find all of its distinct permutations.

Input

letters: a string of unique letters

Output

All of its distinct permutations

Example 1:

input:

letters =`abc`

Output: ````abc acb bac bca cab cba

Solution
--------

Intuition
classic combinatorial search problem, let's apply the 3-step system from backtracking template.

1. Identify States
What state do we  need to know whether we have reached a solution(and using it to construct
a solution if the problem asks for it).
1. We need a state to keep track of the list of letters we have chosen for the current permutation
What state do we need to decide which child nodes should be visited next and which ones should 
be pruned.
2. We have to know what are the letters left that we can still use (since each letter can only be
used once).

2. Draw the State-space Tree


                                0
                     /          |        \
                    [a]        [b]       [c]
                  b/ \c      a / \c     a/  \b
            [a,b]   [a,c] [b,a]  [b,c] [c,a] [c,b]
             |      |       |       |      |      |
            [a,b,c][a,c,b] [b,a,c] [b,c,a][c,a,b] [c,b,a]

3. DFS on the State-space tree
Using the backtracking template as basis, we add the two states we identified in step 1:

1. A list to represent permutation constructed so far, path
2. A list to record which letters are already used, used, used[i] == true means ith letter in the
origin list has been used.
Time Complexity: O(n!)
This is because we have n letters to choose from the n-1 and so on therefore n*(n-1) *(n-2)* ... *1


N/B
Notice how similar the solution is to Ternary Tree Paths. The difference is we have a new 
constraint "number of letters left" while deciding which subtree goes down to.

Note on deep copy
In the exit logic of the above solution, we append a deep copy of path res.append(path[:]). This
creates a new list with elements being the same as current elements of path. Consider what 
happens if we don't make the deep copy:

res =[]
path =[]
for i in range(3):
    path.append(i)
    res.append(path)
print(res)

[[0, 1, 2], [0, 1, 2], [0, 1, 2]]

We get same copy three times! Because append(path) actually appends a reference (memory address),
we actually appended the same list three times. path.append(i) mutates the list and affects
all references to that list. To fix this, we create a new list before we append.
"""

from typing import List

def permutations(letters):
    def dfs(path, used, res):
        if len(path) == len(letters):
            res.append(''.join(path))
            return
        for i, letter in enumerate(letters):
            # skip used letters
            if used[i]:
                continue
            # add letter to permutation, mark letter as used
            path.append(letter)
            used[i]= True
            dfs(path, used, res)
            #remove letter from permutation, mark letter as unused
            path.pop()
            used[i] =False

    res =[]
    dfs([], [False] *len(letters), res)
    return res

if __name__=='__main__':
    # letters = input()
    letters ='abc'
    res = permutations(letters)
    for line in res:
        print(line)
