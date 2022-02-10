from typing import List
import collections
"""
Word Ladder

A transformation sequence from word beginWord to word endWord using a dictionary wordList is
a sequence of words beginWord-> s1 -> s2 -> ... -> sk such that:

-Every adjacent pair of words differs by a single letter.
-Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of 
words in the shortest transformation sequence from beginWord to endword, or 0 if no such
sequence exists.

Example 1:

Input: beginWord = "hit", endWord ="cog", wordList =["hot", "dot", "dog", "lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" ->"dot"->"dog"->"cog",
which is 5 words long.

Constrains:
len(w) <= 10
len(list) <=5000

transform n^2m to n.m^2 because m is smaller than n according to the constraints

BFS is much more efficient to find the shortest path than DFS

(use n.m^2 to generate adjacency list and n^2.m to traverse using BFS)

"""

class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str])->int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern =word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)

        visit =set([beginWord])
        q = collections.deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] +"*"+word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0
