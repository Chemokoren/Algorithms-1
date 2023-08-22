class Node:
    def __init__(self):
        self.children ={}
        self.endofword =False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str)->None:
        """
        Inserts a word into the trie
        """
        ptr = self.root 

        for letter in word:
            if letter not in ptr.children:
                ptr.children[letter] = Node()
            ptr = ptr.children[letter]
        ptr.endofword = True
    
    def search(self, word: str)->bool:
        """
        Returns if the word is in the trie
        """
        ptr= self.root
        for letter in word:
            if letter not in ptr.children:
                return False
            ptr = ptr.children[letter]
            
        # check end of word
        if ptr.endofword:
            return True
        else:
            return False

    def startsWith(self, prefix: str)->bool:
        """
        Returns if there is any word in the trie that starts with the given prefix
        """
        ptr = self.root
        for letter in prefix:
            if letter not in ptr.children:
                return False
            ptr = ptr.children[letter]
        return True

trie = Trie()
trie.insert('apple')
print("search apple: ",trie.search('apple'))
print("search app: ",trie.search('app'))      
trie.startsWith('app') # true
trie.insert('app')
print("search app: ",trie.search('app') )


print("====================================== implementing a Trie using dictionary ======================================")
'''
Time complexity:
insert: O(key_length)
search: O(key_length)

'''
class TrieDict:
    head ={}

    def add(self, word):
        cur = self.head

        for  ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True

    def search(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if '*' in cur:
            return True
        else:
            return False

dictionary = TrieDict()
dictionary.add("hi")
dictionary.add("hello")
print(dictionary.search("hi"))
print(dictionary.search("hello"))
print(dictionary.search("hel"))
print(dictionary.search("hey"))
