"""
problems with this hash
- only hashes strings (we won't worry about this)
- Not constant time - linear in key length
- could be alittle more random

Seperate chaining
-With seperate chaining, at each index in our array we store values using a
more sophisticated data structure e.g an array or a linked list

This allows us to store multiple key-value pairs at the same index.

Linear Probing
-with linear probing, when we find a collision, we search through the array
to find the next empty slot.
-Unlike with seperate chaining, this allows us to store a single key-value
at each index.

Recap
- Hash tables are collections of key-value pairs
- Hash tables can find values quickly given a key
- Hash tables can add new key-values quickly
- Hash tables store data in a large array, and work by hashing the keys
- A good hash should be fast, distribute keys uniformly, and be deterministic
- seperate chaining and linear probing are two strategies used to deal with
two keys that hash to the same index

"""
def hash(key, arrayLen):
    total = 0
    for char in key:
        # map "a" to 1, "b" to 2, "c" to 3, etc.
        val = ord(char) - 96
        total =(total+val) % arrayLen
    return total
print(hash("maroon", 10))

'''
- prime number in the hash is helpful in spreading out the keys more 
uniformly
- It's also helpful if the array that you're putting values into has a 
prime length.

links:
- why do hash funtions use prime numbers?
- Does making array size a prime number help in hash table implementation?
'''
def hashUpdated(key, arrayLen):
    total = 0
    WEIRD_PRIME =31
    for  i in range(0,min(len(key), 100)):
        char = key[i]
        val = ord(char) -96
        total =(total *WEIRD_PRIME + val) % arrayLen
    return total
print("updated: ", hashUpdated("hello", 13))
print("updated: ", hashUpdated("hi", 13))
print("updated: ", hashUpdated("goodbye", 13))
print("updated: ", hashUpdated("cyan", 13))
print("updated: ", hashUpdated("pink", 13))

class HashTable:

    def __init__(self, size=4) -> None:
        self.keyMap =[None] * size

    def _hash(self, key):
        total = 0
        WEIRD_PRIME =31
        for i in range(0, min(len(key),100)):
            char = key[i]
            val =ord(char) -96
            total =(total * WEIRD_PRIME + val) % len(self.keyMap)
        return total

    '''
    set 
    - Accepts a key and a value
    - Hashes the key
    - Stores the key-value pair in the hash table array via seperate chaining
    '''
    def set(self, key, value):
        index = self._hash(key)
        if(not self.keyMap[index]):
            self.keyMap[index] =[]
        self.keyMap[index].append([key, value])

    '''
    get
    - accepts a  key
    - hashes the key
    - retrieves the key-value pair in the hash table
    - if the key isn't found, it returns undefined
    '''
    def get(self, key):
        index = self._hash(key)
        if(not self.keyMap[index]):
            return None
        for i in self.keyMap[index]:
            if(i[0] == key):
                return i[1]

    '''
    keys 
    - loops through the hash table array and returns an array of keys in 
    the table
    '''
    def keys(self):
        keys_arr =[]
        for i in self.keyMap:
            for j in i:
                keys_arr.append(j[0])
        return keys_arr
    '''
    values
    - loops through the hash table array and returns an array of values in
    the table

    '''
    def values(self):
        values_arr =[]
        for i in self.keyMap:
            for j in i:
                if (j[1] not in values_arr):
                    values_arr.append(j[1])
        return values_arr

sol =HashTable()
sol.set("hello world", "goodbye!!")
sol.set("dogs", "are cool")
sol.set("cats", "are fine")
sol.set("i love", "pizza")
sol.set("hi", "not now")
sol.set("french", "fries")
sol.set("local", "fries")
sol.set("stange", "fries")
print(sol.keyMap)
print("get 0:", sol.get("hi"))
print("keys:", sol.keys())
print("values:", sol.values())