"""
Set First i Bits of a number | Change First i Bits to 1
"""

def setFirstIBits(num, i):
    number = num
    count = 0
    while(num > 0):
        num = num >> 1
        count +=1
        
    mask = (( 1 << i) -1) << (count - i)
    output = mask | number
    
    return output

print(setFirstIBits(171, 4))
print(bin(251))