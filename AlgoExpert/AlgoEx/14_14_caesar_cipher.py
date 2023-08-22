"""
explanation

"""
# O(n) time | O(n) space
def caesarCipherEncyptor(string, key):
    newLetters =[]
    newKey = key % 26

    for letter in string:
        newLetters.append(getNewLetter(letter,newKey))
    return "".join(newLetters)

def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96+newLetterCode % 122)



def caesarCipherEncryptorCust(string,key):
    newLetters =[]
    newKey = key % 26
    alphabet =list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewLetterCust(letter, newKey,alphabet))
    return "".join(newLetters)

def getNewLetterCust(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key
    return alphabet[newLetterCode] if newLetterCode <=25 else alphabet[-1 + newLetterCode % 25]

# Test case 1
my_string="xyz"
my_key=2
print("Test case 1: ",caesarCipherEncyptor(my_string,my_key))


# Test case 2
my_string="xyz"
my_key=2
print("Test case 2: ",caesarCipherEncryptorCust(my_string,my_key))