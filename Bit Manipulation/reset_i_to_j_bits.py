"""
Clear i to j bits -> change i to j bits to 0
"""
from unittest import TestCase

def clearItoJBits(num, i, j):
    mask1 =(~0) << (j+1)
    mask2 =2**i -1 # (1 <<i -1)
    mask = mask1 | mask2
    ans = num & mask
    return ans

print(clearItoJBits(119, 2, 4))

class TestclearItoJBits(TestCase):
    
    def test_clear_i_to_j_bits(self):
        self.assertEqual(bin(clearItoJBits(119, 2, 4))[2:], '1100011')

if __name__=='__main__':
    print("here")
    TestclearItoJBits().test_clear_i_to_j_bits()