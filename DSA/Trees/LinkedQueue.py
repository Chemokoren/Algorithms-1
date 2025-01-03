#from DSA.Modules_Exceptions import Empty
from exceptions import Empty

class LinkedQueue:
    class _Node:
        __slots__ ='_element', '_next'
        
        def __init__(self,element,next) -> None:
            self._element =element
            self._next =next

    def __init__(self) -> None:
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
            self._tail._next =newNode
        self._tail =newNode
        self._size = self._size + 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        value = self._head._element
        self._head = self._head._next
        self._size = self._size -1
        if self.is_empty():
            self._tail = None
        return value

    def first(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        return self._head._element

    def display(self):
        temp =self._head
        while temp:
            print(temp._element, end="-->")
            temp =temp._next
        print()