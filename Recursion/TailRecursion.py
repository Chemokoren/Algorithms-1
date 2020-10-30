def TailRecursion(n, result):
    if n ==0:
        return result
    return TailRecursion(n-1, n*result)

print(TailRecursion(5,1))