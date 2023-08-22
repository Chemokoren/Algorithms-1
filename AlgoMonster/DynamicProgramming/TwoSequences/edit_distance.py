"""
Edit Distance

Edit Distance

There are two words word1 and word2, you have to find the minimum number of operations required to convert word1 to word2.

You are allowed to use the following 3 operations on a word:

    Insert a character
    Delete a character
    Replace a character

Example 1:
Input:

word1 = "almost"

word2 = "algomonster"

Output:5
Explanation:

almost    ->  algmost    (insert 'g')

algmost   ->  algomost   (insert 'o')

algomost  ->  algmonst   (insert 'n')

algomonst ->  algomoste  (insert 'e')

algomoste ->  algomoster (insert 'r')

Example 2:
Input:

  word1 = "intention"

  word2 = "execution"

Output:5
Explanation:

intention  ->  inention   (remove 't')

inention   ->  enention   (replace 'i' with 'e')

enention   ->  exention   (replace 'n' with 'x')

exention   ->  exection   (replace 'n' with 'c')

exection   ->  execution  (insert 'u')
"""