""""""
def setLastIBits(num, i):
    mask = (i << i) - 1
    ans = num | mask
    return ans

print(setLastIBits(178, 3))