from exceptions import Empty

class ArrayQueue:
    def __init__(self) -> None:
        self._data =[]
        self._size =0
        self._front=0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        self._data.append(e)
        self._size =self._size + 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is Empty')

        value = self._data[self._front]
        self._data[self._front] =None
        self._front =self._front + 1
        self._size =self._size -1
        return value

    def first(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        return self._data[self._front]
    

s =ArrayQueue()
s.enqueue(10)
s.enqueue(20)
print('Queue: ', s._data)
print('Length: ', s.__len__())
print('Is-Empty: ', s.is_empty())
print('Dequeue: ', s.dequeue())
print('Queue: ', s._data)
print('Dequeue: ', s.dequeue())
print('Is-Empty: ', s.is_empty())
print('Queue: ', s._data)
s.enqueue(30)
s.enqueue(40)
print('Queue: ', s._data)