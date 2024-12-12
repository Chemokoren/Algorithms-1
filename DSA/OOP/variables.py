"""
Instance Variables
"""
class Student:

    def __init__(self, name, roll, marks):
        # instance variables
        self.name =name
        self.roll =roll
        self.marks =marks

    def display(self):
        print('Student Name: ', self.name)
        print('Student Roll No: ', self.roll)
        print('Student Marks: ', self.marks)
        print()

S1= Student('aaa', 101, 78.25)
S2= Student('bbb', 102, 102.25)

S1.display()
S2.display()

"""
Static Variables
- When static variables are present, they have to be preceded by the class name
"""
class Student:
    college ='Moi University' # approach 1
    def __init__(self, name, roll, marks):
        # instance variables
        self.name =name
        self.roll =roll
        self.marks =marks
        Student.motto="Smart Living Made Simple" # approach 2

    def display(self):
        print('Student Name: ', self.name)
        print('Student Roll No: ', self.roll)
        print('Student Marks: ', self.marks)
        print('College Name: ', Student.college)
        print('College Motto: ', Student.motto)
        #Student.semester = "First" -- approach 4
        print('College Semester: ', Student.semester)
        print()

Student.semester="First" # approach 3 - created oustide the class but before instantiating the object
S1= Student('aaa', 101, 78.25)
S2= Student('bbb', 102, 102.25)

# static variable college is the same for all the variables
S1.display()
S2.display()