"""
program to delete a given key from
circular DLL
"""


# Python3 program to delete a given key from
# circular doubly linked list.

# structure of a node of linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def insert(start, value):
    # If the list is empty, create a single node
    # circular and doubly list
    if (start == None):
        new_node = Node(0)
        new_node.data = value
        new_node.next = new_node.prev = new_node
        start = new_node
        return start

    # If list is not empty

    # Find last node /
    last = (start).prev

    # Create Node dynamically
    new_node = Node(0)
    new_node.data = value

    # Start is going to be next of new_node
    new_node.next = start

    # Make new node previous of start
    (start).prev = new_node

    # Make last preivous of new node
    new_node.prev = last

    # Make new node next of old last
    last.next = new_node
    return start


# Function to delete a given node
# from the list
def deleteNode(start, key):
    # If list is empty
    if (start == None):
        return None

    # Find the required node
    # Declare two pointers and initialize them
    curr = start
    prev_1 = None
    while (curr.data != key):

        # If node is not present in the list
        if (curr.next == start):
            print("List doesn't have node",
                  "with value = ", key)
            return start

        prev_1 = curr
        curr = curr.next

    # Check if node is the only node in list
    if (curr.next == start and prev_1 == None):
        (start) = None
        return start

    # If list has more than one node,
    # check if it is the first node
    if (curr == start):

        # Move prev_1 to last node
        prev_1 = (start).prev

        # Move start ahead
        start = (start).next

        # Adjust the pointers of prev_1
        # and start node
        prev_1.next = start
        (start).prev = prev_1

    # check if it is the last node
    elif (curr.next == start):

        # Adjust the pointers of prev_1
        # and start node
        prev_1.next = start
        (start).prev = prev_1

    else:

        # create new pointer,
        # points to next of curr node
        temp = curr.next

        # Adjust the pointers of prev_1
        # and temp node
        prev_1.next = temp
        temp.prev = prev_1

    return start


# Function to display list elements
def display(start):
    temp = start

    while (temp.next != start):
        print(temp.data, end=" ")
        temp = temp.next

    print(temp.data)


# Driver Code
if __name__ == '__main__':
    # Start with the empty list
    start = None

    # Created linked list will be 4.5.6.7.8
    start = insert(start, 4)
    start = insert(start, 5)
    start = insert(start, 6)
    start = insert(start, 7)
    start = insert(start, 8)

    print("List Before Deletion: ")
    display(start)

    # Delete the node which is not present in list
    start = deleteNode(start, 9)
    print("List After Deletion: ")
    display(start)

    # Delete the first node
    start = deleteNode(start, 4)
    print("List After Deleting", 4)
    display(start)

    # Delete the last node
    start = deleteNode(start, 8)
    print("List After Deleting ", 8)
    display(start)

    # Delete the middle node
    start = deleteNode(start, 6)
    print("List After Deleting ", 6)
    display(start)