from exceptions import Empty

class CircularLinkedList:
    class _Node:
        __slots__='_element','_next'

        def __init__(self,element, next) -> None:
            self._element =element
            self._next =next

    def __init__(self) -> None:
            self._head =None
            self._tail =None
            self._size =0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def add_first(self, e):
        newest =self._Node(e,None)
        if self.is_empty():
            newest._next =newest
            self._head =newest
            self._tail=newest
        else:
            self._tail._next =newest
            newest._next =self._head

        self._head =newest
        self._size +=1

    def add_last(self,e):
        newest =self._Node(e, None)
        if self.is_empty():
            self._head =newest
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next =newest
        self._tail = newest
        self._size += 1

    def add_any(self, e, pos):
        newest = self._Node(e,None)
        thead  = self._head
        i = 1
        while i < pos:
            thead =thead._next
            i += 1
        newest._next =thead._next
        thead._next = newest
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Empty('Linked List Empty')
        oldhead = self._tail._next
        self._tail._next = oldhead._next
        self._head = oldhead._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return oldhead._element


    def remove_last(self):
        if self.is_empty():
            raise Empty('Linked List Empty')
        thead = self._head
        i = 0
        while i < len(self) - 2:
            thead =thead._next
            i += 1
        self._tail = thead
        thead =thead._next
        self._tail._next =self._head
        value =thead._element
        self._size -=1
        return value

    def remove_any(self, pos):
        if self.is_empty():
            raise Empty('Linked List Empty')
        thead = self._head
        i = 1
        while i < pos - 1:
            thead = thead._next
            i += 1
        value = thead._next._element
        thead._next = thead._next._next
        self._size -=1
        return value

    def display(self):
        thead =self._head
        i = 0
        while i < len(self):
            print(thead._element, end='-->')
            thead =thead._next
            i += 1
        print()

CL = CircularLinkedList()
CL.add_last(10)
CL.add_last(20)
CL.add_last(30)
CL.add_last(40)
CL.display()
print('Deleted: ', CL.remove_first())
CL.display()
print('Add first: 70')
CL.add_first(70)
CL.display()
print('Deleted: ', CL.remove_last())
CL.display()
print('Add last: 80')
CL.add_last(80)
CL.display()




