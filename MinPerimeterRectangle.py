
"""
1. MinPerimeterRectangle
Find the minimal perimeter of any rectangle whose area equals N.
Task Score
20%
Correctness
40%
Performance
0%
Task description
An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.
Write a function:

def solution(N)

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000,000].
"""



def solution(N):
    my_list =[]
    minimal_perimeter =1000000000
    for i in range(1,N):
        if N%i ==0:
            my_list.append(i)
    for j in range(1,len(my_list)):
        if (2*((N//j)+j)) < minimal_perimeter:
            minimal_perimeter = (2*((N//j)+j))

    return minimal_perimeter

#solution 1 Detected time complexity: O(sqrt(N))
import math
def solution1(N):
    n = math.sqrt(N)
    min = math.inf
    p =None
    for i in range(1, int(n)):
        if N%i==0:
            p = 2*(i+N/i)
            if p<min:
                min = p

    return min

print(solution1(1000000000))
