"""
__author__ = "SRIRAM VETURI"
"""

# Testcases for "substring" module
import substring

# Testcase 1
testOne = substring.substringByInd(initialString="abcdefghijkl")
print("Testcase 1 result :")
print(testOne)
print("\n")

# Testcase 2
testTwo = substring.substringByInd(initialString="abcdefghijkl",
                                   startInd=1,
                                   endInd=10)
print("Testcase 2 result :")
print(testTwo)
print("\n")

# Testcase 3
testThree = substring.substringByInd(initialString="abcdefghijkl",
                                     startInd=1,
                                     endInd=11,
                                     stepSize=2)
print("Testcase 3 result :")
print(testThree)
print("\n")

# Testcase 4
testFour = substring.substringByInd(initialString=1234567890,
                                    startInd=1,
                                    endInd=7,
                                    stepSize=2)
print("Testcase 4 result :")
print(testFour)
print("\n")

# Testcase 5
testFive = substring.substringByChar(initialString="abcdefghijkl",
                                     startChar='b',
                                     endChar='k')
print("Testxase 5 result :")
print(testFive)
print("\n")

# Testcase 6
testSix = substring.substringByChar(initialString="abcdefghijkl",
                                    startChar='b',
                                    endChar='l',
                                    stepSize=2)
print("Testcase 6 result :")
print(testSix)
print("\n")

# Testcase 7
startChar = None
endChar = None
testSeven = substring.substringByChar(initialString="abcdefghijkl")
print("Testcase 7 result :")
print(testSeven)
print("\n")

# Testcase 8
testEight = substring.substringByChar(initialString=12345678)
print("Testcase 8 result :")
print(testEight)
print("\n")
