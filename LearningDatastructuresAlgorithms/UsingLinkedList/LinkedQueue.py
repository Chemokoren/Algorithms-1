"""
"""
from exceptions import Empty

class LinkedQueue:

    class _Node:
        __slots__ ='_element','_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        newNode = self._Node(e, None)
        if self.is_empty():
            self._head = newNode
        else:
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        val = self._head
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail =None
        return val._element

    def is_first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def display(self):
        thead = self._head
        while thead:
            print(thead._element, end="-->")
            thead = thead._next
        print()
    
LQ = LinkedQueue()
LQ.enqueue(10)
LQ.enqueue(20)
LQ.enqueue(30)
LQ.enqueue(40)
LQ.display()
print('dequeue: ',LQ.dequeue())
LQ.display()
print('first: ',LQ.is_first())
print('dequeue: ',LQ.dequeue())
print('dequeue: ',LQ.dequeue())
LQ.display()
print('dequeue: ',LQ.dequeue())
print('dequeue: ',LQ.dequeue())
LQ.display()