# O(n^2) time | O(n) space
def ThreeNumberSum(array, targetSum):
    array.sort()
    triplets =[]
    
    for i in range(len(array)-2):
        left  = i+1
        right = len(array)-1
        
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets
        
        
print(ThreeNumberSum([12,3,1,2,-6,5,-8,6], 0))

def three_number_sum_second(arr, target):
	arr.sort()
	res =[]
	
	third_val= 0
	while third_val < len(arr)-2:
		start = third_val +1
		end =len(arr)-1
		while start < end:
			sum_val =arr[third_val]+arr[start] + arr[end]
			if sum_val == target:
				res.append([arr[third_val], arr[start], arr[end]])
				end -= 1
				start +=1
			elif sum_val > target:
				end -=1
			elif sum_val < target:
				start +=1
		third_val +=1
	return res
		
print(three_number_sum_second([12,3,1,2,-6,5,-8,6], 0))
