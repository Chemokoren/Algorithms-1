from typing import List
"""
Given an m*x board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where 
adjacent cells are horizontally or vertically neighboring. 

The same letter cell may not be used more than once in a word.

Example 1:

o       a       a       n

e       t       a       e

i       h       k       r

i       f       l       v

Input: board =[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
words = ["oath","eat","rain"]
Output: ["eat","oath"]

1dfs =4^mn (where mn are the dimensions of the board)
total time complexity wmn*4^mn (mn*4^mn because we will be doing dfs at each position) 
                                where w is every single word
We can omit w by using Trie(prefix tree)
"""

class TrieNode:

    def __init__(self):
        self.children ={}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] =TrieNode()
            cur =cur.children[c]
        cur.isWord =True

class Solution:

    def findWords(self, board: List[List[str]], words: List[str])->List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit =set(), set()

        def dfs(r, c, node, word):
            if(r < 0 or c < 0 or r ==ROWS or c == COLS or \
                board[r][c] not in node.children 
               or (r,c) in visit):
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r + 1, c , node, word)
            dfs(r - 1, c , node, word)
            dfs(r , c + 1, node, word)
            dfs(r , c - 1, node, word)
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)

board =[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words =["oath","pea","eat","rain"]

sol =Solution()
print(sol.findWords(board,words))