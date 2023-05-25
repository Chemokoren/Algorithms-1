"""
Tasks Details
Easy
1. AbsDistinct
Compute number of distinct absolute values of sorted array elements.
Task Score
7%
Correctness
9%
Performance
0%
Task description
A non-empty array A consisting of N numbers is given. The array is sorted in non-decreasing order.
The absolute distinct count of this array is the number of distinct absolute values among the elements
of the array.

For example, consider array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
The absolute distinct count of this array is 5, because there are 5 distinct absolute values among the
 elements of this array, namely 0, 1, 3, 5 and 6.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N numbers, returns absolute distinct count of array A.

For example, given array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647];
array A is sorted in non-decreasing order."""

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

def solution(A):
    # write your code in Python 3.6
    GEEK = []
    for i in range(len(A) - 1):
        GEEK.append(abs(i))

    return len(Remove(GEEK))


# solution 1
# Task Score
# 7%
# Correctness
# 9%
# Performance 0%
def solution1(A):
    final_list = []
    for num in A:
        if abs(num) not in final_list:
            final_list.append(num)
    return len(final_list)-1

# solution 2
# Task Score 100% Correctness 100% Performance 100%
# Detected time complexity: # O(N) or O(N*log(N))
def solution2(A):
    abs_distinct = 1
    current = max(abs(A[0]), abs(A[-1]))
    index_head = 0
    index_tail = len(A)-1
    while index_head <= index_tail:
        # We travel the array from the greatest
        # absolute value to the smallest.
        former = abs(A[index_head])
        if former == current:
            # Skip the heading elements, whose
            # absolute values are the same with
            # current recording one.
            index_head += 1
            continue
        latter = abs(A[index_tail])
        if latter == current:
            # Skip the tailing elements, whose
            # absolute values are the same with
            # current recording one.
            index_tail -= 1
            continue
        # At this point, both the former and
        # latter has different absolute value
        # from current recorded one.
        if former >= latter:
            # The next greatest value is former
            current = former
            index_head += 1
        else:
            # The next greatest value is latter
            current = latter
            index_tail -= 1
        # Meet with a new absolute value
        abs_distinct += 1
    return abs_distinct



A = [-5, -3, -1, 0, 3, 6]

# use set or maps
def solution(A):
    map = set()

    for i in A:
        map.add(abs(i))
    #    if abs(i)  in map:
    #        pass
    #    else:
    #        map[abs(i)] =True
    return len(map)

solution(A)
