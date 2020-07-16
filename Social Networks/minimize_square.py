#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the square of the difference
# between each element in L and x: SUM_{i=0}^{n-1} (L[i] - x)^2
#
# Your code should run in Theta(n) time
#

def minimize_square(L):
    x = 0
    y = 0
    for i in range(len(L)):
        if ((L[i] - x) * (L[i] - x) < y):
            y = (L[i] - x) * (L[i] - x)
    return x


# L=[10,3,9,50,23,67,34]
L = [1, 2, 3]
print(minimize_square(L))

# Incorrect. Your submission did not return the correct result for the input [1, 2, 3]. Your submission passed 0 out of 4 test cases
