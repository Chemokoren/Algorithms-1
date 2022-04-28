"""
Objectives

- Motivate the need for something like Big O Notation
- Describe what Big O Notation is
- Simplify Big O Expressions
- Define "time complexity" and "space complexity"
- Evaluate the time complexity and space complexity of different algorithms using Big O Notation
- Describe what an algorithm is

What is the idea?

- Imagine we have multiple implementations of the same function.
- How can we determine which one is the "best"?

Example: 

"Write a function that accepts a string input and  returns a reversed copy"

There are like 10 implementations of this problem on stack overflow that work. How do you know which is the
best among them?
-Big O

Who Cares?

When dealing with huge datasets, efficient algorithms can save your hours

- It's important to have a precise vocabulary to talk about how our code performs
- Useful for discussing trade-offs between different approaches
- When your code slows down or crashes, identifying parts of the code that are inefficient can help us find 
pain points in our applications
- It comes up in interviews

Example:

What does better mean?
- Faster? (start here)
- Less memory-intensive?
- More readable?

What are the challenges with recording time?
-Different machines will record different times
- The same machine will record different times!
- For fast algorithms, speed measurements may not be precise enough?


Counting OPerations
-------------------

If not time, then what?

- Rather than counting seconds, which are so variable ...
- Let's count the number of simple operations the computer has to perform!

def addUpTo(n):
    return n * (n+1) /2

- 1 multiplication
- 1 addition
- 1 division
There are 3 simple operations, regardless of the size of n

def addUpTo(n):
    total = 0 # 1 assignment
    for (i =1; i<=n; i++ ):# 1 assignment, n comparisons,  n addions & assignments
        total += 1 # n additions, n assignments
    return total

counting is hard!

- Depending on what we count, the number of operations can be as low as 2n or as high as 5n +2
- But regardless of the exact number, the number of operations grows roughly proportionally with
n

Introducing ... Big O
-----------------------

- Big O Notation is a way to formalize fuzzy counting
- It allows us to talk formally about how the runtime of an algorithm grows as the inputs grow
- We won't care about the details, only the trends

Big O Definition
----------------
We say that an algorithm is O(f(n)) if the number of simple operations the computer has to do is 
eventually less than a constant times f(n), as n increases.

-f(n) could be linear(f(n) =n)
-f(n) could be quadratic(f(n) =n^2)
-f(n) could be constant(f(n) =1)
-f(n) could be something entirely different!

Example

def addUpTo(n):                             # Always 3 operations
    return n *(n+1) /2                      # O(1)

def addUpTo(n):
    total = 0                               # Number of operations is (eventually)
    for(i =1; i<=n; i++):                   # bounded by a multiple of n(say, 10n)
        total +=i                           # O(n)
    return total

Simplifying Big O Expressions
- When determining the time complexity of an algorithm, there are some helpful rule of thumbs for
big O expressions.

- These rules of thumb are consequences of the definition of big O notation.

Constants don't matter
O(2n)                       O(n)
O(500)                      O(1)
O(12n^2)                    O(n^2)

Smaller terms don't matter
O(n + 10)                   O(n)
O(1000n + 50)               O(n)
O(n^2 +5n + 8)              O(n^2)

Big O Shorthands
- Analyzing complexity with big O can get complicated
- There are several rules of thumb that can help
- These rules won't ALWAYS work but are a helpful starting point

1. Arithmetic operations are constant
2. Variable assignment is constant
3. Accessing elements in an array(by index) or object(by key) is constant
4. In a loop, the complexity is the length of the loop times the complexity of whatever happens
inside of the loop


Space Complexity

- so far, we've been focusing on time complexity: how can we analyze the runtime of an algorithm
as the size of the input increases.

- We can also use big O notation to analyze space complexity: how much additional memory do we
need to allocate in order to run the code in our algorithm?
- auxiliary space complexity refers to space needed by the algorithm, not including space taken up
by the inputs.
- Unless otherwise noted, when we talk about space complexity, technically we'll be talking about
auxiliary space complexity.

Rules of thumb
---------------
- most primitives(booleans, numbers, undefined, null) are constant space
- Strings require O(n) space (where n is the string length)
- Reference types are generally O(n), where n is the length(for arrays) or the number of keys
(for objects)

Example:

def sum(arr):
    total = 0 # one number
    for(i =0; i< len(arr);i++): # i=0 is another number
        total += arr[i]
    return total

O(1) space

Example 2:

def double(arr):
    newArr =[]
    for(i =0; i<len(arr); i++):
        newArr.push(2*arr[i])
    return newArr # n numbers

O(n) space
"""

def addUp(n):
    return n *(n+1)/2

print(addUp(1000000000))
