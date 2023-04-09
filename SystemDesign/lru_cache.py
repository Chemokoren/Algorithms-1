"""
LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It
should support the following operations: get and set.

get(key) - Get the value (will always be positive) if the key exists in
the cache, otherwise return -1.

set(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used
item before inserting a new item.

"""
from collections import OrderedDict

class LRUCache(object):
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()
        
        
    def get(self, key):
        """
        :rtype:int
        """
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1
        
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if len(self.cache) >= self.capacity and key not in self.cache:
            self.cache.popitem(last=False)
            self.cache[key] =value
            
        else:
            if key in self.cache:
                self.cache.pop(key)
                self.cache[key] = value
            else:
                self.cache[key] = value