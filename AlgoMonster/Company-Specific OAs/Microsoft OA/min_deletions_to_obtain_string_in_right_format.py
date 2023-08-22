"""
(OA) - Min Deletions To Obtain String in Right Format



Given a string with only characters X and Y. Find the minimum number of characters to remove from 
the string such that there is no interleaving of character X and Y and all the Xs appear before 
any Y.

Example 1:
Input:YXXXYXY
Output: 2
Explanation:

We can obtain XXXYY by:

    Delete first Y -> XXXYXY
    Delete last occurrence pf X -> XXXYY

Example 2:
Input:YYXYXX
Output: 3
Explanation:

We can remove all occurrence of X or Y:
Example 3:
Input:XXYYYY
Output: 0
Explanation:

String matches the format required.

"""
def minStep(str) -> int:
    charX ='X'
    numY =0
    minDel =0

    for i in range(0, len(str)):
        if (charX == str[i]):
            minDel = min(numY, minDel + 1)
        else:
            numY = numY + 1
    return minDel

if __name__ == '__main__':
    string ="YXXXYXY"
    # print(minStep(input()))
    print(minStep(string))
    
