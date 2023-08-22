def factorial(n):
    prod =1
    for i in range(1,n+1):
        prod = prod*i
    return prod

def recursiveFactorial(n):
    if n <=1:
        return n
    return recursiveFactorial(n-1) * recursiveFactorial(n-2)

print(recursiveFactorial(0))
