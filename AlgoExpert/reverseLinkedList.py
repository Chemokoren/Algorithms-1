# O(n) time | O(1) space
def reverseLinkedList(head):
    p1, p2 =None, head
    while p2 is not None:
        p3 = p2.next
        p2.next =p1
        p1 = p2
        p2 = p3
    return p1
# build a linked list for demo
# original linked list: 0->1->2->3->4->5
# reversed linked list: 5->4->3->2->1->0
