"""
Set i to j bits -> change i to j bits to 1

"""
from unittest import TestCase
def setItoJBits(num, i, j):
    N =j - i + 1
    mask = (1 << N) -1
    mask = mask << i
    ans = mask | num
    return ans

print(setItoJBits(171, 2, 4))

class TestSetItoJBits(TestCase):
    
    def test_set_2_to_4(self):
        self.assertEqual(bin(setItoJBits(171, 2, 4))[2:], '10111111')
        
if __name__=='__main__':
    tt = TestSetItoJBits()
    tt.test_set_2_to_4()