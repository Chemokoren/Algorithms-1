# naive approach
# solution 1
# O(bns) time  | O(n) space
def multistringSearch(bigString, smallString):
    return [isInBigString(bigString, smallString) for smallString in smallString]

def isInBigString(bigString, smallString):
    for i in range(len(bigString)):
        if i + len(smallString) > len(bigString):
            break
        if isInBigStringHelper(bigString, smallString, i):
            return True
    return False

def isInBigStringHelper(bigString, smallString, startidx):
    leftBigIdx =startidx
    rightBigIdx = startidx + len(smallString) -1
    leftSmallIdx =0
    rightSmallIdx = len(smallString) -1
    while leftBigIdx <= rightBigIdx:
        if(
            bigString[leftBigIdx]  != smallString[leftSmallIdx] or
            bigString[rightBigIdx] != smallString[rightSmallIdx]
        ):
            return False
        leftBigIdx +=1
        rightBigIdx -=1
        leftSmallIdx +=1
        rightSmallIdx -=1

    return True

# solution 2
# O(b ^ 2 + ns) time | O(b ^ 2 + n ) space
# b ^ 2 - creating suffix tree
# ns - iterating through the small strings of which they are n and calling
# the contains method which runs in at most s time
def multiStringSearch(bigString, smallStrings):
    modifiedSuffixTrie =ModifiedSuffixTrie(bigString)
    return [modifiedSuffixTrie.contains(string) for string in smallStrings]


# needed for solution 2
class ModifiedSuffixTrie:
    def __init__(self, string):
        self.root ={}
        self.populateModifiedSuffixTrieFrom(string)

    def pupulateModifiedSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubStringStartingAt(i, string)

    def insertSubStringStartingAt(self, i, string):
        node =self.root
        for j in range(i, len(string)):
            letter =string[j]
            if letter not in node:
                node[letter] ={}
            node = node[letter]

    def contains(self, string):
        node =self.root
        for letter in string:
            if letter not in node:
                return False
            node =node[letter]
        return True

# solution 3
# O(ns + bs) time | O(ns) space
# where space comes from building the tree with n strings with length at most s
# in time bs because we are iterating throug every character in the bigString
#  and doing at most s traversals in the tree
def multiStringSearch3(bigString, smallStrings):
    trie =Trie()
    for string in smallStrings:
        trie.insert(string)
    containedStrings ={}
    for i in range(len(bigString)):
        findSmallStringsIn(bigString, i, trie, containedStrings)
    return [string in containedStrings for string in smallStrings]

def findSmallStringsIn(string, startIdx, trie, containedStrings):
    currentNode =trie.root
    for i in range(startIdx, len(string)):
        currentChar =string[i]
        if currentChar not in currentNode:
            break
        currentNode =currentNode[currentChar]
        if trie.endSymbol in currentNode:
            containedStrings[currentNode[trie.endSymbol]] = True

# needed for solution 3
class Trie:
    def __init__(self):
        self.root ={}
        self.endSymbol ="*"

    def insert(self, string):
        current =self.root
        for i in range(len(string)):
            if string[i] not in current:
                current[string[i]] ={}
            current =current[string[i]]
        current[self.endSymbol] =string

