#Find out how many dwarfs can fit on a raft such that it's balanced when crossing a river.
# Task Score 100% Correctness 100% Performance
def solution(N, S, T):
    quadrant_left_front = (N // 2) * (N // 2)
    quadrant_left_back = (N // 2) * (N // 2)
    quadrant_right_front = (N // 2) * (N // 2)
    quadrant_right_back = (N // 2) * (N // 2)
    boundary = N // 2
    # Compute how many slots are available in each quadrant.
    for barrel in S.split():
        # Adjust to 0-based index.
        row = int(barrel[:-1]) - 1
        column = ord(barrel[-1]) - ord("A")
        if row < boundary:
            # The barrel is in the front.
            if column < boundary:
                # The barrel is in the left.
                quadrant_left_front -= 1
            else:
                # The barrel is in the right.
                quadrant_right_front -= 1
        else:
            # The barrel is in the back.
            if column < boundary:
                # The barrel is in the left.
                quadrant_left_back -= 1
            else:
                # The barrel is in the right.
                quadrant_right_back -= 1
    # lf is short for left front, etc.
    # To keep balance, we need:
    #   1. weight_lf + weight_lb = weight_rf + weight_rb
    #   2. weight_lf + weight_rf = weight_rf + weight_rb
    # Solve the equations and we can get the answer:
    #   1. weight_lf = weight_rb
    #   2. And weight_rf = weight_lb
    allowance_lf = min(quadrant_left_front, quadrant_right_back)
    allowance_rb = min(quadrant_left_front, quadrant_right_back)
    allowance_lb = min(quadrant_left_back, quadrant_right_front)
    allowance_rf = min(quadrant_left_back, quadrant_right_front)
    # Minus the seats, which are already occupied by dwarfs.
    for dwarf in T.split():
        # Adjust to 0-based index.
        row = int(dwarf[:-1]) - 1
        column = ord(dwarf[-1]) - ord("A")
        if row < boundary:
            # The dwarf is in the front.
            if column < boundary:
                # The dwarf is in the left.
                allowance_lf -= 1
                if allowance_lf < 0:    return -1
            else:
                # The dwarf is in the right.
                allowance_rf -= 1
                if allowance_rf < 0:    return -1
        else:
            # The dwarf is in the back.
            if column < boundary:
                # The dwarf is in the left.
                allowance_lb -= 1
                if allowance_lb < 0:    return -1
            else:
                # The dwarf is in the right.
                allowance_rb -= 1
                if allowance_rb < 0:    return -1
    return allowance_lf + allowance_rb + allowance_lb + allowance_rf


print("##################################### solution 2 #####################################")

# First, get the upper right, lower right, upper left, and lower left according to the string, and the seats
# already occupied by the barrel and the dwarf. Calculate the number of short people and the remaining seats
# in each part. Then judge whether there is a possibility of maintaining balance. For the two diagonal parts,
# only the sum of the number of short people and the number of remaining seats is not less than the number of
# dwarves in the other part to maintain the balance. Therefore, the final number of dwarves that can be carried
# by these two parts is the minimum of the sum of the number of short people and the number of remaining seats
# in the two parts, and finally calculate how many new dwarves need to be admitted in each part to get the final
# answer.


def encode_str(seat_str, n):
    """
    :param seat_str:
    :param n:
    :return:
    """
    # 0， 1， 2， 3
    seat_dict = {i: 0 for i in range(4)}
    if not seat_str:  #
        return seat_dict
    else:
        seat_dict = {i: 0 for i in range(4)}
        str_list = seat_str.split(' ')  #
        for i in str_list:
            if len(i) == 2:  #
                row, column = i
            else:
                row, column = i[:2], i[2]
            if int(row) <= n / 2:  #
                if ord(column) - ord('A') < n / 2:  #
                    seat_dict[0] += 1
                else:  #
                    seat_dict[1] += 1
            else:  #
                if ord(column) - ord('A') < n / 2:  #
                    seat_dict[2] += 1
                else:  #
                    seat_dict[3] += 1
    return seat_dict


def solution1(N, S, T):
    """
    :param N:
    :param S:
    :param T:
    :return:
    """
    barrels_dict = encode_str(S, N)  #
    pepole_dict = encode_str(T, N)   #

    #
    all_seats = (N // 2) ** 2

    #
    part_dict = {k: [pepole_dict[k], all_seats-pepole_dict[k]-barrels_dict[k]] for k in pepole_dict}

    #
    sum_left_up = sum(part_dict[0])
    sum_right_down = sum(part_dict[3])
    #
    if sum_left_up >= part_dict[3][0] and sum_right_down >= part_dict[0][0]:
        left_up_right_down = min(sum_left_up, sum_right_down)  #
    #
        new_left_up_right_down = 2 * left_up_right_down - part_dict[0][0] - part_dict[3][0]
    else:
        return -1

    #
    sum_left_down = sum(part_dict[2])
    sum_right_up = sum(part_dict[1])
    #
    if sum_left_down >= part_dict[1][0] and sum_right_up >= part_dict[2][0]:
        left_down_right_up = min(sum_left_down, sum_right_up)  #
    #
        new_left_down_right_up = 2 * left_down_right_up - part_dict[1][0] - part_dict[2][0]
    else:
        return -1

    return new_left_up_right_down + new_left_down_right_up

print(solution1(4, '1B 1C 4B 1D 2A', '3B 2D'))