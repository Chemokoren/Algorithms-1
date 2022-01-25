"""
Remove Nth Node from end of a Linked List
"""

# O(n) time where n - is the length of the linked list| O(1) space
def removeNthNodeFromEnd(head,n):
    counter = 1
    first = head
    second = head
    while counter <= n:
        second = second.next
        counter += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return 
    while second.next is not None:
        second = second.next
        first = first.next
    # first is pointing to the node right before the node we want to remove
    # first.next  = NODE_TO_REMOVE
    # first.next =NODE_TO_REMOVE.next
    first.next = first.next.next


    # Driver class

