"""
__author__ = "SRIRAM VETURI"
"""


# Substring by Character method
def substringByChar(initialString, startChar=None, endChar=None, stepSize=1):
    sub = str()

    if initialString is None:
        raise ValueError("No string specified.")

    if type(initialString) == int:
        initialString = str(initialString)

    if startChar is None:
        startChar = initialString[0]
    if endChar is None:
        endChar = initialString[-1]

    if type(initialString) == str:
        indDiff = initialString.index(endChar) - initialString.index(startChar)
        if indDiff % stepSize == 0:
            pass
        else:
            raise ValueError("Invalid entry of Step size/ Ending Character.")
    elif type(initialString) == int:
        initialString = str(initialString)
        startChar = str(startChar)
        endChar = str(endChar)
        if initialString.index(endChar) % stepSize == 0:
            pass
        else:
            raise ValueError("Invalid entry of Step size/ Ending Character.")
    else:
        raise ValueError("String/Integer expected. Unknown type passed.")

    if startChar not in initialString:
        raise ValueError("Invalid entry of starting character.")
    elif endChar not in initialString:
        raise ValueError("Invalid entry of ending character.")

    endCharInd = initialString.index(endChar)
    startCharInd = initialString.index(startChar)
    flag = False
    for x in range(startCharInd, len(initialString), stepSize):

        if initialString[x] != startChar and flag is False:
            continue
        else:
            flag = True
            if initialString[x] == endChar:
                sub = sub + initialString[x]
                break
            else:
                sub = sub + initialString[x]

    return sub


# Substring by Index method
def substringByInd(initialString, startInd=None, endInd=None, stepSize=1):

    if initialString is None:
        raise ValueError("No string specified.")

    if type(initialString) == int:
        initialString = str(initialString)

    if type(initialString) == str:
        pass
    elif type(initialString) == int:
        initialString = str(initialString)
        pass
    else:
        raise ValueError("String/Integer expected. Unknown type passed.")

    if startInd is None:
        startInd = 0
    if endInd is None:
        endInd = len(initialString)-1

    if endInd < startInd:
        raise ValueError("Ending index should be greater than starting index.")
    elif endInd > len(initialString) - 1 or startInd > len(initialString) - 1:
        raise ValueError("Invalid entry of start/end index.")

    if (endInd-startInd) % stepSize == 0:
        pass
    else:
        raise ValueError("Invalid entry of Step size/ Ending Character.")

    sub = str()

    flag = False
    for x in range(startInd, len(initialString), stepSize):

        if x != startInd and flag is False:
            continue
        else:
            flag = True
            if x == endInd:
                sub = sub + initialString[x]
                break
            else:
                sub = sub + initialString[x]

    return sub
