# Recursion
- Loops are used to execute repetitive statements e.g. while and for loop in Python
- An entirely different way to achieve execution of repetitive statements is through recursion
- Recursion is a technique where a function or method makes a call to itself
- Example:
  - Factorial Function (Classic Mathematical Function)
  - Fibonacci Series (Sequence of Numbers)
  - Binary Search
# Concept of Recursion
### Base Case - there should be a condition through which no recursive call is made, this value is known 
                  as base case
              - where we terminate the chain of recursive calls
- The chain of recursive calls should eventually reach the base case
- 
"""
Factorial(n)  = n * Factorial(n-1)
e.g. Factorial(5)  Fact = 5 * factorial(4)
Factorial(4)  Fact = 4 * factorial(3)
Factorial(3)  Fact = 3 * factorial(2)
Factorial(2)  Fact = 2 * factorial(1)
Factorial(1)  Fact = 1 * factorial(0)
Factorial(0)  if n == 0 return 1 # base case
"""