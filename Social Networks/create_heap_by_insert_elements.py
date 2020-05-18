"""
Another way to build a heap out of a set of values, vals, is to insert the items one at a time int o the heap
"""
heap =[]
for v in vals:
    insert_heap(heap,v)


def insert_heap(L, v):
    L.append(v)
    up_heapify(L, len(L)-1)
    
"""
what is the running time? O(nlogn)
"""
