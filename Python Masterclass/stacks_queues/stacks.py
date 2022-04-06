"""
Objectives

- Define what a stack is
- Understand use cases for a stack
- implement operations on a stack data structure

What is a stack?
- It is a LIFO data structure
The last element added to the stack will be the first element removed from the stack

How is it used?
- Think about a stack of plates, or a stack of markers, or a stack of ... anything
- As you pile it up, the last thing(or the topmost thing) is what gets removed first.

WHERE STACKS ARE USED
-Managing function invocations
-Undo/Redo
-Routing(the history object) is treated like a stack - in your browser

PUSH Pseudocode
- The function should accept a value
- Create a new node with that value
- If there are no nodes in the stack, set the first and last property to be the newly
created node
- If there is at least one node, create a variable that stores the current first
property on the stack
- Reset the first property to be the newly created node
- Set the next property on the node to be the previously created variable
- Increment the size of the stack by 1

POP Pseudocode

- If there are no nodes in the stack, return null
- Create a temporary variable to store the first property on the stack
- if there is only 1 node, set the first and last property to be null
- if there is more than one node, set the first property to be the next property on the
current first
-Decrement the size by 1
- Return the value of the node removed

Big O of Stacks

Insertion - O(1)
Removal - O(1)
Searching - O(N)
Access - O(N)


RECAP
- Stacks are a LIFO data structure where the last value in is always the first one out
- Stacks are used to handle function invocations(the call stack), for operations like 
undo/redo, and for routing(remember pages you have visited and go back/forward)
- They are not a built in data structure in JavaScript, but are relatively simple to 
implement.
"""
class Stack:

    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0

    def push(self, val):
        n = Node(val)
        if(self.size ==0):
            self.first =n
            self.last = n
        current_first =self.first
        self.first =n
        self.first.next =current_first
        self.size +=1
        return self.size
    
    def pop(self):
        if self.size == 0:
            return None
        current_first = self.first
        if self.size ==1:
            self.first = None
            self.last  = None
        if self.size > 1:
            self.first =current_first.next
        self.size -=1
        return current_first.value
    
    def popOptimized(self):
        if self.size == 0:
            return None
        current_first = self.first
        if self.first == self.last:
            self.first = None
            self.last  = None
        self.first =current_first.next
        self.size -=1
        return current_first.value

class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next =None

st = Stack()
print(st.push(23))
print(st.push(30))
print(st.push(11))
print("size: ",st.size)
print("pop: ", st.popOptimized())
print("size: ",st.size)
print("pop: ", st.popOptimized())
print("size: ",st.size)
print("pop: ", st.popOptimized())
print("size: ",st.size)
print("pop: ", st.popOptimized())
print("size: ",st.size)
print("pop: ", st.popOptimized())
print("size: ",st.size)