"""
Palindrome Partitioning Min Cuts
"""

# O(n^3) time | O(n^2) space
def palindromePartitioningMinCuts(string):
    palindromes =[[False for i in string] for j in string]
    for i in range(len(string)):
        for j in range(i, len(string)):
            palindromes[i][j] = isPalindrome(string[i:j+1])
    cuts =[float("inf") for i in string]
    for i in range(len(string)):
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = cuts[i-1] + 1
            for j in range(1, i):
                if palindromes[j][i] and cuts[j-1]+1 < cuts[i]:
                    cuts[i] = cuts[j-1] + 1
    return cuts[-1]

def isPalindrome(string):
    startIdx =0
    endIdx = len(string) -1

    while startIdx < endIdx:
        if string[startIdx] != string[endIdx]:
            return False
        startIdx += 1
        endIdx -= 1
    return True


# approach 2
# O(n^2) time | O(n^2) space
def palindromePartitioningMinCutsTwo(string):
    palindromes =[[False for i in string] for j in string]
    for i in range(len(string)):
        palindromes[i][i] = True
    
    for length in range(2, len(string) + 1):
        for i in range(0, len(string)-length + 1):
            j = i + length - 1
            if length == 2:
                palindromes[i][j] = string[i] == string[j]
            else:
                palindromes[i][j] = string[i] == string[j] and palindromes[i + 1][j-1]
    
    cuts =[float("inf") for i in string]
    for i in range(len(string)):
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = cuts[i- 1] + 1
            for j in range(1, i):
                if palindromes[j][i] and cuts[j-1] + 1 < cuts[i]:
                    cuts[i] = cuts[j-1] + 1
    return cuts[-1]

my_string ="noonabbad"

print(palindromePartitioningMinCuts(my_string))