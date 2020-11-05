# Tasks Details Medium
# 1. FloodDepth
# Find the maximum depth of water in mountains after a huge rainfall.
# Task description
# You are helping a geologist friend investigate an area with mountain lakes.
# A recent heavy rainfall has flooded these lakes and their water levels have reached the highest possible point.
# Your friend is interested to know the maximum depth in the deepest part of these lakes.
#
# We simplify the problem in 2-D dimensions. The whole landscape can be divided into small blocks and described
# by an array A of length N. Each element of A is the altitude of the rock floor of a block
# (i.e. the height of this block when there is no water at all).
# After the rainfall, all the low-lying areas (i.e. blocks that have higher blocks on both sides)
# are holding as much water as possible.
# You would like to know the maximum depth of water after this entire area is flooded.
# You can assume that the altitude outside this area is zero and the outside area can accommodate
# infinite amount of water.
#
# For example, consider array A such that:
#
#     A[0] = 1
#     A[1] = 3
#     A[2] = 2
#     A[3] = 1
#     A[4] = 2
#     A[5] = 1
#     A[6] = 5
#     A[7] = 3
#     A[8] = 3
#     A[9] = 4
#     A[10] = 2
# The following picture illustrates the landscape after it has flooded:
#
#
#
# The gray area is the rock floor described by the array A above and the blue area with dashed lines represents the water filling the low-lying areas with maximum possible volume. Thus, blocks 3 and 5 have a water depth of 2 while blocks 2, 4, 7 and 8 have a water depth of 1. Therefore, the maximum water depth of this area is 2.
#
# Write a function:
#
# def solution(A)
#
# that, given a non-empty array A consisting of N integers, returns the maximum depth of water.
#
# Given array A shown above, the function should return 2, as explained above.
#
# For the following array:
#
#     A[0] = 5
#     A[1] = 8
# the function should return 0, because this landscape cannot hold any water.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [1..100,000,000].

from collections import namedtuple
def solution(A):
    if len(A) < 3:
        return 0
    # The blocks in the stack is in strictly height descending order.
    # For the first block in the stack, its max_depth is maximum water
    # depth of its (exclusive) left area.
    # The other blocks' max_depth is the maximum water depth between its
    # previous block in the stack and itself, both exclusive.
    Block = namedtuple("Block", ["height", "max_depth"])
    stack = [Block(A[0],0)]
    for height in A[1:]:
        if height == stack[-1].height:
            # These two adjacent blocks have the same height. They act
            # totally the same in building any water container.
            continue
        elif height < stack[-1].height:
            stack.append(Block(height, 0))
        else:
            max_depth = 0
            # Let the current iterating block be C, the previous two
            # blocks in the stack be A and B. And their positions are
            # demoed as:
            #             C
            # A           C
            # A ... B ... C
            # while the blocks between A and B are omitted. So do the
            # blocks between B and C.
            #
            # The additional_depth consider the blocks A, B, and C only,
            # and igonres all the omitted blocks, such as:
            #       C
            # A     C
            # A  B  C   (no block is between A and B, or B and C)
            #
            # HOWEVER, the additional_depth is not always the maximum
            # water depth between A and C, because there may be some
            # water between A and B, or B and C, as exists in the omitted
            # blocks. We need to adjust the additional_depth to get the
            # maximum water depth between A and C, both exclusive.
            while len(stack) > 1 and height > stack[-1].height:
                additional_depth = min(stack[-2].height, height) - stack[-1].height
                max_depth = max(max_depth, stack[-1].max_depth) + additional_depth
                stack.pop()
            # Combine leftward same-or-less-height blocks. These dropped
            # blocks are never going to be part of the remaining water
            # container.
            while len(stack) > 0 and height >= stack[-1].height:
                max_depth = max(max_depth, stack[-1].max_depth)
                stack.pop()
            stack.append(Block(height, max_depth))
    overall_max_depth = 0
    for block in stack:
        if block.max_depth > overall_max_depth:
            overall_max_depth = block.max_depth
    return overall_max_depth

# Task Score # 100% # Correctness # 100% # Performance # 100%
# Detected time complexity: O(N)
def solution1(A):  # O(n) time/space complexity
    n = len(A)

    max_left_heights = A[:]
    max_right_heights = A[:]

    for i in range(1, n):
        max_left_heights[i] = max(A[i], max_left_heights[i - 1])

    for i in range(n - 2, -1, -1):
        max_right_heights[i] = max(A[i], max_right_heights[i + 1])

    depth = 0
    for i in range(n):
        depth = max(depth, min(max_right_heights[i], max_left_heights[i]) - A[i])

    return depth

print(solution([5, 8]))
print(solution([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]))
