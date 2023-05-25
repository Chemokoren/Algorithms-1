#List of distinct two-digit values.
#where will 84 be located in the sorted version
import random

L =[31,45,91,51,66,82,28,33,11,89,84,27,36]

def partition(L, v):
    smaller =[]
    bigger =[]
    for val in L:
        if val < v: smaller +=[val]
        if val > v: bigger +=[val]
    return (smaller,[v], bigger)

def top_k(L,k):
    v =L[random.randrange(len(L))]
    (left, middle, right)= partition(L,v)
    if len(left) ==k :return left
    if len(left)+1 ==k: return left+[v]
    if len(left) > k: return top_k(left,k)
    return left+[v]+top_k(right,k-len(left)-1)

print(top_k(L,5))
