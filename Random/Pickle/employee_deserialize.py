# Import pickle module
import pickle


# Declare employee class to read and print data from a file
class Employee:
    def __init__(self, name, email, post):
        self.name = name
        self.email = email
        self.post = post

    def display(self):
        print('Employee Detils:')
        print('Employee Name  :', self.name)
        print('Employee Email  :', self.email)
        print('Employee Position :', self.post)


# Open the file for reading
fileObject = open('employee_info', 'rb')

# Unpickle the data
employee = pickle.load(fileObject)

# Close file
fileObject.close()

# print the dataframe
employee.display()