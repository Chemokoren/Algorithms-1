"""
Flatten Binary tree to Linked List

Given a binary tree, return a linked list that is a "flattened" version of the tree.

The linked list still uses the same nodes as a normal binary tree, only the left subtree is
always empty, and the right subtree always  points to the next element in the linked list(or 
the empty tree).
The flattened tree represents the pre-order traversal of the tree.

Input

- tree: the binary tree to be flattened.

Output
- A tree representing the flattened binary tree.

Example

input:

1 tree = <see explanation>

Output : <see explanation>

Explanation

                            1
                           / \
                          2   3
                         / \
                        4   5

Flattened tree:

                        1
                         \
                          2
                           \
                            4
                             \
                              5
                               \
                                3
Not that this uses the binary tree structure to represent the linked list.


"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten_tree(tree: Node) -> Node:
    # WRITE YOUR BRILLIANT CODE HERE
    return None

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

def format_tree(node):
    if node is None:
        yield 'x'
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)

if __name__ == '__main__':
    tree = build_tree(iter(input().split()), int)
    res = flatten_tree(tree)
    print(' '.join(format_tree(res)))