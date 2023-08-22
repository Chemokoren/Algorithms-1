from exceptions import Empty

class LinkedDeque:

    class _Node:
        __slots__ ='_element', '_next'

        def __init__(self,element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        self._head =None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, e):
        newNode =self._Node(e, None)
        if self.is_empty():
            self._head = newNode
            self._tail = newNode
        else:
            newNode._next =self._head
        self._head= newNode
        self._size +=1

    def add_last(self, e):
        newNode = self._Node(e, None)
        if self.is_empty():
            self._head = newNode
            self._tail =newNode
        else:
            self._tail._next =newNode
        self._tail=newNode
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        val =self._head._element
        self._head = self._head._next
        self._size -=1
        if self.is_empty():
            self._tail = None
        return val

    def remove_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        thead = self._head
        i =0
        while(i < len(self)-2):
            thead = thead._next
            i += 1
        self._tail =thead
        val = thead._next._element
        self._tail._next = None
        self._size +=1
        return val

    def first(self):
        if self.is_empty():
            raise Empty('Deque is Empty')
        return self._head._element

    def last(self):
        if self.is_empty():
            raise Empty('Deque is Empty')
        thead = self._head
        i = 0
        while i< self._size-3:
            thead = thead._next
            i += 1
        return thead._element


    
    def display(self):
        thead = self._head
        while thead:
            print(thead._element, end="-->")
            thead = thead._next
        print()

LD = LinkedDeque()
LD.add_first(10)
LD.add_first(20)
LD.add_first(30)
LD.display()
LD.add_last(70)
LD.add_last(90)
LD.add_first(1)
LD.display()
LD.remove_first()
LD.remove_first()
LD.display()
LD.remove_last()
LD.display()
print('First: ', LD.first())
print('Last: ', LD.last())
LD.display()


