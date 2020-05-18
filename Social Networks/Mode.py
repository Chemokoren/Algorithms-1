#
# Given a list L of n numbers, find the mode
# (the number that appears the most times).
# Your algorithm should run in Theta(n).
# If there are ties - just pick one value to return
#
from operator import itemgetter
import numpy as np
# def mode(L):
#     count =0;
#     mode_val=0
#     for i in range(len(L)):
#
#         if occurences(L[i],L) > count :
#             count = occurences(L[i],L)
#             mode_val =L[i]
#     return mode_val




#function to find mode
def mode(data):
    modecnt=0
#for count of number appearing
    for i in range(len(data)):
        icount=data.count(data[i])
#for storing count of each number in list will be stored
        if icount>modecnt:
#the loop activates if current count if greater than the previous count
            mode=data[i]
#here the mode of number is stored
            modecnt=icount
#count of the appearance of number is stored
    return mode

def mode1(L):
    counts =dict()
    maxkey =None
    maxvalue =-1
    for val in L:
        if val not in counts:
            counts[val] =1
        else:
            counts[val] +=1
        if(counts[val] > maxvalue):
            maxkey =val
            maxvalue =counts[val]
    return maxkey

from collections import defaultdict
def mode2(L):
    counts =defaultdict(int)
    maxCount =0
    mode =0
    for eID in L:
        counts[eID] +=1
        tmp =counts[eID]
        if tmp >maxCount:
            mode =eID
            maxCount =tmp
    return mode

#one of the fastest
from collections import defaultdict
def mode3(L):
    counts =defaultdict(int)
    for v in L:
        counts[v] +=1
    return max(counts, key =lambda x: counts[x])

def mode4(L):
    vals =set(L) #remove duplicates -gives unique values
    return max(vals, key =lambda x: L.count(x))

def mode5(L):
    return max(set(L),key=lambda x: L.count(x))

def occurences(tokens,L):
    count = 0
    for i in range(len(L)):
        if (L[i] == tokens):
            count += 1
    return count
L=[10, 4, 4, 5, 4, 5, 1, 4, 3, 8]
# L=[10,3,9,50,23,67,10, 34]
print(mode5(L))

####
# Test
#
import time
from random import randint

def test():
    assert 5 == mode([1, 5, 2, 5, 3, 5])
    iterations = (10, 20, 30, 100, 200, 300, 1000, 5000, 10000, 20000, 30000)
    times = []
    for i in iterations:
        L = []
        for j in range(i):
            L.append(randint(1, 10))
        start = time.clock()
        for j in range(500):
            mode(L)
        end = time.clock()
        print (start, end)
        times.append(float(end - start))
    slopes = []
    for (x1, x2), (y1, y2) in zip(zip(iterations[:-1], iterations[1:]), zip(times[:-1], times[1:])):
        print (x1, x2), (y1, y2)
        slopes.append((y2 - y1) / (x2 - x1))
    # if mode runs in linear time,
    # these factors should be close (kind of)
    print (slopes)

#test()

#Look At Coparison functions done by Anthony pace to run test
