"""
Prime Sieve Introduction
The Question

For this article we are interested in the following question, does there exist a method to 
effectively compute prime numbers?

Naive Method

We know we can check if a number is prime by checking all the numbers smaller than it. If not a 
single number can divide the number than the number is prime. This method results in O(n^2) time 
complexity where n is the highest prime number we want to compute.

Improvements

We can improve this by realizing that we only need to check up to the square root of a number. 
Any divisors that are greater than the square root of a number will have a matching divisor less 
than the square root of the number. Mathematically speaking, let us define n as an arbitrary 
composite number and d as a divisor of the number that is greater than its square root. 
We know for a fact that if d is a divisor greater than the square root then so too is
n/d and n/d must be less than the square root. Therefore, we only need to check if n/d is a divisor
of n and if it is then n is composite. This property holds trus for any d greater than the square 
root so therefore we only need to check up to sqrt(n). 

Take for example the number 16, we know 16 = 2 * 8 so we realize that for the number 8 there exists 
a divisor smaller than the square root that matches 8 which is 2. This means compared to before our 
new time complexity is O(n*sqrt(n)), but can we do even better.

Sieve of Erastothenes

Formally speaking, the technique we are about to introduce is called the sieve of erastothenes but 
for simplicity we will refer to it as sieve or prime sieve. This technique has a very simple idea, 
suppose we want to compute all prime number less than or equal to some number n. We start by looping
from 1 to n, if we encounter a prime number we mark all the multiples of the prime number as not 
prime. Our new time complexity then becomes O(n + n/2 + n/3 + n/5 + n/7 + ... + n/n) which is
approximately O(nlog(log(n))). 
Note that we skip over already established composite numbers as we know that we have already set all
the multiples of that number. Now for some code to demonstrate this idea.


"""
from typing import List

def prime_sieve(n:int) -> List[int]:
    primes =[True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, n+1, 1):
        if primes[i]:
            for j in range(i + i, n+ 1, i):
                primes[j] = False
    return primes

"""
If you are still struggling to understand the concept it might be best to try the code out with an 
example with a random n on paper. Hopefully, this short article gives you some insight into the 
mathematical topics that will be covered in this section.

"""