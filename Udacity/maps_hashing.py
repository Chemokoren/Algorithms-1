"""
When we're talking about hash tables, we can define a "load factor":

Load Factor = Number of Entries / Number of Buckets

The purpose of a load factor is to give us a sense of how "full" a hash table is. For example, if we're trying
to store 10 values in a hash table with 1000 buckets, the load factor would be 0.01, and the majority of 
buckets in the table will be empty. We end up wasting memory by having so many empty buckets, so we may want 
to rehash, or come up with a new hash function with less buckets. We can use our load factor as an indicator 
for when to rehash—as the load factor approaches 0, the more empty, or sparse, our hash table is.

On the flip side, the closer our load factor is to 1 (meaning the number of values equals the number of 
buckets), the better it would be for us to rehash and add more buckets. Any table with a load value greater
than 1 is guaranteed to have collisions. 


Load factor Example

One of your coworkers comes to you with a hash function that divides a group of values by 100, and uses the
remainder as a key. The values are 100 numbers that are all multiples of 5

What is the load factor ? Answer: 1

He thinks it's alittle slow - what number would you recommend his function to divide by rather than 
100 to speed it up?


Question:
---------

In this quiz, you'll write your own hash table and hash function that uses string keys. Your table will store
strings in buckets by their first two letters, according to the formula below:

Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 

You can assume that the string will have at least two letters, and the first two characters are uppercase 
letters (ASCII values from 65 to 90). You can use the Python function ord() to get the ASCII value of a 
letter, and chr() to get the letter associated with an ASCII value.

You'll create a HashTable class, methods to store and lookup values, and a helper function to calculate a 
hash value given a string. You cannot use a Python dictionary—only lists! And remember to store lists at each 
bucket, and not just the string itself. For example, you can store "UDACITY" at index 8568 as ["UDACITY"].


"""

"""
Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string.

"""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        pass

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        return -1
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))


"""
class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def lookup(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]:
                    return hv
        return -1

    def calculate_hash_value(self, string):
        value = ord(string[0])*100 + ord(string[1])
        return value

"""