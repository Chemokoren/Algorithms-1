"""
Word Ladder

A transformation sequence from word beginword to word endword using a dictionary wordList is a 
sequence of words beginWord ->s1->s2...->sk such that:
    - Every adjacent pair of words differs by a single letter.
    - Every s1 for 1 <=i <= k is in wordList. Note that beginWord does not need to be in wordList.
    - sk == endWord
Given two words, beginWord and endword, and a dictionary wordList, return the number of words in
the shortest transformation sequence from beginWord to endWord, or 0 if no such sequences exists.

Example 1:
Input: beginWord ="hit", endWord="cog", wordList =["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit"-> "hot"->"dot"->"dog"->"cog", which is
5 words long.

naive approach: n^2*m time complexity ( can be converted to n*m^2)

# patterns: hot , [*ot, h*t, ho*], dot ,[*ot, d*t, do*]

# generating the adjacency list will take n*m^2 time


hit -> hot -> [dot,lot] ->[dog,log] ->cog

"""
import collections
from typing import List
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str])-> int:
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern =word[:j]+"*"+word[j + 1:]
                nei[pattern].append(word)
        visit =set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern =word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res +=1
        return 0

beginWord ="hit"
endWord="cog"
wordList =["hot","dot","dog","lot","log","cog"]

sol = Solution()
print(sol.ladderLength(beginWord,endWord,wordList))