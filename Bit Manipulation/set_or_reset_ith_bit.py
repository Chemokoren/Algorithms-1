"""
Set or Reset ith Bit | Change ith bit to 0 or 1 | change Kth bit to 0 or 1
"""
def changeIthBit(num, i, value):
    mask1 = 1 << i
    mask1 = ~ mask1
    res = num & mask1
    mask2 = value << i
    res = res | mask2
    return res

print(changeIthBit(13,1,1))
print(changeIthBit(13,2,0))