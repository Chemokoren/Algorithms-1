"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

A = [1, 3, 6, 4, 1, 2]
# def solution(A):
#     # write your code in Python 3.6
#     p =[]
#     A.sort()
#     val_arr= list(range(1, A[len(A)-1]+2))
#     diff_val= set(val_arr).difference(A)
#     return min(diff_val)

# def solution(A):
#     a=frozenset(sorted(A))
#     m=max(a)
#     if m>0:
#         for i in range(1,m):
#             if i not in a:
#                 return i
#             else:
#                 return m+1
#         else:
#             return 1

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    max_A=max(A)
    B=set([a if a>=0 else 0 for a in A ])
    b=1
    if max_A<=0:
        return(1)
    else:
        while b in B:
            b+=1
        return(b)

print(solution(A))
