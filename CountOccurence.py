# Tasks Details
# 1. RectangleBuilderGreaterArea
# Count the distinct rectangle sizes, of area greater than or equal to X, that can be built out of a given
# set of segments.
#
# Halfling Woolly Proudhoof is an eminent sheep herder. He wants to build a pen (enclosure) for his new
# flock of sheep. The pen will be rectangular and built from exactly four pieces of fence (so, the pieces
# of fence forming the opposite sides of the pen must be of equal length). Woolly can choose these pieces
# out of N pieces of fence that are stored in his barn. To hold the entire flock, the area of the pen must
# be greater than or equal to a given threshold X.
#
# Woolly is interested in the number of different ways in which he can build a pen. Pens are considered
# different if the sets of lengths of their sides are different. For example, a pen of size 1×4 is different
# from a pen of size 2×2 (although both have an area of 4), but pens of sizes 1×2 and 2×1 are considered
# the same.
#
# Write a function:
#
#     def solution(A, X)
#
# that, given an array A of N integers (containing the lengths of the available pieces of fence) and
# an integer X, returns the number of different ways of building a rectangular pen satisfying the above
# conditions. The function should return −1 if the result exceeds 1,000,000,000.
#
# For example, given X = 5 and the following array A:
#   A[0] = 1
#   A[1] = 2
#   A[2] = 5
#   A[3] = 1
#   A[4] = 1
#   A[5] = 2
#   A[6] = 3
#   A[7] = 5
#   A[8] = 1
#
# the function should return 2. The figure above shows available pieces of fence (on the left) and possible to build pens (on the right). The pens are of sizes 1x5 and 2x5. Pens of sizes 1×1 and 1×2 can be built, but are too small in area. It is not possible to build pens of sizes 2×3 or 3×5, as there is only one piece of fence of length 3.
#
# Write an efficient algorithm for the following assumptions:
#
#         N is an integer within the range [0..100,000];
#         X is an integer within the range [1..1,000,000,000];
#         each element of array A is an integer within the range [1..1,000,000,000].
#


def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


def solution(A, X):
    # write your code in Python 3.6
    count = 0
    for i in range(len(A) - 1):
        for j in range(len(A) - 1):
            if countX(A, i) > 1 and countX(A, j) > 1:
                sum = i * j
                print(i, j, "= ", sum)
                if sum >= X:
                    count = count + 1
    return count // 2


def solution1(A, K):
    count = 0
    length = 0
    for i in A:
        if i >= K:
            length = 0
            count += 1
        else:
            length += i
            if length >= K:
                length = 0
                count += 1
    return count


def solution2(A, X):
    """
  Use the elements in array A to construct the number of different rectangles with an area not less than X
  :param A: Array
  :param X: Area threshold
  :return: The number of rectangles that meet the condition
  """

    count_item = {}
    for i in A:
        if i in count_item:
            count_item[i] += 1
        else:
            count_item[i] = 1
    print(count_item)

    no_less_than_2 = [j for j in count_item if count_item[j] >= 2]  # Store the occurrences greater than or equal to 2
    ordered_list = sorted(no_less_than_2)  # Sort by fence length in ascending order

    length = len(ordered_list)  # Number of available fences

    if not length:  # No fence available
        return 0
    else:
        if length == 1:  # There are only fences of one length, and fences can be built only when the number of fences is not less than 4
            if count_item[ordered_list[0]] >= 4:
                return 1
            else:
                return 0
        else:
            sum_count = 0  # Total number of records
            for index, value in enumerate(ordered_list):
                if count_item[value] >= 4:
                    start = index  # If a fence of one length is used, the number needs to be no less than 4
                else:
                    start = index + 1
                end = length - 1
                #  Start binary search algorithm
                while start <= end:
                    middle = int((start + end) / 2)
                    if ordered_list[middle] * value >= X:
                        end = middle - 1
                    else:
                        start = middle + 1
                sum_count += length - end - 1
                if sum_count > 1e9:
                    return -1
            return sum_count

# solution 3
# Detected time complexity: O(N * log(N))
# Task Score 100% Correctness 100% Performance 100%

def solution3(A, X):
    fence_count = {}
    for fence in A:
        fence_count[fence] = fence_count.get(fence, 0) + 1

    num_of_pens = 0
    usable_fences = []
    for fence in fence_count:
        if fence_count[fence] < 2:
            # Less than one pair. We cannot use it.
            continue
        elif fence_count[fence] < 4:
            usable_fences.append(fence)
        else:
            usable_fences.append(fence)
            # We consider the square pen here.
            if fence * fence >= X:
                num_of_pens += 1
    # We consider the non-square pen here.
    usable_fences.sort()
    candidate_size = len(usable_fences)
    for i in range(candidate_size):
        # Use binary search to find the first fence pair, that
        # could be used with current pair to form a pen.
        begin = i + 1
        end = candidate_size - 1
        while begin <= end:
            mid = (begin + end) // 2
            if usable_fences[mid] * usable_fences[i] >= X:
                end = mid - 1
            else:
                begin = mid + 1
        # Now the usable_fences[end + 1] is the first qualified
        # fence.
        combination_num = candidate_size - (end + 1)
        num_of_pens += combination_num
        if num_of_pens > 1000000000:
            return -1
    return num_of_pens

print(solution3([1, 2, 5, 1, 1, 2, 3, 5, 1], 5))
# print( countX([1, 2, 5, 1, 1, 2, 3, 5, 1], 1))
