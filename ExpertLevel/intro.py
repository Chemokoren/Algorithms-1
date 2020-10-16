import inspect
from queue import Queue


def make_class(x):
    class Dog:
        def __init__(self,name):
            self.name =name
        def print_value(self):
            print(x)
    return Dog

cls = make_class(10)
d =cls("kibz")
print(d.name)
print(d.print_value())
print(cls)

for i in range(10):
    def show():
        print(i*2)

    show()

def func(x):
    if x == 1:
        def rv():
            print("X is equal to 1")
    else:
        def rv():
            print("X is not 1")
    return rv

new_func =func(1)
new_func()
print(inspect.getmembers(new_func))
print(inspect.getsource(new_func))
print(inspect.getsource(Queue))