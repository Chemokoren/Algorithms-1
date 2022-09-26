class Node:
    # Constructor for the new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class generic_doubly_linked_list:
    def __init__(self):
        self.head = None

    # code to insert a new node in front of the list given an integer and a reference to the head of a list
    def push(self, new_data):
        # allocate a node and put data in the node
        new_node = Node(new_data)

        # make previous None (already None), and next of new node as head
        new_node.next = self.head

        # change prev of the head node to the new_node
        if self.head is not None:
            self.head.prev =new_node

        # alter the prev of the former head node to new_node
        if self.head is not None:
            self.head.prev = new_node

        # make the new node the current head
        self.head = new_node

    # given the start node print the nodes as long as we don't get to null
    def printList(self, node):
        while(node is not None):
            print(node.data),
            node = node.next
