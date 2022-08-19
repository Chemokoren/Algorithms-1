"""
Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of
the two sorted arrays.

Follow up: The overall run time complexity should be O(log(m+n))

Example 1:

input: nums1 =[1,3], nums2 =[2]
OUtput: 2.00000
Explanation: merged array =[1,2,3] and median is 2.

Example 2:

input: nums1 =[1,2], nums2=[3,4]
Output: 2.50000
Explanation: merged array =[1,2,3,4] and median is (2+3) / 2 =2.5.

"""
class Solution:
    def findMedianSortedArrays(self, nums1,nums2)->float:
        A,B =nums1, nums2
        total =len(nums1)+len(nums2)
        half =total//2

        if len(B) < len(A):
            A, B =B, A

        # log(min(n,m))
        l, r = 0, len(A) -1
        while True:
            i = (l + r) // 2 # A
            j = half-i-2 # B

            Aleft  = A[i] if i >=0 else float("-infinity")
            Aright = A[i + 1] if (i+1) < len(A) else float("infinity")
            Bleft  = B[j] if j >=0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <=Bright and Bleft <=Aright:
                # odd 
                if total % 2:
                    return min(Aright,Bright)

                # even 
                return (max(Aleft, Bleft)+min(Aright, Bright))/ 2
            elif Aleft >Bright:
                r = i -1
            else:
                l = i + 1

sol =Solution()
print("Expected:2, Actual:", sol.findMedianSortedArrays([1,3], [2]))
print("Expected:2.5, Actual:", sol.findMedianSortedArrays([1,2], [3,4]))

'''

my tests

'''

def my_tests(arr1,arr2):
	arr = merge_sort(arr1,arr2)
	
	# odd
	n=len(arr)
	if(n % 2 !=0):
		return arr[n//2]
	else:
		return (arr[n//2] +arr[(n//2)-1])/2
		
	
def merge_sort(arr1,arr2):
	
	arr =[0] *(len(arr1) + len(arr2))
	i =0
	j =0
	k =0
	
	while(i < len(arr1) and j<len(arr2)):
		if arr1[i] < arr2[j]:
			arr[k] =arr1[i]
			i  += 1
		else:
			arr[k] =arr2[j]
			j +=1
		k +=1
		
	while (i < len(arr1)):
		arr[k] = arr1[i]
		i +=1
		k +=1
		
	while (j < len(arr2)):
		arr[k] = arr2[j]
		j +=1
		k +=1
		
	return arr
	


print("Expected 2: Actual", my_tests([1,3],[2]))
print("Expected 2.5: Actual", my_tests([1,2],[3,4]))

"""
my tests using heapq

"""
import heapq
def my_tests(arr1,arr2):
	max_heap=[]
	min_heap=[]
	
	arr1.extend(arr2)
	
	for i in arr1:
		heapq.heappush(max_heap,(-1 * i))
		if(len(max_heap)>len(min_heap)+1):
			val= -1 *(heapq.heappop(max_heap))
			heapq.heappush(min_heap,val)
		if(len(min_heap)>len(max_heap)+1):
			val= (heapq.heappop(min_heap))
			heapq.heappush(max_heap,(-1 * val))
	
	if(len(max_heap)>len(min_heap)):
			median_val= -1 *(heapq.heappop(max_heap))
	elif(len(min_heap)>len(max_heap)):
			median_val= (heapq.heappop(min_heap))
	elif len(min_heap) == len(max_heap):
		small_val= -1 *(heapq.heappop(max_heap))
		large_val= (heapq.heappop(min_heap))
		median_val =(small_val + large_val)/2
			
	return median_val
	


print("Expected 2: Actual", my_tests([1,3],[2]))
print("Expected 2.5: Actual", my_tests([1,2],[3,4]))