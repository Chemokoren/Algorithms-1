"""
Suffix Trie Construction

- create babc

            o
          / | \
         b  a  c
        / \  \  \
       *   a  b  *
           |  |
           b  c
           |  | 
           c  * 
           |
           *
"""

class SuffixTrie:

    def __init__(self,string) -> None:
        self.root ={}
        self.endSymbol ="*"
        self.populateSuffixTrieFrom(string)

    # O(n^2) time | O(n^2) space except where a single character is repeated giving O(n) space
    def  populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    def insertSubstringStartingAt(self, i, string):
        node = self.root 
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] ={}
            node =node[letter]
        node[self.endSymbol] =True

    # O(m) time | O(1) space where m is the length of the input string
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node

my_string ="babc"

sol= SuffixTrie(my_string)

find_string ="abd"

print(sol.contains(find_string))