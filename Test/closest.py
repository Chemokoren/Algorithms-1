#!/bin/python3


#
# Complete the 'closestNumbers' function below.
#
# The function accepts INTEGER_ARRAY numbers as parameter.
#
def closestNumbers(numbers):
    min_diff = getMinimumDifference(numbers)
    n = len(numbers)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (abs(numbers[i] - numbers[j]) ==min_diff):
                if(numbers[j]>numbers[i]):
                    print(str(numbers[i])+" "+str(numbers[j]))
                else:
                    print(str(numbers[j])+" "+str(numbers[i]))


def getMinimumDifference(numbers):
    n = len(numbers)
    diff_val = 10 ** 20
    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(numbers[i] - numbers[j]) < diff_val:
                diff_val = abs(numbers[i] - numbers[j])
    return diff_val

