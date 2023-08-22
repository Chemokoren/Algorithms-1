"""
Tasks Details
Medium
1. Peaks
Divide an array into the maximum number of same-sized blocks, each of which should contain an index P such that A[P - 1] < A[P] > A[P + 1].
Task Score
45%
Correctness
83%
Performance
0%
Task description
A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbors. More precisely, it is an index P such that 0 < P < N − 1,  A[P − 1] < A[P] and A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly three peaks: 3, 5, 10.

We want to divide this array into blocks containing the same number of elements. More precisely, we want to choose a number K that will yield the following blocks:

A[0], A[1], ..., A[K − 1],
A[K], A[K + 1], ..., A[2K − 1],
...
A[N − K], A[N − K + 1], ..., A[N − 1].
What's more, every block should contain at least one peak. Notice that extreme elements of the blocks (for example A[K − 1] or A[K]) can also be peaks, but only if they have both neighbors (including one in an adjacent blocks).

The goal is to find the maximum number of blocks into which the array A can be divided.

Array A can be divided into blocks as follows:

one block (1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2). This block contains three peaks.
two blocks (1, 2, 3, 4, 3, 4) and (1, 2, 3, 4, 6, 2). Every block has a peak.
three blocks (1, 2, 3, 4), (3, 4, 1, 2), (3, 4, 6, 2). Every block has a peak. Notice in particular that the first block (1, 2, 3, 4) has a peak at A[3], because A[2] < A[3] > A[4], even though A[4] is in the adjacent block.
However, array A cannot be divided into four blocks, (1, 2, 3), (4, 3, 4), (1, 2, 3) and (4, 6, 2), because the (1, 2, 3) blocks do not contain a peak. Notice in particular that the (4, 3, 4) block contains two peaks: A[3] and A[5].

The maximum number of blocks that array A can be divided into is three.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximum number of blocks into which A can be divided.

If A cannot be divided into some number of blocks, the function should return 0.

For example, given:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000].
"""
#Detected time complexity: O(N)
A =[1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
# 45% performance
def solution(A):
    number_picks = 0
    for i in range(1, len(A) - 1):
        if A[i] > A[i + 1] and A[i] > A[i - 1]:
            number_picks = number_picks + 1
    return number_picks


def solution1(A):
    N = len(A)
    peaks = []
    for i in range(1,N-1):
        if (A[i] > A[i-1] and A[i] > A[i+1]):
            peaks.append(i);

    for size in range(1,N):
        if(N % size != 0):
            continue
        find = 0
        groups = N/size
        ok = True
        for peakIdx in range(len(peaks)):
            if (peakIdx/size > find):
                ok = False
                break;
            if(peakIdx/size == find):
                find =find+1
        if(find != groups):
            ok = False
        if(ok):
            return groups
        else:
            return 0

#Task Score 100% Correctness 100% Performance 100%
def solution2(A):
    length = len(A)
    if length <= 2:
        return 0

    peek_indexes = []
    for index in range(1, length-1):
        if A[index] > A[index - 1] and A[index] > A[index + 1]:
            peek_indexes.append(index)

    for block in range(3, int((length/2)+1)):
        if length % block == 0:
            index_to_check = 0
            temp_blocks = 0
            for peek_index in peek_indexes:
                if peek_index >= index_to_check and peek_index < index_to_check + block:
                    temp_blocks += 1
                    index_to_check = index_to_check + block
            if length/block == temp_blocks:
                return temp_blocks

    if len(peek_indexes) > 0:
        return 1
    else:
        return 0

# Detected time complexity:
# O(N * log(log(N)))
def solution3(data):

    length = len(data)

    # array ends can't be peaks, len < 3 must return 0
    if length < 3:
        return 0

    peaks = [0] * length

    # compute a list of 'peaks to the left' in O(n) time
    for index in range(2, length):
        peaks[index] = peaks[index - 1]

        # check if there was a peak to the left, add it to the count
        if data[index - 1] > data[index - 2] and data[index - 1] > data[index]:
            peaks[index] += 1

    # candidate is the block size we're going to test
    for candidate in range(3, length + 1):

        # skip if not a factor
        if length % candidate != 0:
            continue

        # test at each point n / block
        valid = True
        index = candidate
        while index != length:

            # if no peak in this block, break
            if peaks[index] == peaks[index - candidate]:
                valid = False
                break

            index += candidate

        # one additional check since peaks[length] is outside of array
        if index == length and peaks[index - 1] == peaks[index - candidate]:
            valid = False

        if valid:
            return length / candidate

    return 0


print(solution3(A))

