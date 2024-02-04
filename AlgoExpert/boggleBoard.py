"""
[[t, h, i, s, i, s, a]
[s, i, m, p, l, e, x]
[b, x, x, x, x, e, b]
[x, o, g, g, l, x, o]
[x, x, x, D, T, r, a]
[R, E, P, E, A, d, x]
[x, x, x, x, x, x, x]
[N, O, T, R, E, -, P]
[x, x, D, E, T, A, E]]

this
is 
no
a
simple
boggle
board
test
REPEATED
NOTRE-PEATED

Write a function that will return a list of words containing the list of words provided
above that are also in the boggle board

"""

"""
    The boggle_board function takes a boggle board (board) and a list of words (words) as input and 
    returns a list of valid words found on the board.
    It creates a Trie data structure (trie) and adds all words to it using the add method.
    It initializes a dictionary (finalWords) to store the final valid words found on the board.
    It initializes a 2D grid (visited) to keep track of visited cells on the board.
    It iterates through each cell on the board and calls the explore function to search for valid words starting from that cell.
    After exploring all cells, it returns the list of valid words found on the board.

    Time Complexity:

    Trie Construction: Constructing the Trie from the given list of words has a time complexity of
    O(w⋅s), where w is the number of words, and s is the length of the longest word.

    Exploring the Board: We iterate through each cell of the board, and for each cell, we perform 
    a depth-first search (DFS) to explore its neighboring cells. In the worst-case scenario, each DFS
    might explore up to 8^s cells, where s is the length of the longest word in the Trie. 
    Therefore, the time complexity for exploring the board is O(n⋅m⋅8^s).

Overall Time Complexity:

    The overall time complexity is dominated by constructing the Trie (O(w⋅s)) and exploring the
     board (O(n⋅m⋅8^s)). Therefore, the overall time complexity is O(w⋅s+n⋅m⋅8^s).

Space Complexity:

    Trie: Constructing the Trie from the given list of words requires space to store the nodes. 
    In the worst case, if all words are unique and have no common prefixes, the space complexity of 
    the Trie would be O(w⋅s), where w is the number of words, and s is the length of the longest word.

    Visited Array: We use a 2D array to keep track of visited cells on the board. The space complexity
    of this array is O(n⋅m), where n is the width and m is the height of the board.

    Final Words Dictionary: We use a dictionary to store the final valid words found on the board.
  In the worst case, if all words in the Trie are present on the board, the space complexity would 
  be O(w⋅s).

Overall Space Complexity:

    The overall space complexity is dominated by the space required for the Trie, the visited array, 
    and the final words dictionary. Therefore, the overall space complexity is O(w⋅s+n⋅m).

This revised analysis considers the space required for the Trie, the visited array, and the final words
dictionary, providing a more accurate estimation of the overall space complexity.
"""
# O(nm *8^s + ws) time | O(nm + ws) Where n is the width & m is the height of the board,
# s is the length of the longest word, w is the number of words and s is the length of longest word

# O(nm + ws) - nm coz of the visited array and ws for Trie
def boggle_board(board, words):
    """
    Find valid words on the boggle board.

    Args:
        board (List[List[str]]): 2D grid representing the boggle board.
        words (List[str]): List of words to search for on the board.

    Returns:
        List[str]: List of valid words found on the board.
    """

    # Create a Trie data structure and add all words to it.
    trie = Trie()
    for word in words:
        trie.add(word)

    # Initialize a dictionary to store the final valid words found on the board.
    finalWords = {}

    # Initialize a 2D grid to keep track of visited cells on the board.
    visited = [[False for letter in row] for row in board]

    # Iterate through each cell on the board.
    for i in range(len(board)):
        for j in range(len(board[i])):
            # Explore the board starting from the current cell and search for valid words.
            explore(i, j, board, trie.root, visited, finalWords)

    # Return the list of valid words found on the board.
    return list(finalWords.keys())


