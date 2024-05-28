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

transform n^2.m to n.m^2 because m is smaller than n according to the constraints

BFS is much more efficient to find the shortest path than DFS

(use n.m^2 to generate adjacency list and n^2.m to traverse using BFS)

"""

class Solution:
    """
    This class provides a solution to the 'Word Ladder' problem.

    The problem asks for the minimum number of word transformations
    needed to get from a 'beginWord' to an 'endWord' using only words
    from a provided 'wordList'.

    A transformation consists of changing a single letter in the word.
    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Calculates the minimum number of word transformations needed
        to reach the 'endWord' from the 'beginWord' using words in 'wordList'.

        Args:
            beginWord (str): The starting word.
            endWord (str): The target word.
            wordList (List[str]): A list of valid words for transformations.

        Returns:
            int: The minimum number of transformations needed (or 0 if impossible).
        """

        if endWord not in wordList:
            return 0  # No solution if endWord is not in the word list

        # Build a dictionary to efficiently find neighboring words
        nei = collections.defaultdict(list)
        wordList.append(beginWord)  # Add beginWord for completeness
        for word in wordList:
            for i in range(len(word)):
                # Create a pattern with '*' replacing a single character
                pattern = word[:i] + "*" + word[i + 1:]
                nei[pattern].append(word)

        # Visited words to avoid cycles
        visit = set([beginWord])
        # Queue to store words for exploration in BFS order
        q = collections.deque([beginWord])
        # Depth counter to track transformation steps
        res = 1

        while q:
            for _ in range(len(q)):  # Process all words in current level
                word = q.popleft()
                if word == endWord:
                    return res  # Found the end word, return transformation count

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)

            res += 1  # Move to the next level of transformations

        return 0  # No solution found if the loop completes


beginWord = "hit"
endWord ="cog"
wordList =["hot", "dot", "dog", "lot","log","cog"]

sol = Solution()
print(sol.ladderLength(beginWord, endWord, wordList))

import unittest

class TestWordLadder(unittest.TestCase):
    """
    test_empty_wordlist: Checks the case where the provided word list is empty.
    test_target_not_in_list: Ensures the function returns 0 if the target word is not present in the word list.
    test_simple_ladder: Tests a basic scenario with a single transformation.
    test_longer_ladder: Tests a case with multiple transformations.
    test_no_solution: Verifies that the function returns 0 if there's no valid word ladder connecting the begin and end words.
    test_same_word: Confirms that 0 is returned if the begin and end words are the same.
    """

    def test_empty_wordlist(self):
        """Tests the case where the word list is empty."""
        solution = Solution()
        beginWord = "hit"
        endWord = "cog"
        wordList = []
        result = solution.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(result, 0)

    def test_target_not_in_list(self):
        """Tests the case where the target word is not in the word list."""
        solution = Solution()
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog"]
        result = solution.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(result, 0)

    def test_simple_ladder(self):
        """Tests a simple word ladder with one transformation."""
        solution = Solution()
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "cog"]
        result = solution.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(result, 5)  # 1 transformation (hit -> hot -> dot -> dog -> cog)

    def test_longer_ladder(self):
        """Tests a longer word ladder with multiple transformations."""
        solution = Solution()
        beginWord = "leet"
        endWord = "code"
        wordList = ["leet", "leetc", "codes", "code"]
        result = solution.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(result, 2)  # 2 transformations (leet -> leetc -> code)

    def test_no_solution(self):
        """Tests the case where there is no possible word ladder."""
        solution = Solution()
        beginWord = "horse"
        endWord = "ros"
        wordList = ["hot", "dot", "dog", "lot"]
        result = solution.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(result, 0)

    def test_same_word(self):
        """Tests the case where the beginWord and endWord are the same."""
        solution = Solution()
        beginWord = "hit"
        endWord = "hit"
        wordList = ["hot", "dot", "dog"]
        result = solution.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(result, 0)  # No transformation needed

if __name__ == '__main__':
    unittest.main()
