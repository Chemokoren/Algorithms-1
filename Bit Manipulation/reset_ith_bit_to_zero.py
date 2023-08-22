"""
Reset ith bit to 0 | Change ith bit to 0 | Clear Kth bit of binary number
"""

def clearIthBit(num, i):
    mask = 1 << i
    mask =~mask
    num = num & mask
    return num

print(clearIthBit(13, 2))