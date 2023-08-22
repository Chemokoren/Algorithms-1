# def solution(A, X):
#     N = len(A)
#     if N == 0:
#         return -1
#     l = 0
#     r = N - 1
#     while l < r:
#         m = (l + r) // 2
#         if A[m] > X:
#             r = m - 1
#         else:
#             l = m
#     if A[l] == X:
#         return l
#     return -1

def solution(A, X):
    N = len(A)
    if N == 0:
        return -1
    l = 0
    r = N - 1
    while l < r:
        m = (l + r) // 2
        if A[m] > X:
            r = m - 1
        elif A[m] < X:
            l = m
        else:
            return m

my_array =[1, 2, 5, 9, 9]
val= 5
print(solution(my_array,5))
