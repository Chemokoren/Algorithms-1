"""
The idea that you can make recursive functions more efficient by making recursion the last
thing that you do.
"""
import unittest

class Solution:

    def tail_recursion(self, n, result):
        if n ==0:
            return result
        return self.tail_recursion(n-1, n*result)


class TestTailRecursion(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol =Solution()

    def test_tail_recursion(self):
        self.assertEqual(120, self.sol.tail_recursion(5,1))
        self.assertEqual(24, self.sol.tail_recursion(4,1))


# if __name__=="__main__":
#     unittest.main()


print("#################################")
def find_in_array(arr, target):

    if not arr:
        return False
    elif (target ==arr[0]):
        return True
    else:
        return (find_in_array(arr[1:], target))
    

print(find_in_array([1,2,4,5,8], 3))

print("################################# tail recursive implementation of factorial ################################# ")

"""
fact_tail(4) = fact_tail(4, 1)
                = fact_tail(3, 4)
                    = fact_tail(2,12)
                        = fact_tail(1, 24)
             = 24
"""

def fact_tail_inf(n : int, f: int):
    if n <= 1:
        return f
    else:
        return fact_tail_inf(n-1, f * n)
    
def fact_tail(n : int)-> int:
    return fact_tail_inf(n, 1)

print("manenos:: {}".format(fact_tail(4)))
print("manenos:: {}".format(fact_tail(5)))