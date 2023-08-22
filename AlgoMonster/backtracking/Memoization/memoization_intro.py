"""
Memoization

Memoization is a fancy word for a simple concept(so is the case for alot of things we learn at 
school). It means saving the previous function call result in a dictionary and reading from it
when we do the exact same call. The word is meant to mean writing down on a "memo".
A classic example is calculating Fibonacci number



"""
def fib(n):
    if n ==0 or n== 1:
        return n
    return fib(n-1) +fib(n-2)

# This results in alot of repeated computations
"""
The solution is simply saving previous results in a map of function argument to results(the "memo")
and checking it and returning previous results if it has been done before. Otherwise, we carry out
the computation and save the results in the map.

"""
def fib(n, memo):
    if n in memo: # check n memo, if found, retrieve and return right away
        return memo[n]
    if n== 0 or n == 1:
        return n
    res = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = res# save in memo before returning 
    return res

# Memoization is particularly useful for combinatorial problems that have large repeated
# state-space tree branches.

