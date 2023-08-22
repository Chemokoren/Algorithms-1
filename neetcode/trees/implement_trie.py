"""
Implement Trie (Prefix Tree)

A trie(pronounced as "try") or prefix tree is a tree data structure used to efficiently store &
retrieve  keys in a dataset of strings. There are various applications of this data structure, 
such as autocomplete and spellchecker.

Implement the Trie class:

- Trie() initializes the trie object
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie(i.e. was inserted
before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string 
word that has the prefix, and false otherwise.

Example 1:

Input
["Trie", "insert","search", "search","startsWith","insert","search"]
[[],["apple"],["apple"],["app"],["app"],["app"]]

output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple")
trie.search("apple") // return True
trie.search("app") // return False
trie.startsWith("app"); // return True
"""

class TrieNode:
    """
    Initializing the TrieNode
    """

    def __init__(self):
        self.children ={}
        self.endOfWord= False

class Trie:

    def __init__(self):
        """
        Initializing the data structure
        """
        self.root = TrieNode()

    def insert(self, word: str)->None:
        """
        Inserts a word into the trie.
        """
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str)->bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def starts_with(self, prefix: str)->bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

        


trie = Trie()
trie.insert("apple")
print("search for apple::", trie.search("apple")) # return True
print("search for app::", trie.search("app")) # return False
print("search for word starting with app::", trie.starts_with("app")) # return True