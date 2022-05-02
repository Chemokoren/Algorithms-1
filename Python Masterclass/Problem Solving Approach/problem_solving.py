"""
Objectives 
-Define what an algorithm is
-Devise a plan to solve algorithms
-Compare and contrast problem solving patterns including frequency counters, 
two pointer problems, and divide and conquer

What is an algorithm?
---------------------

A process or set of steps to accomplish a certain task.

Why do I need to know this?
--------------------------
- Almost everything that you do in programming involves some kind of algorithm!
- It's the foundation for being a successful problem solving and developer

How do you improve
- Devise a plan for solving problems
- Master common problem solving patterns

Problem solving strategies
-Section is focussed on a simple, foolproof, magical, miraculous, fail-safe approach.

Problem Soving
--------------
- Understand the Problem
- Explore concrete examples
- Break it Down
- Solve / Simplify
- Look back and refactor

Note:
-strategies adapted from George Polya's book, "How to Solve it"

Undestand the Problem
----------------------
1. Can I restate the problem in my own words?
2. What are the inputs that go into the problem?
3. What are the outputs that should come from the solution to the problem?
4. Can the outputs be determined from the inputs? In other words,do I have enough information 
to solve the problem? (You may not be able to answer this question until you set about solving
the problem. That's okay; it's still worth considering the question at this early stage.)
5. How should I label the important pieces of data that are a part of the problem?

Example:
Write a function that takes two numbers and returns their sum.
--------------------------------------------------------------
1. Can I restate the problem in my own words
"implement addition"
2. What are the inputs that go into the problem?
- ints, floats, doubles?
- what about string for large numbers?
- constraints
3.What are the outputs that should come from the solution to the problem?
- int, float, string?
4. Can the outputs be determined from the inputs?
- What if you are only given 1 number, what do you do?
5. How should I label the important pieces of data that are a part of the problem?
- function name ("addTwoNumbers")
- variables: num1, num2, results


2. Explore Concrete Examples
------------------------------
- coming up with examples can help you understand the problem better
- Examples also provide sanity checks that your eventual solution works how it should

- user stories
- Unit tests

Explore examples
- Start with simple examples
- Progress to More complex examples
- Explore examples with Empty inputs
- Explore examples with Invalid inputs

Write a function which takes in a string and returns counts of each character in the string.
charCount("aaa") # {a:3}
charCount("hello") # {h:1, e:1, l:2, o:1}
charCount("my phone number is 182764")
charCount("Hello hi") # how many h?
charCount("") # return empty object, undefined, null?
charCount(67954)

Break it Down
-------------
- explicitly write out the steps you need to take.
This forces you to think about the code you'll write before you write it, and helps you catch
any lingering conceptual issues or misunderstandings before you dive in and have to worry about 
details(e.g. language syntax) as well.

Example:
Write a function which takes in a string and returns counts of each character in the string.

def charCount(str):
    # make object to return at end
    # loop over string, for each character...
        # if the char is a number/letter AND is a key in object, add one to count
        # if the char is a number/letter AND not in object, add it to object and set value to 1
        # if character is something else(space, period, etc.) don't do anything
    # return object at end


4. Solve / simplify
- solve the problem
    if you can't ...
- solve a simpler problem
(ignore the part that is giving you a difficult time and focus on everything else)

SIMPLIFY
- Find the core difficulty in what you're trying to do
- Temporarily ignore that difficulty
- Write a simplified solution
- Then incorporate that difficulty back in

5. Look back & Refactor
-congrats on solving it, but you're not done!

Refactoring Questions
- Can you check the result?
- Can you derive the result differently?
- Can you understand it at a glance?
- Can you use the result or method for some other problem?
- Can you improve the performance of your solution?
- Can you think of other ways to refactor?
- How have other people solved this problem?

"""

from curses import noqiflush


def charCount(str):
    # make object to return at the end
    result ={}
    # loop over string, for each character ...
    for i in range(0, len(str)-1):
        char = str[i]
        # if the char is a number/letter AND is a key in object, add one to count
        print("aaa:", result[char])
        if(result[char]> 0):
            result[char] +=1
        # if the char is a number/letter AND not in object, add it to object and set value to 1
        else:
            result[char] =1
    # if character is something  else (space, period, etc.) don't do anything
    # return object at the end
    return result

print(charCount("hello"))


def charCountUpdated(str):
    obj ={}
    for i in str:
        char =i.lower()
        if(isAlphaNumeric(char)):#if(/[a-z0-9]/.test(char)):
            if(obj[char]>0):
                obj[char] +=1
            else:
                obj[char]=1
            # obj[char] =++obj[char] ||  1
    return obj


def isAlphaNumeric(char):
    code =char.charCodeAt(0);
    if(not (code > 47 and code <58) and # numeric (0-9)
        not(code > 64 and code < 91) and # upper alpha (A-Z)
        not(code > 96 and code <123)):
        return False
    return True
