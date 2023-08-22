# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""
Tasks Details
Medium
1. NailingPlanks
Count the minimum number of nails that allow a series of planks to be nailed.
Task Score
100%
Correctness
100%
Performance
100%
Task description
You are given two non-empty arrays A and B consisting of N integers. These arrays represent N planks. More precisely, A[K] is the start and B[K] the end of the K−th plank.

Next, you are given a non-empty array C consisting of M integers. This array represents M nails. More precisely, C[I] is the position where you can hammer in the I−th nail.

We say that a plank (A[K], B[K]) is nailed if there exists a nail C[I] such that A[K] ≤ C[I] ≤ B[K].

The goal is to find the minimum number of nails that must be used until all the planks are nailed. In other words, you should find a value J such that all planks will be nailed after using only the first J nails. More precisely, for every plank (A[K], B[K]) such that 0 ≤ K < N, there should exist a nail C[I] such that I < J and A[K] ≤ C[I] ≤ B[K].

For example, given arrays A, B such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10
four planks are represented: [1, 4], [4, 5], [5, 9] and [8, 10].

Given array C such that:

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
if we use the following nails:

0, then planks [1, 4] and [4, 5] will both be nailed.
0, 1, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, 3, then all the planks will be nailed.
Thus, four is the minimum number of nails that, used sequentially, allow all the planks to be nailed.

Write a function:

def solution(A, B, C)

that, given two non-empty arrays A and B consisting of N integers and a non-empty array C consisting of M integers, returns the minimum number of nails that, used sequentially, allow all the planks to be nailed.

If it is not possible to nail all the planks, the function should return −1.

For example, given arrays A, B, C such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..30,000];
each element of arrays A, B, C is an integer within the range [1..2*M];
A[K] ≤ B[K].

