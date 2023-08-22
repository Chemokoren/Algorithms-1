'''
python implementation to sort a k sorted dll
'''


class Node:
    data = None
    Node = None
    next = None
    prev = None

    def __init__(self, d):
        data = d
        next = prev = None

class DoublyLinkedList:
    Node =None
    head =None
    '''
        function to sort a k sorted doubly linked list
    '''

    def compare(self,n1, n2):
        return n1.data - n2.data

    def sortAKSortedDLL(self, head, k):
        # if list is empty
        if (head == None):
            return head

        # priority_queue 'pq' implemented as min heap with the
        # help of 'compare' function in compare Node class

        pq =  PriorityQueue < Node > (self.compare)

        newHead = null, last = None

        # Create a Min Heap of first(k + 1) elements from
        # input doubly linked list
        for i  in range(0,k):
            # push the node on to 'pq'
            pq.add(head)
            # move to the next node
            head = head.next

            # loop till there are elements in 'pq' while (!pq.isEmpty())
            # place root or top of 'pq' at the end of the
            # result sorted list so far having the first node
            # pointed to by 'newHead'
            # and adjust the required links
            if (newHead == null):
                newHead = pq.peek()
                newHead.prev = null

                # 'last' points to the last node
                # of the result sorted list so far
                last = newHead
            else:
                last.next = pq.peek()
                pq.peek().prev = last
                last = pq.peek()

                # remove element from 'pq'
                pq.poll()

            # if there are more nodes left in the input list
            if (head != null):
                # push the node on to 'pq'
                pq.add(head)

                # move to the next node
                head = head.next
            # making 'next' of last node point to NULL
            last.next = null

            # new head of the required sorted DLL
            return newHead



        '''
         UTILITY FUNCTIONS 
         Function to insert a node at the beginning of the Doubly Linked List
        '''

    def push(self, new_data):
        '''
        allocate node
        '''

        new_node = Node(new_data)

        # since we are adding at the beginning, prev is always NULL

        new_node.prev = None

        # link the old list off the new node

        new_node.next = self.head

        # change prev of head node to new node
        if (self.head != None):
            self.head.prev = new_node

        # move the head to point to the new node
        self.head = new_node

        # Function to print nodes in a given doubly linked list This function is same as printList()
        # of singly linked list

    def printList(self,node):
        while (node != None):
            print(node.data)
            node = node.next

 # Driver code
if __name__=='__main__':
    list = DoublyLinkedList()
    '''
    Let us create a k sorted doubly linked list to test the functions Created doubly linked list
     will be 3 <->6 <->2 <->12 <->56 <->8    
    '''
    list.push(8)
    list.push(56)
    list.push(12)
    list.push(2)
    list.push(6)
    list.push(3)

    k = 2

    print("Original Doubly linked list:")
    list.printList(list.head)

    sortedDLL = list.sortAKSortedDLL(list.head, k)
    print("")
    print("Doubly Linked List after sorting:")
    list.printList(sortedDLL)
