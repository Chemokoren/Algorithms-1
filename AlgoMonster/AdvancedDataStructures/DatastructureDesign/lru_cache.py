"""
LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support get and 
put operations.

    get(key): Get the value (which will always be positive) of the key if the key exists in the cache,
    otherwise return -1.
    put(key, value): Set or insert the value if the key is not already present. When the cache reached
    its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Can you do both operations in O(1) time complexity?
Input

    operations: the operations

Output

the return values of get operations
Examples
Example 1:

Input:

operations = ```

LRUCache 2

put 1 1

put 2 2

get 1

put 3 3

get 2

put 4 4

get 1

get 3

get 4


**Output**: ````

1

-1

-1

3

4

`

Explanation:

See input.
"""

from typing import List

def exec(operations: List[List[str]]) -> List[int]:
    return []

if __name__ == '__main__':
    operations = [input().split() for _ in range(int(input()))]
    res = exec(operations)
    print(' '.join(map(str, res)))