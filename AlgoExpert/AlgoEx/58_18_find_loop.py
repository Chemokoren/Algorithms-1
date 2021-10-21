"""
Find Loop
0->1->2->4->5->6->7->8->9->4

"""

# O(n) time | O(1) space
def findLoop(head):
    first = head.next
    second = head.next.next

    while first != second:
        first = first.next
        second = second.next.next
    first = head

    while first != second:
        first = first.next
        second = second.next
    return first