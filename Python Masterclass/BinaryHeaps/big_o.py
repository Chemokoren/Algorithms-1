"""
Big O of Binary Heaps

Insertion - O(log(N))
Removal - O(log(N))
Search - O(N)


Why Log(N)?
Log(N) is actually log base 2 of N

-Each time we go down a step  in a binary heap(or just any binary tree structure) we 
have two times the number of nodes

100 19  36  17  12  25  5   9   15  6   11  13  8   1   4

                                                    100
                                                   /     \
                                                19         36
                                               /  \        /  \
                                            17      12    25   5
                                           /  \    /  \  /  \ /  \
                                          9   15  6   11 13 8 1   4    

If we are trying to insert 200 which will become the largest value, then we will make
4 comparisons with 16 elements

-1st comparison (9,200)
-2nd comparison  (17, 200)
-3rd comparison (19, 200)
-4th comparison (100,200)

2^x  = 16
x= 4


RECAP

- Binary heaps are very useful data structures for sorting, and implementing other data
structures like priority queues
- Binary Heaps are either MaxBinaryHeaps or MinBinaryHeaps with parents either being 
smaller or larger than their children
- Heaps are always filled from left to right
- With just a little bit of math, we can represent heaps using arrays!
"""