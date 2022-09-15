# program to find n'th node in a LL
 
 
class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
 
# Linked List class contains a Node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # This function is in LinkedList class. It inserts
    # a new node at the beginning of Linked List.
 
    def push(self, new_data):
 
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(new_data)
 
        # 3. Make next of new Node as head
        new_node.next = self.head
 
        # 4. Move the head to point to new Node
        self.head = new_node

    def getNth(self, key):
        current =self.head 
        count =0 # index of current node

        while(current):
            if(count == key):
                print(" key found !!")
                return current.data
            current =current.next
            count += 1


        # assert(False) # element does not exist
        return False

    def get_nth_recursive(self, ll, position):
        # call recursive method
        return ll.get_nth_node(self.head, position, ll)
    '''
    Time Complexity : O(n) 
    Auxiliary Space : O(n) due to recursive calls.
    '''
    def get_nth_node(self, head, position, ll):
        count = 0
        if (head):
            if count == position:
                print(head.data)
                return head.data
            else:
                ll.get_nth_node(head.next, position-1, ll)
        else:
            print("index doesn\'t exist")
            return False


    def print_ll(self):
        if self.head == None:
            print("No item to Print")
            return
        curr = self.head
        while(curr):
            print(curr.data, end="-->")
            curr = curr.next
        print()


if __name__ == '__main__':
 
    llist = LinkedList()
 
    # Use push() to construct below list
    # 1->12->1->4->1
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)
    llist.print_ll()
 
    print("Expected:False, Actual:", llist.getNth(5))
    print("Expected:True, Actual:", llist.getNth(3))
    print("Recursive Expected:, Actual:",llist.get_nth_recursive(llist, 3))

    
     
 