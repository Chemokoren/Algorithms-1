"""
Find whether a number is EVEN or ODD
1 - % (Modulo operator)
2 - & (Bitwise AND operator)

"""
def even_odd_and(num):
    if(num & 1 ==1):
        return f"{num} is odd"
    return f"{num} is even"

print(even_odd_and(20))
print(even_odd_and(21))