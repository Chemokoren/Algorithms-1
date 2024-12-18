from exceptions import Empty

class ArrayStack:
    def __init__(self) -> None:
        self._data =[]

    def my_len(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data[-1]

s =ArrayStack()
s.push(10)
s.push(20)
print('Stack: ', s._data)
print('Length: ', s.my_len())
print('Is-Empty: ', s.is_empty())
print('Popped: ', s.pop())
print('Stack: ', s._data)
print('Popped: ', s.pop())
print('Is-Empty: ', s.is_empty())
print('Stack: ', s._data)
print(" push 30, 40")
s.push(30)
s.push(40)
print('Stack: ', s._data)
print('Top Element: ', s.top())