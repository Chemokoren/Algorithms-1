"""
Find the two repeating elements in a given array

You are given an array of n+2 elements. All elements of the array are in range 1 to n. And all
elements occur once except two numbers which occur twice. Find the two repeating numbers.

Input: 
arr = [4, 2, 4, 5, 2, 3, 1] 
n = 5
Output:
4 2
Explanation:
The above array has n + 2 = 7 elements with all elements occurring once except 2 and 4 
which occur twice. So the output should be 4 2.

Method 1: Basic

Use two loops. In the outer loop, pick elements one by one and count the number of occurrences of 
the picked element in the inner loop.
This method doesn't use the other useful data provided in questions like range numbers is between
1 to n and there are only two repeating elements.

Time Complexity: O(n*n) 
Auxiliary Space: O(1)
"""

# find two repeating elements in a given array
def print_repeating(arr):
    size = len(arr)
    res = []
    for i in range(0, size-1):
        for j in range(i +1, size):
            if arr[i] == arr[j]:
                res.append(arr[i])

    return res
print("2L Expected:[4,2],Actual:", print_repeating([4, 2, 4, 5, 2, 3, 1]))

"""

Method 2: Use Count Array

Traverse the array once. While traversing, keep track of count of all elements in the array using 
a temp array count[] of size n, when you see an elemenet whose count is already set, print it
as duplicate.
This method uses the range given in the question to restrict the size of count[], but doesn't 
use the data that there are only two repeating elements.

"""
# Time complexity : O(n) | Space complexity : O(n)
def print_repeating_two(arr):
    res =[]
    size = len(arr)
    count =[0] * size
    for i in range(0, size):
        if(count[arr[i]] == 1):
            res.append(arr[i])
        else:
            count[arr[i]] = count[arr[i]] + 1

    return res

print("Count Expected:[4,2],Actual:", print_repeating_two([4, 2, 4, 5, 2, 3, 1]))

"""
Method 3 (Make two equations) 

Let the numbers which are being repeated are X and Y. We make two equations for X and Y and the 
simple task left is to solve the two equations. 
We know the sum of integers from 1 to n is n(n+1)/2 and product is n!. We calculate the sum of 
input array when this sum is subtracted from n(n+1)/2, we get X + Y because X and Y are the two
 numbers missing from set [1..n]. Similarly calculate the product of input array, when this
  product is divided from n!, we get X*Y. Given the sum and product of X and Y, we can find 
  easily out X and Y.
Let summation of all numbers in the array be S and product be P
X + Y = S – n(n+1)/2 
XY = P/n!
Using the above two equations, we can find out X and Y. For array = 4 2 4 5 2 3 1, we get S = 21 
and P as 960.
X + Y = 21 – 15 = 6
XY = 960/5! = 8
X – Y = sqrt((X+Y)^2 – 4*XY) = sqrt(4) = 2
Using below two equations, we easily get X = (6 + 2)/2 and Y = (6-2)/2 
X + Y = 6 
X – Y = 2
Thanks to geek4u for suggesting this method. As pointed by Beginner, there can be an addition and 
multiplication overflow problem with this approach. 

The methods 3 and 4 use all useful information given in the question :
"""
import math 
# Time Complexity: O(n) | Auxiliary Space: O(1) 
def print_reapeating_three(arr):
    size = len(arr)

    # S is for sum of elements in arr[]
    S= 0

    # P is for product of elements in arr[]
    P=1
    n = size -2

    # Calculate Sum and Product of all elements in arr[]
    for i in range(0, size):
        S = S + arr[i]
        P = P * arr[i]

    # S is x + y now
    S = S - n * (n +1) // 2

    # P is x * y now
    P = P // fact(n)

    # D is x - y now
    D = math.sqrt(S * S - 4 *P)

    x = (D + S) // 2
    y = (S - D) // 2

    return x, y

def fact(n):
    if (n == 0):
        return 1
    else :
        return ( n * fact(n - 1))


print(" Three Expected:, Actual:", print_reapeating_three([4, 2, 4, 5, 2, 3, 1]))

"""

Method 4: Use XOR

Let the repeating numbers be X and Y, if we xor all the elements in the array and all integers 
from 1 to n, then the result is X xor Y. 
The 1’s in binary representation of X xor Y is corresponding to the different bits between X 
and Y. Suppose that the kth bit of X xor Y is 1, we can xor all the elements in the array and
all integers from 1 to n, whose kth bits are 1. The result will be one of X and Y. 

Time Complexity: O(n) 
Auxiliary Space: O(1) 

"""
def print_repeating_four(arr):
    
    size = len(arr)
    
    # Will hold xor of all elements
    
    xor = arr[0]
    n = size - 2
    x = 0
    y = 0
	# Get the xor of all elements in arr[] and 1, 2 .. n
    
    for i in range(1 , size):
        xor ^= arr[i]
        
    for i in range(1 , n + 1):
        xor ^= i
	
	# Get the rightmost set
	# bit in set_bit_no
    set_bit_no = xor & ~(xor-1)
	
	# Now divide elements in two
	# sets by comparing rightmost
	# set bit of xor with bit at
	# same position in each element.
    # 
    for i in range(0, size):
        
        if(arr[i] & set_bit_no):
			
			# XOR of first
			# set in arr[]
            x = x ^ arr[i]
            
        else:
            # XOR of second  set in arr[]
            y = y ^ arr[i]
            
    for i in range(1 , n + 1):
        
        if(i & set_bit_no):
			
			# XOR of first set
			# in arr[] and
			# 1, 2, ...n
            x = x ^ i
        else:
			
			# XOR of second set
			# in arr[] and
			# 1, 2, ...n
            y = y ^ i
            
    return (y, x)


