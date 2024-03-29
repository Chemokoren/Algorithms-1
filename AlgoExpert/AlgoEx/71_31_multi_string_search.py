'''
 Suffix Trie  implementation
'''
class ModifiedSuffixTrie:
    def __init__(self,string) -> None:
        self.root ={}
        self.populateModifiedSuffixTrieFrom(string)

    def populateModifiedSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    def insertSubstringStartingAt(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] ={}
            node = node[letter]

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return True

class Trie:
    def __init__(self) -> None:
        self.root ={}
        self.endSymbol ="*"

    def insert(self, string):
        current = self.root
        for i in range(len(string)):
            if string[i] not in current:
                current[string[i]] ={}
            current = current[string[i]]
        current[self.endSymbol] = string



'''
Naive approach
'''
# O(bns) time | O(n) space (b - length of big string, n -no of small strings, s is the length of the largest small string)
def multiStringSearch(bigString, smallStrings):
    return [isInBigString(bigString, smallString) for smallString in smallStrings]

def isInBigString(bigString, smallString):
    for i in range(len(bigString)):
        if i + len(smallString) > len(bigString):
            break
        if isInBigStringHelper(bigString, smallString, i):
            return True
    return False

def isInBigStringHelper(bigString, smallString, startIdx):
    leftBigIdx = startIdx
    rightBigIdx = startIdx + len(smallString) -1
    leftSmallIdx = 0
    rightSmallIdx = len(smallString) -1

    while leftBigIdx <= rightBigIdx:
        if(
            bigString[leftBigIdx] != smallString[leftSmallIdx] or
            bigString[rightBigIdx] != smallString[rightSmallIdx]):
            return False

        leftBigIdx += 1
        rightBigIdx -=1
        leftSmallIdx += 1
        rightSmallIdx -=1
    return True


'''
Approach 2
'''
# O(n^2 + ns) time | O(b^2 + n) space (b^2 comes comes from creating the suffixTrie)
def multiStringSearch(bigString, smallStrings):
    modifiedSuffixTrie = ModifiedSuffixTrie(bigString)
    # ns -(iterating through n small strings and contains method running in at most s time)
    return [modifiedSuffixTrie.contains(string) for string in smallStrings]
'''
approach 3
'''
# O(ns + bs) time | O(ns) space
def multiStringSearchTwo(bigString, smallStrings):
    trie = Trie()
    for string in smallStrings:
        trie.insert(string)
    containedStrings = {}
    for i in range(len(bigString)):
        findSmallStringsIn(bigString,i, trie, containedStrings)
    return [string in containedStrings for string in smallStrings]

def findSmallStringsIn(string, startIdx, trie, containedStrings):
    currentNode = trie.root
    for i in range(startIdx, len(string)):
        currentChar =string[i]
        if currentChar not in currentNode:
            break
        currentNode = currentNode[currentChar]

        if trie.endSymbol in currentNode:
            containedStrings[currentNode[trie.endSymbol]] = True


'''
test
'''
my_big_string="this is a big string"
my_small_string=['this', 'yo','is','a','bigger','string','kappa']

print("naive approach: ", multiStringSearch(my_big_string,my_small_string))

print("approach 2:", multiStringSearch(my_big_string,my_small_string))
print("approach 3:", multiStringSearchTwo(my_big_string,my_small_string))

