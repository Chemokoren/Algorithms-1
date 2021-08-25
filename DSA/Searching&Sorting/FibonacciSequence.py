def getFib(position):
    if (position == 0):
        return 0
    if (position == 1):
        return 1
    first = 0
    second = 1
    next = first + second
    for i in range(2,position):
        first = second
        second = next
        next = first + second
    return next

"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) +get_fib(position - 2)
        # return output
n = 4
if n <= 0:
    print("enter correct value")
else:
    for i in range(n):
        print(get_fib(i))

# Test cases
# print (getFib(4))
# print (get_fib(11))
# print (get_fib(0))


# print(getFib(4))
print("ddddddddddddddddddddddddddddd")
def fib(n):
    a = 0
    b = 1
    if n == 0:
        print(a)
    elif n == 1:
        print(b)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+ b
            a = b
            b = c
            print(c)


fib(4)


