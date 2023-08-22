"""
Product of Array except itself

Given an array arr[] of n integers, construct a Product Array prod[](of same size) such that
prod[i] is equal to the product of all the elements of arr[]  except arr[i]. Solve it without
division operator in O(n time.)

Example : 

Input: arr[]  = {10, 3, 5, 6, 2}
Output: prod[]  = {180, 600, 360, 300, 900}
3 * 5 * 6 * 2 product of other array 
elements except 10 is 180
10 * 5 * 6 * 2 product of other array 
elements except 3 is 600
10 * 3 * 6 * 2 product of other array 
elements except 5 is 360
10 * 3 * 5 * 2 product of other array 
elements except 6 is 300
10 * 3 * 6 * 5 product of other array 
elements except 2 is 900


Input: arr[]  = {1, 2, 3, 4, 5}
Output: prod[]  = {120, 60, 40, 30, 24 }
2 * 3 * 4 * 5  product of other array 
elements except 1 is 120
1 * 3 * 4 * 5  product of other array 
elements except 2 is 60
1 * 2 * 4 * 5  product of other array 
elements except 3 is 40
1 * 2 * 3 * 5  product of other array 
elements except 4 is 30
1 * 2 * 3 * 4  product of other array 
elements except 5 is 24


Naive Solution
--------------
- Create two extra space, i.e. two extra arrays to store the product of all the array elements 
from start, up to that index and another array to store the product of all the array elements 
from the end of the array to that index.
-To get the product excluding that index, muliply the prefix product up to index i-1 with the 
suffix product up to index i+1

Algorithm
- Create two array prefix and suffix of length n, i.e length of the original array, initialize
prefix[0] =1 and suffix[n-1] =1 and also another array to store the product.
- Traverse the array from second index to end.
- For every index i update prefix[i] as prefix[i]=prefix[i-1]*array[i-1], i.e store the 
product upto i-1 index from the start of array.
- Traverse the array from second last index to start.
- For every index i update suffix[i] as suffix[i]=suffix[i+1] *arry[i+1], i.e store the product 
upto i+1 index from the end of array
- Traverse the array from start to end
- For every index i the output will prefix[i]*suffix[i], the product of the array element except
that element.

    Time Complexity: O(n). 
    The array needs to be traversed three times, so the time complexity is O(n).
    Space Complexity: O(n). 
    Two extra arrays and one array to store the output is needed so the space complexity is O(n)

"""
# function responsible for printing product array for a given array arr[] of size n
def productArray(arr):
    n = len(arr)

    if(n == 1):
        print(0)
        return
    
    # Allocate memory for temporary arrays left[] and right[]
    left =[0] * n
    right = [0]*n
    # Allocate memory for the product array
    prod = [0] * n

    # Left most element of left array is always 1
    left[0] =1

    # right most element of right array is always 1
    right[n-1] =1

    # construct the left array
    for i in range(1, n):
        left[i] =arr[i-1] * left[i-1]

    # construct the right rray
    for j in range(n-2, -1, -1):
        right[j] =arr[j+1] * right[j+1]

    # construct the product array using left[] and right[]

    for i in range(n):
        prod[i] =left[i] * right[i]

    # print the constructed prod array
    for i in range(n):
        print(prod[i], end=' ')


print("The product array is:")
productArray([10, 3, 5, 6, 2])


"""
Efficient solution
------------------
- in the previous solution, two extra arrays were created to store the prefix and suffix, in 
this solution, store the prefix and suffix product in the output array(or product array) itself.
Thus reducing the space required.

Algorithm
- Create an array product and initialize its value to 1 and a variable temp=1
- Traverse the array from start to end
- For every index i update product[i] as product[i] =temp and temp=*array[i], i.e store the 
product upto i-1 index from the start of array.
4. Initialize temp =1 and traverse the array from last index to start.
5. For every index i update product[i] as product[i]=product[i] * temp and temp=temp*arr[i],i.e
multiply with the product upto i+1 index from the end of array.
6. Print the product array.

    Time Complexity: O(n). 
    The original array needs to be traversed only once, so the time complexity is constant.
    Space Complexity: O(n). 
    Even though the extra arrays are removed, the space complexity remains O(n), as 
    the product array is still needed.

"""
def product_array_two(arr):

    n = len(arr)
    
    if n == 1:
        print(0)
        return
        
    i, temp = 1, 1
    
    # Allocate memory for the product array
    prod = [1 for i in range(n)]
    
    # Initialize the product array as 1

	# In this loop, temp variable contains product of
	# elements on left side excluding arr[i]
    # 
    for i in range(n):
        prod[i] = temp
        temp *= arr[i]

	# Initialize temp to 1 for product on right side
    temp = 1

	# In this loop, temp variable contains product of
	# elements on right side excluding arr[i]
    
    for i in range(n - 1, -1, -1):
        prod[i] *= temp
        temp *= arr[i]

	# Print the constructed prod array
    
    for i in range(n):
        print(prod[i], end=" ")
        
    return    

product_array_two([10, 3, 5, 6, 2])

"""
Another Approach
- Store the product of all the elements as a variable and then iterate the array and add 
product/current_index_value in a new array. And then return this new array.


Time Complexity: O(n)

Space Complexity: O(1)
"""
def product_except_self(a):
    n = len(a)

    prod = 1
    flag = 0

    for i in range(n):
        # counting number of elements which have value 0
        if(a[i] == 0):
            flag +=1
        else:
            prod *=a[i]

    # Creating a new array of size n
    arr = [0 for i in range(n)]

    for i in range(n):
        # if number of elements in array with value 0 is more than 1 than each value in
        # new array will be equal to 0
        if(flag > 1):
            arr[i] = 0

        # if no element having value 0 then we will insert product/a[i] in new array
        elif(flag == 0):
            arr[i] = (prod // a[i])

        # if 1 element of array having value o than all the elements except that index value, will
        # be equal to 0
        elif (flag == 1 and a[i] != 0):
            arr[i] = 0
        # if(flag == 1 && a[i] == 0)
        else:
            arr[i] = prod
    return arr

ans = product_except_self([10, 3, 5, 6, 2])
 
print(*ans)






print("\n my tests \n ")

'''
my tests

'''
import copy

def arr_product(arr):
    prod =1
    for i in range(len(arr)):
        prod *=arr[i]
    return prod

def my_tests(arr):
    a =copy.deepcopy(arr)
    for i in range(len(arr)):
        if i ==0:
            arr[i] =arr_product(a[i+1:])
        elif  i== len(arr)-1:
            arr[i] =arr_product(a[:-1])
            
        else:
            b = copy.deepcopy(a)
            b.remove(arr[i])
            arr[i] =arr_product(b)

    return arr

print("Expected:, Actual:", my_tests([10, 3, 5, 6, 2]))



def my_tests_two(arr):
    a =copy.deepcopy(arr)

    
    for i in range(len(arr)):
        
        j = i +1
        k = i-1
        prod =1
        if i == 0:
            while j <= len(arr)-1:
                prod *=arr[j]
                j +=1 
        elif i == j:
            while k >=0:
                prod *=arr[k] 
                k -=1
        else:
            while k >=0:
                prod *=arr[k] 
                k -=1

            while j <= len(arr)-1:
                prod *=arr[j]
                j +=1 
        a[i]=prod
    
    return a

print("22 Expected:, Actual:", my_tests_two([10, 3, 5, 6, 2]))
