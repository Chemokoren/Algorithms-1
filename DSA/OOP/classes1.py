class Student:
    """ This class represents a student """

    def __init__(self, name, roll, marks):
        self.name= name
        self.roll= roll
        self.marks = marks

    def __str__(self):
        return "This is a Student Class"

    def display(self):
        print('Student Name:', self.name)
        print('Roll Number:', self.roll)
        print('Marks:', self.marks)

S1= Student('aaa', 101, 78.25)
S2= Student('bbb', 102, 62.25)
S2= Student('ccc', 103, 87.25)
print(S1.display())
print(S2.display())
print(S3.display())

# Alternatively
S = [Student('aaa', 101, 78.25),
     Student('bbb', 102, 62.25),
     Student('ccc', 103, 87.25)]

for s in S:
    s.display()