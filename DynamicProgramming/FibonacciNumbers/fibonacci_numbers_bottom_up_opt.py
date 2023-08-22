# bottom up optimized solution
def fibonacci_numbers_opt(n):
	
	if n == 0:
		return 0
	if n ==1:
		return 1
		
	prev=0
	curr=1
	
	for i in range(2, n):
		res =fibonacci_numbers_opt(n-1) + fibonacci_numbers_opt(n-2)
		prev =curr
		curr = res
	return curr
print("aaa::",fibonacci_numbers_opt(3))