
# O(n^2) time | O (n) space
def isPalindrome(string):
    my_string =""
    for i in reversed((string)):
        my_string += i

    return my_string == string


def isPalindromeArray(string):
    my_array =[]
    for i in reversed(string):
        my_array.append(i)
    return string =="".join(my_array)

# O(n) time | O(1) space
def isPalindromeUsingPointers(string):
    leftIdx = 0
    rightIdx = len(string)-1

    while leftIdx <= rightIdx :
        if(string[leftIdx] != string[rightIdx]):
            return False
        leftIdx +=1
        rightIdx -=1
    return True
# O(n) time | O(n) space
def isPalindromeRecursion(string, i =0):
    j =len(string)-1-i
    return True if i >= j else string[i] == string[j] and isPalindromeRecursion(string, i+1)

# tail recursion
# O(n) time | O(1) space
def isPalindromeTailRecursion(string, i =0):
    j = len(string) -1-i
    if i>=j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindromeTailRecursion(string, i+1)

print(isPalindromeTailRecursion("abcdcba", 0))