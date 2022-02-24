"""
Word Ladder

Word Ladder is "a puzzle begins with two words, and to solve the puzzle one must find a chain
of other words to link the two, in which two adjacent words(that is, words in successive steps)
differ by one letter."

For example: COLD -> CORD ->CARD ->WARD ->WARM

WARM
WARD
CARD
CORD
COLD

Given a start word, an end word and a list of dictionary words. Determine the minimum number
of steps to go from the start word to the end word using only words from the dictionary.

Input:

start ="COLD"
end  = "WARM"
word_list =["COLD","GOLD","CORD","SOLD","CARD","WARD","WARM","TARD"]

Output:

4

Explanation: We can go from COLD to WARM by going through COLD -> CORD -> CARD -> WARD ->WARM


"""
from typing import List

def word_ladder(begin: str, end: str, word_list: List[str]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return 0

if __name__ == '__main__':
    begin = input()
    end = input()
    word_list = input().split()
    res = word_ladder(begin, end, word_list)
    print(res)