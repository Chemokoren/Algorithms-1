def solution(N, M):
    # write your code in Python 3.6
    number_times = 0
    x = 0
    for i in range(0, N, ((x + M)) % N):
        if i == 0 or i == N - 1:
            number_times = 1 + number_times + 1
        if i % M == 0:
            number_times = 1 + number_times + 1
        x = x + i

    return number_times


def gcd(a, b):
    # Get the greatest common divisor
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)


# solution 3
def solution3(N, M):
    lcm = N * M // gcd(N, M)  # Least common multiple
    return lcm // M


# solurion1
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

# Detected time complexity:
# O(log(N + M))
#  Task Score  87%
# Correctness 100%
# Performance 75%


def solution2(N, M):
    """

    :param N:
    :param M:
    :return:
    """

    # We start eating the first candy
    start_eating = 0
    count = 0

    while True:
        # we eat the following candies.
        # Remember we ate one already
        count += 1 + ((N - start_eating - 1) // M)
        # Some are left at the end
        left_candies = (N - start_eating - 1) % M
        # In the next iteration we start eating at a different place
        start_eating = M - left_candies - 1
        # if we are back at candy 0 means we are done
        if start_eating == 0:
            break

    return count


def solution(N, M):
    # write your code in Python 3.6
    number_times = 0
    x = 0
    for i in range(0, N, ((x + M)) % N):
        if i == 0 or i == N - 1:
            number_times = number_times + 1
        if i % M == 0:
            number_times = number_times + 1
        x = x + i

    return number_times


# Task Score 50%
# Correctness 100%
# Performance 0%
# Detected time complexity:
# O(N + M)

def solution4(N, M):
    eaten = [False] * N

    at = 0

    cnt = 0

    while eaten[at] != True:
        eaten[at] = True

        at = (at + M) % N

        cnt += 1

    return cnt


def solution5(N, M):
    if (M % N == 0):
        return 1
    if (N % M == 0):
        return N / M
    ate = []
    pos = 0
    count = 0
    while ate[pos] not in ate:
        ate[pos] = True
        count = count + 1
        pos = (pos + M) % N

    return count


class Solution {
public int solution(int N, int M)
{
# write your code in Java SE 8
int gcd; long ans; gcd = eatChocolate(N, M); ans = N / gcd;


return (int)
ans;} int
eatChocolate(int
a, int
b){ if (b == 0)
{
return a;}
return eatChocolate(b, a % b);}}



public int solution(int N, int M)
{
long pos = 0;
int ans =0;
while(!(pos >= N && pos%N == 0))
{
    pos += M; ans ++;
}

return ans;
}



public int solution(int N, int M) { // write your code in Java SE 8 int[] coList = new int[N]; int pos = 0; int ans = 0; while(coList[pos] == 0){ coList[pos] = 1; ans++; if(pos + M >= N) { pos = (pos + M)%N; }else{ pos = pos+M; } } return ans; }


print(solution3(10, 4))
