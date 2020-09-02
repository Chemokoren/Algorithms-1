# def solution(A):
    # write your code in Python 3.6
    # n =len(A)
    # abs_val=''
    # for i in range(n):
    #     abs_val =abs(A[0]+A[0])
    #     if abs(A[i]+A[j]) < abs_val:
    #         abs_val=abs(A[i]+A[j])
    # return abs_val

"""

Detected time complexity: O(N * log(N))

"""
from jinja2._compat import izip


def solution1(A):
    A.sort()
    ans = abs(A[0]) * 2
    p = 0
    q = len(A) - 1
    while (p < q):
        ans = min(ans, abs(A[p] + A[p]))
        ans = min(ans, abs(A[q] + A[q]))
        ans = min(ans, abs(A[p] + A[q]))
        if (ans == 0):
            return 0
        elif (A[p] + A[q] > 0):
            q=q-1
        else:
            p=p+1
        if ((A[p] > 0 and A[q] > 0) or (A[p] < 0 and A[q] < 0)):
            break

    return ans

# C-style python
def solution2(A):
    value = 2000000000
    front_ptr = 0
    back_ptr = len(A) - 1
    A.sort()

    while front_ptr <= back_ptr: value = min(value, abs(A[front_ptr] + A[back_ptr]))
    if abs(A[front_ptr]) > abs(A[back_ptr]):
        front_ptr += 1
    else:
        back_ptr -= 1

    return value


# Functional pythonesque:

from itertools import *
def getAbsDiff(t):
    return abs(t[0] + t[1])

def solution3(A):
    A.sort(key=abs)
    return getAbsDiff(min(chain(izip(A, A), izip(A, A[1:])), key=getAbsDiff))

def solution4(A):
    len_val = len(A)
    A.sort()
    begin = 0
    end = len_val - 1
    sum = abs(A[begin] + A[end])
    while (begin < end):
        newSum = 0
        if (abs(A[begin+1]+A[end]) < abs(A[begin]+A[end-1])):
            newSum = abs(A[begin+1]+A[end])
            begin =begin+1
        else:
            newSum = abs(A[begin]+A[end-1])
            end=end-1

        sum = min(sum, newSum)

    return sum

# A =[1, 4, -3]
A = [-8, 4, 5, -10, 3]

print(solution4(A))
