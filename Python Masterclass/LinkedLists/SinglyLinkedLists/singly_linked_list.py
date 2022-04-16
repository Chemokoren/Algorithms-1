"""
Objectives 
- Define what a Singly Linked List is
- Compare and contrast Linked Lists with Arrays
- Implement insertion, removal and traversal methods on Singly Linked Lists

What is a Linked List?

- A data structure that contains a head, tail and length property.
- Linked Lists consist of nodes, and each node has a value and a pointer to another node or null

Comparisons with Arrays

Lists
- Do not have indexes!
- Connected via nodes with a next pointer
- Random access is not allowed

Arrays
- Indexed in order!
- Insertion and deletion can be expensive
- Can quickly be accessed at a specific index

Pushing
-Adding a new node to the end of the Linked List!

Pushing Pseudocode
- This function should accept a value
- Create a new node using the value passed to the function
- If there is no head property on the list, set the head and tail to be the newly created node
- Otherwise set the next property on the tail to be the new node and set the tail property on the list to be
the newly created node
- increment the length by one

Popping 
- Removing a node from the end of the Linked List!

Popping pseudocode
- if there are no nodes in the list, return undefined
- Loop through the list until you reach the tail
- Set the next property of the 2nd to last node to be null
- Set the tail to be the 2nd to last node
- Decrement the length of the list by 1
- Return the value of the node to be removed



"""
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def traverse(self):
        current = self.head
        while(current):
            print(current.val, end="-->")
            current = current.next
        print()

    def push(self,val):
        n = Node(val)
        if self.head ==self.tail ==None:
            self.head =n
            self.tail =n
        else:
            self.tail.next =n
            self.tail =n
        self.size += 1
    
    def pop(self):
        # - if there are no nodes in the list, return undefined
        if self.size ==0:
            return None
        elif self.size ==1:
            remove_node = self.head
            self.head = None
            self.tail = None
            return remove_node.val
        else:    
            idx = 0
            start = self.head

            # - Loop through the list until you reach the tail
            while idx < self.size -2:
                start = start.next
                idx +=1
            second_last_node =start
            remove_node = second_last_node.next

            # - Set the next property of the 2nd to last node to be null
            second_last_node.next =None
            # - Set the tail to be the 2nd to last node
            self.tail = second_last_node
            # - Decrement the length of the list by 1
            self.size -=1
            # - Return the value of the node to be removed
            return remove_node.val
        
    def print(self):
        idx =0
        start = self.head
        while idx < self.size:
            print(start.val,end="-->")
            start = start.next
            idx +=1
        print()



# first = Node("Hi")
# first.next =Node("there")
# first.next.next =Node("how")
# first.next.next.next =Node("are")
# first.next.next.next.next =Node("you")

# print("1",first.val)
# print("2",first.next.val)
# print("3",first.next.next.val)
# print("4",first.next.next.next.val)
# print("5",first.next.next.next.next.val)

s = SinglyLinkedList()
s.push("Hi")
s.push("there")
s.push("how")
s.push("are")
s.push("you")
s.traverse()
print("removed node:",s.pop())
s.traverse()
print("removed node:",s.pop())
s.traverse()
print("removed node:",s.pop())
s.traverse()
print("removed node:",s.pop())
s.traverse()
print("removed node:",s.pop())
s.traverse()
print("removed node:",s.pop())
s.traverse()