class Node:
    def __init__(self, d):
        self.data =d
        self.next =None
        self.prev =None


'''Python program to sort a linked list using QuickSort'''
class QuickSort_Using_Doubly_LinkedList:
    def __init__(self):
        self.head =None
    # a node of the doubly linked list
    # A utility function to find last node of linked list
    def lastNode(self,node):
        while(node.next != None):
            node =node.next
        return node

    """
    Considers last element as pivot, places the pivot element at its
    correct position in sorted array, and places all smaller (smaller than
    pivot) to left of pivot and all greater elements to right of pivot
    """
    # Node l, Node h
    def partition(self,l,h):
        # set pivot as h element
        x =h.data

        # similar to i =l-1 for array implementation
        i = l.prev

        # similar to "for (int j =l; j<= h-1; j++)"
        # for(Node j=l; j!=h; j=j.next):
        for j in range(l,h):
            if(j.data <=x):
                # similar to i++ for array
                i = l if(i==None) else i.next
                temp = i.data
                i.data =j.data
                j.data =temp


        i = l if(i==None) else i.next # similar to i++
        temp =i.data
        i.data =h.data
        h.data =temp
        return i



    '''  A recursive implementation of quicksort for linked list '''
    # Node l, Node h
    def _quickSort(self,l, h):
        if( h!=None and l!= h and l!=h.next):
            temp = self.partition(l, h)  # Node temp
            self._quickSort(l, temp.prev)
            self._quickSort(temp.next, h)



     # The main function to sort a linked list. It mainly calls _quickSort()
    def quickSort(self,node):
        # Find last node
        head = self.lastNode(node)

        # call the recursive QuickSort
        self._quickSort(node, head)

    # A utility function to print contents of arr
    def printList(self,head):
        while(head is not None):
            print(str(head.data))
            head = head.next


    ''' Function to insert a node at the beginning of the Doubly Linked List '''
    def push(self,new_Data):
        new_Node =Node(new_Data)  # allocate node

        # if head is null, head =new_Node
        if(self.head ==None):
            self.head =new_Node
            return


         # link the old list off the new node
        new_Node.next =self.head

        #  change prev of head node to new node
        self.head.prev =new_Node

        '''  since we are adding at the beginning, prev is always NULL '''
        new_Node.prev =None

        ''' move to the head to point to the new node '''
        head =new_Node


    ''' Driver program to test QuickSort '''

list = QuickSort_Using_Doubly_LinkedList()

list.push(5)
list.push(20)
list.push(4)
list.push(3)
list.push(30)

print("Linked List before sorting ")
list.printList(list.head)
print("\nLinked List after sorting")
list.quickSort(list.head)
list.printList(list.head)


