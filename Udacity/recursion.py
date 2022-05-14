"""
Fibonacci Sequence

You start with 0 and 1. 
0 + 1 = 1, so you add 1 to the sequence. 
1 + 1 = 2, so 2 is added. 
1 + 2 = 3, so 3. 
2 + 3 = 5, et cetera. 

"""

def fibIterative(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        first = 0
        second =1
        next = first + second
        for i in range(2,n):
            first = second
            second = next
            next = first + second
    return next

print("###################### Iterative fibonacci ######################\n")

print("expected: 0, actual:", fibIterative(0))  # 0
print("expected: 1, actual:", fibIterative(1))  # 1
print("expected: 1, actual:", fibIterative(2))  # 1
print("expected: 2, actual:", fibIterative(3))  # 2
print("expected: 3, actual:", fibIterative(4))  # 3
print("expected: 5, actual:", fibIterative(5))  # 5
print("expected: 8, actual:", fibIterative(6))  # 8
print("expected: 13, actual:", fibIterative(7)) # 13
print("expected: 21, actual:", fibIterative(8)) # 21
print("expected: 34, actual:", fibIterative(9)) # 34


print("###################### Recursive fibonacci ######################")
def fibRecursive(n):
    if n == 0 or n ==1:
        return n
    return fibRecursive(n -1) + fibRecursive(n -2)


print("expected: 0, actual:",  fibRecursive(0))  # 0
print("expected: 1, actual:",  fibRecursive(1))  # 1
print("expected: 1, actual:",  fibRecursive(2))  # 1
print("expected: 2, actual:",  fibRecursive(3))  # 2
print("expected: 3, actual:",  fibRecursive(4))  # 3
print("expected: 5, actual:",  fibRecursive(5))  # 5
print("expected: 8, actual:",  fibRecursive(6))  # 8
print("expected: 13, actual:", fibRecursive(7))  # 13
print("expected: 21, actual:", fibRecursive(8))  # 21
print("expected: 34, actual:", fibRecursive(9))  # 34