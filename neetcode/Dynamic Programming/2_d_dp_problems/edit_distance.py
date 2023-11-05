"""
Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to
convert  word1 to word2.

You have the following three operations permitted on a word:

- insert a character
- delete a character
- replace a character

Example 1:
Input: word1 ="horse", word2="ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
"""

class Solution:

    def word_convert(word1 : str, word2:str) -> int:

        def dfs(i, j, a, count):
            # base case 1
            if word1 and word2 =="":
                return len(word1)
            # base case 2
            if word1 =="" and word2:
                return len(word2)
            
            if a == word2:
                return count
            
            if (word1[i] == word2[j]):
                i +=1
                j +=1
                a = a + word1[i]
            else:
                # I need to make three decisions: replace, delete, and Insert
                replace_operation=""
                delete_operation=""
                insert_operation=""
                count = min(replace_operation, delete_operation, insert_operation)
        return dfs(0, 0, "", count=0)
    
    """
    code walkthrough
    ----------------

    Here's a detailed explanation of the code:

    The word_convert function takes two strings, word1 and word2, as input.

    It initializes a recursive function dfs that explores the conversion from word1 to word2. The function takes three parameters: i and j represent the current positions in word1 and word2, respectively, and count represents the current cost (the number of operations).

    There are three base cases:

        Base Case 1: If j has reached the end of word2, it means there are characters left in word1 that need to be deleted. The function returns the count plus the remaining characters in word1 (len(word1) - i).

        Base Case 2: If i has reached the end of word1, it means there are characters left in word2 that need to be inserted into word1. The function returns the count plus the remaining characters in word2 (len(word2) - j).

        Base Case 3: If the characters at the current positions i and j in word1 and word2 match, there is no cost associated with this character. The function recursively calls itself with i and j incremented by 1 and the same count.

    If the characters at i and j do not match, the function explores three possible operations:
        Replace Operation: It makes a recursive call with i and j incremented by 1 and count incremented by 1.
        Delete Operation: It makes a recursive call with only i incremented by 1 and count incremented by 1.
        Insert Operation: It makes a recursive call with only j incremented by 1 and count incremented by 1.

    The function returns the minimum cost among these three operations (replace, delete, insert) by using min(replace_op, delete_op, insert_op).

    The main word_convert function starts the recursion by calling dfs with initial values: i=0, j=0, and count=0.

    The final result returned by the dfs function is the minimum cost required to convert word1 to word2, considering replacement, deletion, and insertion operations.

This code uses recursion to explore all possible conversion paths, and the result is the minimum cost required to transform one word into another.




    The time complexity of this algorithm is exponential, specifically O(3^N), where N is the length of the longer of the two input words, word1 or word2. The reason for the exponential time complexity is that the algorithm explores all possible combinations of replacements, deletions, and insertions, resulting in a branching factor of 3 at each character position.

    The space complexity is determined by the depth of the recursion, which can go as deep as the length of the longer word. Therefore, the space complexity is O(N), where N is the maximum length between word1 and word2. This space complexity accounts for the call stack memory used during the recursion.

    """
    def word_convert_2(self, word1: str, word2: str) -> int:

        def dfs(i, j, count):
            # Base case 1: If word2 is empty, we need to delete remaining characters in word1.
            if j == len(word2):
                return count + len(word1) - i

            # Base case 2: If word1 is empty, we need to insert remaining characters from word2.
            if i == len(word1):
                return count + len(word2) - j

            # Base case 3: If the characters match, just move to the next character.
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1, count)

            # Apply the three operations: replace, delete, insert.
            replace_op = dfs(i + 1, j + 1, count + 1)  # Replace
            delete_op = dfs(i + 1, j, count + 1)        # Delete
            insert_op = dfs(i, j + 1, count + 1)        # Insert

            # Return the minimum cost among these three operations.
            return min(replace_op, delete_op, insert_op)

        return dfs(0, 0, 0)
    '''
    This code defines a function, word_convert_operations, which is designed to find the minimum cost and a list of operations required to transform one word, word1, into another word, word2, using three types of operations: replace, delete, and insert.

Here's a step-by-step explanation of what's happening in the code:

    The word_convert_operations function takes two strings, word1 and word2, as input.

    It defines a nested function, dfs, which stands for "depth-first search." This function is responsible for exploring and finding the minimum cost and the sequence of operations to convert word1 into word2. It takes four parameters:
        i: The current position in word1.
        j: The current position in word2.
        count: The current cost, which keeps track of the number of operations performed.
        operations: A list that records the sequence of operations performed.

    There are three base cases:
        Base Case 1: If j has reached the end of word2, it means that there are characters left in word1 that need to be deleted. The function returns the count plus the length of the remaining characters in word1, and appends a "Delete" operation to the operations list.
        Base Case 2: If i has reached the end of word1, it means that there are characters left in word2 that need to be inserted into word1. The function returns the count plus the length of the remaining characters in word2, and appends an "Insert" operation to the operations list.
        Base Case 3: If the characters at the current positions i and j in word1 and word2 match, there is no cost associated with this character. The function makes a recursive call to dfs with i and j incremented by 1, and the same count and operations.

    If the characters at i and j do not match, the function explores three possible operations:
        Replace Operation: It makes a recursive call to dfs with i and j incremented by 1, count incremented by 1, and a "Replace" operation appended to the operations list.
        Delete Operation: It makes a recursive call to dfs with only i incremented by 1, count incremented by 1, and a "Delete" operation appended to the operations list.
        Insert Operation: It makes a recursive call to dfs with only j incremented by 1, count incremented by 1, and an "Insert" operation appended to the operations list.

    The function returns the minimum cost among these three operations, along with the list of operations that led to that minimum cost. It compares the three options (replace_op, delete_op, and insert_op) and selects the one with the minimum cost. This is achieved using conditional statements.

    The main word_convert_operations function starts the recursion by calling dfs with initial values: i=0, j=0, count=0, and an empty operations list.

    The final result returned by the dfs function is the minimum cost required to convert word1 to word2, along with the sequence of operations that achieved that minimum cost.

In summary, this code uses recursion to explore different paths to transform one word into another and keeps track of the sequence of operations needed to achieve the transformation. It finds the minimum cost by considering three types of operations: replace, delete, and insert.
    '''
    def word_convert_operations(self, word1: str, word2: str) -> (int, list):
        def dfs(i, j, count, operations):
            # Base case 1: If word2 is empty, we need to delete remaining characters in word1.
            if j == len(word2):
                return count + len(word1) - i, operations + ["Delete " + word1[i:]]

            # Base case 2: If word1 is empty, we need to insert remaining characters from word2.
            if i == len(word1):
                return count + len(word2) - j, operations + ["Insert " + word2[j:]]

            # Base case 3: If the characters match, just move to the next character.
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1, count, operations)

            # Apply the three operations: replace, delete, insert.
            replace_op, replace_ops = dfs(i + 1, j + 1, count + 1, operations + ["Replace " + word1[i] + " with " + word2[j]])
            delete_op, delete_ops = dfs(i + 1, j, count + 1, operations + ["Delete " + word1[i]])
            insert_op, insert_ops = dfs(i, j + 1, count + 1, operations + ["Insert " + word2[j]])

            # Return the minimum cost among these three operations.
            if replace_op <= delete_op and replace_op <= insert_op:
                return replace_op, replace_ops
            elif delete_op <= insert_op:
                return delete_op, delete_ops
            else:
                return insert_op, insert_ops

        min_cost, operations = dfs(0, 0, 0, [])
        return min_cost, operations
    


    
sol = Solution()
# print(sol.word_convert_2(word1 ="horse", word2="ros"))
# sol.word_convert_operations("hello", "herro")
# print(sol.word_convert_operations(word1 ="horse", word2="ros"))

min_cost, sequence = sol.word_convert_operations("horse", "ros")
print("Minimum cost:", min_cost)
print("Sequence of operations:")
for op in sequence:
    print(op)

'''
min_cost, min_operations = min(
    (replace_op, replace_ops),
    (delete_op, delete_ops),
    (insert_op, insert_ops),
    key=lambda x: x[0]  # Use the first element (cost) for comparison
)

return min_cost, min_operations

This code leverages the min function and a key function to compare the first element (cost) of each tuple to find the minimum cost and associated operations among the replace, delete, and insert operations. This simplifies the conditional statements and provides a more concise way to achieve the same result.
'''