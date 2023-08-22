"""

Objectives
- Define what recursion is and how it can be used
- Understand the two essential components of a recursive function
- Visualize the call stack to better debug and understand recursive functions
- Use helper method recursion and pure recursion to solve more difficult problems

What is recursion
- A process(a function in our case) that calls itself

Why should you care?
- It's everywhere
    * DOM traversal algorithms
    * Object traversal
    * In more complex data structures
    * It's sometimes a cleaner alternative to iteration

How recursive functions work
- Invoke the same function with a different input until you reach your base case!

Base Case
- The condition when the recursion ends

Two essential parts of a recursive function!
- Base case 
- Different input every time

"""

'''
example 1: CountDown
'''

def CountDown(num):
    if num ==-1:
        return 0
    print(num)
    num -= 1
    CountDown(num)

CountDown(5)

'''
example 2: sumRange
'''

def sumRange(n):
    if(n==1): return 1
    return n +sumRange(n-1)

print("sum range of 5: ", sumRange(5))
print("sum range of 4: ", sumRange(4))

'''
example 3: Factorial
'''

def factorial(n):
    product=1
    for i in range(1,n+1):
        print("aaa:", i)
        product *=i
    return product

print("factorial of 5: ", factorial(5))
print("factorial of 7: ", factorial(7))

def recursiveFactorial(n):
    if n==1:
        return 1
    product = n * recursiveFactorial(n-1)
    
    return product

print("recursive factorial of 5: ", recursiveFactorial(5))
print("recursive factorial of 7: ", recursiveFactorial(7))

"""
Common Recursion Pitfalls

- Not base case
- Forgetting to return or returning the wrong thing!
- Stack overflow!
e.g.
def factorial(num):
    if(num == 1):print(1)
    return num * factorial(num-1)


HELPER METHOD RECURSION

"""
def outer(input):

    outerScopedVariable =[]

    def helper(helperInput):
        # modify the outerScopedVariable
        helper(helperInput-1)

    helper(input)

    return outerScopedVariable

'''
collect odd values in an array

'''
def collectOddValues(arr):
    result =[]

    def helper(helperInput):
        if(len(helperInput) == 0):
            return
        if(helperInput[0] % 2 != 0):
            result.append(helperInput[0])
        helperInput.pop(0)
        helper(helperInput)

    helper(arr)
    return result

print(collectOddValues([1,2,3,4,5,6,7,8,9]))


'''
Pure Recursion

'''
def collectOddValues(arr):
    newArr=[]

    if len(arr) ==0:
        return newArr
    if(arr[0] % 2 !=0 ):
        newArr.append(arr[0])

    arr.pop(0)
    newArr = newArr +collectOddValues(arr)
    return newArr

print("############## Pure Recursion ##############")
print(collectOddValues([1,2,3,4,5,6,7,8,9]))
print(collectOddValues([1,2,3,4,5]))
