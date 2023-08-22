"""
Program to Convert Decimal to Binary using Bitwise AND operator | Decimal to Binary Bitwise Operator
- Convert Decimal to Binary using Bitwise Operators
"""
from unittest import TestCase

def decimalToBinary(num):
    binary = list()
    while(num > 0):
        lastBit = num & 1
        num = num >> 1
        binary.append(str(lastBit))
    return "".join(binary[::-1])

print(decimalToBinary(171))
print(decimalToBinary(172341))

class TestDecimalToBinary(TestCase):
    
    def test_171_correct(self):
        self.assertEqual(decimalToBinary(171), bin(171)[2:])
        
if __name__=='__main__':
    TestDecimalToBinary().test_171_correct()