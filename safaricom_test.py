def count_negative(array, given_number):
    return given_number in array

def solution(A):
    n = len(A)
    largest = 0
    for i in range(n):
            if A[i] > largest and count_negative(A,-A[i])==True:
                    largest = A[i]

    return largest
# my_array =[3, 2, -2, 5,-3]
my_array =[1, 2, 3, -4]

print(solution(my_array))




#
# print(count_negative(my_array,-3))




# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(A):
    res = 0
    h = 0
    i = 0
    for i in range(len(A)-1):
        if (A[i+1]):
            if A[i] == A[i+1]:
                res +=1
            if (h >= 2):
                res +=1
                h = 0
            if (A[i] < A[i+1]):
                h +=1
            if (h <= -2):
                res +=1
                h = 0
            if A[i] > A[i+1]:
                h -=1
    return res