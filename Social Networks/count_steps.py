import math
"""
For this particular question, the professor is not counting loop overhead; i.e. the statements inside the loop are counted, but loop evaluation itself is not.
 He is also not counting the return statement.
"""

def time(n):
    """ Return the number of steps
    necessary to calculate
    `print countdown(n)`"""
    steps = 0

    # time_to_assign_y = 1
    # time_to_print_y = 1
    # time_to_print_count_donw = 1
    # time_to_print_loop = math.ceil(n / 5)
    # steps = time_to_assign_y + time_to_print_y + time_to_print_count_donw + (2 * time_to_print_loop)
    steps =3 + 2 * math.ceil(n/5.0)
    return steps


def countdown(x):
    y = 0
    while x > 0:
        x = x - 5
        y = y + 1
    print(y)


print(countdown(6))

print(time(6))
