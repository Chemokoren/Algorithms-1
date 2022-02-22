"""

Recursion is one of the most important concepts in computer science. Simply speaking,
recursion is the process of a function calling itself. Using a real life analogy, imagine a
scenario where you invite your friends to lunch:

You first call Ben and ask him if he wants to go for lunch, and Ben said yes but he also want to meet with Sheldon, so he puts you on hold and calls Sheldon.

Sheldon answers Ben's call and says great but he also wants to meet Daniel, so he puts Ben on hold and calls Daniel.

Daniel answers Sheldon's call and says great but he also wants to meet Abdul, so he puts Sheldon on hold and calls Abdul.

Abdul answers Daniel's call and says great but he also wants to meet Dennis, so he puts Daniel on hold and calls Dennis.

Dennis answers Abdul's call and says great but he also wants to meet Carly, so he puts Dennis on hold and calls Carly.

Carly answers Dennis' call and says "ok let's go!" and hangs up.

Dennis returns to Abdul's call and says "ok let's go!" and hangs up.

Abdul returns to Daniel's call and says "ok let's go!" and hangs up.

Daniel returns to Sheldon's call and says "ok let's go!" and hangs up.

Sheldon returns to Ben's call and says "ok let's go!" and hangs up.

Ben returns to your call and says "ok let's go!" and hangs up.

You are happy and can now go to lunch!

Notice that the action of putting the previous person on hold and calling someone else is 
exactly the same except the people involved are different. Imagine this is a function call, 
it would be written as something like this:

def call_for_lunch(person):

    if person == 'Carly': # BASE CASE

        return True

    return call_for_lunch(next_person) # RECURSIVE CALL

This example highlights the key components in writing a correct recursive function:

    Base case/exit, e.g. Carly doesn't call anyone else, she just says yes and hangs up.
    Recursive call, i.e. calling the function itself with different argument, e.g. Ben calling Sheldon.

"""

# Here's a classic textbook example: finding the factorial of a number (5! = 5*4*3*2*1)

def factorial(n):

    if n <= 1: # BASE CASE

        return 1

    return n * factorial(n - 1) # RECURSIVE CALL

print(factorial(5))

"""
Recursion and Stack

How does the computer accomplish such a feat as calling a function itself? 
The answer is quite simple - it uses a stack behind the scene to keep track of where things
are. For this particular problem, the factorial recursive function roughly translates to this
when executed:

"""

def factorial_stack(n):

    stack = []

    # push each call to a stack

    # top of the stack is base case

    while n > 0:

        stack.append(n)

        n -= 1


    res = 1
    print("aaa",stack)

    # pop and use return value until stack is empty

    while len(stack) > 0: # stack is not None

        res *= stack.pop()


    return res

print(factorial_stack(5))

"""
A computer's internal stack is called "call stack" and the data it pushes onto a call stack 
are called "stack frame"s. Strictly speaking, stack frames on a call stack represent the 
function you are calling and its arguments. 

"""