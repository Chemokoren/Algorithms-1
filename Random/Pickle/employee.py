# Import pickle module
import pickle


# Declare the employee class to store the value
class Employee:
    def __init__(self, name, email, post):
        self.name = name
        self.email = email
        self.post = post


# Create employee  object
empObject = Employee('james', 'james01@gmail.com', 'CEO')

# Open file for store data
fileHandler = open('employee_info', 'wb')

# Save the data into the file
pickle.dump(empObject, fileHandler)

# Close the file
fileHandler.close()

# Print message
print('Data is serialized')