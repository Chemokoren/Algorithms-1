"""
Check if an array has a majority element

Given an array, the task is to find if the input array contains a majority element of not

Examples: 

Input : arr[] = {2, 3, 9, 2, 2}
Output : Yes
A majority element 2 is present in arr[]

Input  : arr[] = {1, 8, 9, 2, 5}
Output : No

A simple solution is to traverse through the array. For every element, count its occurrences. 
If the count of occurrence of any element becomes n/2, we return true. 

An efficient solution is to use hashing. We count occurrences of all elements. 
If count becomes n/2 or more return true.
"""
# Returns true if there is a majority element  in a[]
def isMajority(a):
	
	# Insert all elements in a hash table
	mp = {}
	
	for i in a:
		if i in mp: mp[i] += 1
		else: mp[i] = 1
	
	# Check if frequency of any element is n/2 or more.
	for x in mp:
		if mp[x] >= len(a)//2:
			return True
	return False

print("Yes" if isMajority([ 2, 3, 9, 2, 2 ]) else "No")



'''

my tests

'''
def my_tests(arr):
    dic ={}
    for i in arr:
        dic[i] =dic.get(i,0)+1

    max_val =-float("inf")
    max_idx = None

    for k,v in dic.items():
        if v > max_val:
            max_val = v
            max_idx = k
    return "Yes" if max_val > 1 else "No"

print("Expected:Yes, Actual:", my_tests([2, 3, 9, 2, 2]))
print("Expected:No, Actual:", my_tests([1, 8, 9, 2, 5]))

