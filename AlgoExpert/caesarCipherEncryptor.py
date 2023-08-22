# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    newLetters =[]
    newKey = key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey))
    return "".join(newLetters)

def getNewLetter(letter,key):
    newLetterCode =ord(letter)+key
    return chr(newLetterCode) if newLetterCode <=122 else chr(96+newLetterCode % 122)

# O(n) time | O(n) space
def caesarCipherEncryptor1(string, key):
    newLetters =[]
    newKey = key % 26
    alphabet =list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewLetter1(letter, newKey,alphabet))
    return "".join(newLetters)

def getNewLetter1(letter,key,alphabet):
    newLetterCode = alphabet.index(letter) + key
    return alphabet[newLetterCode] if newLetterCode <=25 else alphabet[-1+newLetterCode % 25]


my_array =['x','y','z']
key =54

print(caesarCipherEncryptor1(my_array,key))
print(ord("z"))
print(chr(97))