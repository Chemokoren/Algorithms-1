# O(n) time | O(d) space
def productSum(array, multiplier = 1):
	sum =0
	for element in array:
		if type(element) is list:
			sum +=productSum(element,multiplier +1)
		else:
			sum +=element
	return sum * multiplier


my_array =[5, 2, [7, -1], 3, [6,[-13,8], 4]]
print(productSum(my_array))
