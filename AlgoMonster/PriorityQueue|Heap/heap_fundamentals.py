"""
Priority Queue and Heap

What is the relationship between priority queue and heap?

Priority Queue is an Abstract Data Type, and Heap is the concrete data structure we use to
implement a priority queue.
Priority Queue

A priority queue is a data structure that consists of a collection of items and supports 
the following operations:

    insert: insert an item with a key
    delete_min/delete_max: remove the item with the smallest/largest key and returning it

Note that

    we only allow getting and deleting the element with min/max key and NOT arbitrary key.

Use cases

The hospital triage process is a quintessential priority queue. Patients are sorted based 
on the severity of their condition. For example, a person with the cold comes in and he is
placed near the end of the queue. Then a person who had a car accident comes in, and he is
placed before the person with the cold even though he came in later because his condition
is more severe. Severity is the key in this case.

Consider a problem like Merge K sorted lists. We need to keep track of min value among k 
elements (smallest element in each sorted list) and remove the min value and insert new 
values at will while still having access to the min value at any point in time. Here are 
some other problems where the priority queue comes in handy.

    k closest pointers to origin
    kth largest element
    kth largest element in a stream
    Median of a data stream
    Uniform Cost Search

Implement Priority Queue using an array

To do this, we could try using

    an unsorted array, insert would be O(1) as we just have to put it at the end, but
    finding and deleting min value would be O(N) since we have to loop through the entire
    array to find it
    a sorted array, finding min value would be easy O(1), but it would be O(N) to insert 
    since we have to loop through to find the correct position of the value and move 
    elements after the position to make space and insert into the space

There must be a better way! "Patience you must have, my young padawan." Enter Heap.

Heap
Max Heap and Min Heap

There are two kinds of heaps - Min Heap and Max Heap. A Min Heap is a tree that has two 
properties:

    almost complete, i.e. every level is filled except possibly the last(deepest) level. 
    The filled items in the last level are left-justified.
    for any node, its key (priority) is greater than its parent's key (Min Heap).

A Max Heap has the same property #1 and opposite property #2, i.e. for any node, its key
is less than its parent's key.

Let's play "is it a heap?" game:

Note that

    the number in each node is the key, not value (remember a tree node has a value). 
    Keys are used to sort the nodes/construct the tree, and values are the data we want 
    heap to store.
    unlike a binary search tree, there is no comparable relationship between children.
    For example, the third example in the first row, 17 and 8 are both larger than 2 but 
    they are NOT sorted left to right. In fact, there is no comparable relationship across 
    a level of a heap at all.

Why heaps are useful

By the first look, the heap is an odd data structure - it's required to be a complete tree
but unlike binary search tree, it's not sorted across a level.

What makes it so useful is

    because a heap is a complete tree, the height of a heap is guaranteed to be O(log(N)).
    This makes operations that go from root to leaf guaranteed to be O(log(N)).
    because only nodes in a root-to-leaf path are sorted (nodes in the same level are not 
    sorted), when we add/remove a node, we only have to fix the order in the vertical 
    path the node is in. This makes inserting and deleting O(log(N)) too.
    being complete also makes array a good choice to store a heap since data is
    continuous. As we will see later in this module, we can find the parent and children 
    of a node simply by doing index arithmetics.

Operations
insert

To insert a key into a heap,

    place the new key at the first free leaf
    if property #2 is violated, perform a bubble-up

     

def bubble_up(node):

    while node.parent exist and node.parent.key > node.key:

        swap node and node.parent

        node = node.parent

As the name of the algorithm suggests, it "bubbles up" the new node by swapping it with 
its parent until the order is correct

Since the height of a heap is O(log(N)), the complexity of bubble-up is O(log(N)).

delete_min

What this operation does is:

    delete a node with min key and return it
    reorganize the heap so the two properties still hold

To do that, we:

    remove and return the root since the node with the minimum key is always at the root
    replace the root with the last node (the rightmost node at the bottom) of the heap
    if property #2 is violated, perform a bubble-down

def bubble_down(node):

    while node is not a leaf:

        smallest_child = child of node with smallest key

        if smallest_child < node:

            swap node and smallest_child

            node = smallest_child

        else:

            break

What this says is we keep swapping between the current node and its smallest child until 
we get to the leaf, hence a "bubble down". Again the time complexity is O(log(N)) since 
the height of a heap is O(log(N)).

Implementing Heap

Being a complete tree makes an array a natural choice to implement a heap since it can be
stored compactly and no space is wasted. Pointers are not needed. The parent and children 
of each node can be calculated with index arithmetic

For node i, its children are stored at 2i+1 and 2i+2, and its parent is at floor((i-1)/2). 
So instead of node.left we'd do 2*i+1.

This is exactly how the python language implements heaps.
https://github.com/python/cpython/blob/d3a8d616faf3364b22fde18dce8c168de9368146/Lib/heapq.py#L263

tldr

A Heap

    is a complete tree
    each node of a min heap is less than all of its children
    allows O(log(N)) to insert and remove an element with priority
    is implemented with arrays

Heapify
Heap in Python

Python comes with a built-in heapq we can use, and it is a min heap, i.e. element at top 
is smallest.

heapq.heappush takes two arguments, the first is the heap (an array/list) we want to
push the element into, the second argument can be anything as long as it can be used for 
comparison. Typically we push a tuple as in python tuples are compared item by item in 
order. For example, (1, 10) is smaller than (2, 0) because the first element is smaller.
(1, 10) is smaller than (1, 20) because when the first item is same, we compare next one
and in this case 10 is smaller than 20.

heapq.heappop takes a single argument heap, and pop and return the smallest element in 
the heap.

import heapq

>>> h = []

>>> heapq.heappush(h, (5, 'write code'))

>>> heapq.heappush(h, (7, 'release product'))

>>> heapq.heappush(h, (1, 'write spec'))

>>> heapq.heappush(h, (3, 'create tests'))

>>> heapq.heappop(h) # returns

(1, 'write spec')

>>> h[0]

>>> (3, 'create tests')

If the list is known beforehand, we can create a heap out of it by simply using 
heapify``, which is actually an O(N)` operation.

import heapq

arr = [3, 1, 2]

heapq.heapify(arr)

Given a list of numbers, return top 3 smallest numbers

"""

from heapq import heapify, heappop
from typing import List

def heap_top_3(arr: List[int])->List[int]:
    heapify(arr)
    res =[]
    for i in range(3):
        res.append(heappop(arr))
    return res

if __name__=='__main__':
    arr = [int[x] for x in input().split()]
    res = heap_top_3(arr)
    print(' '.join(map(str, res)))

"""
Implementing Max Heap

The simplest way to implement a max heap is to reverse the sign of the number before we 
push it into the heap and reverse it again when you pop it out. For example, if we want 
to build a max heap out of [3, 1, 2], we can push [-3, -1, -2] into the heap. Because 
default heap is a min heap, when we pop -3 will be popped out and its reverse 3 is the 
max of the three and thus we have a max heap. We will see both min and max heaps in the 
following modules.
"""