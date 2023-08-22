# bottom up solution
def fibonacci_numbers_two(n):
	sub_sol =[-1]*n
	
	if n == 0:
		return 0
	if n ==1:
		return 1
		
	sub_sol[0]=0
	sub_sol[1]=1
	
	for i in range(2, n):
		if sub_sol[i] !=-1:
			return sub_sol[i]
		res =fibonacci_numbers_two(n-1) + fibonacci_numbers_two(n-2)
		sub_sol[i] =res
	return sub_sol[-1]
print(fibonacci_numbers_two(6))