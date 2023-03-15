"""
Clear or change first i bits to 0
"""
def clearFirstIBits(num, i):
    number = num
    count = 0
    while(num > 0):
        num = num >> 1
        count += 1
    mask =(1 << (count - i)) - 1
    output = mask & number
    return output

print(clearFirstIBits(171, 4))
print(clearFirstIBits(171, 2))
