def stairs(n)->int:
	if n == 1:
		return 1
	if n == 2:
		return 2
		
	return stairs(n-1) + stairs(n-2)

print(stairs(3))