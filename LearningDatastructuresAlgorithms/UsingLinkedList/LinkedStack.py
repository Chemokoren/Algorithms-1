from exceptions import Empty

class LinkedStack:

    class _Node:
        __slot__='_element','_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head =None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0
    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size = self._size +1

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        value = self._head._element
        self._head = self._head._next
        self._size = self._size -1
        return value
    
    def top(self):
        if self.is_empty():
            raise Empty ('Stack is Empty')
        return self._head._element

    def display(self):
        thead = self._head
        while thead:
            print(thead._element, end="-->")
            thead =thead._next
        print()

LS = LinkedStack()
LS.push(10)
LS.push(20)
LS.push(30)
LS.push(40)
LS.display()
print('Popped: ', LS.pop())
LS.display()
LS.push(70)
LS.display()
print('Top Element: ', LS.top())
print('Popped: ', LS.pop())
LS.display()
            