"""

# Detected time complexity:
# O((N + M) * log(M))

PLANK_START = 0
PLANK_END = 1

NAIL_ARR_IDX = 0
NAIL_HIT_LOCATION = 1


class NoNailFoundException(Exception):
    def __init__(self):
        pass


def findPosOfNail(nails, plank, previous_max):
    nail_idx = -1
    result = -1

    # logarithmic scan O(log(M))
    lower_idx = 0
    upper_idx = len(nails) - 1

    while lower_idx <= upper_idx:
        mid_idx = (lower_idx + upper_idx) // 2
        if nails[mid_idx][NAIL_HIT_LOCATION] < plank[PLANK_START]:
            lower_idx = mid_idx + 1
        elif nails[mid_idx][NAIL_HIT_LOCATION] > plank[PLANK_END]:
            upper_idx = mid_idx - 1
        else:
            upper_idx = mid_idx - 1
            result = nails[mid_idx][PLANK_START]
            nail_idx = mid_idx

    if result == -1:
        raise NoNailFoundException

    # linear scan O(M)
    nail_idx += 1
    while nail_idx < len(nails):
        if nails[nail_idx][NAIL_HIT_LOCATION] > plank[PLANK_END]:
            break
        result = min(result, nails[nail_idx][NAIL_ARR_IDX])
        if result <= previous_max:
            return result
        nail_idx += 1

    if result == -1:
        raise NoNailFoundException

    return result


def getNrNailsRequired(planks, nails):
    result = 0
    for plank in planks:
        result = max(result, findPosOfNail(nails, plank, result))

    return result + 1


def solution(A, B, C):
    planks = zip(A, B)

    nails = sorted(enumerate(C), key=lambda var: var[1])

    try:
        return getNrNailsRequired(planks, nails)
    except NoNailFoundException:
        return -1

# solution 2
def solution2(A, B, C):
    result = -1         # Global result
    # Sort the planks according to firstly their begin position,
    # and then their end position
    planks = zip(A, B)
    planks.sort()
    # Sort the nails according to their position
    nails = sorted(enumerate(C), key = lambda x: x[1])
    nailsIndex = 0
    # Travel for each plank
    for plankIndex in range(len(planks)):
        plank = planks[plankIndex]
        # Find the first quanified nail in linear manner. Beware
        # that the planks are sorted. For any two adjacent planks,
        # the begin position of the latter one will be:
        #   either the same as the former's begin position
        #   or after the former's
        # In both cases, the nails, which before the nailsIndex
        # of the former plank's round, would never be candidates
        # in the latter plank's round. Thus we only need to search
        # nails from the previous nailsIndex position.
        while nailsIndex < len(nails):
            if nails[nailsIndex][1] < plank[0]:
                nailsIndex += 1
            elif nails[nailsIndex][1] > plank[1]:
                # And all the remaining nails > plank[1]
                # Impossible to find a quanlified nail
                return -1
            else:
                # plank[0] <= nails[nailsIndex][1] <= plank[1]
                break
        else:
            # Cannot find one
            return -1
        if plankIndex != 0 and plank[0] == planks[plankIndex-1][0]:
            # This plank and previous plank have the same begin
            # position. And the planks are sorted. So the end
            # position of this plank is after that of previous
            # plank. We continue the previous search.
            pass
        else:
            # This plank and previous plank have the different
            # begin position. We have to re-search from the
            # nailsIndex.
            tempRes = len(nails)  # Local result for this round
            tempIndex = nailsIndex
        # Find the first one in all the quanlified nails
        while tempIndex < len(nails) and plank[0] <= nails[tempIndex][1] <= plank[1]:
            tempRes = min(tempRes, nails[tempIndex][0])
            tempIndex += 1
            # If we find a tempRes <= result, the final result
            # of current round will <= result. This tempRes
            # would never change the global result. Thus we
            # could ignore it, and continue the next round.
            if tempRes <= result:   break
        result = max(result, tempRes)
    return result+1

# solution 3
# Detected time complexity:
# O((N + M) * log(M))
from collections import deque
class MinQueue():
    ''' Implement a queue with min() function.
    '''
    def __init__(self):
        # all_data is used to store all the raw data for this queue.
        self.all_data = deque()
        # min_data is used to store the data for min() function. The values
        # in min_data is in non-decreasing order.
        self.min_data = deque()
        return
    def enqueue(self, val):
        self.all_data.append(val)
        while self.min_data and self.min_data[-1] > val:
            self.min_data.pop()
        self.min_data.append(val)
        return
    def dequeue(self):
        # Check if the queue is empty.
        if not self.all_data:   return None
        # The to-dequeue value is the minimum in current queue.
        if self.all_data[0] == self.min_data[0]:
            self.min_data.popleft()
        return self.all_data.popleft()
    def dequeue_all_if(self, cond):
        ''' Remove all heading values, if they satisfy the condition "cond".
        '''
        while self.all_data and cond(self.all_data[0]):
            self.dequeue()
        return
    def min(self):
        ''' Return the minimal item in current queue. min() is O(1).
        '''
        if self.min_data:       return self.min_data[0]
        else:                   return None
def solution3(A, B, C):
    # Step 1: Clear all wrapper planks. If there are two planks A and B:
    #                      A.start <= B.start <= B.end <= A.end
    #         A is a wrapper plank to B.
    #    Step 1.1: all these planks having the same start point, remove the
    #              longer wrapper planks. The time complexity is O(N).
    # There are at most 2 * len(C) planks.
    # If plank_end_points[i] is not zero, there is a plank, starting at i,
    # and ending at plank_end_points[i].
    plank_end_points = [0] * (len(C) * 2 + 1)
    for index in range(len(A)):
        if plank_end_points[A[index]] == 0:
            plank_end_points[A[index]] = B[index]
        elif plank_end_points[A[index]] > B[index]:
            # Replace with the new and shorter one.
            plank_end_points[A[index]] = B[index]
        else:
            # Keep the old and shorter one.
            pass
    #    Step 1.2: Remove all the other planks, who do not share the same start
    #              points. The time complexity is O(N), because every plank
    #              after step 1.1 will enter the stack "planks" once and may or
    #              may not exit the queue (once or never).
    # All position values are in range [1..2*M]. Therefore 0 is never used.
    planks = []     # Pairs of (begin, end), sorting with begin position.
    for index in range(1, len(plank_end_points)):
        if plank_end_points[index] != 0:
            # Here is a plank.
            while planks and planks[-1][1] >= plank_end_points[index]:
                # Remove all the wrapper planks to current one.
                planks.pop()
            planks.append((index, plank_end_points[index]))
    del plank_end_points
    # Step 2: counting sort the nails, while removing the duplicate nails.
    #         The time complexity is O(M).
    # If nails[i] is zero, there is not any nail in this place. Otherwise, if
    # nails[i] = j, the j(th) nail in C is placed in the i position of the
    # board.
    nails = [-1] * (len(C) * 2 + 1)
    for index in range(len(C)):
        if nails[C[index]] == -1:
            # If multiple nails hold the same position, we only keep the
            # earliest one.
            nails[C[index]] = index
    # Step 3: find the minimum number of nails that must be used until all the
    #         planks are nailed. The time complexity is O(N+M), because:
    #         a) Every plank after step 1 is checked once and only once; O(N)
    #         b) After step 2, the nails, who are on top of any plank from a),
    #            will be enqueued once and only once; otherwise, the remaining
    #            nails are never touched; O(M)
    #         c) The enqueued nails will dequeue once OR never dequeue. O(M)
    previous_plank = (0, 0)
    # The content in nails_queue is (nail order in C, nail position in board)
    # Nail order in C is used to compute min() function.
    # Nail position in board is determining when to enter and exit queue.
    nails_queue = MinQueue()
    result = (-1, -1)       # An impossible result as the initial value.
    for plank in planks:
        # Remove all nails before this planks.
        nails_queue.dequeue_all_if(lambda x: x[1] < plank[0])
        # Add all nails on this plank, if they are not in the queue.
        # When this plank is overlapping with the previous one, the nails
        # between plank[0] and previous_plank[1]] are already included in
        # queue.
        for index in range(max(plank[0], previous_plank[1]), plank[1] + 1):
            if nails[index] != -1:
                # Enqueue value: (nail order, nail position)
                nails_queue.enqueue((nails[index], index))
        # Maybe there is no nail on this plank.
        if nails_queue.min() == None:       return -1
        # Find the earliest nail, which can fix this plank.
        result = max(result, nails_queue.min())
    return result[0] + 1


# solution 4
def check(A, B, C, K):
    # sort the nails if the positions are random
    C.sort()
    C_len = len(C)
    A_len = len(A)
    i = 0
    j = 0
    while K > 0 and i < C_len:
        while j < A_len:
            if A[j] <= C[i] <= B[j]:
                j += 1
            else:
                break
        K -= 1
        i += 1
    if K < 0 or j < A_len:
        return False
    else:
        return True
def solution4(A, B, C):
    # sort the lists if random
    A, B = (list(x) for x in zip(*sorted(zip(A, B), key=lambda pair: pair[0])))
    # use binary search to findout the minimum number of nails needed
    minPlanks = 1
    maxPlanks = len(C)
    result = -1
    while minPlanks <= maxPlanks:
        currMax = (minPlanks + maxPlanks) / 2
        # pass in only the first currMax num of nails to check
        if check(A, B, C[:currMax], currMax):
            maxPlanks = currMax - 1
            result = currMax
        else:
            minPlanks = currMax + 1
    return result




print(solution2([1, 4, 5, 8], [4, 5, 9, 10], [4, 6, 7, 10, 2]))
