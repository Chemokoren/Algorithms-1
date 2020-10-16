x =[1,2,3]
y =[4,5]

print(x+y)
print(x * 3)

class Person:
    def __init__(self,name):
        self.name =name
    def __repr__(self):
        return f"Person({self.name})"
    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid argument, must be int")
        self.name =self.name *4

    def __call__(self,y):
        print("called this function", y)

    def __len__(self):
        return len(self.name)

p = Person("kibz")
p * 4
print(p)
print("########################################")
m =Person("trial")
m(4)
print("##################__len__######################")
lenP = Person("anii")
print(len(p))

print("################## Queue ######################")
from queue import Queue
import inspect
q =Queue()
print(q)

print(inspect.getsource(Queue))

print("################## own implementation of a Queue ######################")

from queue import Queue as q

class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"

    def __add__(self,item):
        self.put(item)
    def __sub__(self, item):
        self.get()

qu = Queue()
qu + 9
print(qu)
qu + 7
print(qu)
qu - 0
print(qu)