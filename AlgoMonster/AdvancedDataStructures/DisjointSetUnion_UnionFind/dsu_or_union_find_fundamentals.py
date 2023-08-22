"""
Union Find | Disjoint Set Union Data Structure Introduction

    Prereq: Depth First Search Review

Once we have a strong grasp of recursion and Depth First Search we now introduce Disjoint 
Set Union (DSU).

For this data structure we are motivated by the following problem. Suppose we have sets 
of elements and we are asked to check if a certain element belongs to a particular set. 
In addition, we want to have our data structure support updates as well through merging 
two sets into one set. One might think to use a list of hashsets in order to accomplish 
this but our end goal is a data structure that can handle the merge and query operations 
both in effectively O(1) time, the merge operation will take O(n) time as we must add 
each element individually. Therefore, we support the following operations

    We want to be able to query for the Set ID of a given node (find operation)
    We want to merge two disjoint sets into one set (union operation)

We can imagine the disjoint set data structure as a series of trees such that a particular
element within a tree belongs solely to that set and no other set. 

The following graphic illustrates this idea.

            0                       4
           / \                     /
          1   2                   5  
           \
            3

Now what do we mean by set ID and elements. The elements are the particular nodes of the 
tree that belong to that set and we nominate a particular node to be the parent of all the
nodes which will act as an identifier. 

We know that if two nodes share this same parent they must therefore belong to the same 
set. Furthermore, if they don’t share the same parent they don’t belong in the same set. 
In this example we have Set ID 0 and 4 which means nodes 0 and 4 act as the parents of the
set. We can accomplish this with a singular Hash Map where key i in the Hash Map 
represents node i’s parent node. 
Initially, we set every node's parent to itself as every node is in a set by itself. 
We can then merge two sets by setting one node's parent to the other node's parent.
We can find what the Set ID node is by recursively moving up the chain of parents to find
the parent which points back to itself. The following code accomplishes a Union operation 
in O(1) and a Find operation that has best case O(1), average case O(log(n)) 
since we have a randomized trees which have average depth O(log(n)) and a worst case of 
O(n) for a maximum depth tree.


"""

class UnionFind:

    # initialize the data structure using a HashMap
    def __init__(self):
        self.f ={}

    # use find query in order to find Set ID of current set
    def find(self, x):
        y = self.f.get(x, x)
        # this means that we are not at Set ID node yet
        if y != x:
            y = self.find(y)
        # return the value of parent
        return y
    
    # union two different sets setting one Set's parent to the other parent
    def union (self, x, y):
        self.f[self.find(x)] = self.find(y)

"""
Tree Compression Optimization

Now that we have a general idea of the data structure and how it is implemented, we now 
introduce an optimization. We can imagine there may be scenarios where our tree is not
particularly balanced. Therefore, while recursing up the tree we make sure to store the 
Set ID node value and while moving back down the recursive stack set every node to the 
Set ID value. Here is a graphic to demonstrate this idea and should be a good visual 
indication of why this technique is referred to as tree compression as we eventually 
reach a tree with depth of 2 after querying every node.

8-->7-->6-->5

While we try to find the parent node of node id 8 we set every node along the path to the
Set ID node which is 5 which means later queries within our data structure only take 
O(log(n)) time. This technique is called tree compression and allows us to achieve 
amortized O(log(n)) time complexity.

As a reminder, amortized time complexity is referring to the time complexity over a large
number of operations. We eventually get worst, average and best case of O(log(n)) over a
large number of queries which allows us to avoid the worst case of O(n) every operation.
Below now is a code template to implement the idea of path compression discussed in this 
article.

"""
class UnionFind:

    # initialize the data structure using a HashMap
    def __init__(self):
        self.f ={}
    
    # use find query in order to find Set ID of current set
    def find(self, x):
        y = self.get(x, x)
        # this means that we are not at Set ID node yet

        if y != x:
            self.f[x] = y = self.find(y)
        # return value of parent
        return y

    # union two different sets setting one Set's parent to the other parent
    def union(self, x, y):
        self.f[self.find(x)] = self.find(y)

"""
Union by Rank (Advanced)

Can we improve this even more though? We have already discussed tree compression to 
optimize our later queries but there actually does exist a way to improve the time 
complexity. This uses a technique called union by rank where we assign ranks to our nodes 
where the ranks represent the relative depths of our trees. Each time we merge 2 sets we 
always set the parent of the node with the smaller ranks to that of the larger rank and 
update ranks. This technique improves our O(log(n)) algorithm to that of O(alpha(n)) where
alpha(n) represents the inverse Ackermann Function which grows very slowly relative to n. 
The proof for the time complexity is a bit complicated so we will not touch upon it here. 
It should be noted that since the inverse Ackermann Function grows so slowly it will never
practically speaking exceed O(4) effectively making it O(1) but precisely speaking the 
time complexity is defined by O(alpha(n)).

As a final note, in most cases using union by rank is likely not necessary as O(log(n)) is 
likely to be sufficiently fast for most cases but this is still a good trick to know for 
cases where it is required. Now our final code taking into account union by rank,

"""

class UnionFind:

    # initialize the data structure using a HashMap
    def __init__(self):
        self.f ={}
        self.rank ={}

    # use find query in order to find Set ID of current set
    def find(self, x):
        # Get the value associated with key x, if it's not in the map return x
        y = self.f.get(x, x)
        # check if the current node is a Set ID node
        if y != x:
            # change the hash value of node x to Set ID value of node y
            self.f[x] = y = self.find(y)
        return y

    # union two different sets setting one Set's parent to the other parent
    def union(self, x, y):
        # check if keys exist in our rank map if not add them
        if self.find(x) not in self.rank:
            self.rank[self.find(x)] = 0
        if self.find(y) not in self.rank:
            self.rank[self.find(y)] = 0
        if self.rank[self.find(x)] < self.rank[self.find(y)]:
            self.f[self.find(x)] = self.find(y)
        else:
            self.f[self.find(y)] = self.find(x)
            # if rank is the same then we update x rank and increment by 1 since we make
            # y's parent
            if self.rank[self.find(x)] == self.rank[self.find(y)]:
                self.rank[self.find(x)] = self.rank[self.find(x)] + 1

"""
Do I Need to Know or Implement Union Find for the Interview?

It's slightly more advanced. For implementation, knowing the version with Tree
Compression Optimization is enough. No interviewer would expect you to write union by 
rank version in the short interview time.

"""
