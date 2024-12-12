"""
Implicit call
"""
class Student:

    def __init__(self):
        self.name ='abc'
        self.roll =101
        self.marks =78.25
        print('In Constructor')

    def display(self):
        print(self.name, self.roll, self.marks)

S= Student() # implicit call to __init__ method
S.__init__() # explicit call to --init__ method
