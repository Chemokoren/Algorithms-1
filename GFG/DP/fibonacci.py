# iterative
def iterativeFib(n):
    sum =0
    for i in range(0,n+1):
        if i <= 1:
            sum =i
        else:
            sum =i-1+(i-2)
        print(i,sum)
    #     if i >=2:
    #         sum =i + i-1
    # return sum


# Recursive
def fib(n):
    if n <=1:
        return n
    return fib(n-1) + fib(n-2)

# Dynamic Programming solution
def fib1(n):
    f = [0] * n
    f[0] =0
    f[1] =1
    for i in range(2,n-1):
        f[i] =f[n-1] +f[n-2]
    return f[n]

# print("Base case: "+ str(fib(2)))
print(iterativeFib(2))
