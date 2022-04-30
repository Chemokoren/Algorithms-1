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

"""