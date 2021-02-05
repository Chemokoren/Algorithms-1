class LinkedList:
    def __init__(self,value):
        self.value =value
        self.next =None

    # O(n + m) time | O(1) space
    def mergeLinkedLists(self, headOne, headTwo):
        p1 =headOne
        p1Prev =None
        p2 =headTwo

        while p1 is not None and p2 is not None:
            if p1.value < p2.value:
                p1Prev =p1
                p1 = p1.next
            else:
                if p1Prev is not None:
                    p1Prev.next = p2
                p1Prev =p2
                p2 =p2.next
                p1Prev.next = p1
        if p1 is None:
            p1Prev.next =p2
        return headOne if headOne.value < headTwo.value else headTwo

    # Recursive solution
    # O(n + m) time | O(n + m) space
    def mergeLinkedListsRecursive(self,headOne, headTwo):
        self.recursiveMerge(headOne, headTwo, None)
        return headOne if headOne.value < headTwo.value else headTwo

    def recursiveMerge(self,p1, p2, p1Prev):
        if p1 is None:
            p1Prev.next =p2
            return
        if p2 is None:
            return
        if p1.value < p2.value:
            self.recursiveMerge(p1.next, p2, p1)
        else:
            if p1Prev is not None:
                p1Prev.next =p2
            newP2 =p2.next
            p2.next =p1
            self.recursiveMerge(p1,newP2,p2)

    #first_linked_list = 2->6->7->8
    # second_linked_list = 1->3->4->5->9->10
    # final_linked_list = 1->2->3->4->5->6->7->8->9->10
    
