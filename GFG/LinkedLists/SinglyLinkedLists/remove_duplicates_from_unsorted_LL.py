"""
Remove duplicates from an unsorted linked list

Write a removeDuplicates() function that takes a list and deletes any duplicate nodes
from the list. The list is not sorted.

For example if the linked list is 12->11->12->21->41->43->21 then removeDuplicates()
should convert the list to 12->11->21->41->43




METHOD 1 (Using two loops)
This is the simple way where two loops are used. Outer loop is used to pick
the elements one by one and inner loop compares the picked element with rest of the elements.
"""
from generic_singly_linked_list import generic_singly_linked_list, Node

# program to remove duplicates from unsorted LL : Time Complexity: O(n^2)
class Node:
    def __init__(self, d):
        data = d
        next = None

class LinkedList:

    # Function to remove duplicates from an unsorted linked list
    def remove_duplicates(self, head):
        ptr1 = ptr2 = dup = None
        ptr1 = head

        # Pick elements one by one
        while (ptr1 != None and ptr1.next != None):
            ptr2 = ptr1

            # Compare the picked element with rest of the elements
            while (ptr2.next != None):

                # If duplicate then delete it
                if (ptr1.data == ptr2.next.data):
                    # sequence of steps is important here
                    dup = ptr2.next
                    ptr2.next = ptr2.next.next
        # garbagge collection
        else:  # This is tricky
            ptr2 = ptr2.next

        ptr1 = ptr1.next

    def printList(self,node):
        while (node != None):
            print(node.data + " ")
            node = node.next

if __name__=='__main__':
    list = LinkedList()
    list.head = Node(10)
    list.head.next = Node(12)
    list.head.next.next = Node(11)
    list.head.next.next.next = Node(11)
    list.head.next.next.next.next = Node(12)
    list.head.next.next.next.next.next = Node(11)
    list.head.next.next.next.next.next.next = Node(10)

    # print("Linked List before removing duplicates : \n ")
    # list.printList(list.head)

    # list.remove_duplicates()
    # print("")
    # print("Linked List after removing duplicates : \n ")
    # list.printList(list.head)


"""
METHOD 2 (Use Sorting) 
In general, Merge Sort is the best-suited sorting algorithm for sorting linked lists efficiently. 
1) Sort the elements using Merge Sort. O(nLogn) 
2) Remove duplicates in linear time using the algorithm for removing duplicates in sorted Linked List. O(n) 
Please note that this method doesn’t preserve the original order of elements.
Time Complexity: O(nLogn)
"""


"""
METHOD 3 (Use Hashing) 
We traverse the link list from head to end. For every newly encountered element, 
we check whether it is in the hash table: if yes, we remove it; otherwise we put it 
in the hash table.
"""


# Python3 program to remove duplicates
# from unsorted linkedlist
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None

    # Function to print nodes in a
    # given linked list
    def printlist(self):

        temp = self.head

        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

    # Function to remove duplicates from a
    # unsorted linked list
    def removeDuplicates(self, head):

        # Base case of empty list or list with only one element
        if self.head is None or self.head.next is None:
            return head

        # Hash to store seen values
        hash = set()

        current = head
        hash.add(self.head.data)

        while current.next is not None:

            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next

        return head


# Driver code
if __name__ == "__main__":
    # Creating Empty list
    llist = LinkedList()
    llist.head = Node(10)
    second = Node(12)
    third = Node(11)
    fourth = Node(11)
    fifth = Node(12)
    sixth = Node(11)
    seventh = Node(10)

    # Connecting second and third
    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh

    # Printing data
    print("Linked List before removing Duplicates.")
    llist.printlist()
    llist.removeDuplicates(llist.head)
    print("\nLinked List after removing duplicates.")
    llist.printlist()

    

print("\n my tests \n")
class my_tests(generic_singly_linked_list):
    def __init__(self) -> None:
        super().__init__()

    def remove_duplicates(self, head):
        current = head
        dic ={}

        while (current):
            if current.data in dic:
                current =current.next
            else:
                print(current.data, end="-->")
                dic[current.data]=True

    

llist = my_tests()
llist.push(21)
llist.push(43)
llist.push(41)
llist.push(21)
llist.push(12)
llist.push(11)
llist.push(12)
llist.print_ll()
llist.remove_duplicates(llist.head)

# 12->11->21->41->43
