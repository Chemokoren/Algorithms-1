def fibonacci_numbers(n):
	if n == 0:
		return 0
	if n ==1:
		return 1
		
	return fibonacci_numbers(n-1) + fibonacci_numbers(n-2)
    
print(fibonacci_numbers(6))