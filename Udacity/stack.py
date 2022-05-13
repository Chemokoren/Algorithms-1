"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next =self.head
        self.head = new_element
        

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        if self.head ==None:
            return None
        current = self.head
        if self.head:
            if self.head.next:
                self.head =self.head.next
            else:
                self.head =None        
        return current
    
    def delete_first_updated(self):
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            deleted_element.next =None
            return deleted_element
        else:
            return None
                
    def print_ll(self):
        current =self.head
        while current:
            print(current.value, end="-->")
            current =current.next
        print()
                

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()

    def printStack(self):
        return self.ll.print_ll()
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)



print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
stack.push(e4)
print(stack.pop().value)
stack.printStack()