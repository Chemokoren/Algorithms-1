def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)


print(gcd(8,9))
print(gcd(3,9))