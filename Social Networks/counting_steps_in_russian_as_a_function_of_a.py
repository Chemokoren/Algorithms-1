#counting stpes in russian as a function of a
"""
The number of times the loop is going to be executed is going to be the same as the number of times that it takes to divide x in half before you get down to 0.
How many times can you divide x in half rounding down before you get down to 0?
e.g. x
x   	0	1	2	3	4	5	6	7	8	9	10	11
halving	0	1	2	2	3	3	3	3	4	4	4	4

THe function that captures the relationship between x and the number of times x needs to be halved to get down to 0.
(log to base 2 of x rounded down)+1


steps to execute russian(a,b)

3(round_down(log a to base 2 )+1) + 3 +# of "on" bits in a

The floor log base 2 of a rounded down plus 1 is the number of times the while loop is executed.
There are three statements that are going to be executed inside  plus additional three statements that are executed outside plus
there is going to be one statement executed for each of the bits of a that it's on and particularly the summation.

<= 4 rounded_down(log a to the base 2) + 7
###this is upper bounded by 4 times the rounded down logarithm of a plus 7.
The reason for that being that the most number of bits you can have in a number is if all the bits are on and how many bits can you have in a
number? Well if you have a number like this --a a binary number like 111111, each time you have it, you're chopping of one of the bits.
The rounded down log base 2 of the number plus 1 is actually a count of the maximum number of bits that you can have on.

The answer here is much, much, much, much less in general than some linear function in a
like what we get for naive. Naive grows a lot faster --in fact, exponentially faster than the bound
on the running time is for Russian

"""

def russian(a,b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x % 2 == 1 :
            z = z + y
            y = y << 1
            x = x >> 1
    return z

