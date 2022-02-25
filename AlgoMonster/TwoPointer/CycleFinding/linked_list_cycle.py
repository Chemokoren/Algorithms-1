"""
Linked List Cycle

Given a linked list with potentially a loop, determine whether the linked list from the first
node contains a cycle in it. For bonus points, do this with constant space.
Parameters

    nodes: The first node of a linked list with potentially a loop.

Result

    Whether there is a loop contained in the linked list.

Examples
Example 1

Input:

0-->1-->2-->3-->4-->1

Answer: There is a loop of size 4, starting from node 1

Output:

true

Example 2

input:

0-->1-->2-->3-->4

Answer: There is no loop

Output:
false

Constraints

    1 <= len(nodes) <= 10^5


"""