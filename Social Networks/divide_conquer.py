#divide and conquer
"""
What is it about the Russian algorithm is designed that makes it so much better than the
naive approach that is just repetitive addition.
multiplication -is repeated addition

when a is even (like 8)
-regroup them as 2 sums
a/2 times + a/2 times i.e. B added to itself a over 2 times
2(b added to itself a over 2 times)
The idea of divide and conquer is that you can break a problem into roughly
equal size sub-problems,seperately and combine the results.
you are saving yourself half the effort every time that you do this,
half keeps compounding and that's how we get down to algorithmic number of steps instead
of linear number of steps

Leads to expressing the algorithm recursively.

1 - the idea here is that we're going to multiply a and b together
2 -what we're going to do is say if a is 0 to start, we can just retun 0
3 -if a is even, then multiplying a times b is the same as adding b to itself
a over 2 times, so its it's a over 2 times b which we are going to compute recursively
4 - once we have the answer to that we multiply that by 2 to get the answer to the original problem
so, we can use the solution to the sub-problem to solve the big problem.

#####when its odd -complicated ##########
1 -we are actually adding a's and b's together, but a is odd, sol let's pull one of the b's out and add to that
what's left, there is a minus 1, repetitions of b that we're adding together, but a minus 1 is now even,
so we can have that compute what a minus 1 over 2 times b is recursively.
once we have the answe to that, we can multiply it by 2.
- its going to give us what a minus 1 times b is, whis is a times b minues b.
- using the solution to the sub-problem, we can compute the solution to the original problem.

## this may seem a little bit circular, but each time that the Russian peasant algorithm is being
called here, it's being called with a much smaller value --a half that it was before.


"""

def rec_russian(a,b):
    if a ==0: return 0
    if a % 2 ==0:
        return 2 * rec_russian(a/2,b)
    return b + 2 * rec_russian((a-1)/2,b)

print(rec_russian(4,4))



"""
we should assume that a>0a
to calculate time t(a)
T(a) = 
if a =0, 1
elif a is even:
    3+ T(a/2)
else 
    3+ T((a-1)/2)    

====
T(a) =3 round_down(log a to base 2) +4

"""
