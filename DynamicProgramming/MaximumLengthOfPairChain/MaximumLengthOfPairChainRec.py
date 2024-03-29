"""
you are given n pairs of numbers. In every pair, the first number is always smaller than 
the second number.
Now, we define a pair(c, d) can follow another pair(a,b) if and only if b< c.
Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up 
all the given pairs. You can select pairs in any order.

input: [[1,2],[2,3],[3,4]]


Time complexity:
O(n^2)

optimum solution  has a time complexity of O(nlogn)
"""

def MaximumLengthOfPairChain(pairs): # pairs -two dimensional array
	n = len(pairs)
	dp ={}
	dp[0] = 1
	
    # try to break the double for loop using binary search to get (nlogn)
	for i in range(1,n):
		dp[i] = dp[i-1]
		for j in range(i-1,0,-1):
			if(pairs[j][1] < pairs[i][0]):
				dp[i] = max(dp[i], dp[j]+1)
	print("aa::", dp)
	return dp[len(pairs)-1]
	
	
c1 =[1,2]
c2 =[2,3]
c3 = [3,4]
pairs=[c1,c2,c3]
print(MaximumLengthOfPairChain(pairs))

# answer is 2
def test_vals(arr):
	if len(arr) ==0 or len(arr) ==1:
		return arr
	
	res =[]
	for i in  range(0,len(arr)-1):
		for j in range(i+1,len(arr)):
			if arr[i][1] < arr[j][0]:
				res.append((arr[i],arr[j]))
	return res
			


print(test_vals([[1,2],[2,3], [3,4]]))