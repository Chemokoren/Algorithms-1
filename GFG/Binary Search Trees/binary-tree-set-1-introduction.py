"""
Trees: Unlike Arrays, Linked List
s, Stack and Queues which are linear data structures
, trees are hierarchical data structures.

Main applications of trees;
- manipulate hierarchical data
- Make information easy to search - tree traversal
- Manipulate sorted lists of data
- As a workflow for compositing digital images for visual effects
- Router algorithms
- form of a multi-stage decision-making

Properties of a binary tree
1) The maximum number of nodes at level 'l' of a binary tree is 2^l
Here level is the number of nodes on the path from the root to the node (including
root and node). Level of the root is 0.
This can be proved by induction.
For root, l =0, number of nodes = 2^0 =1
Assume that the maximum number of nodes on level 'l' is 2^l
Since in Binary tree every nde has at most 2 children, next level would have twice
nodes, i.e. 2*2^l

2) The maximum number of nodes in a binary tree of height 'h' is 2^h - 1
Here the height of a tree is the maximum number of nodes from the root to leaf path
Height of a tree with a single node is considered as 1.
The result can be derived from point 2 above. A tree has maximum nodes if all levels 
have maximum nodes. So, the maximum number of nodes in a binary tree of height h
is 1 + 2 + 4 + ... + 2^h . THis is a simple geometric series with h terms and sum of 
this series is 2^h -1
When the height of the tree is considered as 0, then in this convention, the above 
formular becomes 2^h+1 -1

3) In a Binary Tree with N nodes, minimum possible height or the minimum number
of levels is? |Log(N+1) base 2| -1

4) A Binary Tree with L leaves has at least | Log L to base 2| + 1 levels
A Binary tree has the maximum number of leaves (and a minimum number of levels) when
all levels are fully filled. Let all leaves be at level l, then below is true for
the number of leaves L.

L   <=  2^(l-1)  [From Point 1]
l =   | Log L to base 2| + 1 
where l is the minimum number of levels.

5) In Binary tree where every node has 0 or 2 children, the number of leaf nodes is
always one more than nodes with two children.

L = T + 1
Where L = Number of leaf nodes
T = Number of internal nodes with two children

proof:
No. of leaf nodes (L) i.e. total elements present at the bottom of 
tree = 2^(h-1) h is the height of tree
No. of internal nodes = { total no. of nodes } - {leaf nodes}
= {2^h -1} - {2^(h-1)}
= 2^h-1 (2-1) -1
=2^(h-1) -1
so,
L = 2^(h-1)
T = 2^(h-1) -1
Therefore L= T + 1



Types of Binary Tree:

1) Full Binary Tree - A binary Tree is a full binary tree if every node has 0 or 2 
children - binary tree in which all nodes except leaf nodes have two children.

2) Complete Binary Tree: - A Binary tree is a complete binary tree if all levels are
completely filled except possibly the last level and the last level has all keys as 
left as possible
3) Perfect Binary Tree- all the internal nodes have two children and all leaf nodes 
are at the same level

In a Perfect Binary Tree, the number of leaf nodes is the number of internal nodes 
plus 1
L = I + 1 where L=Number of leaf nodes, I = Number of internal nodes.

A perfect Binary Tree of height h( where the height of the binary tree is the longest
path from the root node to any leaf node in the tree, height of root node is 1)
has 2^h - 1 node.

An example of a Perfect binary tree is ancestors in the family. Keep a person at root
,parents as children, parents of parents as their children

Balanced Binary Tree - a binary tree is balanced if the height of the tree is O(Log n)
where n is the number of nodes. For example, the AVL tree maintains O(Log n) height
by making sure that the difference between the heights of the left and right subtree
is at most 1. Red-Black trees maintain O(Log n) height by making sure that the number
of  Black nodes on every root to leaf paths is the same and there are no adjacent red
nodes.  Balanced Binary search trees are performance-wise good as they provide O(log n)
time for search, insert and delete.

A degenerate(or pathological) tree  - a tree where every internal node has one child.
Such trees ate performance-wise same as linked list.

"""

# program to introduce Binary Tree
# A class that represents an individual node in a Binary tree

class Node:
    def __init__(self, key) -> None:
        self.left =None
        self.right =None
        self.val =key

# create root
root = Node(1)
root.left =Node(2)
root.right =Node(3)
root.left.left =Node(4)

print(root)

