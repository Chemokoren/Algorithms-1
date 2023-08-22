"""
With a solid understanding of recursion under our belt, we are now ready to tackle one of the 
most useful technique in coding interviews - Depth First Search (DFS). As the name suggests, 
DFS is a bold search. We go as deep as we can to look for a value, and when there is nothing 
new to discover, we retrace our steps to find something new. To put it in a term we already 
know, the pre-order traversal of a tree is DFS. Let's look at a simple problem of searching 
for a node in a binary tree whose value is equal to target.

"""
def dfs(root, target):

    if root is None:

        return None

    if root.val == target:

        return root

    # return non-null return value from the recursive calls

    left = dfs(root.left, target)

    if left is not None:

        return left


    # at this point, we know left is null, and right could be null or non-null

    # we return right child's recursive call result directly because

    # - if it's non-null we should return it

    # - if it's null, then both left and right are null, we want to return null

    return dfs(root.right, target)

    # the code can be shortened to: return dfs(root.left, target) or dfs(root.right, target)

# or

def dfs(root, target):
    if root is None:
        return
    if root.val == target:
        return root
    return dfs(root.left, target) or dfs(root.right, target)

"""
Being able to visualize recursion and call stack of a DFS function in your mind is extremely 
important.

The example above also introduces two other concepts, backtracking and divide and conquer. 
The action of retracing steps (e.g. from 2 we first visited 3 depth first and retraced back 
and visit the other child 4) is called backtracking.

Backtracking and DFS are similar concept and essentially the same thing since in DFS you 
always "backtrack" after exploring a deeper node. It's like saying I program computers by
doing coding. If we really want to make the distinction, then backtracking is the concept of 
retracing and DFS is the algorithm that implements it. 
Backtracking is often mentioned and associated with combinatorial search problems. 
We will do the same in the course.

We have two recursive calls dfs(root.left) and dfs(root.right), and return based on results 
from the recursive calls. This is also a divide and conquer algorithm, i.e. splitting into 
subproblems of the same type (search in left and right children) until they are simple enough 
to be solved directly (null nodes or found target) and combine the results from these 
subproblems (return non-null node). We'll investigate divide and conquer more in a later module.


When to use DFS

Tree

DFS is essentially pre-order tree traversal.

    Traverse and find/create/modify/delete node
    Traverse with return value (finding max subtree, detect balanced tree)

Combinatorial problems

DFS/backtracking and combinatorial problems are a match made in heaven (or silver bullet and
 werewolf 😅). As we will see in the Combinatorial Search module, combinatorial search 
 problems boil down to searching in trees.

    How many ways are there to arrange something
    Find all possible combinations of ...
    Find all solutions to a puzzle

Graph

Trees are special graphs that have no cycle. We can still use DFS in graphs with cycles. 
We just have to record the nodes we have visited and avoiding re-visiting them and going into 
an infinite loop.

    Find a path from point A to B
    Find connected components
    Detect cycles




References

    Robert Sedgewick and Kevin Wayne. Algorithms, 4th Edition.
    Steve Skiena. The Algorithm Design Manual, 2nd Edition.
    Richard E. Neapolitan. Foundations of Algorithms, 5th Edition.


"""