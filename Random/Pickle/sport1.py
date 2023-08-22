print(" ###########  ")

# Import the pickle module
import pickle

# Declare the object to store data
dataObject = []

# Iterate the for loop for 5 times and take language names
for n in range(5):
  raw = input('Enter name for a sport  :')

dataObject.append(raw)

# Open a file for writing data
file_handler = open('sport', 'wb')

# Dump the data of the object into the file
pickle.dump(dataObject, file_handler)

# close the file handler to release the resources
file_handler.close()

# Print message
print('Data is serialized')