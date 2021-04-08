"""
code to implement priority queue using DLL

1. Create a doubly linked list having fields info(hold the information of the Node), priority(hold the priority of the Node), prev(point to previous Node), next(point to next Node).
2. Insert the element and priority in the Node.
3. Arrange the Nodes in the increasing order of priority. 
"""
# Linked List Node
class Node:
    def __init__(self):
        self.data =0
        self.priority =0
        self.next =None
        self.prev =None

head = None
tail = None

# Function to insert a new Node
def push(_head, _tail, data, _priority):
    global head, tail

    new_node =Node()
    new_node.data =data
    new_node.priority=_priority

    # if linked list is empty
    if(_head == None):
        _head =new_node
        _tail =new_node
        new_node.next =None

    else:
        # if _priority is less than or equal _head
        # node's priority, then insert at the _head.
        if(_priority <= _head.priority):
            new_node.next =_head
            _head.prev =new_node.next
            _head =new_node

            # if _priority is more than _tail node's priority,
            # then insert after the _tail
        elif (_priority > _tail.priority):
            new_node.next =None
            _tail.next =new_node
            new_node.prev = _tail.next
            _tail =new_node

        # handle other cases
        else:
            # Find position where we need to insert
            start = _head.next
            while (start.priority > _priority):
                start =start.next

            start.prev.next =new_node
            new_node.next =start.prev
            new_node.prev =start.prev.next
            start.prev =new_node.next

    head = _head
    tail =_tail

# Return the value at _tail
def peek(head):
    return head.data

def isEmpty(head):
    return head == None


# Removes the element with the least priority value from the list
def pop(_head, _tail):
    global head, tail
    temp =_head
    res =temp.data
    _head =_head.next
    if(_head == None):
        _tail =None
    head =_head
    tail ==_tail
    return res


# Driver code
if __name__ == '__main__':
    push(head, tail, 2, 3)
    push(head, tail, 3, 4)
    push(head, tail, 4, 5)
    push(head, tail, 5, 6)
    push(head, tail, 6, 7)
    push(head, tail, 1, 2)

    print(pop(head, tail))
    print(peek(head))

