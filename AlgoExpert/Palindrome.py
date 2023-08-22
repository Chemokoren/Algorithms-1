# O(n^2) time | O(n) space
def  isPalindrome(string):
    reversedString =""
    for i in reversed(range(len(string))):
        reversedString += string[i]
        return string == reversedString

# O(n) time | O(n) space
def isPalindrome1(string):
    reversedChars =[]
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])
    return string == "".join(reversedChars)

# O(n) time | O(n) space
def isPalindrome2(string, i =0):
    j =len(string) -1-i
    return True if i >= j else string[i] == string[j] and isPalindrome2(string, i+1)

# Tail Recursive function
def isPalindrome4(string, i=0):
    j = len(string) -1 -i
    if i >=j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindrome4(string, i+1)

# O(n) time | (1) space
def isPalindrome3(string):
    leftIdx =0
    rightIdx =len(string) -1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx +=1
        rightIdx -=1
    return True



my_string ="abcdcba"
print(isPalindrome4(my_string))
