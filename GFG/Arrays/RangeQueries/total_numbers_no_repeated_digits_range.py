"""
Total numbers with no repeated digits in a range

Given a range L, R find total such numbers in the given range such that they have no 
repeated digits.

For example:
12 has no repeated digit.
22 has repeated digit.
102, 194 and 213 have no repeated digit.
212, 171 and 4004 have repeated digits.

Examples:

Input : 10 12
Output : 2
Explanation : In the given range 
10 and 12 have no repeated digit 
where as 11 has repeated digit.

Input : 1 100
Output : 90

"""
# Function to check if the given number has repeated digit or not 
def repeated_digit(n):
    a =[]

    # Traversing through each digit
    while n!=0:
        d = n%10

        #if the digit is present more than once in the number
        if d in a:

            # return if the number has repeated digit
            return 0
        a.append(d)
        n = n//10
    # return 1 if the number has no repeated digit
    return 1

# Function to find total number in the given range which has no repeated digit
def calculate(L, R):
    answer = 0

    # Traversing through the range
    for i in range(L, R + 1):

        # Add 1 to the answer if i has no repeated digit else 0
        answer = answer + repeated_digit(i)

    return answer

print(calculate(1, 100))

"""
This method will answer each query in O( N ) time.

Efficient Approach
------------------

We will calculate a prefix array of the numbers which have no repeated digit.

Prefix[i] = Total number with no repeated digit less than or equal to 1.

Therefore each query can be solved in O(1) time.

Answer = Prefix[R] - Prefix[L-1]

"""


# prefix array
Prefix =[0]

# Fuction to check if the given number has repeated digit or not
def repeated_digit(n):
    a = []

    # Traversing through each digit 
    while n != 0:
        d =  n % 10
        # if the digit is present more than once in the number
        if d in a:
            # return 0 if the number has repeated digit
            return 0
        a.append(d)
        n = n//10
    
    # return 1 if the number has no repeated digit
    return 1

# Function to pre calculate the prefix array
def pre_calculation(MAX):

    # To use to global Prefix array
    global Prefix
    Prefix.append(repeated_digit(1))

    # Traversing through the numbers from 2 to MAX
    for i in range(2,MAX+1):
        # Generating the Prefix array
        Prefix.append(repeated_digit(i) + Prefix[i-1])


# Calculate Function
def calculate(L, R):
    return Prefix[R] -Prefix[L-1]

MAX = 1000
  
# Pre-calculating the Prefix array.
pre_calculation(MAX)
  
# Calling the calculate function
# to find the total number of number
# which has no repeated digit
print(calculate(1, 100))


print("\n my tests \n")

'''
my tests

'''
def my_tests(L,R):
    count =0
    for i in range(L, R+1):
        if check_if_repeated(i) == False:
            count += 1
    return count

def check_if_repeated(N):
    str_val =str(N)
    new_set =set(str_val)

    if(len(new_set) == len(str_val)):
        return False
    else:
        return True

print("expected 2, actual: ", my_tests(10,12))
print("expected 90, actual: ", my_tests(1,100))
