"""
a.b =x.y+z
63.12=20.12+z
756-240 =z
z=516

"""


def naive(a,b):
    x =a;y = b
    z = 0
    while x > 0:
        z =z + y
        x =x -1
    return z

print(naive(63,12))
