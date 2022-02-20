"""
Call Center

For this quesiton, you need to design a program for a call center. You must design the system in
 a way that is easily expandable. 
 
This question will come in parts, and you need to answer the previous part before moving on. You
are advised to copy the code from the previous section to be used as a starting point for the
next.

Part One

the call center consists of many employees, who are able to handle incoming calls. An employee 
can be represented by their name (one word, no space).

Your system must support these following commands:
hire[employee]: Hire a new employee, adding them to the system. Input guarantees that the 
employee with the same name is not already in the database.
end[phone]: End the current conversation with the phone number phone, if phone is in a 
conversation. Print "Call between and  ended". If phone is currently in the queue, or if it is
not calling, do nothing.
dispatch[phone]: if phone is not already in a call and not already queued, assign the phone 
call to the first available employee (in the order they are inserted into the database). If
all employees are unavailable, queue that call until an employee becomes available (in which
case assign this phone call to the first available employee). When the call is connected, 
print("Connecting to").


Input 

instructions: A list of instructions.

Output

The list of strings as outputs.

Example 1

Input:

instructions = [

  ["hire", "James"],

  ["hire", "Angie"],

  ["dispatch", "303-1142"],

  ["dispatch", "583-9045"],

  ["dispatch", "711-4375"],

  ["end", "583-9045"],

  ["end", "303-1142"],

  ["end", "711-4375"]

]

Output

[

  "Connecting 303-1142 to James",

  "Connecting 583-9045 to Angie",

  "Call between 583-9045 and Angie ended",

  "Connecting 711-4375 to Angie",

  "Call between 303-1142 and James ended",

  "Call between 711-4375 and Angie ended",

]



"""

from typing import List

def simulate_call_center(instructions: List[List[str]])->List[str]:
    return []

if __name__=='__main__':
    pass