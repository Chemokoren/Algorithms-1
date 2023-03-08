"""
Clear i to j bits -> change i to j bits to 0
"""
import unittest

def clearItoJBits(num, i, j):
    mask1 = (~0)<< (j+1)
    #mask2 = (2**i) -1
    mask2 = (1 << i) -1
    mask = mask1 | mask2
    ans = num & mask
    return ans
print(clearItoJBits(119, 2, 4))

class TestComputation(unittest.TestCase):
    def test_clear_i_to_j_bits(self):
        self.assertEqual(bin(119)[2:], str(1110111))
    def test_return_value_expected(self):
        self.assertEqual(clearItoJBits(119, 2, 4), 99)
    
if __name__=='__main__':
    tt = TestComputation()
    tt.test_return_value_expected()
    tt.test_clear_i_to_j_bits()