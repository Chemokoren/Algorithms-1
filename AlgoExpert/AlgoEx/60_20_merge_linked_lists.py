"""
Merge Linked Lists

"""

class LinkedList:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

# O(n + m) time | O(1) space
def mergeLinkedLists(headOne, headTwo):
    p1 = headOne
    p1Prev = None
    p2 = headTwo

    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            p1Prev = p1
            p1 =p1.next
        else:
            if p1Prev is not None:
                p1Prev.next = p2
            p1Prev = p2
            p2 = p2.next
            p1Prev.next = p1

    if p1 is None:
        p1Prev.next = p2
    return headOne if headOne.value < headTwo.value else headTwo

# approach 2 - recursive function
# (n + m)  time | O(n + m) space
def mergeLinkedLists(headOne, headTwo):
    recursiveMerge(headOne, headTwo, None)
    return headOne if headOne.value < headTwo.value else headTwo

def recursiveMerge(p1, p2, p1Prev):
    if p1 is None:
        p1Prev.next = p2
        return
    if p2 is None:
        return

    if p1.value < p2.value:
        recursiveMerge(p1.next, p2, p1)
    else:
        if p1Prev is not None:
            p1Prev.next = p2
        newP2 = p2.next
        p2.next = p1
        recursiveMerge(p1, newP2, p2)

