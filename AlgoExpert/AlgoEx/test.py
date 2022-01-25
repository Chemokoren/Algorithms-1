def lps(S):
	n = len(S)

	L = [[0 for x in range(n)]for y in range(n)]

	for i in range(n):
		L[i][i] = 1

	for cl in range( 2, n+1):
		for i in range(n - cl + 1):
			j = i + cl - 1
			if (str[i] == str[j] and cl == 2):
				L[i][j] = 2
			elif (str[i] == str[j]):
				L[i][j] = L[i + 1][j - 1] + 2
			else:
				L[i][j] = max(L[i][j - 1],L[i + 1][j])

	return L[0][n - 1]

# calculate minimum number of deletions
def solution(S):

	n = len(S)

	l = lps(S)
	return (n - l)

# print("actual problem: ",solution('ervervige'))




# def minDeletions(X, i, j):
 
#     # base condition
#     if i >= j:
#         return 0
 

#     if X[i] == X[j]:
#         return minDeletions(X, i + 1, j - 1)
 
 
#     return 1 + min(minDeletions(X, i, j - 1), minDeletions(X, i + 1, j))
 
 
# if __name__ == '__main__':
 
#     X = 'ACBCDBAA'
#     n = len(X)
 
#     print('The minimum number of deletions required is', minDeletions(X, 0, n - 1))

def minDeletions(X, i, j):
 
    # base condition
    if i >= j:
        return 0
 

    if X[i] == X[j]:
        return minDeletions(X, i + 1, j - 1)
 
 
    return 1 + min(minDeletions(X, i, j - 1), minDeletions(X, i + 1, j))

def solution(S):
    n = len(S)
    return minDeletions(S, 0, (n-1))

print(solution('aaabab'))

def minDeletions(X):
 
    n = len(X)
 
    # string 'Y' is a reverse of 'X'
    Y = X[::-1]
 
    # `lookup[i][j]` stores the length of LCS of substring `X[0…i-1]` and `Y[0…j-1]`
    lookup = [[0 for x in range(n + 1)] for y in range((n + 1))]
 
    # fill the lookup table in a bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # if current character of 'X' and 'Y' matches
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
 
            # otherwise, if the current character of 'X' and 'Y' don't match
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])
 
    # Now, `lookup[n][n]` contains the size of the longest palindromic subsequence.
 
    # The minimum number of deletions required will be the difference in the size
    # of the string and the size of the palindromic subsequence
 
    return n - lookup[n][n]
 
 
if __name__ == '__main__':
 
    X = 'aaabab'
    print('The minimum number of deletions required is', minDeletions(X))

"""

 program to find minimum number of deletions to make a string palindromic

"""


# Returns the length of the longest palindromic subsequence in 'str'
def lps(str):
	n = len(str)

	# Create a table to store results of subproblems
	L = [[0 for x in range(n)]for y in range(n)]

	# Strings of length 1 are palindrome of length 1
	for i in range(n):
		L[i][i] = 1

	# Build the table. Note that the lower diagonal values of table are useless and
	# not filled in the process. c1 is length of substring
	for cl in range( 2, n+1):
		for i in range(n - cl + 1):
			j = i + cl - 1
			if (str[i] == str[j] and cl == 2):
				L[i][j] = 2
			elif (str[i] == str[j]):
				L[i][j] = L[i + 1][j - 1] + 2
			else:
				L[i][j] = max(L[i][j - 1],L[i + 1][j])

	# length of longest palindromic subseq
	return L[0][n - 1]

def minimumNumberOfDeletions( str):

	n = len(str)

	# Find longest palindromic
	# subsequence
	l = lps(str)

	# After removing characters
	# other than the lps, we
	# get palindrome.
	return (n - l)

# Driver Code
if __name__ == "__main__":
	
	str = "aaabab"
	str= "ervervige"
	print("Minimum number of deletions = ", minimumNumberOfDeletions(str))


"""

"""
class find_Biggest_Num_N_In_Array_Occures_N_times:
	def Solution(self, ar):
		counter= [0]* len(ar)
		for i in range(len(ar)):
			pos=ar[i]
			counter[pos] +=1

		for j in range(len(ar)-1, 0, -1):
			if(counter[j]==j):
				return j
		return -1

cls = find_Biggest_Num_N_In_Array_Occures_N_times()
ar =[1,2,2,3,4,4,4,4,3,5,5,5,5,5,1]
print("kkkk: ",cls.Solution(ar))


"""
minimum-insertion-steps-to-make-a-string-palindrome

"""
