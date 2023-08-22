def stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return stairs(n - 1) + stairs(n - 2)

def stairs1(n):
    var = s[n]
    s[1] =1
    s[2] =2
    for i in range(3,n): #  for i=3 to n
        s[i]=s[i-1]+s[i-2]
    return s[n]


print(stairs1(3))