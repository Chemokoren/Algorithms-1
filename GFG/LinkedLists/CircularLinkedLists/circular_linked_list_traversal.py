"""
program to demonstrate traversal of a circular linked list

Time Complexity: O(n)

Auxiliary Space: O(1)
"""
from generic_circular_linked_list import Circular_Linked_list


class CircularLinkedList(Circular_Linked_list):
    def __init__(self) -> None:
        super().__init__()

    # recursive traversal
    def traverse(self, temp=None):
        if temp == None:
            temp = self.head
  
        if temp.next == self.head:
            print(temp.data, end="\n")
            return
        print(temp.data, end="-->")
        self.traverse(temp.next)




cllist = CircularLinkedList()
# Created linked list will be 11->2->56->12
cllist.push(12)
cllist.push(56)
cllist.push(2)
cllist.push(11)

print("Contents of circular Linked List")
cllist.print_cll()
print("\n new traversal")
cllist.traverse()
