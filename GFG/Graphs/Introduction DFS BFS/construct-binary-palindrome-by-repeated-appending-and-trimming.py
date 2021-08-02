"""
construct binary palindrome by repeated appending and trimming

Given n and k, construct a palindrome of size n using a binary number of size k 
repeating itself to wrap into the palindrome. The palindrome must always begin with 1 
and contains maximum number of zeros.

Examples:

Input : n = 5,  k = 3
Output : 11011 
Explanation : the 3 sized substring is
110 combined twice and trimming the extra 
0 in the end to give 11011.

Input : n = 2,  k = 8
Output : 11 
Explanation : the 8 sized substring is 11...... 
wrapped to two places to give 11.

The naive approach would be to try every palindrome of size k starting with 1 such that
a palindrome of size n is formed. This approach has an exponential complexity.

A better way to do this is to initialize the k sized binary number with the index
and connect the palindrome in the way it should be. Like last character of palindrome
should match to first, find which indexes will be present at those locations and link 
them. Set every character linked with  0th index to 1 and the string is ready.
This approach will have a linear complexity.
In this approach, first lay  the index of the k sized binary to hold into an array,
example if n =7, k =3 arr becomes [0,1,2,0,1,2,0]. Following that in the connectchars 
graph, connect the indices of the k sized binary which should be same by going through
the property of palindrome which is kth and(n-k-1)th variable should be same, such that
0 is linked to 1(and vice versa), 1 is linked to 2(and vice versa) and so on. 
After that, check what is linked with 0 in connectchars array and make all of the 
associated indices one(because the first numbers should be non-zero) by using dfs 
approach. In the dfs, pass 0, the final answer string and the graph. Begin by making 
the parent 1 and checking if its children are zero, if they make them and 
their children 1. This makes only the required indices of the k sized string one, 
others are left zero. Finally the answer contains the 0 to k-1 indexes and 
corresponding to arr the digits are printed.

Time Complexity : O(n)

"""
# code to form binary palindrome

# function to apply DFS
def dfs(parent, ans, connectchars):

    # set the parent marked
    ans[parent] = 1

    # if the node has not been visited set it and its children marked
    for i in range(len(connectchars[parent])):
        if(not ans[connectchars[parent][i]]):
            dfs(connectchars[parent][i], ans, connectchars)

    
def printBinaryPalindrome(n, k):
    arr=[0] * n
    ans =[0] * n

    # link which digits must be equal
    connectchars =[[] for i in range(k)]

    for i in range(n):
        arr[i] = i % k

    # connect the two indices
    for i in range(int(n/2)):
        connectchars[arr[i]].append(arr[n-i-1])
        connectchars[arr[n-i-1]].append(arr[i])

    # set everything connected to first character as 1
    dfs(0, ans, connectchars)

    for i in range(n):
        print(ans[arr[i]], end="")

if __name__ == '__main__':
 
    n = 10
    k = 4
    printBinaryPalindrome(n, k)