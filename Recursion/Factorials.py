def factorial(n):
    result =1
    for i in range(1,n):
        result *= i
    return result

def recursiveFactorial(n):
    if n==1:
        return 1
    return n * recursiveFactorial(n-1)

print(recursiveFactorial(4))