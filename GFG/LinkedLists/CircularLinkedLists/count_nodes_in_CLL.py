"""
program to count number of nodes in a circular linked list

Time Complexity: O(n), As we are visiting every node just once.
Auxiliary Space: O(1), As constant extra space is used

"""
from generic_circular_linked_list import Circular_Linked_list

class count_nodes_in_cll(Circular_Linked_list):
    def __init__(self) -> None:
        super().__init__()

    def countNodes(self, head):
        temp =head
        result =0
        if(head != None):
            while True:
                temp =temp.next
                result =result + 1
                if(temp == head):
                    break
        return result

if __name__ =='__main__':
   
    cll =count_nodes_in_cll()
    cll.push(12)
    cll.push(56)
    cll.push(2)
    cll.push(11)
    print(cll.countNodes(cll.head))