from exceptions import Empty

class ArrayDeque:
    def __init__(self):
        self._data =[]
        self._front=0
    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('Deque is Empty')
        return self._data[self._front]
    
    def add_first(self, e):
        self._data.insert(self._front,e)
    
    def add_last(self, e):
        self._data.append(e)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is Empty')
        value = self._data.pop(self._front)
        return value

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is Empty')
        value =self._data.pop()
        return value

d = ArrayDeque()
d.add_last(10)
d.add_last(20)
d.add_last(30)
d.add_last(40)
d.add_last(50)

print('Deque: ', d._data)
print(" delete first")
d.delete_first()
print('\nDeque: ', d._data)
print(" delete last")
d.delete_last()
print('\nDeque: ', d._data)
print(" add first")
d.add_first(50)
print('\nDeque: ', d._data)
d.add_last(60)
print('\nDeque: ', d._data)
print('\nLength: ', d.__len__())