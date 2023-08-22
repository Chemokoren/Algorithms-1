"""
group anagrams

- the question gives you a list of words, or arbitrary strings and wants you to write
a function that returns a list of other lists where  each of these other lists  are 
groups of anagrams.

anagrams -words formed by the same letters but might just be arranged differently

"""

# O(w * n * log(n) + n * w * log(w)) time | O(wn) space where w is the no. of words and n is the longest word
def groupAnagrams(words):
    if len(words) == 0:
        return []
    
    sortedWords =["".join(sorted(w)) for w in words]
    indices =[i for i in range(len(words))]
    indices.sort(key=lambda x:sortedWords[x])

    result = []
    currentAnagramGroup =[]
    currentAnagram = sortedWords[indices[0]]
    for index in indices:
        word = words[index]
        sortedWord = sortedWords[index]

        if sortedWord == currentAnagram:
            currentAnagramGroup.append(word)
            continue

        result.append(currentAnagramGroup)
        currentAnagramGroup =[word]
        currentAnagram = sortedWord

    result.append(currentAnagramGroup)
    return result


# Approach 2
# O(w * n * log(n)) time | O(wn) space
def groupAnagramsTwo(words):
    anagrams ={}
    for word in words:
        sortedWord ="".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] =[word]
    return list(anagrams.values())

my_list =["yo", "act", "flop", "tac", "cat", "oy", "olfp"]

print(groupAnagramsTwo(my_list))