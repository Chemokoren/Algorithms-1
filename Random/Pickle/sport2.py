# Import the pickle module
import pickle

# Open a file handler for reading a file from where the data will load
file_handler = open('sport', 'rb')

# Load the data from the file after deserialization
dataObject = pickle.load(file_handler)

# Close the file handler
file_handler.close()

# Print message
print('Data after deserialization')

# Iterate the loop to print the data after deserialization
for val in dataObject:
    print('The data value : ', val)