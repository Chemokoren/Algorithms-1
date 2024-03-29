# x =[1,2,3]
# y =[4,5]
#
# print(x+y)
# print(x * 3)
#
class Person:
    def __init__(self,name):
        print("__init__")
        self.name =name
    def __repr__(self):
        print("__repr__")
        return f"Person({self.name})"
    def __mul__(self, x):
        print("__mul__")
        if type(x) is not int:
            raise Exception("Invalid argument, must be int")
        self.name =self.name * 4

    """
    The __call__ method can be useful for creating callable objects that maintain state, as well as
    for implementing function-like behavior for instances of a class.
    """
    def __call__(self,y):
        print("__call__")
        print("called this function", y)

    def __len__(self):
        print("__len__")
        return len(self.name)

p = Person("kibz")
res = p(5)
p * 4
print(p)

# print("########################################")
# m =Person("trial")
# m(4)
# print("##################__len__######################")
# lenP = Person("anii")
# print(len(lenP))
#
# print("################## Queue ######################")
# from queue import Queue
# import inspect
# q =Queue()
# print(q)
#
# print(inspect.getsource(Queue))
#
print("################## own implementation of a Queue ######################")

# from queue import Queue as q

# class Queue(q):
#     def __repr__(self):
#         return f"Queue({self._qsize()})"

#     def __add__(self,item):
#         self.put(item)
#     def __sub__(self, item):
#         self.get()

# qu = Queue()
# qu + 9
# print(qu)
# qu + 7
# print(qu)
# qu - 0
# print(qu)