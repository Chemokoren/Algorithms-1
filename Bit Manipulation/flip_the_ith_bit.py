from unittest import TestCase

def flipIthBit(num, i):
    mask = 1 << i
    ans = num ^ mask
    return ans

print(flipIthBit(171, 3))
print(flipIthBit(171, 6))

class FlipBitTest(TestCase):
    
    def test_flipping_3rd_bit(self):
        self.assertEqual(bin(flipIthBit(171, 3))[2:], '10100011')
        
    def test_flipping_6th_bit(self):
        self.assertEqual(bin(flipIthBit(171, 6))[2:], '11101011')
        
        
if __name__=='__main__':
    tt = FlipBitTest()
    tt.test_flipping_3rd_bit()
    tt.test_flipping_6th_bit()