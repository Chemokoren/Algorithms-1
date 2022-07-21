"""
Longest Span with same Sum in two Binary arrays

Given two binary arrays, arr1[] and arr2[] of the same size n. Find the length of the 
longest common span(i, j) where j>=i such that arr1[i]+arr1[i+1]+ ... +arr1[j] = 
arr2[i] + arr2[i+1] + ... +arr2[j]

The time complexity expected is O(n)


Input: arr1[] = {0, 1, 0, 0, 0, 0};
       arr2[] = {1, 0, 1, 0, 0, 1};
Output: 4
The longest span with same sum is from index 1 to 4.

Input: arr1[] = {0, 1, 0, 1, 1, 1, 1};
       arr2[] = {1, 1, 1, 1, 1, 0, 1};
Output: 6
The longest span with same sum is from index 1 to 6.

Input: arr1[] = {0, 0, 0};
       arr2[] = {1, 1, 1};
Output: 0

Input: arr1[] = {0, 0, 1, 0};
       arr2[] = {1, 1, 1, 1};
Output: 1 

Method 1: Simple Solution
-------------------------
One by one consider same subarrays of both arrays. For all subarrays, compute sums and if
sums are same and current length is more than max length, then update max length. 

Time Complexity : O(n2) 
Auxiliary Space : O(1)
  

"""
# function to return length of the longest common subarray with same sum
def longestCommonSum(arr1, arr2):
    
    n = len(arr1)

    # Initialize result
    maxLen = 0

    # One by one pick all possible starting points of subarrays
    for i in range(0, n):

        # Initialize sums of current subarrays
        sum1 = 0
        sum2 = 0

        # Consider all points for starting with arr[i]
        for j in range(i,n):

            # update sums
            sum1 += arr1[j]
            sum2 += arr2[j]

            # if sums are same and current length is more than maxLen, update maxLen
            if(sum1 == sum2):
                len_val = j-i+1
                if( len_val > maxLen):
                    maxLen = len_val

    return maxLen



print("Expected: 6, Actual ",longestCommonSum([0, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1]))

"""
Method 2 (Using Auxiliary Array) 

The idea is based on the below observations. 

    Since there are total n elements, maximum sum is n for both arrays.
    The difference between two sums varies from -n to n. So there are total 2n + 1 
    possible values of difference.
    If differences between prefix sums of two arrays become same at two points, then 
    subarrays between these two points have same sum.

Below is the Complete Algorithm.  

1. Create an auxiliary array of size 2n+1 to store starting points of all possible values 
of differences (Note that possible values of differences vary from -n to n, i.e., there 
are total 2n+1 possible values)
2. Initialize starting points of all differences as -1.
3. Initialize maxLen as 0 and prefix sums of both arrays as 0, preSum1 = 0, preSum2 = 0

4. Traverse both arrays from i = 0 to n-1. 

    i) Update prefix sums: preSum1 += arr1[i], preSum2 += arr2[i]
    ii) Compute difference of current prefix sums: curr_diff = preSum1 – preSum2
    iii) Find index in diff array: diffIndex = n + curr_diff // curr_diff can be negative 
    and can go till -n
    iv) If curr_diff is 0, then i+1 is maxLen so far
    v) Else If curr_diff is seen first time, i.e., starting point of current diff is -1, 
    then update starting point as i
    vi) Else (curr_diff is NOT seen first time), then consider i as ending point and find
    length of current same sum span. If this length is more, then update maxLen

5. Return maxLen


Time Complexity: O(n) 
Auxiliary Space: O(n)

"""

# Python program to find longest common
# subarray of two binary arrays with
# same sum

def longestCommonSum(arr1, arr2, n):

	# Initialize result
	maxLen = 0
	
	# Initialize prefix sums of two arrays
	presum1 = presum2 = 0
	
	# Create a dictionary to store indices
	# of all possible sums
	diff = {}
	
	# Traverse both arrays
	for i in range(n):
	
		# Update prefix sums
		presum1 += arr1[i]
		presum2 += arr2[i]
		
		# Compute current diff which will be
		# used as index in diff dictionary
		curr_diff = presum1 - presum2
		
		# If current diff is 0, then there
		# are same number of 1's so far in
		# both arrays, i.e., (i+1) is
		# maximum length.
		if curr_diff == 0:
			maxLen = i+1
		elif curr_diff not in diff:
			# save the index for this diff
			diff[curr_diff] = i
		else:				
			# calculate the span length
			length = i - diff[curr_diff]
			maxLen = max(maxLen, length)
		
	return maxLen

# Driver program
arr1 = [0, 1, 0, 1, 1, 1, 1]
arr2 = [1, 1, 1, 1, 1, 0, 1]
print("Length of the longest common",
	" span with same", end = " ")
print("sum is",longestCommonSum(arr1,
				arr2, len(arr1)))


"""
Method 3 (Using Hashing)

    Find difference array arr[] such that arr[i] = arr1[i] – arr2[i].
    Largest subarray with equal number of 0s and 1s in the difference array.

Time Complexity: O(n)  (As the array is traversed only once.)
Auxiliary Space: O(n) (As hashmap has been used which takes extra space.)

"""

# Function returns largest common subarray with equal
# number of 0s and 1s
def longestCommonSum(arr1, arr2):
    
    n = len(arr1)
    # Find difference between the two
    
    arr = [0 for i in range(n)]
    
    for i in range(n):
        arr[i] = arr1[i] - arr2[i]
        
    # Creates an empty hashMap hM 
    hm = {}
    sum = 0	 # Initialize sum of elements 
    max_len = 0	 #Initialize result 
    
    # Traverse through the given array 
    
    for i in range(n):
        
        # Add current element to sum 
        sum += arr[i]
        
        # To handle sum=0 at last index
        
        if (sum == 0):
            max_len = i + 1
            
        # If this sum is seen before then update max_len if required
        
        if sum in hm:
            max_len = max(max_len, i - hm[sum])
        else: # Else put this sum in hash table
            hm[sum] = i
            
    return max_len

print(longestCommonSum([0, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1]))


