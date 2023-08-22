"""
Levenshtein Distance

- find the minimum number of edit operations that we can perform on one string 
to turn it into another string.
- the edit operations are:
    - insertion
    - deletion
    - substitution (replacement)

Expected output: 2 minimum operations to turn abc to yabd by:
- inserting y at the beginning (yabc)
- substituting c with d (yabd)
"""

# O(nm) time | O(nm) space where nm are the respective lengths of str1 and str2
def levenshteinDistance(str1, str2):
    edits =[[x for x in range(len(str1)+1)] for y in range(len(str2)+1)]
    for i in range(1, len(str2) + 1):
        edits[i][0] = edits[i-1][0] + 1
        

    for i in range(1, len(str2)+ 1):
        for j in range(1,len(str1)+1):
            if str2[i-1] == str1[j-1]:
                edits[i][j] = edits[i-1][j-1]
            else:
                edits[i][j] = 1 + min(edits[i-1][j-1],edits[i][j-1],edits[i-1][j])
    return edits[-1][-1]


# O(nm) time | O(min(n,m)) space
def levenshteinDistanceOpt(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2

    evenEdits =[x for x in range(len(small)+1)] # store the fewest no. of columns
    oddEdits =[None for x in range(len(small)+1)]

    for i in range(1, len(big)+1):
        if i % 2 == 1:
            currentEdits = oddEdits
            previousEdits = evenEdits
        else:
            currentEdits = evenEdits
            previousEdits = oddEdits
        currentEdits[0] = i # first value in our current edits

        for j in range(1, len(small)+ 1):
            if big[i-1] == small[j-1]:
                currentEdits[j] = previousEdits[j-1]
            else:
                currentEdits[j] = 1 + min(previousEdits[j-1], previousEdits[j], currentEdits[j-1])
        return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]

def levenshteinDistance1(str1,str2):
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2

    evenEdits =[x for x in range(len(small)+1)]
    oddEdits =[None for x in range(len(small)+1)]

    for i in range(1, len(big) +1):
        if i % 2 == 1:
            currentEdits = oddEdits
            previousEdits = evenEdits
        else:
            currentEdits =evenEdits
            previousEdits =oddEdits
        currentEdits[0] = i
        
        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j -1]:
                currentEdits[j] =previousEdits[j -1]
            else:
                currentEdits[j] =1 + min(previousEdits[j - 1], previousEdits[j], currentEdits[j -1 ])
    return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]

str1 ="abc"
str2 ="yabd"
print("levenshtein distance using 2d array: ",levenshteinDistanceOpt(str1,str2))
print("levenshtein distance Opt: ",levenshteinDistance1(str1,str2))