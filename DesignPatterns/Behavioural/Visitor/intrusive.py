class DoubleExpression:

    def __init__(self, value):
        self.value =value

    def print(self, buffer):
        buffer.append(str(self.value))

    def eval(self): return self.value

class AdditionExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left

    def print(self, buffer):
        buffer.append('(')
        self.left.print(buffer)
        buffer.append('+')
        self.right.print(buffer)
        buffer.append(')')

    def eval(self):
        return self.left.eval() + self.right.eval()
    
if __name__ =='__main__':
    # represents 1 + (2+3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    buffer = []
    e.print(buffer)
    print(''.join(buffer), '=', e.eval())

# breaks OCP: requires we modify the entire hierarchy
# what is more likely: new type or new operation
    
e = AdditionExpression(left=5, right=3)
buffer =[]
e.print(buffer)
print(f" mine :: {''.join(buffer)}, second:: {e}")

"""

In the provided code, self.left and self.right are instances of the AdditionExpression class, and print is a method of the AdditionExpression class. When you call self.left.print(buffer) and self.right.print(buffer), you are invoking the print method of the AdditionExpression instances stored in the left and right attributes of the current instance.

Let's break it down:

    Initialization (__init__ method):
        When you create an instance of AdditionExpression using left_instance = AdditionExpression(...), the left_instance becomes the self inside the methods of that instance.
        Similarly, if you have a right_instance = AdditionExpression(...), it becomes the self when calling methods on it.

    Printing (print method):
        The print method takes a buffer argument, which is likely a mutable container (like a list) used to accumulate the characters of the printed expression.
        When you call self.left.print(buffer) or self.right.print(buffer), you are invoking the print method of the AdditionExpression instance stored in self.left or self.right.
        This process is recursive. Each call to print on the left and right expressions results in further calls until you reach the base case where an expression does not have sub-expressions.

Example:

# Create an instance of AdditionExpression
expression = AdditionExpression(
    left=AdditionExpression(left=2, right=3),
    right=AdditionExpression(left=4, right=5)
)

# Create an empty list to store the printed characters
output_buffer = []

# Call the print method on the main expression
expression.print(output_buffer)

# Concatenate the characters in the buffer to get the final printed expression
result_string = ''.join(output_buffer)
print(result_string)  # Output: ( (2+3) + (4+5) )


In this example, calling expression.print(output_buffer) initiates the printing process for the entire expression and accumulates the characters in the output_buffer. The recursive calls to print on self.left and self.right handle the sub-expressions until the entire expression is printed.

"""