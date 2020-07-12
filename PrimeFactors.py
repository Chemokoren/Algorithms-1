def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n
    return i

def get_divisors(n):
    list_data=[]
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            list_data.append(i)
            # yield (i)
    # yield n
    return list_data


print(get_divisors(9))





def gcd(a, b):
	if(b == 0):
		return a
	else:
		return gcd(b, a % b)

def isDivisible(x,y):

	if (y == 1):
		return 1

	z = gcd(x, y);

	if (z == 1):
		return false;

	return isDivisible(x, y / z);

# Driver Code
x = 18
y = 12
if (isDivisible(x, y)):
	print("Yes")
else:
	print("No")

# This code is contributed by Sam007


def solution(A, B):
    for i in range(len(A)):
