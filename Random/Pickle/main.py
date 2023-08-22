""""
Example 3
"""

import pickle
from fruit import Fruit
import joblib

# Create a new fruit object
_fruit = Fruit('Mango')

# Pickle the object into a text file
file = open('fruit.txt', 'wb')
pickle.dump(_fruit, file)
file.close()

# Open file and unpickle data back into a Python object
new_fruits_file = open('fruit.txt', 'r')
p = pickle.load(new_fruits_file)
# Use the intact object's method
p.show()
