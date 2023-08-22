# O(2^n) time | O(n) space =naive recursive solution
def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n-1) + getNthFib(n-2)

# O(n) time | O(n) space
def getNthFib1(n, memoize = {1:0,2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] =getNthFib1(n -1, memoize) + getNthFib1(n - 2, memoize)
        return memoize[n]

# version 2 of memoization
def fib (n,memo):
    if memo[n] is not None: # if memo[n] != null:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result =fib(n-1,memo) + fib(n-2,memo)
    memo[n] =result
    return result

def fib_memo(n):
    memo =[None] * (n + 1)
    return fib(n,memo)

# O(n) time | O(1) space
def getNthFib2(n):
    lastTwo =[0,1]
    counter =3
    while counter <= n:
        nextFib =lastTwo[0] + lastTwo[1]
        lastTwo[0] =lastTwo[1]
        lastTwo[1] =nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]


# bottom-up approach

def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n + 1 ):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

    # for i in range(3,n):  #  for i from 3 upto n:
    #     bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    # return bottom_up[n]

print(getNthFib2(20))
print(fib_memo(20))
print(getNthFib1(20))
print(getNthFib(20))
print(fib_bottom_up(10000))


# 0,1,1,2,3,5,8,13,21,34
