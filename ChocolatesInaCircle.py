def solution(N, M):
    # write your code in Python 3.6
    number_times=0
    x =0
    for i in range(0,N,((x+M))%N):
        if i==0 or i==N-1:
            number_times =1+number_times+1
        if i%M ==0:
            number_times =1+number_times+1
        x =x+i

    return number_times


def gcd(a, b):
    # Get the greatest common divisor
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)
#solution 3
def solution3(N, M):
    lcm = N * M / gcd(N, M) # Least common multiple
    return lcm / M

#solurion1
# def solution1(N, M):
#     # write your code in Python 3.6
#     if (M == 1):
#         return N
#     if (M == N):
#         return 1
#
#     a = N
#     b = M
#     while (b != 0):
#         {
#             temp_val = b
#             b = a % b
#             a = temp_val
#
#
#         }
#
#     return N / a


def solution2(N,M):

    # We start eating the first candy
    start_eating = 0
    count = 0

    while True:
        # we eat the follwing candies.
        # Remember we ate one already
        count += 1 + ( (N - start_eating - 1) // M)
        # Some are left at the end
        left_candies = (N - start_eating - 1) % M
        # In the next iteration we start eating at a different place
        start_eating = M - left_candies - 1
        # if we are back at candy 0 means we are done
        if start_eating == 0:
            break

    return count

print(solution3(10,4))
