"""
Design a data structure that supports adding new words and finding if a string matches
any previously added string.

Implement the WordDictionary class:

-WordDictionary() Initializes the object.
-void addWord(word) Adds word to the data structure, it can be matched later.
-bool search(word) Returns true if there is any string in the data structure that 
 matches word or false
otherwise. word may contain dots '.' where dots can be matched with any letter.

Example :

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

Output :
[null,null,null,null,false,true,true,true]

Explanation

WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
"""

class TrieNode:
    def __init__(self):
        self.children={} # a: TrieNode
        self.word = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        
        """
        self.root = TrieNode()

    def addWord(self, word: str)-> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str)->bool:
        
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):# we are skipping the dot
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        return dfs(0, self.root)


obj =WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
# obj.addWord("pad")

print("has the word pad:",obj.search("pad"))
print("has the word bad:",obj.search("bad"))
print("starts with any character:",obj.search(".ad"))
print("starts with b and ends in any character:",obj.search("b.."))