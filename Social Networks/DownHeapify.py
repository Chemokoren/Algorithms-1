#import random
# L = [random.randrange(90)+10 for i in range(20)]
L =[50,88,27,58,30,21,58,21,58,13,84,24,29,43,61,44,65,74,76,30,82,]
#Heap shortcuts
def left(i): return i*2+1
def right(i): return i*2+2
def parent(i): return (i-1)/2
def root(i): return i==0
def leaf(L, i): return right(i) >=len(L) and left(i) >=len(L)
def one_child(L,i): return  right(i) ==len(L)

#call this routine if the heap rooted at i satisfies the heap property
# *except* perhaps i to its children immediate children

def down_heapify(L,i):
    # if i is a leaf, heap property holds
    if leaf(L, i): return
    # if i has one child ...
    if one_child(L, i):
        # check heap property
        if L(i) > L[left(i)]:
            #check heap property
            if L[i] > L[left(i)]:
                # if it fails, swap, fixing i and its child (a leaf)
                (L[i],L[left(i)]) =(L[left(i)], L[i])
                return
            #if i has two children...
            #check heap property
            if min(L[left(i)],L[right(i)]) >= L[i]: return
            #if i has two children ...
            #check heap property
            if min(L[left(i)], L[right(i)]) >= L[i]: return
            #if it fails, see which child is the smaller
            # and swap i's value into that child
            # Afterwards, recurse into that child, which might violate
            if L[left(i)] < L[right(i)]:
                # Swap into left child
                (L[i],L[left(i)]) =(L[left(i), L[i]])
                down_heapify(L,left(i))
                return
            (L[i], L[right(i)]) =(L[right(i)],L[i])
            down_heapify(L,right(i))
            return

