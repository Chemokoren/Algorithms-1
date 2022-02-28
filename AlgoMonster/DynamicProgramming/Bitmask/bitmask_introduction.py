"""
Bitmask and Dynamic Programming
What is a bitmask?
Binary Numbers

At the smallest scale in computers, data are stored as bits. A bit stores either 0 or 1. 
A binary number is a number expressed in the base-2 system. Each digit can be either 0 or
1. The integer types we use in programming languages are actually stored as binary numbers
.Here is how binary numbers converts to decimal numbers:

You can check that in python:

>>> bin(21)

'0b10101'

Note that 0b means it's a binary number. The leading 0s are omitted and that's why we 
have 10101 instead of 010101.

Bit-wise AND

We can AND two binary numbers by comparing each digits. If they are both 1 then the 
resulting digit is 1, otherwise it's 0.

Bitmask

Now finally what's a mask? We can construct a binary number such that certain digit is 
set to 1 and other digits are all set to 0. This creates a "mask" that when we AND it to
another binary it "turns off" (set to 0) all digits except the 1 digit in the mask.

Encoding the state

Now how is this all useful to algorithms and dynamic programming? The answer is to encode
states. Remember in backtracking problems like permutation, we used a boolean array to
keep track of state, i.e. which character has been used. If we were memoizing the state, 
we need to somehow serialize the array, e.g. turning it into a string which has extra 
computational cost. With a bitmask, the serialization from boolean array to integer is
already done for you - it's just an integer. 
This reduces memory consumption and makes the algorithm faster and simpler.

For instance, let us say that we are on a graph and the problem requires us to remember 
all the nodes that we visted. 
We can encode each node as a boolean bit value as part of our bitmask and use that value 
as our dp state.

In the example, we have visited nodes 1 and 4 nodes. We encode that as 1001 which is 
equal to 2^0+2^3=9.

Bitmask questions can vary and additional dp states may be required so the code proviced 
will loosely follow what a bitmask type question will look like.

Common bit manipulation operations

Typically, these problems use a recursive function as well in order to do dp. 
Below is some pseudocode to outline this idea. Here are some useful operations to keep 
in mind

    (1 << i) -> simply to access the ith bit in the mask such as through a loop

    (bitmask | (1 << i)) -> this operation sets the ith bit in the bitmask to 1

    (bitmask & ~(1 << i)) -> this operation sets the ith bit in the bitmask to 0

    (bitmask & (1 << i)) -> this operation checks if the ith bit in the bitmask is set 
    to 1 or not

Here's another example.
Use bitmask to generate all subsets:

>>> nums

[1, 2, 3]

>>> n = len(nums)

>>> subsets = []

>>> for mask in range(2 ** n):

...     subset = []

...     for i in range(n):

...         if mask & (1 << i):

...             subset.append(nums[i])

...     subsets.append(subset[:])

...

>>> subsets

[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

We didn't need to use backtracking for this. Pretty cool, eh!

Bitmask and Dynamic Programming

Now here is pseudocode for how a bitmask dp problem for dynamic programming.

function f(int bitmask, int [] dp) {

    if calculated bitmask {

        return dp[bitmask];

    }

    for each state you want to keep track of {

        if current state not in mask {

            temp = new bitmask

            dp[bitmask] = max(dp[bitmask], f(temp,dp) + transition_cost)

        }

    }

    return dp[bitmask]

}

Bitmask is helpful with problems that would normally require factorial complexity, 
something like n! but can instead reduce the computational complexity to 2^n through 
storing the dp state. It can also act as an effective "upper-bound" on the number of 
computations that can take place.

"""