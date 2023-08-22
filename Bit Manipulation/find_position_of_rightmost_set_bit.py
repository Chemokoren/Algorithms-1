"""
Find position of rightmost set bit | Find the right most set bit of a number | Find first 1 Set Bit
Find position of First 1 (Set Bit) From Right Side
"""

def firstSetBitFromRight(num):
    if (num == 0):
        return -1
    position = 0
    while(num & 1 == 0):
        position += 1
        num = num >> 1
    return position

print(firstSetBitFromRight(176))
print(firstSetBitFromRight(0))
print(firstSetBitFromRight(1716))