"""
Vending Machine

For this question, we ask you to design a vending machine. We divide this question in to three 
parts, so you can complete them in order

Part One

For the firs part, you must design a Machine class representing the vending machine. You system
must support the following commands:

- new_product <name><price>: Creates a new product object with name which is a string, and price
which is a non-negative integer.
- print_products: Prints all products, each product in a line in format <name><price>, sorted
by price from lowest to highest.
- print_products: Prints all products, each product in a line in format<name><price>,sorted
by price from lowest to highest.
- insert_coin <value>: Adds money to internal state.
- purchase <name>: Checks if the user inserted enough money and return a boolean.
- checkout: Prints the money left by the previous user, and clears internal state for the next user.

You may implement these however you like. However, preferably this should be easily expandable to
accomodate new requirements.

Example

input:

instructions = [

  ["new_product", "apple", "4"],

  ["insert_coin", "5"],

  ["purchase", "apple"],

  ["purchase", "apple"],

  ["checkout"],

]

Output:

[

  "true",

  "false",

  "1"

]


"""
from typing import List

def vending_machine(instructions: List[List[str]])->List[str]:
    return []

if __name__=='__main__':
    pass