"""
The explore function recursively explores the board starting from the cell (i, j).
It checks if the current cell has already been visited, if the letter at the cell exists in the
current trie node, and if the end symbol '*' exists in the trie node to indicate a valid word.

If a valid word is found, it is added to the finalWords dictionary.
The function then recursively explores the neighboring cells of the current cell.
After exploring all neighbors, the current cell is marked as unvisited to allow other paths to
explore it again

"""
def explore(i, j, board, trieNode, visited, finalWords):
    """
    Explore the board recursively to find valid words starting from the cell (i, j).

    Args:
        i (int): Row index of the current cell.
        j (int): Column index of the current cell.
        board (List[List[str]]): 2D grid representing the board.
        trieNode (dict): Current node in the trie representing the prefix of words.
        visited (List[List[bool]]): 2D grid representing visited cells on the board.
        finalWords (dict): Dictionary to store final words found on the board.

    Returns:
        None
    """

    # If the cell has already been visited, return.
    if visited[i][j]:
        return

    # Get the letter at the current cell.
    letter = board[i][j]

    # If the letter is not in the trie node, return.
    if letter not in trieNode:
        return

    # Mark the current cell as visited.
    visited[i][j] = True

    # Move to the next node in the trie.
    trieNode = trieNode[letter]

    # If the end symbol '*' is found in the trie node, add the corresponding word to finalWords.
    if "*" in trieNode:
        finalWords[trieNode["*"]] = True

    # Get neighboring cells of the current cell.
    neighbors = get_neighbors(i, j, board)

    # Recursively explore each neighboring cell.
    for neighbor in neighbors:
        explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWords)

    # Mark the current cell as unvisited after exploring its neighbors.
    visited[i][j] = False


"""
    We define a function get_neighbors that takes the row index i, column index j, and the board as input.
    We initialize an empty list neighbors to store the neighboring cell coordinates.
    We check each direction around the cell (i, j) to see if there are neighboring cells, and if so, we append their coordinates to the neighbors list.
    Finally, we return the list of neighboring cell coordinates.
"""
def get_neighbors(i, j, board):
    """
    Get the neighbors of a cell (i, j) on the board.

    Args:
        i (int): Row index of the cell.
        j (int): Column index of the cell.
        board (List[List[str]]): 2D grid representing the board.

    Returns:
        List[List[int]]: List of coordinates of neighboring cells.
    """

    # Initialize an empty list to store the neighbors.
    neighbors = []

    # Check if the cell has a neighbor to the top-left.
    if i > 0 and j > 0:
        neighbors.append([i - 1, j -1])

    # Check if the cell has a neighbor to the top-right.
    if i > 0 and j < len(board[0]) -1:
        neighbors.append([i - 1, j + 1])

    # Check if the cell has a neighbor to the bottom-right.
    if i < len(board) -1 and j < len(board[0]) -1:
        neighbors.append([i + 1, j + 1])

    # Check if the cell has a neighbor to the bottom-left.
    if i < len(board) -1 and j > 0:
        neighbors.append([i + 1, j - 1])

    # Check if the cell has a neighbor to the top.
    if i > 0:
        neighbors.append([i - 1, j])

    # Check if the cell has a neighbor to the bottom.
    if i < len(board) -1:
        neighbors.append([i + 1, j])

    # Check if the cell has a neighbor to the left.
    if j > 0:
        neighbors.append([i, j - 1])

    # Check if the cell has a neighbor to the right.
    if j < len(board[0]) -1:
        neighbors.append([i, j + 1])

    # Return the list of neighboring cell coordinates.
    return neighbors


class Trie:
    """
    Trie data structure implementation for efficient prefix-based searching.
    """

    def __init__(self):
        """
        Initialize a Trie object with an empty root node.
        """
        self.root = {}
        self.endSymbol = "*"

    def add(self, word):
        """
        Add a word to the Trie.

        Args:
            word (str): The word to be added to the Trie.
        """
        current = self.root
        for letter in word:
            # If the letter is not already present in the current node's children,
            # create a new node for it.
            if letter not in current:
                current[letter] = {}
            # Move to the next node corresponding to the letter.
            current = current[letter]
        # Mark the end of the word by adding the end symbol as a key in the current node.
        # This indicates that the word ends at this node.
        current[self.endSymbol] = word


board=[
        ['t', 'h', 'i', 's', 'i', 's', 'a'],
        ['s', 'i', 'm', 'p', 'l', 'e', 'x'],
        ['b', 'x', 'x', 'x', 'x', 'e', 'b'],
        ['x', 'o', 'g', 'g', 'l', 'x', 'o'],
        ['x', 'x', 'x', 'D', 'T', 'r', 'a'],
        ['R', 'E', 'P', 'E', 'A', 'd', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['N', 'O', 'T', 'R', 'E', '-', 'P'],
        ['x', 'x', 'D', 'E', 'T', 'A', 'E']
    ]
words =['this','is', 'no','a','simple','boggle','board''test','REPEATED','NOTRE-PEATED']


import unittest 
class BoggleBoardTest(unittest.TestCase):

    def test_boggle_board(self):
        self.assertListEqual(boggle_board(board, words), ['this', 'is', 'simple', 'a', 'boggle', 'NOTRE-PEATED'])

    def test_empty_list(self):
        self.assertNotEqual(boggle_board(board, words), [])

if __name__ =="__main__":
    unittest.main()