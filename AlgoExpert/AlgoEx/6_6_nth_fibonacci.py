"""
Nth Fibonacci 
"""

# Naive approach
def getNthFibRecur(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    else:
        return getNthFibRecur(n-1) + getNthFibRecur(n-2)

print("Fibonacci using Naive Approach:", getNthFibRecur(8))
    
# using memoization
def getNthFibMemoize(n,memoize={1:0,2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] =getNthFibMemoize(n-1,memoize) + getNthFibMemoize(n-2, memoize)
        return memoize[n]

print("Fibonacci using Memoization :", getNthFibMemoize(300))

# using Bottom up
def getNthFibBottomUp(n):
    lastTwo =[0,1]
    counter = 3

    while counter <= n:
        nextFib = lastTwo[0] +lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter +=1
    return lastTwo[1] if n>1 else lastTwo[0]
print("Fibonacci using Bottom up :", getNthFibBottomUp(300))

# using modified memoization
def getNthFibMemo(n):
	memo ={}
	if n in memo:
		return memo[n]
	if n == 1:
		return 0
	if n == 2:
		return 1
	if n >2:
		result= getNthFibMemo(n-1) +getNthFibMemo(n-2)
		memo[n] = result
		return result
		
print("using modified memoization:", getNthFibMemo(8))
	
# using modified Bottom-up approach
def getNthFibBottomUp(n):
	memo ={}
	memo[1] = 0
	memo[2] = 1
	for i in range(3,n+1):
		result= memo[i-1] + memo[i-2]
		memo[i] = result
	return memo[n]
		
print("using Modified Bottom up approach:", getNthFibBottomUp(300))