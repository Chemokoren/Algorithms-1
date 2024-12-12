class Student:
    """ This class represents a student """

    def __init__(self):
        self.name= 'John'
        self.roll= 101
        self.marks = 78.25

    def __str__(self):
        return "This is a Student Class"

    def display(self):
        print('Student Name:', self.name)
        print('Roll Number:', self.roll)
        print('Marks:', self.marks)

S= Student()
print(S.name)
print(S.roll)
print(S.marks)
print(S.__doc__)
print(S)
S.display()