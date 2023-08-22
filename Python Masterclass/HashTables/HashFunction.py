"""
Objectives
- Explain what a hash table is
- Define what a hashing algorithm 
- Discuss what makes a good hashing algorithm
- Understand how collisions occur in a hash table
- Handle collissions using seperate chaining or linear probing

What is a hash table?
- Hash tables are used to store  key-value pairs
- They are like arrays, but the keys are not ordered.
- Unlike arrays, hash tables are fast for all of the following operations: finding values,
adding new values, and removing values!

Why shoud I care?

-Nearly every programming language has some sort of hash table data structure
- Because of their speed, hash tables are very commonly used!

Hash tables in the wild
-Python has Dictionaries
-JS has Objects and Maps*
-Java, Go, & Scala have Maps
-Ruby has ... Hashes

* Objects have some restrictions, but are basically hash tables

How would we implement our own version???

THE HASH PART
- To implement a hash table we'll be using an array.
- In order to look up values by key, we need a way to convert keys into valid array
indices
- A function that performs this task is called a hash function

What Makes a Good Hash? (not a cryptographically secure one)
- Fast(i.e. constant time)
- Doesn't cluster outputs at specific indices, but distributes uniformly e.g. not 
everything can be hashed to a zero
- Deterministic (same input yields same output)

Prime numbers?
- The prime number in the hash is helpful in spreading out the keys more uniformly.

- It's also helpful if the array that you're putting values into has a prime length.

links if you're curious:
 why do hash functions use prime numbers?
 Does making array size a prime number help in hash table implementation?

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
-Unlike seperate chaining, this allows us to store a single key-value
at each index.

Big O of Hash tables
Time Complexity
(average case)

-insert: O(1)
-Deletion: O(1)
-Access: O(1)

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
print("hello: ", hashUpdated("hello", 13))
print("hi: ", hashUpdated("hi", 13))
print("goodbye: ", hashUpdated("goodbye", 13))
print("cyan: ", hashUpdated("cyan", 13))
print("pink: ", hashUpdated("pink", 13))

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
    set method
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
    get method
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
    keys method
    - loops through the hash table array and returns an array of keys in the table
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