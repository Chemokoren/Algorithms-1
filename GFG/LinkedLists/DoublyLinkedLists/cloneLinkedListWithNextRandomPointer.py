# Program to clone a linked list
# with random pointers

class Node:
    def __init__(self,data):
        self.data=data
        self.next =None
        self.random =None

# Ductionary
class MyDictionary(dict):

    # __init__ function
    def __init__(self):
        super().__init__()
        self =dict()

    # Function to add key:value
    def add(self, key, value):
        # Adding Values to dictionary
        self[key] = value

# Linked list class
class LinkedList:
    # Linked list constructor
    def __init__(self,node):
        self.head =node

    # Method to print the list.
    def __repr__(self):
        temp =self.head
        while temp is not None:
            random =temp.random
            random_data =(random.data if random is not None else -1)
            data = temp.data
            print(
                f"Data-{data}, Random data: {random_data}")
            temp =temp.next
        return "\n"
    # push method to put data always at the head
    # in the linked list
    def push(self,data):
        node =Node(data)
        node.next =self.head
        self.head = node

    # Actual clone method which returns head
    # reference of cloned linked list.
    def clone(self):
        # initialize two references, one
        # with original list's head.

        original =self.head
        clone = None

        # Initialize two references, one
        # with original lis's hea
        mp = MyDictionary()

        # Traverse the original list and
        # make a copy of that
        # in the clone linked list
        while original is not None:
            clone = Node(original.data)
            mp.add(original,clone)
            original =original.next

        # Adjusting the original
        # list reference again
        original =self.head

        # Traversal of original lst again
        # to adjust the next and random
        # references of clone list using hash map.
        while original is not None:
            clone =mp.get(original)
            clone.next=mp.get(original.next)
            clone.random =mp.get(original.random)
            original =original.next

        # Return the head reference of the clone list.
        return LinkedList(self.head)

# Driver code for the progrm

# Pushing data in the linked list.

l =LinkedList(Node(5))
l.push(4)
l.push(3)
l.push(2)
l.push(1)

# Setting up random references.
l.head.random =l.head.next.next
l.head.next.random = l.head.next.next.next
l.head.next.next.random = l.head.next.next.next.next
l.head.next.next.next.random =(l.head.next.next.next.next.next)
l.head.next.next.next.next.random =l.head.next

# Making a clone of the
# original linked list.
clone =l.clone()

# print the original and cloned
# linked lists

print("Original linked list")
print(l)
print("Cloned linked list")
print(clone)




