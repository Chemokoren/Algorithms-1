"""
This question is the same as Linked List Cycle, except in addition to checking whether a 
linked list has a loop, we also find the entry point to the loop, if possible.

Parameters

    nodes: The first node of a linked list with potentially a loop.

Result

    An integer representing the value contained by the entry point to the loop, 
    if there is one. If there is no loop, output -1.

Example 1

Input:

0-->1-->2-->3-->4-->1

Answer: There is a loop of size 4, starting from node 1

Output:

1
Example 2

Input:
0-->1-->2-->3-->4

Answer: There is no loop

Output:

-1

Constraints

    1 <= len(nodes) <= 10^5


"""
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def cycle_entry_point(nodes: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return 0

if __name__ == '__main__':
    raw_input = [int(x) for x in input().split()]
    nodes_list = []
    for i, entry in enumerate(raw_input):
        nodes_list.append(Node(i))
    for i, entry in enumerate(raw_input):
        if entry != -1:
            nodes_list[i].next = nodes_list[entry]
    nodes = nodes_list[0]
    res = cycle_entry_point(nodes)
    print(res)
    