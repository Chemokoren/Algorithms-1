"""
Reverse Linked List
input: 0->1->2->3->4->5
output: 5->4->3->2->1->0
"""
# O(n) time | O(1) space
def reverseLinkedList(head):
    p1, p2 = None, head
    while p2 is not None:
        p3 = p2.next
        p2.next= p1
        p1 = p2
        p2 = p3 

    return p1
