"""
Exception Handling
- Various errors may be generated at runtime
- When exception occurs the python program terminates
- Exceptions can be handled by program for smooth continuation of execution
- Exception is an Object in Python

Standard Exceptions
- ImportError
- IndexError
- NameError
- TypeError
- ValueError
- IOError

"""
l = [10, 20, 30, 40]
print(l[2])

# print(l[10]) ---# returns IndexError exception showing that the list index is out of range

# handle exceptions
try:
    print(l[10])
except IndexError as e:
    print(e)
    # pass - if you do not want to display the description of the error
print(l)

# use Exception if you do not know/are not sure  of the exact exception e.g. IndexError