"""
Design a data structure that follows the constraints of a Least Recenly used (LRU) cache.
It should support the get and put operations.

get(key): get the value(will always be positive) of the key if the key exists in the cache 
otherwise return -1
put(key, value): set or insert hte value if the ikey is not already present. If it is we will
update the key with our new value.

Implement the LRUCache class:
- LRUCache(int capacity) initialize the LRU cache with positive size capacity
- int get(int key) return the value of the key if the key exists otherwise return -1
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, 
add the key-value pair to the cache. If the number of keys exceeds the capacity from this
operation, evict the least recently used key.

when the cache reached its capacity, put(key, value) should invalidate the least
recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Cache -is a memory that stores data for it to be served faster in the future. It's purpose 
is to speed up data requests

LRU = Least recently used is a  policy that is used to remove items from the cache.
Stacks follow the LIFO policy, queues follow the FIFO policy, a cache can follow the LRU policy.

Example:
cache: [2,3,4,5]
What this means is that 2 was accessed the most recently, followed by 3, followed by 4 and
then 5.
Sy we want to add a new item 1, where would we add it?

Using the LRU principle, we should remove the least recently used item, aka, the 5
We would add it right at the front of the cache because that means that 1 was the most recently 
used item.
[1,2,3,4]

The functions get and put must each run in O(1) average time complexity.

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:

1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.

"""
from collections import deque

class LRUCache:
    def __init__(self, capacity:int) -> None:
        self.c = capacity
        self.m = dict()
        self.deq =deque()

    def get(self, key:int)->int:
        if key in self.m:
            value = self.m[key]
            self.deq.remove(key)
            self.deq.append(key)
            return value
        else:
            return -1

    def put(self, key:int, value:int)->None:
        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 obj.get(key)
        # obj.put(key, value)
        if key not in self.m:
            if len(self.deq) == self.c:
                oldest = self.deq.popleft()
                del self.m[oldest]

        else:
            self.deq.remove(key)

        self.m[key] =value
        self.deq.append(key)
        

first =  [1, 10]
second = [2, 11]
third = [3, 15]
fourth =[4, 16]

sol =LRUCache(4)
sol.put(1,10)
sol.put(2,11)
sol.put(3,15)
sol.put(4,16)
print("dictionary before : ",sol.deq)
print(sol.get(4))
print("dictionary after : ",sol.deq)
sol.put(5,20)
print("dictionary XXXXX : ",sol.deq)