# x =[i**2 for i in range(1000000000000)]
#
# for el in x:
#     print(el)

# for i in range(1000000000000):
#     print(i**2)


# class Gen:
#     def __init__(self,n):
#         self.n =n
#         self.last =0
#
#     def next(self):
#         if self.last == self.n:
#             raise StopIteration()
#
#         rv =self.last ** 2
#         self.last += 1
#         return rv
#
# g = Gen(100)
#
# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break

def gen(n):
    for i in range(n):
        yield i**2

g =gen(100)
# for i in g:
#     print(i)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


print("############################################")
import sys
def gen(n):
    for i in range(n):
        yield i**2

x =[i ** 2 for i in range(10000)]
g =gen(10000)
print(sys.getsizeof(x))
print(sys.getsizeof(g))