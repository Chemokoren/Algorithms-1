"""
program to split circular linked list into two halves
"""


from generic_circular_linked_list import Circular_Linked_list
# class to create a new Circular Linked List
class CircularLinkedList(Circular_Linked_list):

    def __init__(self) -> None:
        super().__init__()


    def my_tests(self):
        curr =self.head
        count = 0
        if self.head is not None:
            while(True):
                count +=1
                curr =curr.next
                if(curr == self.head):
                    break
        return count

    def create_2_LL(self):
        num =self.my_tests()
        first_head =[]
        second_head=[] 

        count =0
        curr =self.head
        while(True):
            count +=1
            if(count <=(num/2)):
                first_head.append(curr.data)

            if(count > (num/2) and count <=(num)):
                second_head.append(curr.data)
            curr = curr.next
            if(curr == self.head):
                break
            

        return f"first: {first_head}, second: {second_head}"



    '''
    Function to split a list (starting with head) into two lists. 
    head1 and head2 are the head nodes of the two resultant linked lists
    '''
    def splitList(self, head1, head2):
        slow_ptr =self.head
        fast_ptr = self.head

        if self.head is None:
            return

        # if there are odd nodes in the circular list then
        # fast_ptr->next becomes head and
        # for even nodes fast_ptr->next->next becomes the head

        while(fast_ptr.next != self.head and fast_ptr.next.next !=self.head):
            fast_ptr =fast_ptr.next.next
            slow_ptr =slow_ptr.next

        # if there are even elements in list then move fast_ptr
        if fast_ptr.next.next ==self.head:
            fast_ptr = fast_ptr.next

        # set the head pointer of first half
        head1.head =self.head

        # set the head pointer of second half
        if self.head.next !=self.head:
            head2.head =slow_ptr.next

        # Make second half circular
        fast_ptr.next = slow_ptr.next

        # Make first half circular
        slow_ptr.next =self.head

# initialize lists as empty
head =CircularLinkedList()
head1 =CircularLinkedList()
head2 =CircularLinkedList()


head.push(12)
head.push(56)
head.push(2)
head.push(11)

print("number of items in list:", head.my_tests())
print("AAA", head.create_2_LL())

print("Original Circular Linked List")
head.print_cll()

# Split the list
head.splitList(head1, head2)

print (" \n First Circular Linked List")
head1.print_cll()

print("\nSecond Circular Linked List")
head2.print_cll()
