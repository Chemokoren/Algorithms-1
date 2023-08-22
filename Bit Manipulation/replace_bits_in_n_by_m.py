"""
Replace "num" by M from i to j bits
num = "1001001"->73
M ="101"-> 5
i =2
j =4
ans ="1010101" -> 85

"""

def replaceNumByM(num, M, i, j):
    mask1 =(~0) << (j + 1)
    mask2 =(1 << i) -1
    mask = mask1 | mask2
    ans = num & mask
    M =M << i
    num = ans | M
    return num
print(replaceNumByM(73, 5, 2,4))
print(replaceNumByM(73, 3, 2,4))