print("4 Expected:, Actual:", print_repeating_four([4, 2, 4,5, 2, 3, 1]))

"""
Method 5: Use array elements as index

Traverse the array. Do following for every index i of A[].
{
check for sign of A[abs(A[i])] ;
if positive then
   make it negative by   A[abs(A[i])]=-A[abs(A[i])];
else  // i.e., A[abs(A[i])] is negative
   this   element (ith element of list) is a repetition
}

Example: A[] =  {1, 1, 2, 3, 2}
i=0; 
Check sign of A[abs(A[0])] which is A[1].  A[1] is positive, so make it negative. 
Array now becomes {1, -1, 2, 3, 2}

i=1; 
Check sign of A[abs(A[1])] which is A[1].  A[1] is negative, so A[1] is a repetition.

i=2; 
Check sign of A[abs(A[2])] which is A[2].  A[2] is  positive, so make it negative. '
Array now becomes {1, -1, -2, 3, 2}

i=3; 
Check sign of A[abs(A[3])] which is A[3].  A[3] is  positive, so make it negative. 
Array now becomes {1, -1, -2, -3, 2}

i=4; 
Check sign of A[abs(A[4])] which is A[2].  A[2] is negative, so A[4] is a repetition.

Note that this method modifies the original array and may not be a recommended method 
if we are not allowed to modify the array. 


"""
# Time Complexity: O(n) | Auxiliary Space: O(1) 
def print_repeating_five(arr):
    size = len(arr)
    for i in range(0, size):
        if(arr[abs(arr[i])] > 0):
            arr[abs(arr[i])] = (-1) * arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")

print_repeating_five([4, 2, 4, 5, 2, 3, 1])



"""
The point is to increment every element at (arr[i]th-1)th index by N-1 (as the elements are 
present upto N-2 only) and at the same time check if element at that index when divided by (N-1) 
gives 2. If this is true then it means that the element has appeared twice and we can easily say 
that this is one of our answers. This is one of the very useful techniques when we want to 
calculate Frequencies of Limited Range Array Elements  (see this post to know more).

    This method works on the fact that the remainder of an element when divided by any number 
    greater than that element will always give that same element. Similarly, as we are incrementing 
    each element at (arr[i]th-1) index by N-1, so when this incremented element is divided by N-1 
    it will give number of times we have added N-1 to it, hence giving us the occurrence of that 
    index (according to 1-based indexing).

"""
# Time Complexity: O(n) | Auxiliary Space: O(1) 
def print_repeated_six(arr):
    N = len(arr)
    m = N - 1
    for i in range(N):
        arr[arr[i] % m - 1] += m
        if ((arr[arr[i] % m - 1] // m) == 2):
            print(arr[i] % m ,end= " ")
      

print("The two repeating elements are ", end = "")
print_repeated_six([4, 2, 4, 5, 2, 3, 1])


"""
Method 7

The point here is to enter the array elements one by one into the unordered set. If a particular 
element is already present in the set it’s a repeating element.

"""
# Time Complexity: O(n)  | Auxiliary Space: O(n)  

 
def print_repeating_seven(arr):

    size =len(arr)
    
    s = set()
    
    for i in range(size):
        if (len(s) and arr[i] in s):
            print(arr[i], end = " ")
        s.add(arr[i])
		
print("\n seven \n")
print_repeating_seven([ 4, 2, 4, 5, 2, 3, 1 ])








print("\n my tests \n")


'''
my tests

'''
# Time complexity: O(n) | Space complexity :O(n)
def my_tests(arr):
    dic ={}
    res =[]

    for i in range(len(arr)):
        dic[arr[i]] =dic.get(arr[i],0) +1

    for k, v in dic.items():
        if v > 1:
            res.append(k)
    return res

print("Expected:[4,2],Actual:", my_tests([4, 2, 4, 5, 2, 3, 1]))

# Time complexity: O(nlogn) | Space complexity: O(1)
def my_tests_two(arr):
    res =[]
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            res.append(arr[i])
    return res

print("Sort Expected:[4,2],Actual:", my_tests_two([4, 2, 4, 5, 2, 3, 1]))

def my_tests_three(arr):
    res =[]
    for i in range(len(arr)):
        if(arr.count(arr[i]) >1):
            res.append(arr[i])
    res =set(res)
    return list(res)

print("Sort Expected:[4,2],Actual:", my_tests_three([4, 2, 4, 5, 2, 3, 1]))