"""
how many additions does it take to compoute that rec_naive(17,6) =102?
answer =17
Don't count subtractions, just additions. -MLL
"""

def rec_naive(a, b):
    if a == 0:
        return 0
    return b + rec_naive(a - 1, b)


print(rec_naive(17, 16))
