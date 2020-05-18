#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the absolute value of the difference
# between each element in L and x: SUM_{i=0}^{n-1} |L[i] - x|
#
# Your code should run in Theta(n) time
#


def minimize_absolute(L):
    x = 0
    for i in range(len(L)):
        if x < abs(L[i]-x):
            x=abs(L[i]-x)
    return x

L=[6, 5, 4, 5]
# L=[10,3,9,50,23,67,34]
print(minimize_absolute(L))

