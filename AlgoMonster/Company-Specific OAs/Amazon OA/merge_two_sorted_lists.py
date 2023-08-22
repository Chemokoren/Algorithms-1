"""
(OA) - Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by 
splicing together the nodes of the given two lists.

Example1:
1-->2-->4

1-->3-->4

1-->1-->2-->3-->4-->4

Input: l1 = [1,2,4], l2 = [1,3,4]

Output: [1, 1, 2, 3, 4, 4]
Example 2:
Input: l1 = [], l2 = []

Output: []
Example 3:
Input: l1 = [], l2 = [0]

Output: [0]
Constraints:

The number of nodes in both lists is in the range [0, 50].

    -100 <= Node.val <= 100
    Both l1 and l2 are sorted in non-decreasing order.

"""

class Node:

    def __init__(self, val, next =None):
        self.val =val
        self.next = next

def merge(l1: Node, l2:Node)->Node:
    cur = dummy = Node(0)

    while l1 and l2:
        if l1.val < l2.val:
            cur.next, l1= l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next

    cur.next = l1 or l2
    return dummy.next

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None: return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)

def format_list(node):
    if node is None: return
    yield str(node.val)
    yield from format_list(node.next)

if __name__ == '__main__':
    l1 = build_list(iter(input().split()), int)
    l2 = build_list(iter(input().split()), int)
    res = merge(l1, l2)
    print(' '.join(format_list(res)))