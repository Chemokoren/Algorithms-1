"""
Clear last i bits -> change last i bits to 0
"""
def  clearLastIBits(num, i):
    mask =(~0) << i
    num &= mask
    return num

print(clearLastIBits(13, 3))