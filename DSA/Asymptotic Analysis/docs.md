# asymptotic analysis
- In this section we will cover the asymptotic analysis that is the Big O notation, Omega, Theta and 
  through the annotations 
- The meaning of the term asymptotic is approaching a value with some limits.

Now let us take an example of a function f(n) where the n value can be any positive integer in algorithms.

We are not bothered about the small values of n, instead we are bothered about the large values of n.

And so if you consider an input and n of 5 or n of 10 then it doesn't make sense to compute the running

time of an algorithm but if you have a larger values of n for example thousands, ten thousands, a million

then obviously the running time of algorithms will matter a great deal.



And let us take this function f(n) which is N squared plus six N if the value of n as large as that

is let's take thousand then N squared would be a million and six N would be six thousand if you compare

six thousand with a million it is negligible.  Therefore six N is insignificant.

So, what we say here is f(n) is said to be asymptotically equivalent to n squared(n^2).



Algorithms are analyzed using mathematical notations for functions which disregards constant factors.

For example in the previous case we had a mathematical function f event and we represented that as N

squared plus six N. So, algorithms are analyzed using f(n) or mathematical functions.


The running time of algorithms are characterised by using functions that is same f of n.

These functions are marked with the size of the input n. so here we are bothered about n approaching a large value R in approaching

infinity.

The running time of algorithm grows proportional to n i.e. the input size.

# 1. Constant O(1)
# 2. Logarithm log(n)
# 3. Linear O(n)
# 4. n-log-n nlog(n)
# 5. Quadratic O(n^2)
# 6. Cubic O(n^3)
# 7. Exponential O(2^n)

 
we have already seen functions taking constant time logarithm time that

is log in.

We have also seen linear which is represented by N quadratic. That doesn't square.

For example if you have a function which contains two nested for loops then it can be represented as

a mathematical function and square then we have cubic.

We have three nested loops and that is something known as log in as well as exponential that is to power.

And now we have already talked about these complexities if you remember constant takes less time than

log in log and takes less time than any and takes less time than in logging and logging takes less time

than in squared as well as in squared takes less time than in N cubed which take less time than exponential.

And that is exponential.

- Always remember that when we are talking about n we are talking about large values of n
- To represent the time complexity, we have asymptotic notation

### Big Oh Notation - f(n) <= cg(n) for n >= no (n note)

We have an asymptotic notation known as big oh defined as f(n) often less than equal to C G often yet f() often and G often are two functions and C is a constant and n is greater
than and of 0.

### Omega Notation - f(n) >= cg(n) for n >= no

- We also have Omega notation that is f() often is greater than C of the event and hero to f event.

And Giovanna do different function C meaning the constant then we have a t done notation which says

### Theta  - c`g(n) <= f(n) <=c``g(n) for n >=no
they are two constant C dash and c double dash and c dash of G often is less than f often and F often

is less than equal to C double natural G F ing 9 year olds f event and G F and are two different functions.

The big notation works on the concept of less than equal to Omega notation works on a concept of greater

than equal so therefore "big o notation" defines the upper bound of the function  while Omega defines the lower

bound of the function and theta notation defines the tailbone of a function.


Therefore if an alligator has N squared as its complexity then we say that its complexity is v go off and square because we are always bothered

about the upper bounds that is the larger values the omega and teeth are also used but most of the alligator

talks about the big on rotation that is the complexity is defined using big ole notation so therefore, 
we have seen the complexities earlier we have defined functions and we have praised the functions also

in the earlier sections and now we have defined these three as interdict notation that is bingo Omega
and theta.

# - Big-Oh notation works on the concept of <=
# - Omega notation works on the concept of >=
- Big-Oh notation defines the uppwerbound of the function
- Omega notation defines the lowerbound of the function
- Theta notation defines the tightbound of the function
Therefore, if an algorithm has n^2 as its complexity then we say that it's complexity is O(n^2) 
because we are always bothered about the upper bounds i.e. the larger values