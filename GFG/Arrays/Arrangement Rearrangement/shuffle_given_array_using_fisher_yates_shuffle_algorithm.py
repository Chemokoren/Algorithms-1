"""
Shuffle a given array using Fisher-Yates shuffle Algorithm

Given an array, write a program to generate a random permulation of array elements.
This question is also asked as "Shuffle a deck of cards" or "randomize a given array". 
Here shuffle means that every permutation of array element should equally likely.

Let the given array be arr[]. A simple solution is to create an auxiliary array temp[]
which is initially a copy of arr[]. Randomly select an element from temp[], copy the 
randomly selected element to arr[0] and remove the selected element from temp[].
Repeat the same process n times and keep copying elements to arr[1], arr[2] ... The
time complexity of this solution will be O(n^2).

Fisher-Yates shuffle algorithm works in O(n) time complexity. The assumption here is,
we are given a function rand() that generates random number in O(1) time.

The idea is to start from the last element, swap it with a randomly selected element
from the whole array(including last). Now consider the array from 0 to n-2(size reduced by 1)
, and repeat the process till we hit the first element.

Detailed algorithm:

To shuffle an array a of n elements(indices 0..n-1):
    for i from n - 1 down to 1 do
        j = random integer with 0 <= j <= i
        exchange a[j] and a[i]

The function assumes that rand() generates a random number.

Time Complexity: O(n), assuming that the function rand() takes O(1) time.

How does this work? 
-------------------

The probability that ith element (including the last one) goes to last position is 1/n, 
because we randomly pick an element in first iteration.
The probability that ith element goes to second last position can be proved to be 1/n 
by dividing it in two cases. 
Case 1: i = n-1 (index of last element): 
The probability of last element going to second last position is = (probability that 
last element doesn’t stay at its original position) x (probability that the index picked 
in previous step is picked again so that the last element is swapped) 
So the probability = ((n-1)/n) x (1/(n-1)) = 1/n 
Case 2: 0 < i < n-1 (index of non-last): 
The probability of ith element going to second position = (probability that ith element is 
not picked in previous iteration) x (probability that ith element is picked in this iteration) 
So the probability = ((n-1)/n) x (1/(n-1)) = 1/n
We can easily generalize above proof for any other position.
"""

# program to shuffle a given array
import random

# A function to generate a random permutation of arr[]
def randomize(arr, n):
    # start from the last element and swap one by one. We don't need to run for the first 
    #element that's why i>0
    for i in range(n-1, 0, -1):

        # pick a random index from 0 to i
        j = random.randint(0,i+1)

        # swap arr[i] with element at random index
        arr[i], arr[j] = arr[j], arr[i]

    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr)
print(randomize(arr, n))
