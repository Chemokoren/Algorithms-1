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

def getFib1(position):
    if position == 0 or position == 1:
        return position
    first, second = 0, 1
    for _ in range(2, position):
        first, second = second, first + second
    return first + second


def get_fib(position):
    """
    recursively Fibonacci sequence """
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)


print("aaa::", get_fib(4))


