"""
Word Search II | Depth First Search + Trie

For this question we ask you to determine if it is possible to make certain words given a 2-d matrix 
of characters. What we mean is that you will be given a 2-d grid of characters as well as a list of
words. You may start at any point on the grid and move from cell to cell without looping back to a 
cell already travelled through and see if it is possible to make every word in the list of words. 
Output all possible words that can be created in the EXACT order that they appear in the list. 
The input for the matrix will appear as a list of words to represent the matrix.

NOTE: test case 7 might be hard to handle for slower languages such as Javascript and Python in which 
case you should skip the case. Solutions written in faster compiled languages such as Java and C++ 
should aim to pass the case.

Input

    matrix: list of strings representing the 2-d matrix of characters
    words: list of words to check if they can be made

Output

list of all possible words that can be made
Examples

Example 1:

Input:

matrix = [aab, aaa]

words = [bb, aa, abaa]

Output: [aa, abaa]

Explanation:

We can easily make aa by starting at any of the cells containing a in the matrix then moving to 
another cell containing a. We cannot make bb as once we start at the 1 b position there is no other 
b to move onto to make bb.

Constraints

    1 <= (row of matrix) * (column of matrix) <= 100
    Each character will be a lower case english letter
    1 <= words.length <= 30001
    1 <= words[i].length <= 10

"""
from typing import List

def word_search_ii(matrix: List[str], words: List[str]) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    return []

if __name__ == '__main__':
    matrix = input().split()
    words = input().split()
    res = word_search_ii(matrix, words)
    print(' '.join(res))