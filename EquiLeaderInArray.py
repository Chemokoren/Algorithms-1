"""
1. EquiLeader
Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.
Task description
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].

"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# solution 1
# Detected time complexity: O(N)
def solution1(A):
    A_len = len(A)
    candidate = -1
    candidate_count = 0
    candidate_index = -1
    # Find out a leader candidate
    for index in range(A_len):
        if candidate_count == 0:
            candidate = A[index]
            candidate_index = index
            candidate_count += 1
        else:
            if A[index] == candidate:
                candidate_count += 1
            else:
                candidate_count -= 1
    # Make sure the candidate is the leader
    leader_count = len([number for number in A if number == candidate])
    if leader_count <= A_len // 2:
        # The candidate is not the leader
        return 0
    else:
        leader = candidate
    equi_leaders = 0
    leader_count_so_far = 0
    for index in range(A_len):
        if A[index] == leader:
            leader_count_so_far += 1
        if leader_count_so_far > (index + 1) // 2 and leader_count - leader_count_so_far > (A_len - index - 1) // 2:
            # Both the head and tail have leaders of the same value
            # as "leader"
            equi_leaders += 1
    return equi_leaders


# solution 2
from collections import defaultdict


def solution(A):
    # write your code in Python 3.6
    marker_l = defaultdict(lambda: 0)
    marker_r = defaultdict(lambda: 0)

    for i in range(len(A)):
        marker_r[A[i]] += 1

    n_equi_leader = 0
    leader = A[0]
    for i in range(len(A)):
        marker_r[A[i]] -= 1
        marker_l[A[i]] += 1

        if i == 0 or marker_l[leader] < marker_l[A[i]]:
            leader = A[i]

        if (i + 1) // 2 < marker_l[leader] and (len(A) - (i + 1)) // 2 < marker_r[leader]:
            n_equi_leader += 1

    return n_equi_leader


# solution 3
def solution3(A):
    # write your code in Python 2.7
    size = len(A)
    cnt, cnt1, s, ans = 0, 0, 0, 0
    for i in A:
        if 0 == cnt:
            s = i
        if s == i:
            cnt += 1
        else:
            cnt -= 1
    cnt = A.count(s)
    if cnt > size // 2:
        for i in range(size):
            if A[i] == s:
                cnt1 += 1
            if cnt1 > (i + 1) // 2 and cnt - cnt1 > (size - 1 - i) // 2:
                ans += 1
    return ans


# solution 4
def solution4(A):
    n = len(A)
    size = 0
    for k in range(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1
    candidate = -1
    if (size > 0):
        candidate = value
    leader = -1
    count = 0
    Acopy = []
    for k in range(n):
        Acopy.append(A[k])
        if (A[k] == candidate):
            count += 1
    if (count > n // 2):
        leader = candidate
    result = 0
    max_occ = A.count(leader)
    if leader == -1:
        return 0
    else:
        cntLeft = 0
        cntRight = max_occ
        for q in range(0, n - 1):
            if A[q] == leader:
                cntLeft += 1
                cntRight -= 1
            lenL = q + 1
            lenR = n - q - 1
            if lenL // 2 + 1 <= cntLeft and lenR // 2 + 1 <= cntRight:
                result += 1
    return result


# solution 5
from collections import Counter


def solution5(A):
    result = 0
    b = Counter(A)
    maxinstance = b.most_common(1)
    max = maxinstance[0]
    maxinstance, count = max
    count = len(A)
    for index, num in enumerate(A):
        first = A[:index + 1]
        second = A[index + 1:]
        temp = (index + 1) / 2.0
        if (first.count(maxinstance) > temp) and (second.count(maxinstance) > ((count - index - 1) / 2)):
            result += 1
    return result


# solution 6
def solution(A):
    # write your code in Python 3.6
    candidate = []
    for i, v in enumerate(A):
        if len(candidate) == 0 or v == candidate[-1]:
            candidate.append(v)
        elif v != candidate[-1]:
            candidate.pop()

    try:
        count = A.count(candidate[0])
    except:
        count = 0

    if count <= len(A) // 2:
        return 0

    p1_len = 0
    p2_len = len(A)
    p1_count = 0
    p2_count = count
    equi = 0
    for i, v in enumerate(A):
        p1_len += 1
        p2_len -= 1
        if v == candidate[0]:
            p1_count += 1
            p2_count -= 1
        if p1_count > p1_len // 2 and p2_count > p2_len // 2:
            equi += 1
    return equi
